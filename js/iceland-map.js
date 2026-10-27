/* Discover Iceland interactive map.
   The base layer is our own branded relief map (Web Mercator), placed on its
   real geographic bounds so highlights can be pinned by GPS coordinates.
   Usage: <div class="imap" data-map></div>  (needs Leaflet loaded first) */
(function () {
  "use strict";

  var BOUNDS = [[63.1191, -24.8526], [66.7502, -13.0427]];
  var BASE = "/assets/img/map-general-2800.jpg";
  var COLORS = {
    waterfalls: "#4aa8ff", glaciers: "#9fd4e2", coast: "#e8eef1", mountains: "#d9a066",
    canyons: "#3cc4b0", "hot-springs": "#ff7a59", highlands: "#a3c46b", aurora: "#3cf08c", culture: "#d9483b"
  };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function build(el, data) {
    var fallback = el.querySelector(".imap-fallback");
    var mapEl = document.createElement("div");
    mapEl.className = "imap-canvas";
    el.appendChild(mapEl);

    var touch = window.matchMedia("(pointer: coarse)").matches;
    var map = L.map(mapEl, {
      zoomSnap: 0, zoomDelta: 0.5, wheelPxPerZoomLevel: 120, scrollWheelZoom: false, attributionControl: false,
      zoomControl: false, maxBoundsViscosity: 1, dragging: !touch, tap: false
    });
    L.control.zoom({ position: "bottomright" }).addTo(map);
    L.imageOverlay(BASE, BOUNDS, { alt: "Map of Iceland" }).addTo(map);
    map.fitBounds(BOUNDS, { padding: [0, 0] });
    var min = map.getZoom();
    map.setMinZoom(min);
    map.setMaxZoom(min + 2.75);
    map.setMaxBounds(BOUNDS);
    if (fallback) fallback.remove();

    // Wheel zoom only after the visitor clicks into the map, so page scrolling is never hijacked.
    mapEl.addEventListener("click", function () { map.scrollWheelZoom.enable(); });
    mapEl.addEventListener("mouseleave", function () { map.scrollWheelZoom.disable(); });
    // On phones, one-finger drag only once zoomed in (pinch always works).
    if (touch) {
      map.on("zoomend", function () {
        if (map.getZoom() > min + 0.1) map.dragging.enable(); else map.dragging.disable();
      });
    }

    var markers = [];
    data.items.forEach(function (h) {
      var color = COLORS[h.cats[0]] || "#e8eef1";
      var icon = L.divIcon({
        className: "imap-pin",
        html: '<span style="--c:' + color + '"></span>',
        iconSize: [22, 22], iconAnchor: [11, 11]
      });
      var m = L.marker(h.ll, { icon: icon, title: h.name, keyboard: true, riseOnHover: true });
      m.bindTooltip(esc(h.name), { direction: "top", offset: [0, -10], className: "imap-tip" });
      m.bindPopup(
        '<a class="imap-card" href="' + esc(h.url) + '">' +
          '<img src="' + esc(h.img) + '" alt="' + esc(h.alt) + '" loading="lazy">' +
          '<span class="imap-card-body"><span class="imap-region">' + esc(h.region) + "</span>" +
          "<strong>" + esc(h.name) + "</strong><span class=\"imap-text\">" + esc(h.text) + "</span>" +
          '<span class="imap-more">Read more →</span></span></a>',
        { maxWidth: 280, minWidth: 260, className: "imap-popup", autoPanPadding: [30, 30] }
      );
      m._cats = h.cats;
      m._slug = h.slug;
      m.addTo(map);
      markers.push(m);
    });

    var focus = el.getAttribute("data-focus");
    if (focus) {
      markers.forEach(function (m) {
        if (m._slug === focus) {
          m.setIcon(L.divIcon({ className: "imap-pin imap-pin-focus", html: '<span style="--c:#d9483b"></span>', iconSize: [30, 30], iconAnchor: [15, 15] }));
          m.setZIndexOffset(1000);
          m.unbindPopup();
          m.bindTooltip(esc(m.options.title), { direction: "top", offset: [0, -14], className: "imap-tip", permanent: true });
          map.setView(m.getLatLng(), min + 1.6, { animate: false });
          if (touch) map.dragging.enable();
        }
      });
    }

    if (el.hasAttribute("data-nochips")) {
      var h2 = document.createElement("p");
      h2.className = "imap-hint";
      h2.textContent = "Tap a pin to see a nearby place";
      el.parentNode.insertBefore(h2, el.nextSibling);
      return;
    }

    // Category chips
    var chips = document.createElement("div");
    chips.className = "imap-chips";
    var used = data.categories.filter(function (c) {
      return markers.some(function (m) { return m._cats.indexOf(c[0]) > -1; });
    });
    var all = [["all", "All"]].concat(used);
    all.forEach(function (c) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "imap-chip";
      b.setAttribute("aria-pressed", c[0] === "all" ? "true" : "false");
      b.innerHTML = (c[0] === "all" ? "" : '<i style="background:' + (COLORS[c[0]] || "#fff") + '"></i>') + esc(c[1]);
      b.addEventListener("click", function () {
        chips.querySelectorAll(".imap-chip").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        map.closePopup();
        markers.forEach(function (m) {
          var on = c[0] === "all" || m._cats.indexOf(c[0]) > -1;
          if (on && !map.hasLayer(m)) m.addTo(map);
          if (!on && map.hasLayer(m)) map.removeLayer(m);
        });
      });
      chips.appendChild(b);
    });
    el.parentNode.insertBefore(chips, el);

    var hint = document.createElement("p");
    hint.className = "imap-hint";
    hint.textContent = touch ? "Pinch to zoom · tap a pin for a preview" : "Click a pin for a preview · scroll or use + / − to zoom · drag to move";
    el.parentNode.insertBefore(hint, el.nextSibling);
  }

  function init() {
    var els = document.querySelectorAll("[data-map]");
    if (!els.length || !window.L) return;
    fetch("/assets/map-data.json").then(function (r) { return r.json(); }).then(function (data) {
      els.forEach(function (el) {
        if ("IntersectionObserver" in window) {
          var io = new IntersectionObserver(function (entries) {
            if (entries[0].isIntersecting) { io.disconnect(); build(el, data); }
          }, { rootMargin: "400px" });
          io.observe(el);
        } else {
          build(el, data);
        }
      });
    }).catch(function () {});
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
