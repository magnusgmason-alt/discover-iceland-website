"""Waterfalls cluster: seven journal articles (pillar first)."""

MAP_WATERFALLS = '<figure class="a-figure a-map"><a href="/assets/img/map-waterfalls-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-waterfalls-1800.jpg" srcset="/assets/img/map-waterfalls-800.jpg 800w, /assets/img/map-waterfalls-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="ALT" loading="lazy" decoding="async"></a><figcaption>CAPTION Tap to open full size.</figcaption></figure>'


def _map(alt, caption):
    return MAP_WATERFALLS.replace("ALT", alt).replace("CAPTION", caption)


ARTICLES = [
    # ------------------------------------------------------------------ 1 PILLAR
    {
        "slug": "waterfalls-in-iceland",
        "cluster": "waterfalls",
        "pillar": True,
        "short": "Iceland's Best Waterfalls: The Complete Map",
        "title": "Waterfalls in Iceland: The Best Falls by Region, With Map and Tips (2027)",
        "description": "The best waterfalls in Iceland by region: Seljalandsfoss, Skógafoss, Gullfoss, Dettifoss, Dynjandi, Hengifoss and more, with heights, walks, fees and a map.",
        "category": "Nature · Waterfalls",
        "teaser": "Every major fall around the island, with heights, walks, fees and seasons.",
        "image": "hx-gullfoss",
        "image_alt": "Gullfoss waterfall in winter, churning between snow-covered rocks",
        "stats": [
            ("44 m", "Drop of Dettifoss into the Jökulsárgljúfur canyon"),
            ("~228 m", "Height of Morsárfoss, Iceland's tallest waterfall"),
            ("128 m", "Hengifoss, the third-highest waterfall in Iceland"),
            ("360 m³/s", "Average flow of Urriðafoss, the highest in Iceland"),
        ],
        "body": """
<p>The best waterfalls in Iceland sit along the Ring Road and the Golden Circle, so you can see the famous ones without a 4x4. On the South Coast, Seljalandsfoss and Skógafoss are about 30 km apart. Gullfoss is the end point of the Golden Circle. In the north, Dettifoss is the most powerful waterfall in Europe and Goðafoss is a short stop near Akureyri. This guide covers the main falls region by region, with heights, walking times, fees and seasons, plus a map.</p>
<!--TOC-->
<h2>Which are the best waterfalls in Iceland?</h2>
<p>If you only have time for a handful, these are the waterfalls in Iceland most worth planning around. Each one is different, which is the point: you get curtains, canyons, columns and sheer power.</p>
<ol>
<li><strong>Seljalandsfoss</strong> (South Coast): a 60 m fall with a path that runs behind it in the warmer months.</li>
<li><strong>Skógafoss</strong> (South Coast): about 60 m high and 25 m wide, with a 527-step staircase to the top.</li>
<li><strong>Gullfoss</strong> (Golden Circle): two drops of 11 m and 21 m into a deep canyon on the Hvítá river.</li>
<li><strong>Dettifoss</strong> (North): 44 m high and about 100 m wide, with an average flow of 193 m³/s.</li>
<li><strong>Goðafoss</strong> (North): a 12 m high, 30 m wide horseshoe on the Skjálfandafljót river.</li>
<li><strong>Dynjandi</strong> (Westfjords): about 100 m of tiered water, 30 m wide at the top and 60 m at the base.</li>
<li><strong>Svartifoss</strong> (Skaftafell): a 20 m fall framed by black basalt columns.</li>
<li><strong>Hengifoss</strong> (East): 128 m, with red layers in the cliff behind it.</li>
</ol>
<p>Add Gljúfrabúi and Kvernufoss on the South Coast, Brúarfoss and Háifoss inland from the Golden Circle, and Kirkjufellsfoss on Snæfellsnes if you have more time.</p>
""" + _map("Map of Iceland showing the main waterfalls around the country", "Iceland's main waterfalls. Most sit on or near the Ring Road; a few need a gravel road or a hike.") + """
<h2>How do Iceland's main waterfalls compare?</h2>
<p>Heights for Iceland's waterfalls vary between sources, because it depends where you measure from. The figures below are the commonly published ones, rounded.</p>
<div class="table-wrap"><table>
<thead><tr><th>Waterfall</th><th>Region</th><th>Height</th><th>Walk from parking</th><th>Winter access</th></tr></thead>
<tbody>
<tr><td>Seljalandsfoss</td><td>South Coast</td><td>60 m</td><td>A few minutes</td><td>Yes; path behind closed</td></tr>
<tr><td>Gljúfrabúi</td><td>South Coast</td><td>About 40 m</td><td>About 10 min from Seljalandsfoss</td><td>Often, with care</td></tr>
<tr><td>Skógafoss</td><td>South Coast</td><td>About 60 m</td><td>A few minutes</td><td>Yes</td></tr>
<tr><td>Kvernufoss</td><td>South Coast</td><td>About 30–40 m</td><td>15–20 min each way</td><td>Icy; no walk behind</td></tr>
<tr><td>Svartifoss</td><td>Skaftafell</td><td>20 m</td><td>About 45 min each way</td><td>Yes, with spikes</td></tr>
<tr><td>Gullfoss</td><td>Golden Circle</td><td>32 m in two drops</td><td>A few minutes</td><td>Yes; lower path often closed</td></tr>
<tr><td>Brúarfoss</td><td>Golden Circle</td><td>Small, very blue</td><td>About 5 min, or 3.5 km each way</td><td>Check road</td></tr>
<tr><td>Háifoss</td><td>Inland south</td><td>122 m</td><td>Short walk to viewpoint</td><td>Usually not</td></tr>
<tr><td>Kirkjufellsfoss</td><td>Snæfellsnes</td><td>Small</td><td>A few minutes</td><td>Yes</td></tr>
<tr><td>Dynjandi</td><td>Westfjords</td><td>About 100 m</td><td>15–20 min up</td><td>Pass often closed</td></tr>
<tr><td>Goðafoss</td><td>North</td><td>12 m</td><td>A few minutes</td><td>Yes</td></tr>
<tr><td>Dettifoss</td><td>North</td><td>44 m</td><td>About 800 m (west side)</td><td>West side, limited</td></tr>
<tr><td>Hengifoss</td><td>East</td><td>128 m</td><td>40–60 min up</td><td>Icy trail</td></tr>
</tbody></table></div>
<h2>Which waterfalls are on the South Coast?</h2>
<p>The South Coast has the most famous run of waterfalls in Iceland, all within a few minutes of Route 1. Seljalandsfoss is about 120 km and two hours from Reykjavík. Skógafoss is 29 km further east, and Vík is another 34 km on.</p>
<p><a href="/places/seljalandsfoss">Seljalandsfoss</a> drops 60 m from a high cliff, and a footpath runs behind the curtain when the path is free of ice. A few hundred metres north, Gljúfrabúi hides inside a narrow gorge. You reach it by wading a shallow stream into the slot.</p>
<p>Skógafoss is wide and loud, and on sunny days the spray often throws a single or double rainbow. The staircase on its east side climbs to a viewpoint at the top and is the start of the Fimmvörðuháls trail. Kvernufoss is a short walk from the Skógar museum car park, in a quiet canyon with a path behind the fall in summer.</p>
<p>Further east, Systrafoss falls above the village of Kirkjubæjarklaustur and Foss á Síðu sits beside an old farm about 10 km beyond it. Svartifoss, in <a href="/places/skaftafell">Skaftafell</a>, is a 1.9 km walk from the visitor centre. Our <a href="/blog/south-coast-waterfalls">South Coast waterfalls in one day</a> guide has a timed route.</p>
<p>One more South Coast fall is worth knowing about. Urriðafoss on the Þjórsá, Iceland's longest river, is low but carries the highest average flow of any Icelandic waterfall, about 360 m³/s.</p>
<h2>Which waterfalls can you see on the Golden Circle?</h2>
<p><a href="/places/gullfoss">Gullfoss</a> is the waterfall of the Golden Circle. The Hvítá river drops 11 m, turns, and drops another 21 m into a canyon. It carries about 140 m³/s in summer and about 80 m³/s in winter. It was sold to the state and protected in 1979, and a memorial above the falls remembers Sigríður Tómasdóttir, the farmer's daughter credited with fighting to save it.</p>
<p>Inside <a href="/places/thingvellir">Þingvellir National Park</a>, Öxarárfoss falls on the Öxará river, a short walk from the main paths. Faxi, another Golden Circle stop, is only about 7 m high but 80 m wide.</p>
<p>Brúarfoss is small but famous for its bright blue glacial water. You can walk about 3.5 km each way from a free car park on Route 37, or use a paid lot that opened in 2023, about five minutes from the falls along a rough access road.</p>
<p>East of the Golden Circle, Háifoss falls 122 m into a canyon beside its neighbour Granni. The last 7.2 km on road 332 are rough gravel, and a 4x4 is the sensible choice. See <a href="/blog/golden-circle-extra-stops">Golden Circle extra stops</a> for more detours.</p>
<h2>What are the best waterfalls in West Iceland and the Westfjords?</h2>
<p>In West Iceland, Hraunfossar is a line of small falls that seep out of the Hallmundarhraun lava field along a stretch of about 900 m. Barnafoss, the "children's falls", is close by, with viewpoints near the bridge. Glymur in Hvalfjörður was long called Iceland's tallest waterfall at about 198 m. The hike to the top takes 2.5 to 3.5 hours or more, with steep slopes and a river crossing, and is best in summer.</p>
<p>On the <a href="/places/snaefellsnes">Snæfellsnes peninsula</a>, Kirkjufellsfoss is a small fall that is famous for its view of <a href="/places/kirkjufell">Kirkjufell</a> mountain behind it. It is about 180 km from Reykjavík.</p>
<p>Dynjandi is the great waterfall of the Westfjords. It falls about 100 m in a broad, stepped fan, and six smaller named falls line the path below it. The walk up takes 15 to 20 minutes. The road over the Dynjandisheiði pass is high and exposed, so plan Dynjandi for summer. The <a href="/blog/westfjords-road-trip">Westfjords road trip</a> guide covers the drive.</p>
<h2>Which waterfalls should you see in North Iceland?</h2>
<p>Dettifoss and Goðafoss are the two essential waterfalls of the north. Dettifoss sits in Vatnajökull National Park on the Jökulsá á Fjöllum. It is 44 m high and about 100 m wide, with an average flow of 193 m³/s. Selfoss is a wide, lower fall a short walk upstream, and Hafragilsfoss is a short way downstream.</p>
<p>You can visit Dettifoss from the west on paved road 862 or from the east on gravel road 864. They give very different views and seasons, which we compare in <a href="/blog/dettifoss-east-or-west">Dettifoss: east or west side?</a></p>
<p>Goðafoss, the "waterfall of the gods", is about 45 minutes from Akureyri on the way to Mývatn. A popular story says the lawspeaker Þorgeir threw his statues of the old gods into the falls after Iceland adopted Christianity around the year 1000, although historians think the tale is much later. In the highlands, Aldeyjarfoss drops about 20 m and needs a 4x4 in summer.</p>
<h2>Which waterfalls are in East Iceland?</h2>
<p>East Iceland's headline fall is <a href="/places/hengifoss">Hengifoss</a>, at 128 m the third-highest in Iceland. The trail is about 2.5 km each way, and halfway up you pass Litlanesfoss, which is ringed by tall basalt columns. Near Egilsstaðir, Fardagafoss is a short walk from road 93, and Gufufoss sits beside the same road on the descent to Seyðisfjörður. Our <a href="/blog/east-iceland-waterfalls">East Iceland waterfalls</a> guide has the details.</p>
<h2>What are the tallest waterfalls in Iceland?</h2>
<p>Morsárfoss is the tallest waterfall in Iceland at about 228 m, but most visitors never see it up close. The tallest falls you can reach on a normal trip are Glymur, Hengifoss and Háifoss. Heights below are the commonly listed figures.</p>
<div class="table-wrap"><table>
<thead><tr><th>Waterfall</th><th>Height</th><th>Region</th></tr></thead>
<tbody>
<tr><td>Morsárfoss</td><td>About 228 m</td><td>Skaftafell, remote</td></tr>
<tr><td>Glymur</td><td>About 198 m</td><td>Hvalfjörður, West</td></tr>
<tr><td>Hengifoss</td><td>128 m</td><td>East</td></tr>
<tr><td>Háifoss</td><td>122 m</td><td>Inland south</td></tr>
<tr><td>Granni</td><td>About 101 m</td><td>Beside Háifoss</td></tr>
<tr><td>Dynjandi</td><td>About 100 m</td><td>Westfjords</td></tr>
<tr><td>Rjúkandi</td><td>About 93 m</td><td>East, beside Route 1</td></tr>
</tbody></table></div>
<p>Height is not everything. Dettifoss is only 44 m high but by far the most powerful, and Gullfoss at 32 m is one of the most impressive because of its volume and canyon.</p>
<h2>When is the best time of year to see Iceland's waterfalls?</h2>
<p>June to September is the best time for most waterfalls in Iceland. Every road is open, including the gravel roads to Háifoss and the east side of Dettifoss, the path behind Seljalandsfoss is usually open, and you get long days. Reykjavík has around 21 hours of daylight at the June solstice, so you can visit the busiest falls late in the evening when the tour buses have gone.</p>
<p>Glacier-fed rivers carry the most water in summer. Gullfoss, for example, carries about 140 m³/s in summer and about 80 m³/s in winter. Winter brings ice formations, quiet car parks and the chance of the aurora over a waterfall, but only four to five hours of daylight in December.</p>
<p>Spring and autumn are a good middle ground, with fewer people and enough light, though the first frosts can close the path behind Seljalandsfoss from autumn.</p>
<h2>Which waterfalls need a 4x4 or a long hike?</h2>
<p>Most of the famous falls are a short walk from a paved car park, but a few take more effort:</p>
<ul>
<li><strong>Háifoss and Granni:</strong> rough gravel on road 332; best from June to mid-September.</li>
<li><strong>Aldeyjarfoss:</strong> in the highlands; a 4x4 and a summer visit.</li>
<li><strong>Glymur:</strong> a hike of several hours with a river crossing.</li>
<li><strong>Dettifoss east side:</strong> gravel road 864, usually open only in summer.</li>
<li><strong>Morsárfoss:</strong> Iceland's tallest waterfall at about 228 m. It was revealed as the Morsárjökull glacier retreated and overtook Glymur as the tallest in 2011. It is remote and not a casual walk.</li>
</ul>
<h2>Can you walk behind a waterfall in Iceland?</h2>
<p>Yes, at a few. Seljalandsfoss has a footpath behind it, closed when ice forms, usually from about November to March. Kvernufoss near Skógar has a path into a cave behind the fall when it is free of snow. Near Egilsstaðir, you can step behind Fardagafoss to the remains of an old cave. At Gljúfrabúi you walk into the gorge, not behind the water. Full details are in <a href="/blog/waterfalls-you-can-walk-behind">waterfalls you can walk behind</a>.</p>
<h2>Do you have to pay to visit Iceland's waterfalls?</h2>
<p>The waterfalls themselves are free, but many car parks now charge. Fees are per vehicle and usually paid by app, online or at a machine. Cameras read number plates at some sites, so pay before you leave to avoid a higher charge later.</p>
<div class="table-wrap"><table>
<thead><tr><th>Site</th><th>Car parking (2026)</th></tr></thead>
<tbody>
<tr><td>Seljalandsfoss</td><td>About ISK 900 for 24 hours</td></tr>
<tr><td>Skógafoss</td><td>About ISK 1,000</td></tr>
<tr><td>Skaftafell (for Svartifoss)</td><td>About ISK 1,100</td></tr>
<tr><td>Hengifoss</td><td>About ISK 1,000 for the day</td></tr>
<tr><td>Kirkjufellsfoss</td><td>About ISK 700–1,000</td></tr>
<tr><td>Dynjandi</td><td>Per-car service charge since 2024</td></tr>
</tbody></table></div>
<p>Prices change at short notice, so treat these as a guide.</p>
<h2>Can you visit Iceland's waterfalls in winter?</h2>
<p>Yes. Most of the Ring Road waterfalls stay open all year, and they look completely different with ice around them. Seljalandsfoss, Skógafoss, Gullfoss and Goðafoss are all reachable in normal winter conditions. The path behind Seljalandsfoss and the lower path at Gullfoss close when they ice up. Dettifoss east, Háifoss, Aldeyjarfoss and Dynjandi depend on roads that are closed or not serviced for much of the winter. See <a href="/blog/iceland-waterfalls-in-winter">Iceland's waterfalls in winter</a> for what stays open.</p>
<p class="callout">Pack microspikes from October to April. Spray freezes on every path and step near a waterfall, and the ice is often clear and hard to see.</p>
<h2>How do you stay safe at Iceland's waterfalls?</h2>
<ul>
<li><strong>Stay on the marked paths.</strong> Ropes and fences are there because of loose edges, falling rocks or slippery rock.</li>
<li><strong>Respect closures.</strong> If a path is closed, it is closed for a reason, usually ice or rockfall.</li>
<li><strong>Dress for spray.</strong> A waterproof jacket and trousers keep you dry at Seljalandsfoss, Skógafoss and Dettifoss.</li>
<li><strong>Watch for falling ice in winter.</strong> Icicles and ice sheets break off cliffs as the day warms.</li>
<li><strong>Check conditions daily.</strong> Use umferdin.is for roads, vedur.is for wind and weather, and safetravel.is for alerts.</li>
</ul>
<h2>How do you plan a waterfall trip around Iceland?</h2>
<p>Build the trip around the Ring Road and add detours. A day on the South Coast covers Seljalandsfoss, Gljúfrabúi, Skógafoss and Kvernufoss. A Golden Circle day gives you Gullfoss, Öxarárfoss and Faxi. On a full Ring Road trip, add Svartifoss, Hengifoss, Dettifoss and Goðafoss. Leave Dynjandi and Kirkjufellsfoss for separate trips to the west.</p>
<p>Visit the busiest falls early in the morning or in the long summer evenings to avoid crowds. If you want photos, our <a href="/blog/photographing-iceland-waterfalls">waterfall photography guide</a> covers settings, filters and light. For routes, start with the <a href="/blog/iceland-ring-road-guide">Ring Road guide</a>, explore every sight on our <a href="/highlights">highlights map</a>, and if you like to plan on paper, our <a href="/#guides">printed guidebooks</a> cover the whole country by season.</p>
""",
        "checked_note": "Facts checked October 2026. Waterfall heights vary between sources. Parking fees, path closures and winter road service change often; check umferdin.is, vedur.is and safetravel.is before you go.",
        "sources": [
            ("List of waterfalls in Iceland (Wikipedia)", "https://en.wikipedia.org/wiki/List_of_waterfalls_in_Iceland"),
            ("Dettifoss (North Iceland Marketing Office)", "https://www.northiceland.is/diamondcircle/dettifoss"),
            ("Gullfoss (Wikipedia)", "https://en.wikipedia.org/wiki/Gullfoss"),
            ("Explore the waterfalls of the South Coast (South Iceland)", "https://south.is/en/travel-info/newsblog/explore-the-waterfalls-of-the-south-coast-of-iceland"),
            ("Hengifoss and Litlanesfoss (East Iceland)", "https://www.east.is/en/natural-and-cultural-monuments/hengifoss-and-litlanesfoss-waterfalls"),
            ("Dynjandi waterfall (isnet)", "https://isnet.is/iceland/westfjords/dynjandi/"),
            ("Parking fees and road tolls in Iceland (Happy Campers)", "https://happycampers.is/driving-in-iceland-parking-fees-and-road-tolls/"),
            ("Waterfalls in Iceland (Guide to Iceland)", "https://guidetoiceland.is/nature-info/waterfalls-in-iceland"),
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "south-coast-waterfalls",
        "cluster": "waterfalls",
        "pillar": False,
        "short": "South Coast Waterfalls in One Day",
        "title": "South Coast Iceland Waterfalls: A One-Day Route From Reykjavík (2027)",
        "description": "South Coast Iceland waterfalls in one day: Seljalandsfoss, Gljúfrabúi, Skógafoss and Kvernufoss, with drive times from Reykjavík, walks, parking fees and tips.",
        "category": "Nature · Waterfalls",
        "teaser": "Seljalandsfoss, Gljúfrabúi, Skógafoss and Kvernufoss in a single day.",
        "image": "hx-solheimajokull",
        "image_alt": "The ash-streaked ice of Sólheimajökull with a waterfall in the cliffs above",
        "stats": [
            ("~120 km", "Reykjavík to Seljalandsfoss, about two hours"),
            ("29 km", "Seljalandsfoss to Skógafoss on Route 1"),
            ("527", "Steps up the staircase beside Skógafoss"),
            ("187 km", "Reykjavík to Vík, about 2.5 hours"),
        ],
        "body": """
<p>You can see the four best South Coast Iceland waterfalls in one day: Seljalandsfoss, Gljúfrabúi, Skógafoss and Kvernufoss. They sit within about 30 km of each other on Route 1, two hours east of Reykjavík. Allow a full day for the round trip, or continue to Vík and stay the night. Here is the route, with drive times, walks, fees and what each fall is like.</p>
<!--TOC-->
<h2>Which waterfalls can you see on the South Coast in one day?</h2>
<p>In one day from Reykjavík you can comfortably see Seljalandsfoss, Gljúfrabúi, Skógafoss and Kvernufoss, and still add a black-sand beach. These four are the core of the South Coast. Svartifoss in Skaftafell is also a South Coast waterfall, but it is 140 km beyond Vík, so it belongs on a two-day trip.</p>
<p>Seljalandsfoss and Gljúfrabúi share a car park. Skógafoss and Kvernufoss share the village of Skógar. That means only two real stops, each with a walk, which keeps the day relaxed even with short winter light.</p>
""" + _map("Map of Iceland's main waterfalls, including Seljalandsfoss and Skógafoss on the South Coast", "The South Coast waterfalls sit together on Route 1 east of Reykjavík.") + """
<figure class="a-figure a-map"><a href="/assets/img/map-south-coast-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-south-coast-1800.jpg" srcset="/assets/img/map-south-coast-800.jpg 800w, /assets/img/map-south-coast-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="Detailed map of Iceland's South Coast with Seljalandsfoss, Skógafoss, Systrafoss, Foss á Síðu and Svartifoss marked" loading="lazy" decoding="async"></a><figcaption>The South Coast in detail: Seljalandsfoss and Gljúfrabúi (1), Skógafoss (3), Systrafoss (10), Foss á Síðu (11) and Svartifoss in Skaftafell (12), all close to Route 1. Tap to open full size.</figcaption></figure>
""" + """
<h2>What is the best one-day route?</h2>
<p>Drive east on Route 1 and work your way along the coast. Times are for good summer conditions and do not include stops.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stop</th><th>Drive from previous</th><th>Time to allow</th></tr></thead>
<tbody>
<tr><td>1. Seljalandsfoss</td><td>About 120 km, 2 h from Reykjavík</td><td>45–60 min</td></tr>
<tr><td>2. Gljúfrabúi</td><td>On foot, about 10 min</td><td>20–30 min</td></tr>
<tr><td>3. Skógafoss</td><td>29 km, about 25 min</td><td>45–60 min with the stairs</td></tr>
<tr><td>4. Kvernufoss</td><td>On foot from the Skógar museum, 15–20 min</td><td>About 1 h</td></tr>
<tr><td>5. Optional: Reynisfjara and Vík</td><td>About 34 km to Vík</td><td>1–2 h</td></tr>
</tbody></table></div>
<p>Reykjavík to Vík is about 187 km, roughly 2.5 hours of driving. If you go all the way to Vík and back in a day, you will drive about five hours. Leave Reykjavík by 08:00 to beat the tour buses to Seljalandsfoss.</p>
<h2>What is Seljalandsfoss like?</h2>
<p><a href="/places/seljalandsfoss">Seljalandsfoss</a> falls about 60 m from a cliff at the foot of the Eyjafjallajökull glacier. Its party trick is the footpath behind the water, so you can see the valley through the curtain. Wear waterproofs: the spray soaks you within a minute.</p>
<p>The path behind the falls is slippery even in summer. It is closed when ice builds up, roughly from November to March, and the farm that runs the site enforces it. Parking costs about ISK 900 for 24 hours (2026), paid at a machine or online.</p>
<h2>How do you find Gljúfrabúi?</h2>
<p>Gljúfrabúi is a few hundred metres north of Seljalandsfoss, about a 10-minute walk along the foot of the cliff past several smaller falls. The roughly 40 m waterfall is hidden inside a narrow gorge. To see it, you step through a slot in the rock and wade a stream that is usually 10 to 30 cm deep.</p>
<p>Bring waterproof shoes or sandals if you want to go in. Rocks can fall in the gorge, so do not linger under the walls. If you would rather stay dry, you can still glimpse it through the slot from outside.</p>
<h2>What is there to see at Skógafoss?</h2>
<p>Skógafoss is about 60 m high and 25 m wide, a solid wall of water you can walk right up to On sunny days the spray often makes a single or double rainbow. Parking costs about ISK 1,000 (2026), paid through an app.</p>
<p>A 527-step staircase on the east side climbs to a platform at the top. The path from the top is the start of the Fimmvörðuháls trail between the glaciers, so you can walk as far as you like and turn back. Our <a href="/blog/fimmvorduhals-hike">Fimmvörðuháls guide</a> covers the full route.</p>
<p>A local legend says the first settler, Þrasi, hid a chest of treasure behind the falls. The Skógar museum next door has an old church door ring said to come from it.</p>
<h2>Is Kvernufoss worth the walk?</h2>
<p>Yes. Kvernufoss is a quiet 30 to 40 m fall in its own canyon, about 1.5 km east of Skógafoss. Start from the Skógar museum car park and follow the path along the Kverna river. It takes 15 to 20 minutes each way.</p>
<p>Part of the route crosses private land, so you climb a small ladder stile over a fence, which can be awkward for some walkers. In summer, when the area is free of snow, a path leads behind the fall into a large cave. The museum car park may charge a small fee.</p>
<h2>Can you add a beach or a glacier?</h2>
<p>Yes, if you start early. Between Skógar and Vík, the side road to the <a href="/places/solheimajokull">Sólheimajökull</a> glacier is a popular detour; only walk on the ice with a guide. <a href="/places/reynisfjara">Reynisfjara</a> black-sand beach is just west of Vík.</p>
<p class="callout">At Reynisfjara, never turn your back on the sea and stay well above the wet sand. Sneaker waves reach far up the beach without warning. Swimming there is never safe.</p>
<p>For more stops along this coast, see our <a href="/blog/south-coast-iceland">South Coast guide</a>.</p>
<h2>Which other waterfalls are along the South Coast?</h2>
<p>With a second day, keep driving east. Systrafoss falls above Kirkjubæjarklaustur, and Foss á Síðu sits beside an old farm about 10 km further on. Svartifoss in <a href="/places/skaftafell">Skaftafell</a> is a 20 m fall framed by black basalt columns, about 1.9 km and 45 minutes each way from the visitor centre.</p>
<p>Closer to Reykjavík, Urriðafoss on the Þjórsá river is a short detour from Route 1. It is low but has the highest average flow of any Icelandic waterfall. The access road is bumpy, and harder in winter.</p>
<h2>What should you bring for a South Coast waterfall day?</h2>
<ul>
<li><strong>Full waterproofs.</strong> Jacket and trousers for the spray at Seljalandsfoss and Skógafoss.</li>
<li><strong>Waterproof shoes or sandals.</strong> For the stream into Gljúfrabúi, plus spare socks.</li>
<li><strong>A payment app or card.</strong> Most car parks are paid by app, online or at a machine, not cash.</li>
<li><strong>Food and fuel.</strong> Services between towns are limited, so bring snacks and fill up before you leave the Reykjavík area.</li>
<li><strong>Microspikes from October to April.</strong> Spray freezes on paths and steps.</li>
</ul>
<h2>When is the best time to see the South Coast waterfalls?</h2>
<p>Summer is easiest. From June to August you have up to 21 hours of daylight, the path behind Seljalandsfoss is open, and you can visit in the quiet evening hours. Midday in July and August is the busiest time at every stop.</p>
<p>Winter has its own reward: ice around the falls and few people. But daylight in December is only about four to five hours, and the paths are icy. Wear microspikes and check umferdin.is and vedur.is each morning. Our <a href="/blog/iceland-waterfalls-in-winter">winter waterfalls guide</a> explains what is open. For every waterfall around the island, see <a href="/blog/waterfalls-in-iceland">Iceland's best waterfalls</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Drive times are for good conditions without stops. Parking fees and the seasonal closure of the path behind Seljalandsfoss change; check on arrival and on safetravel.is.",
        "sources": [
            ("Reykjavík to Diamond Beach: full driving guide (Guide to Iceland)", "https://guidetoiceland.is/travel-info/reykjavik-to-diamond-beach-full-driving-guide"),
            ("Walking behind Seljalandsfoss and finding Gljúfrabúi (isnet)", "https://isnet.is/iceland/south-iceland/seljalandsfoss/"),
            ("Skógafoss (Wikipedia)", "https://en.wikipedia.org/wiki/Sk%C3%B3gafoss"),
            ("Explore the waterfalls of the South Coast (South Iceland)", "https://south.is/en/travel-info/newsblog/explore-the-waterfalls-of-the-south-coast-of-iceland"),
            ("Tips for visiting Kvernufoss (Adventurous Kate)", "https://www.adventurouskate.com/?p=31402"),
            ("Parking fees and road tolls in Iceland (Happy Campers)", "https://happycampers.is/driving-in-iceland-parking-fees-and-road-tolls/"),
            ("Iceland daylight hours (Go Campers)", "https://www.gocampers.is/guides/weather/iceland-daylight-hours/"),
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "waterfalls-you-can-walk-behind",
        "cluster": "waterfalls",
        "pillar": False,
        "short": "Waterfalls You Can Walk Behind in Iceland",
        "title": "Walk Behind a Waterfall in Iceland: Where, When and How (2027)",
        "description": "Where you can walk behind a waterfall in Iceland: Seljalandsfoss, Kvernufoss and Fardagafoss, when the paths close for ice, and what to wear to stay dry.",
        "category": "Nature · Waterfalls",
        "teaser": "Seljalandsfoss, Kvernufoss and Fardagafoss, and when their paths close.",
        "image": "hx-seljalandsfoss",
        "image_alt": "Seljalandsfoss waterfall falling from a mossy cliff into a green valley",
        "stats": [
            ("60 m", "Height of Seljalandsfoss, the classic walk-behind fall"),
            ("Nov–Mar", "Rough period the Seljalandsfoss path is closed for ice"),
            ("15–20 min", "Walk each way to Kvernufoss from Skógar"),
            ("10–30 cm", "Usual depth of the stream into Gljúfrabúi"),
        ],
        "body": """
<p>You can walk behind a waterfall in Iceland at three places: Seljalandsfoss and Kvernufoss on the South Coast, and Fardagafoss near Egilsstaðir in the east. All three paths are seasonal. They close or become unsafe once spray freezes, which usually means from about November to March. Nearby Gljúfrabúi lets you walk into its gorge, but not behind the water. Here is what each one is like and when you can go.</p>
<!--TOC-->
<h2>Which waterfalls can you walk behind in Iceland?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Waterfall</th><th>Where</th><th>Behind the water?</th><th>When</th></tr></thead>
<tbody>
<tr><td>Seljalandsfoss</td><td>South Coast, Route 1</td><td>Yes, on a footpath</td><td>Usually closed about Nov–Mar for ice</td></tr>
<tr><td>Kvernufoss</td><td>Skógar, South Coast</td><td>Yes, into a cave</td><td>When free of snow; not in winter</td></tr>
<tr><td>Fardagafoss</td><td>Near Egilsstaðir, East</td><td>Yes, to the remains of a cave</td><td>Summer; slippery in rain</td></tr>
<tr><td>Gljúfrabúi</td><td>Beside Seljalandsfoss</td><td>No, you wade into the gorge</td><td>Most of the year, with care</td></tr>
</tbody></table></div>
<p>Skógafoss, <a href="/places/gullfoss">Gullfoss</a>, Svartifoss, Dettifoss and the other big falls do not have paths behind them. Do not climb over ropes to try. The rock around a waterfall is wet, mossy and often loose, and the safe routes are the ones that have been built and marked.</p>
""" + _map("Map of Iceland's main waterfalls, including Seljalandsfoss on the South Coast", "Seljalandsfoss and Kvernufoss are on the South Coast; Fardagafoss is near Egilsstaðir in the east.") + """
<h2>Can you walk behind Seljalandsfoss?</h2>
<p>Yes. <a href="/places/seljalandsfoss">Seljalandsfoss</a> is the best-known waterfall you can walk behind in Iceland. A footpath runs from the car park, behind the 60 m curtain of water, and back out on the other side. From the hollow behind the falls you look out at the valley through the water.</p>
<p>The path is gravel and rock with steps and a metal staircase, and it is wet and slippery all year. Expect to be soaked by spray, especially on the far side. </p>
<p>In 2023 rockfall from the cliff closed the full loop for a time, and walkers had to return the way they came. Follow the signs on the day: if part of the path is closed, there is a reason.</p>
<h2>When is the path behind Seljalandsfoss closed?</h2>
<p>The path behind Seljalandsfoss closes when ice forms, which is roughly from November to March. Spray freezes on the cliff and the path into thick ice, and icicles can fall. The farm that runs the site closes the path, and the closure is not a suggestion.</p>
<p>The exact dates change every year with the weather. A mild spell can open it briefly; an early frost in October can close it. You can still see the falls from the front all winter. Our <a href="/blog/iceland-waterfalls-in-winter">winter waterfalls guide</a> explains what else is open.</p>
<h2>Can you walk behind Kvernufoss?</h2>
<p>Yes, when the area is free of snow. Kvernufoss is a 30 to 40 m fall in a small canyon about 1.5 km east of Skógafoss. A path leads around the side of the fall into a large cave behind it. You get wet on the way in, but the cave itself is fairly dry. Go out the way you came in.</p>
<p>Park at the Skógar museum and follow the path along the Kverna river. It is mostly flat and takes 15 to 20 minutes each way, with a short steep drop into the canyon at the end. The ground behind the fall is uneven and rocky.</p>
<p>Part of the trail crosses private farmland, so you climb a small ladder stile over a fence. There is no other way around, which matters if you have limited mobility. Respect the land and take your rubbish with you. In winter the trail freezes, and going behind the falls in snow and ice is not safe.</p>
<h2>Can you walk behind Fardagafoss?</h2>
<p>Yes. Fardagafoss is a 20 m fall at the foot of the Fjarðarheiði mountain pass, about 5 km from Egilsstaðir on road 93. A marked trail leads up from a small parking area by the road. The full walk is about 2.6 km there and back, and the final section to the falls is a bit harder to cross.</p>
<p>Behind the water are the remains of a cave. Local legend says a giantess lived there, with a tunnel under the mountain to Gufufoss in Seyðisfjörður. The rock is slippery after rain, so this is a summer walk. See <a href="/blog/east-iceland-waterfalls">East Iceland waterfalls</a> for nearby stops.</p>
<h2>Is Gljúfrabúi a walk-behind waterfall?</h2>
<p>Not quite. Gljúfrabúi, a few hundred metres north of Seljalandsfoss, drops about 40 m into a narrow gorge. You walk into the gorge through a slot in the rock to stand in front of the water, not behind it.</p>
<p>The entrance is a stream that is usually 10 to 30 cm deep, so wear waterproof boots or sandals. The rock walls can shed stones. If you prefer to stay dry, you can still glimpse the falls through the slot from outside.</p>
<h2>Can you see them all in one trip?</h2>
<p>Seljalandsfoss and Kvernufoss fit easily into one day. They are 29 km apart on Route 1, about 25 minutes by car, and Gljúfrabúi shares the Seljalandsfoss car park. Start at Seljalandsfoss, walk on to Gljúfrabúi, then drive to Skógar for Skógafoss and the walk to Kvernufoss.</p>
<p>Fardagafoss is on the other side of the country, about 5 km from Egilsstaðir in East Iceland. It fits into a Ring Road trip on the day you pass through Egilsstaðir, or on the drive over to Seyðisfjörður. Plan all three for the summer months, when the paths are most likely to be open and free of ice.</p>
<h2>What should you wear to walk behind a waterfall?</h2>
<ul>
<li><strong>Waterproof jacket and trousers.</strong> You will be wet through in a minute without them.</li>
<li><strong>Boots with good grip.</strong> Wet rock and moss are slippery in every season.</li>
<li><strong>Spare socks and a towel in the car.</strong> Especially for Gljúfrabúi.</li>
<li><strong>A phone pouch or camera rain cover.</strong> The spray is fine and gets into everything.</li>
<li><strong>Microspikes outside summer.</strong> Frozen spray makes approach paths icy even when the area behind the fall is closed.</li>
</ul>
<p class="callout">Visit Seljalandsfoss early in the morning or after 18:00 in summer. The path behind the falls is narrow, and around midday it fills with tour groups.</p>
<h2>Is it safe to walk behind Iceland's waterfalls?</h2>
<p>It is safe on the open, marked paths in the right season, if you take care. The risks are slipping on wet rock, falling stones and, in cold weather, falling ice. Stay on the path, keep children close, and do not climb onto rocks for a photo. When a path is roped off or signed closed, stay out.</p>
<p>For more on photographing the view through the curtain, see our <a href="/blog/photographing-iceland-waterfalls">waterfall photography guide</a>. To see all the falls on one map, start with <a href="/blog/waterfalls-in-iceland">Iceland's best waterfalls</a>, and for the rest of the coast, the <a href="/blog/south-coast-waterfalls">South Coast waterfalls route</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Seasonal closures at Seljalandsfoss and conditions at Kvernufoss depend on the weather each year; follow signs on site and check safetravel.is.",
        "sources": [
            ("Seljalandsfoss waterfall (South Iceland)", "https://south.is/en/place/seljalandsfoss-waterfall"),
            ("Walking behind Seljalandsfoss and finding Gljúfrabúi (isnet)", "https://isnet.is/iceland/south-iceland/seljalandsfoss/"),
            ("Not possible to walk the circular route (Iceland Monitor, 2023)", "https://icelandmonitor.mbl.is/news/news/2023/04/23/not_possible_to_walk_the_circular_route"),
            ("Kvernufoss (Wikipedia)", "https://en.wikipedia.org/wiki/Kvernufoss"),
            ("Tips for visiting Kvernufoss (Adventurous Kate)", "https://www.adventurouskate.com/?p=31402"),
            ("Fardagafoss hiking trail (East Iceland)", "https://east.is/en/place/fardagafoss"),
            ("Fardagafoss (Iceland Travel Guide)", "https://icelandtravelguide.is/locations/fardagafoss/"),
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "dettifoss-east-or-west",
        "cluster": "waterfalls",
        "pillar": False,
        "short": "Dettifoss: East or West Side?",
        "title": "Dettifoss East or West? Roads 862 and 864 and Winter Access (2027)",
        "description": "Dettifoss east or west: how the two sides compare, roads 862 and 864, walks to Selfoss and Hafragilsfoss, spray, facilities and which side is open in winter.",
        "category": "Nature · Waterfalls",
        "teaser": "Paved road 862 or gravel road 864: views, walks and winter access.",
        "image": "hx-braided-rivers",
        "image_alt": "Black meltwater channels branching across a snow-covered plain",
        "stats": [
            ("44 m", "Drop of Dettifoss into Jökulsárgljúfur canyon"),
            ("193 m³/s", "Average flow of the Jökulsá á Fjöllum at Dettifoss"),
            ("~100 m", "Width of Dettifoss"),
            ("34 km", "Canyon trail from Dettifoss to Ásbyrgi"),
        ],
        "body": """
<p>Dettifoss has two sides, and you choose by season and by how much effort you want. The west side, on paved road 862, has a large car park, platforms that face the falls and the only realistic access outside summer. The east side, on gravel road 864, is open only in summer, has less spray and lets you get closer. If you want one answer on the Dettifoss east or west question: go west unless you are travelling in summer and want the wilder side.</p>
<!--TOC-->
<h2>Should you visit Dettifoss from the east or the west?</h2>
<p>For most visitors, the west side is the better choice. It is paved all the way, has the bigger car park, and its platforms look at Dettifoss head-on, so you see a larger part of the falls. It is also the only side with any winter road service.</p>
<p>The east side suits summer travellers who want a rougher, quieter visit. You see the falls from the side but can stand closer, and the spray usually blows the other way. It is also the side for Hafragilsfoss, the next waterfall downstream.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>West side (road 862)</th><th>East side (road 864)</th></tr></thead>
<tbody>
<tr><td>Road</td><td>Paved</td><td>Gravel, narrow, slow</td></tr>
<tr><td>From Route 1</td><td>About 24 km, 20 min</td><td>About 32 km, 45 min</td></tr>
<tr><td>Season</td><td>Most of the year; limited winter service</td><td>Summer only, no winter service</td></tr>
<tr><td>View</td><td>Head-on, from platforms</td><td>From the side, closer to the edge</td></tr>
<tr><td>Spray</td><td>Often heavy</td><td>Little to none</td></tr>
<tr><td>Walk to Dettifoss</td><td>About 800 m to the upper viewpoint</td><td>About 400 m, steep and rocky</td></tr>
<tr><td>Car park</td><td>Large, with toilets</td><td>Small, fills up in summer</td></tr>
</tbody></table></div>
""" + _map("Map of Iceland's main waterfalls, with Dettifoss in the north-east", "Dettifoss and Selfoss sit on the Jökulsá á Fjöllum in the north, between Mývatn and Ásbyrgi.") + """
<h2>What is Dettifoss?</h2>
<p>Dettifoss is a waterfall on the Jökulsá á Fjöllum, a glacial river flowing north from Vatnajökull. It drops 44 m into the Jökulsárgljúfur canyon and is about 100 m wide. With an average flow of 193 m³/s, it is described as the most powerful waterfall in Europe. The falls are inside <a href="/places/vatnajokull">Vatnajökull National Park</a>, which reaches from the ice cap all the way north to this canyon.</p>
<p>Selfoss is a wider, lower fall, about 11 m high, a short walk upstream. Hafragilsfoss is a short distance downstream. A 34 km hiking trail follows the canyon from Dettifoss north to Ásbyrgi.</p>
<h2>What is the west side of Dettifoss like?</h2>
<p>The west side is the easy, well-built side. Road 862 is paved from Route 1 to the car park, about 24 km or 20 minutes, and roughly 45 minutes from Mývatn. The paved road continues north to Ásbyrgi and Route 85. It was opened in stages from 2010 to 2021 and completed the Diamond Circle loop.</p>
<p>From the car park it is about 800 m, mostly downhill, to the upper viewpoint. A steeper path leads down to a lower viewpoint, and the climb back up takes effort. The platforms face the falls, so you see the full width of the water.</p>
<p>The trade-off is spray. On many days the wind blows a heavy mist across the west platforms. Bring a waterproof jacket and a cloth for your lens, and on a windy day the upper viewpoint may not be worth the soaking.</p>
<h2>What is the east side of Dettifoss like?</h2>
<p>The east side is wilder and quieter. Road 864 is a narrow gravel road that runs between Route 85 and Route 1, about 45 minutes and 32 km from the Ring Road. Drive it slowly. It usually reopens around the end of May and closes again in autumn, depending on snow and mud.</p>
<p>The car park is small, and in summer it can fill by late morning. From there, a steep, rocky path of about 400 m takes about 10 minutes down to the falls. You can stand close to the edge here, and there is usually little spray, which makes it the better side for photos.</p>
<p>From the east car park it is a 3 km drive north to a separate lot for Hafragilsfoss. A few minutes' walk leads to a viewpoint over the canyon.</p>
<h2>How do you walk to Selfoss?</h2>
<p>Selfoss is about 1 km upstream of Dettifoss on both sides of the river. On the west side, a rocky trail of about 1 km leads from the lower Dettifoss viewpoint. The loop from the car park to Dettifoss, Selfoss and back is about 2.5 km and takes about an hour.</p>
<p>On the east side the trail to Selfoss is rougher, with some boulder scrambling, and the loop takes about 1.5 hours. From the west side you see only part of Selfoss, so the east side gives the fuller view.</p>
<h2>Can you visit Dettifoss in winter?</h2>
<p>Only from the west side, and not always. Road 864 on the east side has no winter service at all and is closed in winter. Road 862 on the west side gets some winter service until the end of December and again from around mid-March. Between those dates it is not serviced and can be closed by snow, and storms can close it at short notice at any time.</p>
<p>Check the road status on umferdin.is and the forecast on vedur.is before setting out, and turn back if conditions change. The paths to the viewpoints are icy in winter, so wear microspikes and stay well back from frozen edges. Our <a href="/blog/iceland-waterfalls-in-winter">winter waterfalls guide</a> covers the other northern falls.</p>
<p class="callout">If road 862 is closed, Goðafoss on the way between Akureyri and Mývatn is a reliable winter alternative. It is about 45 minutes from Akureyri.</p>
<h2>Can you fly a drone at Dettifoss?</h2>
<p>Only on the west side, and only within set times. Vatnajökull National Park allows recreational drones over the canyon on the west side of Dettifoss, not north of the northernmost viewing platform. Flying is banned in most of the rest of Jökulsárgljúfur. The allowed hours change by season, so check the park's drone rules before you fly.</p>
<h2>What should you bring to Dettifoss?</h2>
<p>Bring a waterproof jacket for the spray on the west side, and boots with good grip for the rocky paths, especially to Selfoss and the lower viewpoints. The paths are uneven and steep in places, so take your time. In the shoulder months and winter, add microspikes. There are no shops at the falls, so bring water and snacks, and fill up with fuel in Mývatn or on the Ring Road before you turn off.</p>
<h2>How do you fit Dettifoss into a trip?</h2>
<p>Most people visit Dettifoss on a day around Mývatn, or as part of the Diamond Circle with Húsavík, Ásbyrgi and Goðafoss. Driving the Ring Road from the east, it makes a natural stop on the way to Mývatn. Allow one to two hours for Dettifoss and Selfoss from one side.</p>
<p>See the <a href="/blog/north-iceland-guide">North Iceland guide</a> for the rest of the region, the <a href="/blog/iceland-ring-road-guide">Ring Road guide</a> for routes, and <a href="/blog/waterfalls-in-iceland">Iceland's best waterfalls</a> for every major fall on one map. The <a href="/highlights">highlights map</a> shows the other sights of the north.</p>
""",
        "checked_note": "Facts checked October 2026. Winter service on road 862 and the opening date of road 864 change with the weather each year; check umferdin.is and the Vatnajökull National Park pages before you go.",
        "sources": [
            ("Dettifoss (North Iceland Marketing Office)", "https://www.northiceland.is/diamondcircle/dettifoss"),
            ("Dettifoss (Visit Akureyri)", "https://www.visitakureyri.is/en/see-and-do/attractions/dettifoss"),
            ("Dettifoss (Wikipedia)", "https://en.wikipedia.org/wiki/Dettifoss"),
            ("Dettifoss east vs west (Earth Trekkers)", "https://www.earthtrekkers.com/?p=36413"),
            ("Selfoss waterfall guide (Campervan Iceland)", "https://www.campervaniceland.com/blog/things-to-do/selfoss-waterfall"),
            ("Diamond Circle (Wikipedia)", "https://en.wikipedia.org/wiki/Diamond_Circle"),
            ("Drone rules (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/drone-rules"),
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "east-iceland-waterfalls",
        "cluster": "waterfalls",
        "pillar": False,
        "short": "East Iceland Waterfalls: Hengifoss and More",
        "title": "East Iceland Waterfalls: Hengifoss, Fardagafoss and Gufufoss (2027)",
        "description": "East Iceland waterfalls near Egilsstaðir: the Hengifoss and Litlanesfoss hike, Fardagafoss, Gufufoss on the road to Seyðisfjörður and Rjúkandi on Route 1.",
        "category": "Nature · Waterfalls",
        "teaser": "Hengifoss, Litlanesfoss, Fardagafoss, Gufufoss and Rjúkandi around Egilsstaðir.",
        "image": "hx-hengifoss",
        "image_alt": "Hengifoss waterfall falling past red and black rock layers",
        "stats": [
            ("128 m", "Hengifoss, the third-highest waterfall in Iceland"),
            ("~5 km", "Round-trip walk to Hengifoss"),
            ("25–30 m", "Litlanesfoss, ringed by basalt columns"),
            ("~5 km", "From Egilsstaðir to Fardagafoss"),
        ],
        "body": """
<p>The best East Iceland waterfalls are all within reach of Egilsstaðir. Hengifoss, at 128 m the third-highest in the country, is a 5 km return hike that also passes Litlanesfoss and its basalt columns. Fardagafoss and Gufufoss are short stops on road 93 to Seyðisfjörður, and Rjúkandi falls beside Route 1 in Jökuldalur. Together they make an easy day from Egilsstaðir.</p>
<!--TOC-->
<h2>What are the best waterfalls in East Iceland?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Waterfall</th><th>Height</th><th>Where</th><th>Walk</th></tr></thead>
<tbody>
<tr><td>Hengifoss</td><td>128 m</td><td>Fljótsdalur, south-west of Egilsstaðir</td><td>About 2.5 km each way, 40–60 min up</td></tr>
<tr><td>Litlanesfoss</td><td>About 25–30 m</td><td>Halfway up the Hengifoss trail</td><td>About 20–30 min up</td></tr>
<tr><td>Fardagafoss</td><td>About 20 m</td><td>Road 93, about 5 km from Egilsstaðir</td><td>About 2.6 km return</td></tr>
<tr><td>Gufufoss</td><td>About 27 m</td><td>Road 93, above Seyðisfjörður</td><td>Roadside</td></tr>
<tr><td>Rjúkandi</td><td>About 93 m</td><td>Route 1, Jökuldalur</td><td>Short stop</td></tr>
</tbody></table></div>
<p>If you only have time for one, choose Hengifoss. If you have an hour, Fardagafoss and Gufufoss fit easily into a drive to Seyðisfjörður.</p>
""" + _map("Map of Iceland's main waterfalls, with Hengifoss in East Iceland", "Iceland's main waterfalls. Hengifoss is south-west of Egilsstaðir in the east.") + """
<h2>How do you hike to Hengifoss?</h2>
<p><a href="/places/hengifoss">Hengifoss</a> is a 128 m waterfall on the Hengifossá river in Fljótsdalur. The hike is about 2.5 km each way, around 5 km in total. It climbs about 250 to 300 m and is steepest near the start. Allow 40 to 60 minutes up and 1.5 to 2 hours in total with stops.</p>
<p>What makes Hengifoss different is the cliff behind it. Bands of black basalt alternate with thin red layers, like a layer cake. At the base are sedimentary layers about 5 to 6 million years old, with lignite at the top, the remains of an ancient forest.</p>
<p>The trail ends at a viewpoint in front of the falls. Do not continue into the gorge below the cliff, especially in winter, when ice can fall.</p>
<h2>Is the Hengifoss hike difficult?</h2>
<p>The Hengifoss hike is moderate. It is a steady uphill walk on a clear path, and most reasonably fit walkers manage it without trouble. The steepest section is near the start, and benches along the trail give you places to rest. Walking boots are better than trainers, because the path is loose and stony in places and can be muddy after rain.</p>
<p>Coming down is quicker but harder on the knees. In winter and early spring the trail can be icy, and traction spikes make a big difference. If the weather turns, Litlanesfoss is a good point to turn back.</p>
<h2>What is Litlanesfoss?</h2>
<p>Litlanesfoss is the smaller waterfall you pass about halfway up the Hengifoss trail. It drops about 25 to 30 m in two steps and is surrounded by unusually tall columns of basalt. Many people think it is the more photogenic of the two, and it is a natural place to rest on the climb.</p>
<h2>How do you get to Hengifoss, and is there a fee?</h2>
<p>Hengifoss is in Fljótsdalur, beyond Lagarfljót, the long lake south-west of Egilsstaðir. Route 931 runs around the lake. You can drive via Fellabær on the north side, or via Hallormsstaðaskógur forest on route 95 and then route 931. The distance is similar either way.</p>
<p>The car park has a service building with toilets, and rangers are on site in summer. Parking costs about ISK 1,000 per car for the day (2026). Cameras read number plates, so pay at the kiosk or online before you leave. Stops of under 15 minutes are free.</p>
<p class="callout">If the Hengifoss car park is full, the Skriðuklaustur visitor centre is about 5 km further along the road.</p>
<h2>Where is Fardagafoss?</h2>
<p>Fardagafoss is about 5 km from Egilsstaðir on road 93, at the foot of the Fjarðarheiði pass. It is one of three waterfalls on the Miðhúsaá river. A marked trail leads from a small parking area by the road, about 2.6 km there and back. The walk is easy, but the final section to the falls is a bit tricky.</p>
<p>The fall is about 20 m high, and you can walk behind it to the remains of an old cave. Local legend says a giantess lived in the cave. She is said to have hidden a cauldron of gold in a pothole at Gufufoss, and its handle is supposed to show when the river is low. The path is slippery after rain, so treat it as a summer walk. See <a href="/blog/waterfalls-you-can-walk-behind">waterfalls you can walk behind</a> for more like it.</p>
<h2>Where is Gufufoss?</h2>
<p>Gufufoss is on road 93 as it descends from the Fjarðarheiði pass into Seyðisfjörður. It is about 27 m high and sits on the south side of the road. Coming from Egilsstaðir, it is easy to miss on the way down. There is a pull-off on the right as you head toward Seyðisfjörður.</p>
<p>If you miss it, drive into Seyðisfjörður and stop on the way back up. Seyðisfjörður also has its own waterfall walk, the Vestdalsfossar trail.</p>
<h2>What is Rjúkandi?</h2>
<p>Rjúkandi is a tall waterfall beside Route 1 in Jökuldalur, north-west of Egilsstaðir. It is listed at about 93 m. It makes a good 20 to 30 minute stop if you are driving the Ring Road between Mývatn and Egilsstaðir.</p>
<h2>What else is near these waterfalls?</h2>
<p><a href="/places/studlagil">Stuðlagil canyon</a>, with its basalt columns and blue-green river, is in Jökuldalur and pairs well with Rjúkandi. In the south of the region, the <a href="/places/east-fjords-road">East Fjords road</a> follows the coast past small fishing villages. The Hallormsstaðaskógur forest on Lagarfljót is on the way to Hengifoss.</p>
<p>For the waterfalls further north, read <a href="/blog/dettifoss-east-or-west">Dettifoss: east or west side?</a></p>
<h2>How do you see East Iceland's waterfalls in one day?</h2>
<p>From Egilsstaðir you can see the main East Iceland waterfalls in one relaxed day. A sensible order:</p>
<ol>
<li><strong>Morning: Hengifoss and Litlanesfoss.</strong> Drive around Lagarfljót on route 931 and allow two hours for the hike. Arrive early in summer, when the car park fills.</li>
<li><strong>Lunch: Egilsstaðir.</strong> The town has shops, cafés and fuel.</li>
<li><strong>Afternoon: Fardagafoss.</strong> About 5 km out on road 93; allow an hour for the walk.</li>
<li><strong>Late afternoon: Gufufoss and Seyðisfjörður.</strong> Continue over the pass and stop at Gufufoss on the way down into town.</li>
</ol>
<p>If you are arriving from the north on the Ring Road, stop at Rjúkandi and detour to Stuðlagil on the way into Egilsstaðir.</p>
<h2>When can you visit East Iceland's waterfalls?</h2>
<p>June to September is the best time. The trails are dry, the days are long, and road 93 over Fjarðarheiði is usually clear. In winter the Hengifoss trail is icy, so take microspikes and turn back if it is unsafe. Fjarðarheiði is a high mountain pass and can close in storms. Check umferdin.is and vedur.is before driving it.</p>
<p>For a full trip around the island, see the <a href="/blog/iceland-ring-road-guide">Ring Road guide</a>, and for every waterfall on one map, <a href="/blog/waterfalls-in-iceland">Iceland's best waterfalls</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Parking fees and trail conditions change; winter conditions on road 93 and the Hengifoss trail vary from day to day, so check umferdin.is before you go.",
        "sources": [
            ("Hengifoss and Litlanesfoss (East Iceland)", "https://www.east.is/en/natural-and-cultural-monuments/hengifoss-and-litlanesfoss-waterfalls"),
            ("Hike to Hengifoss and Litlanesfoss (Iceland Travel Guide)", "https://icelandtravelguide.is/blog-posts/hike-to-hengifoss-litlanesfoss"),
            ("Hengifoss (Wikipedia)", "https://en.wikipedia.org/wiki/Hengifoss"),
            ("Fardagafoss hiking trail (East Iceland)", "https://east.is/en/place/fardagafoss"),
            ("Fardagafoss (Iceland Travel Guide)", "https://icelandtravelguide.is/locations/fardagafoss/"),
            ("Gufufoss, Iceland (Waterfall Record)", "https://waterfallrecord.com/2022/07/13/gufufoss-iceland/"),
            ("List of waterfalls in Iceland (Wikipedia)", "https://en.wikipedia.org/wiki/List_of_waterfalls_in_Iceland"),
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "slug": "iceland-waterfalls-in-winter",
        "cluster": "waterfalls",
        "pillar": False,
        "short": "Iceland's Waterfalls in Winter: What's Open",
        "title": "Iceland Waterfalls in Winter: What's Open and Icy Paths (2027)",
        "description": "Iceland waterfalls in winter: which falls you can reach, which paths and roads close, how frozen they get, daylight, and how to stay safe on icy paths.",
        "category": "Nature · Waterfalls · Winter",
        "teaser": "Which falls you can reach from November to March, and how to stay upright.",
        "image": "hx-seljalandsfoss-winter",
        "image_alt": "Seljalandsfoss in winter with snow on the slopes and walkers on the path",
        "stats": [
            ("4–5 h", "Daylight in Reykjavík in December"),
            ("~80 m³/s", "Winter flow of Gullfoss, which keeps running"),
            ("Nov–Mar", "Rough closure of the path behind Seljalandsfoss"),
            ("No service", "Winter road service on road 864 to Dettifoss east"),
        ],
        "body": """
<p>Most of Iceland's best-known waterfalls stay open in winter. Seljalandsfoss, Skógafoss, Gullfoss, Goðafoss and Kirkjufellsfoss sit on main roads and can be visited all season. What changes is the detail: the path behind Seljalandsfoss and the lower path at Gullfoss close once ice forms, and falls on gravel or mountain roads, like Dettifoss east, Háifoss and Dynjandi, are usually out of reach. Here is what to expect at Iceland's waterfalls in winter.</p>
<!--TOC-->
<h2>Which waterfalls can you visit in winter?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Waterfall</th><th>Winter access</th><th>What changes</th></tr></thead>
<tbody>
<tr><td>Seljalandsfoss</td><td>Open</td><td>Path behind the falls closed, roughly Nov–Mar</td></tr>
<tr><td>Gljúfrabúi</td><td>Usually open</td><td>Icy stream and slippery rock</td></tr>
<tr><td>Skógafoss</td><td>Open</td><td>Staircase to the top can be icy</td></tr>
<tr><td>Kvernufoss</td><td>Trail icy</td><td>No walk behind the falls</td></tr>
<tr><td>Svartifoss</td><td>Open</td><td>Trail icy; spikes needed</td></tr>
<tr><td>Gullfoss</td><td>Open</td><td>Lower path often closed Nov–Mar</td></tr>
<tr><td>Öxarárfoss</td><td>Open</td><td>Very slippery; crampons advised</td></tr>
<tr><td>Kirkjufellsfoss</td><td>Open</td><td>Icy ground by the falls</td></tr>
<tr><td>Goðafoss</td><td>Open</td><td>Icy paths</td></tr>
<tr><td>Dettifoss (west)</td><td>Limited</td><td>Road 862 not serviced from about January to mid-March</td></tr>
<tr><td>Dettifoss (east)</td><td>Closed</td><td>Road 864 has no winter service</td></tr>
<tr><td>Hengifoss</td><td>Open</td><td>Icy trail; avoid the gorge</td></tr>
<tr><td>Háifoss, Aldeyjarfoss</td><td>Usually not</td><td>Gravel and highland roads not cleared</td></tr>
<tr><td>Dynjandi</td><td>Often not</td><td>High pass road often closed or difficult</td></tr>
</tbody></table></div>
""" + _map("Map of Iceland's main waterfalls", "Iceland's main waterfalls. In winter, stick to those on the Ring Road and the Golden Circle.") + """
<h2>Is the path behind Seljalandsfoss open in winter?</h2>
<p>No. The path behind <a href="/places/seljalandsfoss">Seljalandsfoss</a> is closed once ice forms, which is roughly from November to March. Spray freezes onto the cliff and the path, and icicles can fall from above. The farm that runs the site closes the path. You can still walk to the front of the falls, and the frozen spray on the slopes is spectacular.</p>
<p>Gljúfrabúi, a 10-minute walk north, is usually reachable in winter, though you may cross water and ice. Take care on the rocks and see <a href="/blog/waterfalls-you-can-walk-behind">waterfalls you can walk behind</a> for when the paths reopen.</p>
<h2>What is Gullfoss like in winter?</h2>
<p><a href="/places/gullfoss">Gullfoss</a> keeps flowing all winter, at about 80 m³/s compared with about 140 m³/s in summer. The upper viewpoint is open in almost all conditions and is a short, level walk from the car park, but it has no shelter from the wind. The lower path that leads close to the first drop closes frequently between November and March.</p>
<p>By midwinter, frozen spray coats the canyon edges and the railings. The visitor centre at the upper car park stays open in winter, with a café and toilets. The <a href="/blog/golden-circle-in-winter">Golden Circle in winter</a> guide covers the rest of the route.</p>
<h2>What are the South Coast and Skaftafell waterfalls like in winter?</h2>
<p>The South Coast is the easiest region for winter waterfalls. Route 1 is a main road with regular winter service, and Seljalandsfoss and Skógafoss are only a few minutes from their car parks. At Skógafoss you can walk to the foot of the falls all winter, but the 527-step staircase to the top can be icy and is not worth the risk without spikes.</p>
<p>Kvernufoss is still worth the walk in winter, but its trail freezes and you should not try to go behind the falls in snow or ice. Further east, the 1.9 km trail to Svartifoss in <a href="/places/skaftafell">Skaftafell</a> is often packed snow and ice, so spikes are essential.</p>
<h2>Do Iceland's waterfalls freeze in winter?</h2>
<p>Partly, but the big ones keep running. Large falls like Gullfoss, Skógafoss and Dettifoss carry too much water to freeze solid. What you see instead is ice building around them: frozen spray on the cliffs, icicles hanging beside the water, and shelves of ice along the canyon rims.</p>
<p>Smaller falls on low-flow streams can partly freeze in long cold spells, which is why photos of Kirkjufellsfoss in winter often show ice around the water. How much ice you get depends on the weather that week, not the month.</p>
<h2>How do you stay safe at waterfalls in winter?</h2>
<p>The main danger at a waterfall in winter is ice underfoot. Spray freezes into clear, hard ice that is easy to miss, and it covers paths, steps and viewing platforms. </p>
<ul>
<li><strong>Wear microspikes or ice cleats.</strong> Þingvellir National Park strongly recommends crampons on the Öxarárfoss trail in icy conditions.</li>
<li><strong>Use the handrails,</strong> even if they are coated in ice.</li>
<li><strong>Stay out from under cliffs.</strong> Ice sheets and icicles break off as the day warms.</li>
<li><strong>Keep well back from frozen edges.</strong> Snow can overhang a canyon rim with nothing under it.</li>
<li><strong>Respect closures.</strong> Closed paths are closed because of ice or rockfall.</li>
<li><strong>Watch the wind.</strong> Strong gusts at open viewpoints like Gullfoss can knock you off balance.</li>
</ul>
<p class="callout">Check three things every morning: road conditions on umferdin.is, wind and weather on vedur.is, and alerts on safetravel.is. In winter the weather decides which waterfalls you can reach.</p>
<h2>How much daylight is there for waterfalls in winter?</h2>
<p>Very little in midwinter. Reykjavík gets about 4 to 5 hours of daylight in December, with sunrise after 10:45 and sunset around 15:30. In February it is already 7 to 10 hours, and by March 10 to 13 hours.</p>
<div class="table-wrap"><table>
<thead><tr><th>Month</th><th>Daylight in Reykjavík</th></tr></thead>
<tbody>
<tr><td>November</td><td>About 5–8 h</td></tr>
<tr><td>December</td><td>About 4–5 h</td></tr>
<tr><td>January</td><td>About 4.5–7 h</td></tr>
<tr><td>February</td><td>About 7–10 h</td></tr>
<tr><td>March</td><td>About 10–13 h</td></tr>
</tbody></table></div>
<p>Plan short driving days and aim to arrive at each waterfall in daylight. The low winter sun gives soft, golden light all day, which is a bonus for photos.</p>
<h2>What should you pack for waterfalls in winter?</h2>
<ul>
<li><strong>Microspikes or ice cleats</strong> that fit over your boots. They are the single most useful item.</li>
<li><strong>Waterproof outer layers.</strong> Spray soaks you and then freezes in the wind.</li>
<li><strong>Warm layers, hat and gloves.</strong> Thin liner gloves let you work a phone or camera.</li>
<li><strong>A head torch.</strong> With so little daylight, you may walk back to the car at dusk.</li>
<li><strong>A flask of something hot.</strong> Viewpoints like Gullfoss and Skógafoss are exposed to the wind.</li>
</ul>
<p>Leave enough time. Walking on ice is slower than on dry gravel, and short paths can take twice as long in January as they do in July.</p>
<h2>Which winter waterfall trips work best?</h2>
<p>From Reykjavík, the Golden Circle with Gullfoss and Öxarárfoss and the South Coast with Seljalandsfoss and Skógafoss are both good winter day trips. Our <a href="/blog/south-coast-waterfalls">South Coast waterfalls route</a> gives drive times. In the north, Goðafoss is easy to reach from Akureyri. Dettifoss is possible from the west side on serviced days, which we explain in <a href="/blog/dettifoss-east-or-west">Dettifoss: east or west side?</a></p>
<p>For winter driving, see the <a href="/blog/iceland-ring-road-winter">Ring Road in winter</a>. If you are hoping for the aurora too, Kirkjufellsfoss and Skógafoss are popular places to wait for it; our <a href="/northern-lights">northern lights guide</a> explains the forecasts. For every fall on one map, see <a href="/blog/waterfalls-in-iceland">Iceland's best waterfalls</a>, and for the whole season in print, our <a href="/#guides">Winter guidebook</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Path closures and winter road service depend on the weather each year. Check umferdin.is, vedur.is and safetravel.is every day you travel.",
        "sources": [
            ("Waterfall Seljalandsfoss in winter (Zigzag on Earth)", "https://www.zigzagonearth.com/waterfall-seljalandsfoss-winter-iceland/"),
            ("Walking behind Seljalandsfoss (isnet)", "https://isnet.is/iceland/south-iceland/seljalandsfoss/"),
            ("Gullfoss in winter (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/blog/gullfoss-in-winter"),
            ("Waterfall Gullfoss in winter (Zigzag on Earth)", "https://www.zigzagonearth.com/waterfall-gullfoss-winter-iceland/"),
            ("Closed trails (Þingvellir National Park)", "https://www.thingvellir.is/en/education/news/general-news/closedtrails/"),
            ("Dettifoss (Visit Akureyri)", "https://www.visitakureyri.is/en/see-and-do/attractions/dettifoss"),
            ("Iceland daylight hours (Go Campers)", "https://www.gocampers.is/guides/weather/iceland-daylight-hours/"),
            ("Gullfoss (Wikipedia)", "https://en.wikipedia.org/wiki/Gullfoss"),
        ],
    },
    # ------------------------------------------------------------------ 7
    {
        "slug": "photographing-iceland-waterfalls",
        "cluster": "waterfalls",
        "pillar": False,
        "short": "Photographing Iceland's Waterfalls",
        "title": "Iceland Waterfall Photography: Settings, ND Filters, Spray and Light (2027)",
        "description": "Iceland waterfall photography made practical: shutter speeds, ND and polarising filters, beating the spray, the best light by season and drone rules.",
        "category": "Nature · Waterfalls · Photography",
        "teaser": "Shutter speeds, filters, spray and the best light through the year.",
        "image": "hx-kirkjufell",
        "image_alt": "Northern lights over Kirkjufell mountain beside a frozen waterfall",
        "stats": [
            ("~21 h", "Daylight in Reykjavík around the June solstice"),
            ("4–5 h", "Daylight in Reykjavík in December"),
            ("120 m", "General maximum drone height above the ground"),
            ("~midnight", "Sunset in Reykjavík around the June solstice"),
        ],
        "body": """
<p>Good Iceland waterfall photography comes down to three things: a tripod and a slow shutter for smooth water, a plan for the spray, and the right light for the season. You do not need expensive gear. A camera or phone with manual control, a tripod, a neutral density filter and a stack of lens cloths will cover almost every fall in the country. Here is how to set up, what to pack and when to go.</p>
<!--TOC-->
<h2>What camera settings work best for waterfalls?</h2>
<p>Start in manual or aperture priority at your camera's base ISO, usually 100, with an aperture of about f/8 to f/11 for front-to-back sharpness. Then choose the shutter speed for the look you want. The shutter speed changes the water more than any other setting.</p>
<div class="table-wrap"><table>
<thead><tr><th>Shutter speed</th><th>What the water looks like</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>1/500 s or faster</td><td>Frozen drops and texture</td><td>Power: Dettifoss, Gullfoss</td></tr>
<tr><td>1/15 – 1/4 s</td><td>Soft but still with detail</td><td>Most falls; a safe middle ground</td></tr>
<tr><td>0.5 – 2 s</td><td>Silky, smooth streams</td><td>Svartifoss, Kirkjufellsfoss, Hraunfossar</td></tr>
<tr><td>10 s or longer</td><td>Mist-like water, moving clouds</td><td>Calm days, with an ND filter</td></tr>
</tbody></table></div>
<p>Use a two-second timer or a remote so you do not shake the camera when you press the shutter. Shoot several frames at each speed and compare them on the screen. In the wind, shorter exposures are often sharper.</p>
<h2>Do you need ND filters for waterfall photos?</h2>
<p>For long exposures in daylight, yes. A neutral density (ND) filter cuts the light reaching the sensor so you can use a slow shutter without overexposing. Iceland's summer days are bright and long, so you will want one more often than you might expect.</p>
<ul>
<li><strong>3-stop ND:</strong> takes a 1/30 s exposure to about 1/4 s. Enough for soft water on overcast days.</li>
<li><strong>6-stop ND:</strong> takes 1/60 s to about 1 s. The most useful single filter for waterfalls.</li>
<li><strong>10-stop ND:</strong> for exposures of many seconds in bright light, and for smoothing moving cloud.</li>
<li><strong>Circular polariser:</strong> cuts the glare on wet rocks and moss and deepens colour. Rotate it slowly: it can strengthen or remove a rainbow in the spray.</li>
</ul>
<p>Screw-in filters are faster to handle in wind and spray than square filter systems. Take the filter off before shooting at night.</p>
""" + _map("Map of Iceland's main waterfalls for planning photo stops", "Iceland's main waterfalls. Use it to plan photo stops around the light.") + """
<h2>How do you deal with spray at Icelandic waterfalls?</h2>
<p>Spray is the biggest problem at big falls like Seljalandsfoss, Skógafoss and the west side of Dettifoss. A single drop on the front element will ruin a long exposure. Work like this:</p>
<ol>
<li>Compose and focus with the lens cap on or a cloth over the lens.</li>
<li>Wait for a lull in the wind, then uncover, shoot and cover again.</li>
<li>Wipe the lens or filter with a dry microfibre cloth between every few frames. Bring several cloths and keep them in a sealed bag.</li>
<li>Use a lens hood and a rain cover, or at least a plastic bag, on the camera body.</li>
<li>Back off. A longer lens from further away often gives a cleaner shot than a wide angle in the mist.</li>
</ol>
<p>Choose your side carefully. At Dettifoss, the east side usually has little spray, while the west platforms are often soaked. See <a href="/blog/dettifoss-east-or-west">Dettifoss: east or west side?</a></p>
<h2>When is the best light for waterfall photography in Iceland?</h2>
<p>It depends on the season more than the time of day. Iceland's light changes hugely through the year, so plan your shoots around it.</p>
<p><strong>Summer (June to August).</strong> Around the June solstice Reykjavík gets about 21 hours of daylight, and the sun sets close to midnight. The midday light is hard and the falls are busy. Shoot in the late evening and around midnight, when the light is warm and low and most visitors have gone. Late evening is a popular time at <a href="/places/seljalandsfoss">Seljalandsfoss</a>, when you can shoot the setting sun through the curtain from the path behind it.</p>
<p><strong>Autumn and spring (September, October, March, April).</strong> Days of 8 to 16 hours, gentler light and changing colours in the moss and birch. These months are a good balance of light, dark nights and open roads.</p>
<p><strong>Winter (November to February).</strong> December gives only 4 to 5 hours of daylight, but the sun stays low all day. The soft, often golden light lasts for hours, and ice around the falls adds texture. You also get dark skies for the aurora. See <a href="/blog/iceland-waterfalls-in-winter">waterfalls in winter</a> for what is open.</p>
<p>Overcast days are underrated. Flat, even light suits long exposures and keeps the white water from blowing out.</p>
<h2>Where can you photograph rainbows at waterfalls?</h2>
<p>You need sun behind you and spray in front. Skógafoss is the classic spot: on sunny days its heavy spray often throws a single or double rainbow. Seljalandsfoss and Gullfoss also show rainbows in the right sun. A polariser lets you control how strongly the rainbow shows.</p>
<h2>How do you photograph the northern lights over a waterfall?</h2>
<p>Kirkjufellsfoss on <a href="/places/snaefellsnes">Snæfellsnes</a>, with <a href="/places/kirkjufell">Kirkjufell</a> behind it, is the best-known aurora and waterfall scene in Iceland. Skógafoss and Seljalandsfoss are also popular, and both are close to dark countryside.</p>
<p>Set up in daylight or blue hour, so you know where to stand and where the ice is. As a starting point, use a wide lens at f/2.8 or its widest aperture, ISO 1600 to 3200 and 5 to 15 seconds. Focus manually on a bright star or a distant light. Our <a href="/northern-lights">northern lights guide</a> explains the forecasts and the best months.</p>
<p class="callout">Bring a head torch with a red-light mode and microspikes for night shoots. Frozen spray turns paths into ice rinks after dark, and you will be walking back in the dark.</p>
<h2>Can you fly a drone at Iceland's waterfalls?</h2>
<p>Often not. Drone rules are strict and changed in 2026, so check before you fly. In Vatnajökull National Park, drones are banned in most of Skaftafell (including Svartifoss) and most of Jökulsárgljúfur. They are allowed only over the canyon on the west side of Dettifoss, within set hours. Recreational permits are reported to no longer be issued at protected sites such as Gullfoss, Skógafoss and Goðafoss.</p>
<p>Everywhere, the general height limit is 120 m above the ground. Keep away from people and wildlife, and register as an operator if your drone needs it. Rules can change at short notice, so read the managing authority's current page before every flight.</p>
<h2>How do you get photos without the crowds?</h2>
<ul>
<li><strong>Go early or late.</strong> In summer the evening and night are quietest; in winter, arrive at first light.</li>
<li><strong>Use long exposures.</strong> A 30-second exposure with a strong ND filter can blur moving people until they almost vanish.</li>
<li><strong>Pick quieter falls.</strong> Kvernufoss, Gljúfrabúi and Litlanesfoss on the Hengifoss trail see far fewer visitors. Read the <a href="/blog/south-coast-waterfalls">South Coast waterfalls route</a> and <a href="/blog/east-iceland-waterfalls">East Iceland waterfalls</a> for ideas.</li>
<li><strong>Stay on the path.</strong> Do not cross ropes or step onto moss for a better angle. Moss takes decades to recover.</li>
</ul>
<p>For every major fall on one map, start with <a href="/blog/waterfalls-in-iceland">Iceland's best waterfalls</a>, and browse the <a href="/highlights">highlights</a> for more scenes to shoot.</p>
""",
        "checked_note": "Facts checked October 2026. Camera settings are starting points, not rules. Drone regulations in Iceland changed in 2026 and differ by site; always check the managing authority's current rules before flying.",
        "sources": [
            ("Iceland daylight hours (Go Campers)", "https://www.gocampers.is/guides/weather/iceland-daylight-hours/"),
            ("Skógafoss (Wikipedia)", "https://en.wikipedia.org/wiki/Sk%C3%B3gafoss"),
            ("Seljalandsfoss photo location (Locationscout)", "https://locationscout.net/iceland/1250-seljalandsfoss"),
            ("Dettifoss east vs west (Earth Trekkers)", "https://www.earthtrekkers.com/?p=36413"),
            ("Drone rules (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/drone-rules"),
            ("Drone flying in Iceland: all you need to know in 2026 (JVN Photo)", "https://jvn.photo/drone-flying-in-iceland-all-you-need-to-know-in-2026/"),
        ],
    },
]
