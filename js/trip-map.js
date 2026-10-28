/* Discover Iceland: full-screen map and trip planner (/map).
   Needs Leaflet. Data comes from /assets/map-data.json. The trip is kept in
   localStorage (this browser only) and in the URL (#trip=slug,slug) for sharing. */
(function () {
  "use strict";

  var BOUNDS = [[63.1191, -24.8526], [66.7502, -13.0427]];
  var BASE = "/assets/img/map-general-2800.jpg";
  var COLORS = {
    waterfalls: "#4aa8ff", glaciers: "#9fd4e2", coast: "#e8eef1", mountains: "#d9a066",
    canyons: "#3cc4b0", "hot-springs": "#ff7a59", highlands: "#a3c46b", aurora: "#3cf08c", culture: "#d9483b"
  };
  var KEY = "di-trip";

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function km(a, b) {
    var R = 6371, r = Math.PI / 180;
    var dLat = (b[0] - a[0]) * r, dLon = (b[1] - a[1]) * r;
    var x = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(a[0] * r) * Math.cos(b[0] * r) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return 2 * R * Math.asin(Math.sqrt(x));
  }
  function load() {
    var m = location.hash.match(/trip=([a-z0-9,-]+)/);
    if (m) return m[1].split(",").filter(Boolean);
    try { return JSON.parse(localStorage.getItem(KEY) || "[]"); } catch (e) { return []; }
  }

  function start(data) {
    var items = {}, order = data.items.map(function (h) { items[h.slug] = h; return h.slug; });
    var trip = load().filter(function (s) { return items[s]; });
    var selected = null, filter = "all", query = "";

    var mapEl = document.getElementById("mpMap");
    mapEl.innerHTML = "";
    var touch = window.matchMedia("(pointer: coarse)").matches;
    var map = L.map(mapEl, { zoomSnap: 0, zoomDelta: 0.5, wheelPxPerZoomLevel: 90, attributionControl: false, zoomControl: false, tap: false });
    L.control.zoom({ position: "bottomright" }).addTo(map);
    L.imageOverlay(BASE, BOUNDS, { alt: "Map of Iceland" }).addTo(map);
    map.fitBounds(BOUNDS);
    var min = map.getZoom();
    map.setMinZoom(min - 0.3);
    map.setMaxZoom(min + 3.5);
    map.setMaxBounds(L.latLngBounds(BOUNDS).pad(0.25));
    window.addEventListener("resize", function () { map.invalidateSize(); });

    var line = L.polyline([], { color: "#d9483b", weight: 3, dashArray: "6 8", opacity: 0.9 }).addTo(map);
    var markers = {};
    order.forEach(function (slug) {
      var h = items[slug];
      var m = L.marker(h.ll, { title: h.name, keyboard: true, riseOnHover: true });
      m.bindTooltip(esc(h.name), { direction: "top", offset: [0, -12], className: "mp-tip" });
      m.on("click", function () { select(slug, false); });
      m.addTo(map);
      markers[slug] = m;
    });

    var card = document.querySelector(".mp-card");
    var list = document.querySelector(".mp-list");
    var tripList = document.querySelector(".mp-trip");
    var count = document.getElementById("mpCount");
    var toast = document.querySelector(".mp-toast");

    function icon(slug) {
      var h = items[slug], i = trip.indexOf(slug);
      var cls = "mp-pin" + (i > -1 ? " trip" : "") + (slug === selected ? " on" : "");
      var inner = i > -1 ? '<span>' + (i + 1) + "</span>" : '<span style="--c:' + (COLORS[h.cats[0]] || "#e8eef1") + '"></span>';
      var size = i > -1 ? 26 : 20;
      return L.divIcon({ className: cls, html: inner, iconSize: [size, size], iconAnchor: [size / 2, size / 2] });
    }
    function visible(slug) {
      var h = items[slug];
      var okCat = filter === "all" || h.cats.indexOf(filter) > -1;
      var okQ = !query || (h.name + " " + h.region).toLowerCase().indexOf(query) > -1;
      return (okCat && okQ) || trip.indexOf(slug) > -1;
    }
    function drawPins() {
      order.forEach(function (slug) {
        var m = markers[slug];
        m.setIcon(icon(slug));
        m.setZIndexOffset(trip.indexOf(slug) > -1 ? 500 : slug === selected ? 800 : 0);
        var show = visible(slug);
        if (show && !map.hasLayer(m)) m.addTo(map);
        if (!show && map.hasLayer(m)) map.removeLayer(m);
      });
      line.setLatLngs(trip.map(function (s) { return items[s].ll; }));
      list.querySelectorAll(".mp-item").forEach(function (li) {
        var s = li.dataset.slug, h = items[s];
        if (!h) { li.hidden = true; return; }
        var okCat = filter === "all" || h.cats.indexOf(filter) > -1;
        var okQ = !query || (h.name + " " + h.region).toLowerCase().indexOf(query) > -1;
        li.hidden = !(okCat && okQ);
        li.classList.toggle("on", s === selected);
        var b = li.querySelector(".mp-add"), inTrip = trip.indexOf(s) > -1;
        b.setAttribute("aria-pressed", String(inTrip));
        b.textContent = inTrip ? "✓" : "+";
      });
    }
    function save() {
      try { localStorage.setItem(KEY, JSON.stringify(trip)); } catch (e) {}
      var url = location.pathname + (trip.length ? "#trip=" + trip.join(",") : "");
      try { history.replaceState(null, "", url); } catch (e) {}
    }
    function drawTrip() {
      count.textContent = trip.length;
      document.querySelector(".mp-empty").hidden = trip.length > 0;
      document.querySelector(".mp-actions").hidden = trip.length === 0;
      var total = 0, out = "";
      trip.forEach(function (s, i) {
        var h = items[s];
        if (i > 0) {
          var d = km(items[trip[i - 1]].ll, h.ll); total += d;
          out += '<li class="mp-leg" aria-hidden="true">↓ about ' + Math.round(d) + " km in a straight line</li>";
        }
        out += '<li class="mp-stop" data-slug="' + s + '"><span class="n">' + (i + 1) + "</span>" +
          '<div><strong>' + esc(h.name) + "</strong><small>" + esc(h.region) + "</small></div>" +
          '<div class="ctl"><button type="button" data-mv="-1" aria-label="Move up"' + (i === 0 ? " disabled" : "") + ">↑</button>" +
          '<button type="button" data-mv="1" aria-label="Move down"' + (i === trip.length - 1 ? " disabled" : "") + ">↓</button>" +
          '<button type="button" data-rm aria-label="Remove">×</button></div></li>';
      });
      tripList.innerHTML = out;
      document.querySelector(".mp-total").innerHTML = trip.length > 1
        ? "<strong>" + trip.length + " stops</strong>, about " + Math.round(total) + " km in straight lines.<span>Roads wind around fjords and mountains, so expect to drive noticeably further. Check umferdin.is before each drive.</span>"
        : "";
      drawPins();
      if (selected) renderCard(selected);
    }
    function toggle(slug) {
      var i = trip.indexOf(slug);
      if (i > -1) trip.splice(i, 1); else trip.push(slug);
      save(); drawTrip();
      flash(i > -1 ? items[slug].name + " removed from your trip" : items[slug].name + " added to your trip (" + trip.length + ")");
    }
    function flash(t) {
      toast.textContent = t; toast.hidden = false;
      clearTimeout(flash._t); flash._t = setTimeout(function () { toast.hidden = true; }, 2200);
    }
    function renderCard(slug) {
      var h = items[slug], inTrip = trip.indexOf(slug) > -1;
      card.innerHTML = '<button type="button" class="mp-x" aria-label="Close">×</button>' +
        '<img src="' + esc(h.img) + '" alt="' + esc(h.alt) + '">' +
        '<div class="mp-card-body"><small>' + esc(h.region) + "</small><h2>" + esc(h.name) + "</h2><p>" + esc(h.text) + "</p>" +
        '<div class="mp-card-btns"><button type="button" class="btn primary' + (inTrip ? " on" : "") + '" data-act="toggle">' + (inTrip ? "✓ In your trip" : "+ Add to my trip") + "</button>" +
        '<a class="btn outline" href="' + esc(h.url) + '">Read the guide</a></div></div>';
      card.hidden = false;
      card.querySelector(".mp-x").onclick = function () { selected = null; card.hidden = true; drawPins(); };
      card.querySelector('[data-act="toggle"]').onclick = function () { toggle(slug); };
    }
    function select(slug, fly) {
      selected = slug;
      renderCard(slug);
      drawPins();
      if (fly) map.flyTo(items[slug].ll, Math.max(map.getZoom(), min + 1.4), { duration: 0.6 });
    }

    // Category chips
    var chips = document.querySelector(".mp-chips");
    var used = data.categories.filter(function (c) { return order.some(function (s) { return items[s].cats.indexOf(c[0]) > -1; }); });
    [["all", "All"]].concat(used).forEach(function (c) {
      var b = document.createElement("button");
      b.type = "button"; b.className = "mp-chip";
      b.setAttribute("aria-pressed", String(c[0] === "all"));
      b.innerHTML = (c[0] === "all" ? "" : '<i style="background:' + (COLORS[c[0]] || "#fff") + '"></i>') + esc(c[1]);
      b.onclick = function () {
        filter = c[0];
        chips.querySelectorAll(".mp-chip").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        drawPins();
      };
      chips.appendChild(b);
    });
    document.querySelector(".mp-search").addEventListener("input", function (e) { query = e.target.value.trim().toLowerCase(); drawPins(); });

    // List: click row to preview, + to add
    list.addEventListener("click", function (e) {
      var li = e.target.closest(".mp-item"); if (!li) return;
      if (e.target.closest(".mp-add")) { e.preventDefault(); toggle(li.dataset.slug); return; }
      if (e.target.closest("a") && !e.metaKey && !e.ctrlKey) e.preventDefault();
      select(li.dataset.slug, true);
      if (window.matchMedia("(max-width: 860px)").matches) document.querySelector(".mp-mapwrap").scrollIntoView({ behavior: "smooth" });
    });
    // Trip: reorder / remove / focus
    tripList.addEventListener("click", function (e) {
      var li = e.target.closest(".mp-stop"); if (!li) return;
      var s = li.dataset.slug, i = trip.indexOf(s);
      var mv = e.target.closest("[data-mv]");
      if (mv) { var j = i + Number(mv.dataset.mv); trip.splice(i, 1); trip.splice(j, 0, s); save(); drawTrip(); return; }
      if (e.target.closest("[data-rm]")) { toggle(s); return; }
      select(s, true);
    });
    document.querySelector('[data-act="clear"]').onclick = function () { trip = []; save(); drawTrip(); };
    document.querySelector('[data-act="share"]').onclick = function () {
      var url = location.origin + "/map#trip=" + trip.join(",");
      var done = function () { flash("Trip link copied"); };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () { prompt("Copy this link", url); });
      else prompt("Copy this link", url);
    };
    // Tabs
    var tabs = document.querySelectorAll(".mp-tab");
    tabs.forEach(function (t) {
      t.onclick = function () {
        tabs.forEach(function (x) { x.setAttribute("aria-selected", String(x === t)); });
        document.querySelectorAll(".mp-panel").forEach(function (p) { p.hidden = p.dataset.panel !== t.dataset.tab; });
      };
    });

    // A shared trip link opened in a tab that already shows /map only changes the hash: reload to load it.
    window.addEventListener("hashchange", function () {
      var m = location.hash.match(/trip=([a-z0-9,-]+)/);
      if (m && m[1] !== trip.join(",")) location.reload();
    });

    drawTrip();
    if (trip.length) {
      if (/trip=/.test(location.hash)) tabs[1].click();
      map.fitBounds(L.latLngBounds(trip.map(function (s) { return items[s].ll; })).pad(0.3), { maxZoom: min + 1.5 });
    }
  }

  function init() {
    if (!window.L) return;
    fetch("/assets/map-data.json").then(function (r) { return r.json(); }).then(start).catch(function () {});
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
