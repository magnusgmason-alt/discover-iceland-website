"""Ring Road cluster articles for the Discover Iceland journal.
Same format as articles_content.py. The first article is the cluster pillar."""

MAP_RING = """<figure class="a-figure a-map"><a href="/assets/img/map-ring-road-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-ring-road-1800.jpg" srcset="/assets/img/map-ring-road-800.jpg 800w, /assets/img/map-ring-road-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{cap} Tap to open full size.</figcaption></figure>"""

MAP_GENERAL = """<figure class="a-figure a-map"><a href="/assets/img/map-general-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-general-1800.jpg" srcset="/assets/img/map-general-800.jpg 800w, /assets/img/map-general-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{cap} Tap to open full size.</figcaption></figure>"""

MAP_GOLDEN = """<figure class="a-figure a-map"><a href="/assets/img/map-golden-circle-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-golden-circle-1800.jpg" srcset="/assets/img/map-golden-circle-800.jpg 800w, /assets/img/map-golden-circle-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{cap} Tap to open full size.</figcaption></figure>"""

MAP_WESTFJORDS = """<figure class="a-figure a-map"><a href="/assets/img/map-westfjords-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-westfjords-1800.jpg" srcset="/assets/img/map-westfjords-800.jpg 800w, /assets/img/map-westfjords-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{cap} Tap to open full size.</figcaption></figure>"""


ARTICLES = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "iceland-ring-road-guide",
        "cluster": "ring-road",
        "pillar": True,
        "short": "The Iceland Ring Road: Complete Driving Guide",
        "title": "Iceland Ring Road: Complete Driving Guide, Route, Stops and Map (2027)",
        "description": "The Iceland Ring Road explained: the 1,322 km route, how many days you need, the best stops, driving rules, tolls, fuel, winter closures and a 7-day map.",
        "category": "Itineraries · Ring Road",
        "teaser": "Route 1 around the whole island: days, stops, rules and seasons.",
        "image": "hx-east-fjords-road",
        "image_alt": "The Ring Road winding between snow-covered mountains",
        "stats": [
            ("1,322 km", "Length of Route 1 around Iceland"),
            ("1974", "Year the Ring Road was completed"),
            ("7 days", "Minimum Visit Iceland suggests for the full loop"),
            ("90 km/h", "Speed limit on paved rural roads"),
        ],
        "body": """
<p>The Iceland Ring Road is Route 1, a paved road of about 1,322 km that circles the whole island and links most of its towns and famous sights. You need at least seven days to drive it, and ten to fourteen days if you want short driving days and time for detours. In summer an ordinary car is enough. In winter it is a serious drive that needs flexible plans. This guide covers the route, how long it takes, where to stop, the rules of the road and what changes with the seasons.</p>
<!--TOC-->
<h2>What is the Iceland Ring Road?</h2>
<p>The Ring Road is Iceland's main highway, numbered Route 1, and it runs right around the country. Visit Iceland gives its length as 1,322 km. The Icelandic Road and Coastal Administration simply says "more than 1,300 km", because small realignments change the figure from year to year.</p>
<p>The loop was completed in 1974, when bridges across the Skeiðarársandur glacial plain in the south-east finally joined the northern and southern roads. The last gravel stretch was paved in 2019, so today the whole of Route 1 has a hard surface. Most of it is still a two-lane road with no hard shoulder, and it carries more than 2,000 vehicles a day on many sections in summer.</p>
<p>The road passes Reykjavík, Selfoss, Hella, Vík, Höfn, Egilsstaðir, the Mývatn area, Akureyri, Blönduós and Borgarnes. It skips two of the best regions in the country, the Snæfellsnes peninsula and the Westfjords, which you reach on side roads.</p>
<h2>How many days do you need for the Ring Road?</h2>
<p>Plan at least seven days for the Ring Road, and ten if you can. Without stops the loop is roughly 17 to 20 hours of driving, but nobody drives it that way. Every day you will stop at waterfalls, walk to viewpoints and wait out showers.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trip length</th><th>Driving per day</th><th>What it feels like</th></tr></thead>
<tbody>
<tr><td>5–6 days</td><td>4–6 hours</td><td>Possible in summer, but mostly driving. Not recommended.</td></tr>
<tr><td>7 days</td><td>2–5 hours</td><td>The classic loop. Long days, the main sights only.</td></tr>
<tr><td>10 days</td><td>1–4 hours</td><td>Time for short hikes, a glacier walk and one or two detours.</td></tr>
<tr><td>14 days</td><td>1–3 hours</td><td>Adds Snæfellsnes or the Westfjords at an easy pace.</td></tr>
</tbody></table></div>
<p>Our <a href="/blog/iceland-ring-road-7-days">7-day Ring Road itinerary</a> follows the fast loop day by day. The <a href="/blog/iceland-ring-road-10-days">10-day Ring Road itinerary</a> is the slower version, with nights at Skaftafell and in the east. If you only have a few days, skip the full loop and use our <a href="/blog/iceland-5-day-itinerary">5-day Iceland itinerary</a> or <a href="/blog/iceland-3-day-itinerary">3 days in Iceland</a> plan instead.</p>
""" + MAP_RING.format(
            alt="Map of a 7-day Ring Road route around Iceland with overnight stops at Hella, Vík, Höfn, Egilsstaðir, Mývatn and Akureyri",
            cap="A 7-day Ring Road route, driven anticlockwise from Reykjavík with the day-by-day distances.",
        ) + """
<h2>Which direction should you drive the Ring Road?</h2>
<p>Most people drive anticlockwise, heading east along the south coast first. That puts the big sights, the Golden Circle, the south coast waterfalls and the glacier lagoons, at the start of the trip while you are fresh. It also means the remote east and north come in the middle, when you are used to the roads.</p>
<p>Driving clockwise works just as well and can be the better choice in late summer. You get the quieter north first and finish on the south coast, which usually has the most daylight and the mildest weather. In winter, decide on the day: start in whichever direction the forecast is better.</p>
<h2>What are the best stops on the Ring Road?</h2>
<p>The best stops on the Ring Road are spread evenly around the island. Here they are region by region, anticlockwise from Reykjavík.</p>
<h3>Golden Circle and the south coast</h3>
<ul>
<li><strong>Þingvellir, Geysir and Gullfoss:</strong> the Golden Circle is a short loop off Route 1 and an easy first day.</li>
<li><strong><a href="/places/seljalandsfoss">Seljalandsfoss</a> and Skógafoss:</strong> two 60-metre waterfalls right beside the road. You can walk behind Seljalandsfoss, and 527 steps climb to the top of Skógafoss.</li>
<li><strong>Reynisfjara:</strong> the black sand beach and basalt columns near Vík. Stay well back from the water; the waves here are deadly.</li>
</ul>
<h3>The glacier coast</h3>
<ul>
<li><strong><a href="/places/skaftafell">Skaftafell</a>:</strong> walking trails, Svartifoss and glacier views in Vatnajökull National Park.</li>
<li><strong><a href="/places/jokulsarlon">Jökulsárlón</a> and Fjallsárlón:</strong> glacier lagoons full of icebergs, with Diamond Beach across the road from Jökulsárlón.</li>
<li><strong>Stokksnes and Vestrahorn:</strong> black dunes below jagged peaks, just before Höfn.</li>
</ul>
<h3>The East Fjords and the north</h3>
<ul>
<li><strong>The East Fjords road:</strong> fishing villages and empty bays between Höfn and Egilsstaðir.</li>
<li><strong>Hengifoss and Stuðlagil:</strong> a 128-metre waterfall and a basalt canyon, both short detours from Egilsstaðir.</li>
<li><strong>Dettifoss, Mývatn and Goðafoss:</strong> a 44-metre waterfall 100 metres wide, a volcanic lake district, and the 12-metre Goðafoss right beside Route 1.</li>
<li><strong>Akureyri:</strong> the largest town on the Ring Road and a good place to rest for a night.</li>
</ul>
<p>For every sight on one interactive map, see our <a href="/highlights">Iceland highlights</a>.</p>
<h2>How long are the drives between the main stops?</h2>
<p>The longest single legs are Vík to Höfn, Höfn to Egilsstaðir and Akureyri back to Reykjavík. These are rough distances and drive times without stops, in good summer conditions.</p>
<div class="table-wrap"><table>
<thead><tr><th>Leg</th><th>Distance</th><th>Drive time</th></tr></thead>
<tbody>
<tr><td>Reykjavík to Vík</td><td>about 185 km</td><td>about 2.5 h</td></tr>
<tr><td>Vík to Höfn</td><td>about 270 km</td><td>about 3.5 h</td></tr>
<tr><td>Höfn to Egilsstaðir (coast)</td><td>about 250 km</td><td>about 3.5–4 h</td></tr>
<tr><td>Egilsstaðir to Mývatn</td><td>about 165 km</td><td>about 2 h</td></tr>
<tr><td>Mývatn to Akureyri</td><td>about 90 km</td><td>about 1–1.5 h</td></tr>
<tr><td>Akureyri to Reykjavík</td><td>about 390 km</td><td>about 4.5–5 h</td></tr>
</tbody></table></div>
<p>For every leg stop by stop, plus the main detours, see our <a href="/blog/ring-road-driving-times">Ring Road driving times</a> table.</p>
<h2>What are the rules for driving the Ring Road?</h2>
<p>The speed limit on the paved Ring Road is 90 km/h, dropping to 50 km/h or less in towns. Gravel roads off the Ring Road are 80 km/h. Speed cameras are common and fines are high.</p>
<ul>
<li><strong>Headlights on, always.</strong> Icelandic law requires dipped headlights and tail lights day and night, all year.</li>
<li><strong>Single-lane bridges.</strong> The first car to reach the bridge has priority. SafeTravel advises slowing to 50 km/h and stopping for oncoming traffic. As of 2023 there were 29 single-lane bridges on Route 1, down from 140 in 1990, and the road authority aims to replace the rest before 2039.</li>
<li><strong>No stopping on the road.</strong> Pull into a proper car park or lay-by for photos. Stopping on the carriageway causes accidents every year.</li>
<li><strong>No off-road driving.</strong> Leaving the road damages moss and soil for decades and is illegal.</li>
<li><strong>No phones.</strong> Using a phone while driving is illegal.</li>
<li><strong>Seatbelts for everyone</strong>, and child seats for children under 135 cm.</li>
</ul>
<h2>Is the Ring Road safe to drive?</h2>
<p>Yes, the Ring Road is safe in summer for any confident driver, and in winter for drivers who respect the weather. The road authority warns that rental-car drivers and people unused to Icelandic roads have a higher risk of accidents, so the main danger is unfamiliarity, not the road itself.</p>
<p>The typical hazards are easy to plan for. Blind summits and sharp bends appear on older stretches. Sheep wander onto the road in summer. Gravel shoulders are soft, and the change from tarmac to gravel catches people out. Wind is the biggest surprise: strong gusts can push a car sideways and tear a door from its hinges. Do not drive tired; switch drivers or stop for a rest, and avoid long days at the wheel. Carry water, food and warm clothes, because help can be far away in remote areas.</p>
<h2>Do you need a 4x4 for the Ring Road?</h2>
<p>No. The whole of Route 1 is paved, and a two-wheel-drive car is fine in summer. Guide to Iceland recommends a 4x4 between October and May, when snow and ice are likely. A 4x4 is also needed if you want to leave the Ring Road for the highland F-roads, which only open in summer and where normal cars are not allowed.</p>
<p>Many sights sit a short way off Route 1 on gravel roads. Slow down as you move from tarmac to gravel, because grip changes suddenly. Rental contracts often exclude gravel damage, so read the insurance terms before you choose a car.</p>
<h2>Are there tolls on the Ring Road?</h2>
<p>There is one toll, at the Vaðlaheiðargöng tunnel just east of Akureyri. The fee for a car was ISK 2,216 per trip when we checked in 2026. There are no booths: cameras read your plate and you pay online at veggjald.is within 24 hours before or after you drive through. If you do not pay, the bill goes to the rental company, which usually adds a fee.</p>
<p>The Hvalfjörður tunnel north of Reykjavík has been free since September 2018. Several popular sights charge for parking, including Þingvellir, where a car with up to five seats pays ISK 1,000 for the day.</p>
<h2>Where can you get fuel on the Ring Road?</h2>
<p>Fuel stations are frequent in the south-west and around Akureyri, but gaps open up in the east. Between Höfn and Egilsstaðir and on the high plateau east of Mývatn, keep the tank above half and fill up whenever you can. Many pumps are self-service and card-only, so carry a payment card that works abroad.</p>
<p>Electric cars are workable on the Ring Road in summer, with fast chargers along the route, but plan each charge in advance in the east and north.</p>
<h2>What is the best time of year to drive the Ring Road?</h2>
<p>June to August is the easiest time to drive the Ring Road. The days are long, the mountain passes are clear and every side road is open. It is also the busiest time: Visit Iceland notes that rooms between Selfoss and Höfn fill up in peak summer, and traffic between Reykjavík and Akureyri can be heavy in July. May and September are a good balance, with fewer people and usually dry roads.</p>
<p>From September to May, watch the mountain passes. Visit Iceland names Holtavörðuheiði, Öxnadalsheiði and Möðrudalsöræfi as the stretches that most often close in storms or high wind. Our full guide to the <a href="/blog/iceland-ring-road-winter">Ring Road in winter</a> covers tyres, daylight and closures. For month-by-month weather, see <a href="/blog/best-time-to-visit-iceland">the best time to visit Iceland</a>.</p>
<p>Autumn and winter add one big reward. From late August to April the nights are dark enough for the northern lights, and the countryside along Route 1, far from town lights, is an ideal place to watch them on a clear night. Never stop on the road to look; pull fully into a car park first. Our <a href="/northern-lights">northern lights guide</a> explains the forecasts.</p>
<p class="callout"><strong>Every morning:</strong> check the road map at road.is (or call 1777), the forecast and wind warnings at vedur.is, and alerts on SafeTravel. Check again during the day. Conditions can change within hours.</p>
<h2>What detours are worth adding to the Ring Road?</h2>
<p>The most rewarding detours are the ones Route 1 leaves out. With extra days, consider these:</p>
<ul>
<li><strong><a href="/places/snaefellsnes">Snæfellsnes</a>:</strong> Kirkjufell, lava fields and the 1,446-metre Snæfellsjökull, about two to two and a half hours from Reykjavík. It fits well on the last day or two.</li>
<li><strong>The Westfjords:</strong> the region the Ring Road skips entirely, with Dynjandi, Látrabjarg and quiet fjord roads. It needs four days or more; see our <a href="/blog/westfjords-road-trip">Westfjords road trip</a>.</li>
<li><strong>Seyðisfjörður:</strong> a small fjord town over a mountain pass from Egilsstaðir.</li>
<li><strong>Húsavík:</strong> about an hour from Akureyri, known for whale watching.</li>
<li><strong>Öxi pass (Route 939):</strong> a 19 km gravel shortcut that cuts about 70 km off the drive from Djúpivogur to Egilsstaðir. It is steep and narrow, closed in winter, and best avoided in fog.</li>
</ul>
<h2>Can you do the Ring Road without a car?</h2>
<p>It is possible, but hard. Rural buses link many towns along Route 1, but some run only a few times a day and they do not stop at most sights. You would spend days waiting and still miss the waterfalls and lagoons between towns.</p>
<p>The realistic alternatives are a guided multi-day Ring Road tour, or a mix of day tours from Reykjavík and a domestic flight to Akureyri or Egilsstaðir.</p>
<h2>Where should you stay along the Ring Road?</h2>
<p>Stay somewhere new every one or two nights. The classic overnight stops are Hella or Selfoss, Vík, the Skaftafell area or Höfn, Egilsstaðir, Mývatn and Akureyri. Book the stretch from Vík to Höfn first, because there are few beds and they go early. Campervans must use campsites, not lay-bys. Our guide to <a href="/blog/where-to-stay-in-iceland">where to stay in Iceland</a> compares each base.</p>
<h2>How much does it cost to drive the Ring Road?</h2>
<p>Car hire and rooms are the big costs, and both depend heavily on season and how early you book. A compact car in winter and a 4x4 or campervan in July can differ several times over in price, so compare quotes for your exact dates. Then budget for fuel, which is expensive in Iceland, plus the tunnel toll and parking fees.</p>
<p>You can save by cooking some meals, using campsites in summer and swimming in the local geothermal pools rather than the big lagoons. For everything else about cars, buses and flights, see <a href="/blog/getting-around-iceland">getting around Iceland</a>.</p>
<h2>What should you pack for a Ring Road trip?</h2>
<ul>
<li>Waterproof jacket and trousers, warm layers, hat and gloves, in every season.</li>
<li>Walking boots with good grip, and ice cleats from October to April.</li>
<li>A swimsuit and towel for the town pools.</li>
<li>Offline maps on your phone, because signal drops in the east and north.</li>
<li>Snacks and water for the long empty stretches, and a phone charger for the car.</li>
</ul>
<p>Before you go, leave a travel plan on SafeTravel and save 112, the emergency number. If you want everything in one place on the road, our <a href="/#guides">printed Complete Guide to Iceland</a> covers the Ring Road region by region.</p>
""",
        "checked_note": "Facts checked October 2026. Road lengths, single-lane bridge counts, the Vaðlaheiðargöng toll and parking fees change; check road.is, veggjald.is and each site's own page before you travel, and check road and weather conditions every day.",
        "sources": [
            ("The Ring Road – Route Number One (Visit Iceland)", "https://visiticeland.com/article/the-ring-road"),
            ("The Ring Road (Icelandic Road and Coastal Administration)", "https://www.vegagerdin.is/en/home/exploring-iceland/the-ring-road"),
            ("Route 1 (Iceland) (Wikipedia)", "https://en.wikipedia.org/wiki/Route_1_(Iceland)"),
            ("Ring Road travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/ring-road"),
            ("Top 12 tips for driving in Iceland (SafeTravel)", "https://safetravel.is/driving/top-12-tips/"),
            ("Vaðlaheiðargöng tunnel toll (Go Car Rental)", "https://www.gocarrental.is/driving/driving-tips/iceland-tunnel-toll/"),
            ("How long to drive around Iceland (Blue Car Rental)", "https://www.bluecarrental.is/blog/how-long-to-drive-around-iceland-complete-ring-road-timing-tips---itineraries/"),
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "iceland-ring-road-7-days",
        "cluster": "ring-road",
        "pillar": False,
        "short": "The Ring Road in 7 Days: Day-by-Day Itinerary",
        "title": "Ring Road 7 Days: A Day-by-Day Iceland Itinerary with Map (2027)",
        "description": "The Ring Road in 7 days: a day-by-day route with distances, nights in Hella, Vík, Höfn, Egilsstaðir, Mývatn and Akureyri, and what to see each day.",
        "category": "Itineraries · Ring Road",
        "teaser": "The classic loop in one week, with distances and nightly stops.",
        "image": "hx-vestrahorn",
        "image_alt": "A walker in a blue jacket crossing black dunes below the jagged peaks of Vestrahorn",
        "stats": [
            ("~1,545 km", "Total of the seven daily legs on our map"),
            ("~390 km", "Longest day: Akureyri back to Reykjavík"),
            ("6 nights", "On the road before you return to Reykjavík"),
            ("ISK 2,216", "Vaðlaheiðargöng tunnel toll per trip (2026)"),
        ],
        "body": """
<p>Seven days is the shortest comfortable time to drive the whole Ring Road. This itinerary goes anticlockwise from Reykjavík, with nights in Hella, Vík, Höfn, Egilsstaðir, Mývatn and Akureyri, and a long last day back to the capital. Most days have two to four hours of driving plus stops. It works best from late May to September, when the days are long and the mountain passes are clear.</p>
<!--TOC-->
<h2>Is 7 days enough for the Ring Road?</h2>
<p>Yes, 7 days is enough to drive the Ring Road and see its main sights, but it is a full week. Visit Iceland suggests at least seven days for the loop. You will have time for short walks at each stop, not for long hikes or many detours. If you can add even two or three days, the <a href="/blog/iceland-ring-road-10-days">10-day Ring Road itinerary</a> spreads the same route out and adds Snæfellsnes.</p>
<p>In winter, seven days is too tight for the full loop. Short daylight and storm closures make long days risky. See our guide to the <a href="/blog/iceland-ring-road-winter">Ring Road in winter</a> for alternatives.</p>
""" + MAP_RING.format(
            alt="Map of the 7-day Ring Road itinerary with daily legs from Reykjavík via Hella, Vík, Höfn, Egilsstaðir, Mývatn and Akureyri",
            cap="The 7-day route: each day's leg and approximate distance, anticlockwise from Reykjavík.",
        ) + """
<h2>What does the 7-day Ring Road route look like?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>Route</th><th>Distance</th><th>Overnight</th></tr></thead>
<tbody>
<tr><td>1</td><td>Golden Circle to Hella</td><td>≈230 km</td><td>Hella</td></tr>
<tr><td>2</td><td>Waterfalls and Reynisfjara to Vík</td><td>≈100 km</td><td>Vík</td></tr>
<tr><td>3</td><td>Glacier lagoons to Höfn</td><td>≈275 km</td><td>Höfn</td></tr>
<tr><td>4</td><td>East Fjords to Egilsstaðir</td><td>≈250 km</td><td>Egilsstaðir</td></tr>
<tr><td>5</td><td>Dettifoss to Mývatn</td><td>≈200 km</td><td>Mývatn</td></tr>
<tr><td>6</td><td>Goðafoss to Akureyri</td><td>≈100 km</td><td>Akureyri</td></tr>
<tr><td>7</td><td>West via Borgarnes to Reykjavík</td><td>≈390 km</td><td>Reykjavík</td></tr>
</tbody></table></div>
<p>Distances include the short detours to the sights. For the leg-by-leg breakdown, see our <a href="/blog/ring-road-driving-times">Ring Road driving times</a>.</p>
<h2>Day 1: What do you see on the Golden Circle?</h2>
<p>Day 1 covers the Golden Circle and ends in Hella, about 230 km in all. Leave Reykjavík early for <a href="/places/thingvellir">Þingvellir National Park</a>, where you walk through the rift between two tectonic plates. Parking costs ISK 1,000 for a car for the day.</p>
<p>Continue to the Geysir geothermal area, where Strokkur erupts every six to ten minutes, usually 15–20 metres high. Then drive ten minutes on to Gullfoss, which drops 32 metres in two steps into a canyon. From Gullfoss, head south through farmland to Route 1 and Hella for the night.</p>
<h2>Day 2: Which waterfalls do you pass on the way to Vík?</h2>
<p>Day 2 is a short drive of about 100 km with some of the best stops in Iceland. Seljalandsfoss falls 60 metres, and a path leads behind the water into a small cave. Bring a waterproof jacket.</p>
<p>About 30 km further on, Skógafoss is just as tall and 25 metres wide. A staircase of 527 steps climbs to the top. In the afternoon, visit the Dyrhólaey headland and the black sand beach at <a href="/places/reynisfjara">Reynisfjara</a> before checking in at Vík.</p>
<p class="callout"><strong>At Reynisfjara:</strong> stay well back from the water, even when the sea looks calm. Sudden "sneaker waves" run far up the beach and have killed visitors. Never turn your back on the sea.</p>
<h2>Day 3: How do you fit in Skaftafell and Jökulsárlón?</h2>
<p>Day 3 is the longest drive of the first half, about 275 km to Höfn, so start early. East of Vík the road crosses the Eldhraun lava field to Kirkjubæjarklaustur, the last fuel stop for a while.</p>
<p>At Skaftafell, walk to Svartifoss, a waterfall framed by black basalt columns. The round trip is about 5.5 km and takes 1.5 to 2 hours. If you do not have that much time, walk to the Skaftafellsjökull glacier viewpoint instead.</p>
<p>Next come the glacier lagoons. Fjallsárlón is smaller and quieter. <a href="/places/jokulsarlon">Jökulsárlón</a>, about 60 km east of Skaftafell, is filled with icebergs, and Diamond Beach lies just across the road. Höfn is roughly an hour further on.</p>
<h2>Day 4: What is the drive through the East Fjords like?</h2>
<p>Day 4 follows the coast for about 250 km to Egilsstaðir. Leaving Höfn, stop at Stokksnes to see the black dunes below Vestrahorn.</p>
<p>The rest of the day winds in and out of the <a href="/places/east-fjords-road">East Fjords</a>, through the harbour village of Djúpivogur and past long empty bays. In summer you can take the Öxi pass from Djúpivogur, a 19 km gravel road that saves about 70 km. It is steep and narrow, and closed in winter. Keep the fuel tank above half on this stretch.</p>
<h2>Day 5: How do you get to Dettifoss and Mývatn?</h2>
<p>Day 5 crosses the high, empty plateau from Egilsstaðir to Mývatn, about 200 km including Dettifoss. Before you leave, consider an early walk to Hengifoss, a 128-metre waterfall 40–60 minutes' walk from its car park.</p>
<p>For Dettifoss, turn north off Route 1 onto Route 862, the paved road to the west bank. Dettifoss drops 44 metres over a width of 100 metres. The east bank road, Route 864, is gravel and usually only passable in summer. Back on Route 1, stop at the steaming mud pots of Hverir before reaching Mývatn. End the day in the Mývatn Nature Baths.</p>
<h2>Day 6: What is there to see between Mývatn and Akureyri?</h2>
<p>Day 6 is a short drive of about 100 km, so spend the morning at Mývatn. Walk around the Hverfjall crater or the lava formations at Dimmuborgir. Then drive west to Goðafoss, a 12-metre waterfall right beside Route 1.</p>
<p>Akureyri is about 45 minutes beyond Goðafoss. The road goes through the Vaðlaheiðargöng tunnel, which costs ISK 2,216 per trip (2026). Pay online at veggjald.is within 24 hours. In the evening, walk the old town and use the town pool.</p>
<h2>Day 7: How long is the drive from Akureyri to Reykjavík?</h2>
<p>Day 7 is the longest day, about 390 km and 4.5 to 5 hours of driving without stops. The road crosses the Öxnadalsheiði and Holtavörðuheiði mountain passes, which can close in storms, so check road.is before you set off.</p>
<p>Break the drive in Blönduós or Borgarnes, about 75 km from Reykjavík. If you have energy left, Hraunfossar and Deildartunguhver are short detours inland from Borgarnes. The Hvalfjörður tunnel takes you under the fjord to Reykjavík, toll-free.</p>
<h2>How should you change the plan if it rains or roads close?</h2>
<p>Keep one flexible evening. If a pass closes, wait it out in the nearest town rather than looking for an alternative route; mountain roads are not alternatives. Book rooms with free cancellation where you can, and check the weather at vedur.is every morning.</p>
<p>If you fall behind, cut detours, not sleep. Dettifoss and the Öxi pass are the easiest to drop. For the full picture of rules, tolls and fuel, read our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a>.</p>
<h2>What is the best month for a 7-day Ring Road trip?</h2>
<p>June, July and August give you long days and the most reliable roads, so a 7-day loop is easiest then. Late May and early September are quieter and still usually clear. Before booking, check our <a href="/blog/best-time-to-visit-iceland">month-by-month guide</a>. Our <a href="/#guides">printed Summer Guide</a> covers the route in more detail if you like a book in the car.</p>
""",
        "checked_note": "Facts checked October 2026. Daily distances are approximate and include short detours. The Vaðlaheiðargöng toll and parking fees change; check veggjald.is, road.is and vedur.is before each day's drive.",
        "sources": [
            ("The Ring Road – Route Number One (Visit Iceland)", "https://visiticeland.com/article/the-ring-road"),
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("South Coast Iceland guide (Slice of Iceland)", "https://sliceoficeland.is/articles/south-coast-iceland-guide"),
            ("Dettifoss (Wikipedia)", "https://en.wikipedia.org/wiki/Dettifoss"),
            ("Öxi Pass, Route 939 (Lonely Planet)", "https://www.lonelyplanet.com/points-of-interest/oxi-pass-route-939/1603264"),
            ("Vaðlaheiðargöng tunnel toll (Go Car Rental)", "https://www.gocarrental.is/driving/driving-tips/iceland-tunnel-toll/"),
            ("Driving distances between hotels (Iceland Hotel Collection by Berjaya)", "https://www.icelandhotelcollectionbyberjaya.com/magazine/blog/driving-distances-mag"),
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "iceland-ring-road-10-days",
        "cluster": "ring-road",
        "pillar": False,
        "short": "The Ring Road in 10 Days: The Slower Route",
        "title": "Ring Road 10 Days: A Slower Iceland Itinerary with Snæfellsnes (2027)",
        "description": "The Ring Road in 10 days: a slower day-by-day Iceland itinerary with nights at Skaftafell and Egilsstaðir, time for hikes, and Snæfellsnes at the end.",
        "category": "Itineraries · Ring Road",
        "teaser": "The same loop with shorter days, more walking and Snæfellsnes.",
        "image": "hx-studlagil",
        "image_alt": "The blue river running through Stuðlagil canyon between basalt columns",
        "stats": [
            ("1–4 h", "Typical driving per day on a 10-day loop"),
            ("128 m", "Height of Hengifoss, a detour on day 6"),
            ("463 m", "Height of Kirkjufell on Snæfellsnes"),
            ("44 m", "Drop of Dettifoss into Jökulsárgljúfur"),
        ],
        "body": """
<p>Ten days is the best length for a first Ring Road trip. You drive the same loop as the 7-day route, but with shorter days, a full day around Egilsstaðir and time for a glacier walk and proper hikes. The last two days swing out to the Snæfellsnes peninsula, which the Ring Road skips. Most days have one to four hours of driving.</p>
<!--TOC-->
<h2>Why drive the Ring Road in 10 days instead of 7?</h2>
<p>With ten days you see more and drive less each day. On a 7-day trip, the stretch from Vík to Höfn and the run from Akureyri to Reykjavík are long days in the car. Here they are split, so you have time for the Svartifoss walk, a guided glacier hike, Stuðlagil canyon and the Snæfellsnes coast.</p>
<p>The extra days also give you a weather buffer. If a storm closes a pass, you can lose a day without dropping half the trip. If you only have a week, use our <a href="/blog/iceland-ring-road-7-days">7-day Ring Road itinerary</a> instead.</p>
""" + MAP_RING.format(
            alt="Map of the Ring Road route around Iceland with daily legs and overnight towns",
            cap="The Ring Road route. The 10-day plan follows the same loop, with extra nights at Skaftafell and Egilsstaðir and a finish via Snæfellsnes.",
        ) + """
<h2>What does the 10-day Ring Road route look like?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>Route</th><th>Approx. distance</th><th>Overnight</th></tr></thead>
<tbody>
<tr><td>1</td><td>Reykjavík, Golden Circle</td><td>230 km</td><td>Hella or Selfoss area</td></tr>
<tr><td>2</td><td>South coast waterfalls</td><td>100 km</td><td>Vík</td></tr>
<tr><td>3</td><td>Vík to Skaftafell</td><td>140 km</td><td>Skaftafell area</td></tr>
<tr><td>4</td><td>Glacier lagoons to Höfn</td><td>140 km</td><td>Höfn</td></tr>
<tr><td>5</td><td>East Fjords</td><td>250 km</td><td>Egilsstaðir</td></tr>
<tr><td>6</td><td>Hengifoss and Stuðlagil</td><td>loop, varies</td><td>Egilsstaðir</td></tr>
<tr><td>7</td><td>Dettifoss to Mývatn</td><td>200 km</td><td>Mývatn</td></tr>
<tr><td>8</td><td>Goðafoss to Akureyri</td><td>100 km</td><td>Akureyri</td></tr>
<tr><td>9</td><td>Akureyri to Snæfellsnes</td><td>long day</td><td>Grundarfjörður or Stykkishólmur</td></tr>
<tr><td>10</td><td>Snæfellsnes to Reykjavík</td><td>2–2.5 h drive</td><td>Reykjavík</td></tr>
</tbody></table></div>
<p>Distances are rounded and include short detours. Check every leg on our <a href="/blog/ring-road-driving-times">Ring Road driving times</a> page.</p>
<h2>Days 1 and 2: Golden Circle and the south coast waterfalls</h2>
<p>Start with the Golden Circle: Þingvellir, the hot springs at Geysir and the two-step drop of Gullfoss. Sleep near Hella or Selfoss, where the countryside is dark enough for the aurora from late August.</p>
<p>On day 2, walk behind <a href="/places/seljalandsfoss">Seljalandsfoss</a> and see the neighbouring Gljúfrabúi, five minutes' walk away in a narrow gorge. Then climb the steps at Skógafoss, look at the ash-streaked tongue of Sólheimajökull, and finish at Reynisfjara before Vík. Stay back from the waves.</p>
<h2>Days 3 and 4: How much time do you need at Skaftafell and the lagoons?</h2>
<p>Give the glacier coast two days. On day 3, drive east past Kirkjubæjarklaustur to Fjaðrárgljúfur, a mossy canyon about 6 km off Route 1, then on to Skaftafell. Walk to Svartifoss (about 5.5 km return) and the glacier viewpoint in the afternoon.</p>
<p>Day 4 is your best chance for a guided <a href="/places/glacier-hikes">glacier hike</a> from Skaftafell. Never walk onto a glacier without a guide; crevasses are hidden under snow. In the afternoon, see Fjallsárlón, then Jökulsárlón and Diamond Beach, before driving about an hour to Höfn.</p>
<h2>Day 5: Which way through the East Fjords?</h2>
<p>From Höfn, stop at Stokksnes for Vestrahorn, then follow the coast through Djúpivogur. In summer, the Öxi pass saves about 70 km but is a steep, narrow gravel road. The coastal Ring Road is longer and more scenic, and it is the only choice once snow arrives. Fill up whenever you can.</p>
<h2>Day 6: What can you do around Egilsstaðir?</h2>
<p>Day 6 is a day off from the Ring Road. Walk up to Hengifoss, which falls 128 metres past red layers of rock; the walk takes 40–60 minutes each way. Then drive to <a href="/places/studlagil">Stuðlagil</a> canyon in Jökuldalur, where a glacier river runs between basalt columns.</p>
<p>If you prefer towns to hikes, drive over the mountain to Seyðisfjörður instead, with its coloured wooden houses and quiet fjord.</p>
<h2>Days 7 and 8: Dettifoss, Mývatn and Akureyri</h2>
<p>Cross the plateau to Dettifoss, taking paved Route 862 to the west bank. Dettifoss is 100 metres wide and drops 44 metres into the Jökulsárgljúfur canyon. Continue to Hverir and Mývatn, and soak at the Mývatn Nature Baths in the evening.</p>
<p>On day 8, walk the Hverfjall crater rim in the morning, then drive to Goðafoss on Route 1. Akureyri is about 45 minutes further, through the Vaðlaheiðargöng toll tunnel (ISK 2,216 per trip in 2026, paid online at veggjald.is). With time to spare, Húsavík is about an hour from Akureyri for whale watching.</p>
<h2>Days 9 and 10: Is Snæfellsnes worth the detour?</h2>
<p>Yes. Snæfellsnes packs lava fields, black beaches, fishing villages and the 1,446-metre Snæfellsjökull glacier volcano into one peninsula. Day 9 is a long drive from Akureyri over the Öxnadalsheiði and Holtavörðuheiði passes, turning west towards the peninsula after Borgarnes. Stay in Grundarfjörður, below <a href="/places/kirkjufell">Kirkjufell</a>, or in Stykkishólmur.</p>
<p>On day 10, drive around the peninsula's western tip through Snæfellsjökull National Park, past Arnarstapi and Hellnar, then back to Reykjavík in about two to two and a half hours.</p>
<p class="callout"><strong>Short on time on day 9?</strong> Sleep in Borgarnes instead and do a shorter Snæfellsnes loop on day 10. You will still see Kirkjufell and the coast, just faster.</p>
<h2>How much driving is there each day?</h2>
<p>Most days on this route have one to four hours of driving. Days 1, 5 and 9 are the long ones, at around three to five hours plus stops. Days 2, 4, 6 and 8 are short, which leaves time for a long walk, a guided tour or a swim. Keep the long days for good weather where you can, and swap days around if the forecast demands it.</p>
<h2>Where should you stay on a 10-day Ring Road trip?</h2>
<p>Book the beds in this order: the Skaftafell area and Höfn, then Vík, then Egilsstaðir and Mývatn. These are small places with few rooms, and they fill months ahead in summer. Akureyri and Reykjavík have the most choice. Two nights in Egilsstaðir mean you can leave your bags in one place for day 6. On Snæfellsnes, Grundarfjörður puts you closest to Kirkjufell, while Stykkishólmur has more restaurants and the ferry to the Westfjords. Our guide to <a href="/blog/where-to-stay-in-iceland">where to stay in Iceland</a> compares each base.</p>
<h2>When is the best time for a 10-day Ring Road trip?</h2>
<p>June to early September is best. Stuðlagil and the Öxi pass are easiest in summer, and the long days let you walk in the evening. In September the first dark nights bring a chance of northern lights; see our <a href="/northern-lights">northern lights guide</a>. In winter, read our <a href="/blog/iceland-ring-road-winter">Ring Road in winter</a> guide before committing to the full loop.</p>
<p>For rules, tolls and fuel on the road, see our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a>. If you like a book on the dashboard, our <a href="/#guides">Complete Guide to Iceland</a> follows the same loop.</p>
""",
        "checked_note": "Facts checked October 2026. Distances are approximate. Stuðlagil's colour, the Öxi pass and Route 864 depend on the season; check road.is and vedur.is each day, and confirm toll and parking fees before you travel.",
        "sources": [
            ("The Ring Road – Route Number One (Visit Iceland)", "https://visiticeland.com/article/the-ring-road"),
            ("South Coast Iceland guide (Slice of Iceland)", "https://sliceoficeland.is/articles/south-coast-iceland-guide"),
            ("Hengifoss (Wikipedia)", "https://en.wikipedia.org/wiki/Hengifoss"),
            ("Dettifoss (Wikipedia)", "https://en.wikipedia.org/wiki/Dettifoss"),
            ("North Iceland itinerary: Akureyri to Mývatn (Arctic Adventures)", "https://adventures.is/blog/north-iceland-itinerary/"),
            ("Kirkjufell (Wikipedia)", "https://en.wikipedia.org/wiki/Kirkjufell"),
            ("Snæfellsnes (Wikipedia)", "https://en.wikipedia.org/wiki/Sn%C3%A6fellsnes"),
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "iceland-ring-road-winter",
        "cluster": "ring-road",
        "pillar": False,
        "short": "Driving the Ring Road in Winter: Is It Safe?",
        "title": "Ring Road in Winter: Is It Safe to Drive Iceland's Route 1? (2027)",
        "description": "Is the Ring Road safe in winter? Route 1 from November to March: closures, mountain passes, winter tyres, daylight, wind warnings and how many days to allow.",
        "category": "Planning · Ring Road",
        "teaser": "Closures, tyres, daylight and how to plan a winter loop safely.",
        "image": "winter-road",
        "image_alt": "A cleared two-lane road winding between snow-covered mountains under a grey winter sky",
        "stats": [
            ("~4 h", "Daylight in Reykjavík around the December solstice"),
            ("1 Nov–15 Apr", "Studded winter tyres on rental cars (Blue Car Rental)"),
            ("3 mm", "Minimum tread depth for winter tyres"),
            ("1777", "Road conditions phone line"),
        ],
        "body": """
<p>Yes, the Ring Road can be driven safely in winter, but only with the right car, flexible plans and a daily check of the weather and road conditions. Route 1 is paved and has the highest priority for snow clearing. Even so, storms close the mountain passes in the north and east several times each winter, and daylight in December lasts only about four hours. Allow at least ten days for the full loop, or drive only the south coast.</p>
<!--TOC-->
<h2>Is it safe to drive the Ring Road in winter?</h2>
<p>It is safe if you drive to the conditions and are willing to wait. The road authority keeps Route 1 open as much as possible and aims to clear snow and ice before morning traffic on serviced days. The real risks are ice, wind and darkness. Blue Car Rental notes that most winter accidents are caused by ice, especially black ice around 0°C, when the road looks merely wet.</p>
<p>If you have never driven on snow and ice, think hard before booking a self-drive winter loop. Guided tours from Reykjavík or a base in one region are good alternatives. Our <a href="/blog/getting-around-iceland">getting around Iceland</a> guide compares the options.</p>
<h2>Which parts of the Ring Road close in winter?</h2>
<p>The mountain passes close most often. Visit Iceland names three: Holtavörðuheiði between Borgarnes and the north, Öxnadalsheiði west of Akureyri, and Möðrudalsöræfi, the high plateau between Mývatn and Egilsstaðir. Stretches of Route 1 in the East Fjords also close in severe weather.</p>
<p>Closures usually last hours, sometimes a day or two. When a road is closed, a sign or gate will say "Lokað", meaning closed. Respect it; closures are only put in place when needed.</p>
<p>Some side roads are effectively shut all winter. The Öxi pass (Route 939) is closed, the gravel road to the east bank of Dettifoss (Route 864) is usually impassable, and the highland F-roads are closed until summer. Paved Route 862 to the west side of Dettifoss is open more often, but it too closes in bad weather.</p>
""" + MAP_GENERAL.format(
            alt="Map of Iceland showing the Ring Road, main towns, glaciers and regions",
            cap="The Ring Road and its towns. The passes in the north and east close most often in winter.",
        ) + """
<h2>How much daylight do you get on a winter road trip?</h2>
<p>Very little in midwinter. Around the December solstice Reykjavík gets about four hours of daylight, with sunrise after 11 am. By early February that has grown to around six hours forty minutes, and to about ten hours by the end of the month. The north gets even less light in December.</p>
<p>In deep winter, plan to drive only between about 10:00 and 16:00. That means short legs of two to three hours, and sights visited in twilight. Driving in the dark on ice, with oncoming headlights and no streetlights, is much harder than it sounds.</p>
<div class="table-wrap"><table>
<thead><tr><th>Month</th><th>Daylight in Reykjavík</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>December</td><td>about 4 h</td><td>One short leg a day, or stay in one region</td></tr>
<tr><td>Early February</td><td>about 6.5 h</td><td>Short legs with one or two stops</td></tr>
<tr><td>Late February</td><td>about 10 h</td><td>A full loop becomes realistic with 10+ days</td></tr>
</tbody></table></div>
<h2>What car and tyres do you need in winter?</h2>
<p>A 4x4 is strongly recommended between October and May, according to Guide to Iceland, although Route 1 can be driven in a two-wheel-drive car all year. More important than four-wheel drive is good tyres and the experience to use them.</p>
<p>Rental cars come with winter tyres in the cold months; Blue Car Rental, for example, fits studded tyres from 1 November to 15 April. The legal minimum tread depth for winter tyres is 3 mm. Snow chains are not normally used on rental cars. Ask the rental company what tyres you will get and confirm it in writing.</p>
<h2>How do you check road conditions and weather?</h2>
<p>Check three sources every morning and again during the day:</p>
<ol>
<li><strong>road.is (umferdin.is):</strong> the road map from the Icelandic Road and Coastal Administration shows which roads are open, slippery or closed. You can also call 1777.</li>
<li><strong>vedur.is:</strong> the Icelandic Met Office forecast, with yellow, orange and red wind and snow warnings. Do not drive in orange or red warnings.</li>
<li><strong>SafeTravel:</strong> the conditions map collects alerts and closures. You can also leave your travel plan there.</li>
</ol>
<p>General weather apps are unreliable in Iceland. Use the official sources.</p>
<p class="callout"><strong>Wind is the hidden danger.</strong> Gusts can push a car across the road and tear a door off its hinges. Park facing into the wind, open doors with both hands, and treat an orange wind warning as a reason to stay put.</p>
<h2>How many days do you need for the Ring Road in winter?</h2>
<p>Allow at least ten days for the full loop in winter, not seven. That leaves short driving days and a spare day or two for closures. Book rooms with free cancellation so you can move a night if a pass shuts.</p>
<p>With seven days or fewer, skip the full loop. Drive the south coast from Reykjavík as far as <a href="/places/jokulsarlon">Jökulsárlón</a> or Höfn and back. You see <a href="/places/seljalandsfoss">Seljalandsfoss</a>, <a href="/places/reynisfjara">Reynisfjara</a> and the glacier lagoons, and in winter you can join a guided tour into the <a href="/places/ice-caves">ice caves</a> of Vatnajökull. Our <a href="/blog/iceland-5-day-itinerary">5-day Iceland itinerary</a> follows this route.</p>
<h2>What are the best things about the Ring Road in winter?</h2>
<p>Winter brings the northern lights, frozen waterfalls, snow-covered lava fields and far fewer people. The nights are long and dark from September to April, so every clear evening outside the towns is a chance to see the aurora. See our <a href="/northern-lights">northern lights guide</a> for forecasts and tips.</p>
<p>Ice caves under Vatnajökull are a winter-only experience, open only with a guide. Lake Mývatn and Akureyri are beautiful under snow, and a hot soak at the Mývatn Nature Baths ends a cold day well.</p>
<h2>What should you carry in the car in winter?</h2>
<ul>
<li>Warm layers, a hat, gloves and a blanket for everyone in the car.</li>
<li>Water, snacks and a charged power bank.</li>
<li>A snow brush and ice scraper (check the rental car has them).</li>
<li>Ice cleats for walking at icy car parks and viewpoints.</li>
<li>A full tank: never let it drop below half, as stations are far apart in the east and north.</li>
</ul>
<p>Save 112, the emergency number, and leave your travel plan with SafeTravel before you set off.</p>
<h2>What are the golden rules for winter driving in Iceland?</h2>
<ul>
<li>Drive slower than the limit when the road is icy, especially in bends and on bridges.</li>
<li>Headlights must be on at all times, day and night.</li>
<li>Never stop on the road for photos or the aurora; pull fully into a car park.</li>
<li>Stay on Route 1. Satnav apps sometimes suggest shortcuts on mountain roads that are closed.</li>
<li>If the forecast is bad, wait. A lost day is better than a dangerous drive.</li>
</ul>
<p>For everything else about Route 1, read our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a>. Our <a href="/#guides">printed Winter Guide</a> has more on driving, aurora spots and ice caves.</p>
""",
        "checked_note": "Facts checked October 2026. Winter closures happen at short notice, and rental tyre policies vary by company. Check road.is, vedur.is and SafeTravel every morning, and confirm tyres with your rental company before you travel.",
        "sources": [
            ("The Ring Road – Route Number One (Visit Iceland)", "https://visiticeland.com/article/the-ring-road"),
            ("Winter services (Icelandic Road and Coastal Administration)", "https://www.vegagerdin.is/en/the-transportation-system/the-road-system/services/winter-services"),
            ("Driving a car in the winter? (SafeTravel)", "https://safetravel.is/driving/winter/drivers-test/car/"),
            ("Top 12 tips for driving in Iceland (SafeTravel)", "https://safetravel.is/driving/top-12-tips/"),
            ("Snow tires in Iceland (Blue Car Rental)", "https://www.bluecarrental.is/blog/snow-tires-iceland/"),
            ("Winter driving in Iceland (Blue Car Rental)", "https://www.bluecarrental.is/useful-information/driving-in-iceland/winter/"),
            ("Ring Road in winter: what's open, what to skip (isnet)", "https://isnet.is/guides/ring-road-in-winter-whats-open-skip"),
            ("Ring Road travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/ring-road"),
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "iceland-5-day-itinerary",
        "cluster": "ring-road",
        "pillar": False,
        "short": "5 Days in Iceland Without the Full Ring Road",
        "title": "5 Day Iceland Itinerary: Golden Circle, South Coast and Jökulsárlón (2027)",
        "description": "A 5 day Iceland itinerary without the full Ring Road: the Golden Circle, south coast waterfalls, Vík, Skaftafell and Jökulsárlón, with distances and tips.",
        "category": "Itineraries · Ring Road",
        "teaser": "Golden Circle, south coast and the glacier lagoon in five days.",
        "image": "hx-seljalandsfoss",
        "image_alt": "Seljalandsfoss waterfall falling from a mossy cliff into a green valley",
        "stats": [
            ("~370 km", "Reykjavík to Jökulsárlón, the turning point"),
            ("60 m", "Height of Seljalandsfoss and of Skógafoss"),
            ("32 m", "Total drop of Gullfoss in two steps"),
            ("6–10 min", "Typical gap between Strokkur eruptions"),
        ],
        "body": """
<p>Five days is not enough for the whole Ring Road, but it is enough for the best of the south. This 5 day Iceland itinerary covers the Golden Circle, the south coast waterfalls, the black beaches at Vík, Skaftafell and the Jökulsárlón glacier lagoon, then returns to Reykjavík. You drive part of Route 1 out and back, with three nights on the road and short days in winter or summer.</p>
<!--TOC-->
<h2>Can you drive the Ring Road in 5 days?</h2>
<p>You can, but you should not. Driving the full loop takes roughly 17 to 20 hours without stops, so five days means four to six hours behind the wheel every day and little time at the sights. In winter it is not realistic at all.</p>
<p>The south-west holds many of Iceland's most famous sights within about 370 km of Reykjavík. Driving out to the glacier lagoon and back lets you see them properly. Save the full loop for a trip of seven days or more; see our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a>.</p>
""" + MAP_GENERAL.format(
            alt="Map of Iceland showing the Ring Road, towns, glaciers and the main regions",
            cap="Iceland overview. This 5-day plan follows Route 1 along the south coast from Reykjavík to the glacier lagoons and back.",
        ) + """
<h2>What does a 5-day Iceland itinerary look like?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>Route</th><th>Approx. drive</th><th>Overnight</th></tr></thead>
<tbody>
<tr><td>1</td><td>Golden Circle</td><td>230 km, 3–3.5 h</td><td>Hella or Selfoss area</td></tr>
<tr><td>2</td><td>Waterfalls, Sólheimajökull, Reynisfjara</td><td>100 km, 1.5 h</td><td>Vík</td></tr>
<tr><td>3</td><td>Vík to Skaftafell and Jökulsárlón</td><td>190 km, 2.5–3 h</td><td>Near Skaftafell or the lagoons</td></tr>
<tr><td>4</td><td>Back west along the south coast</td><td>about 320 km, 4–4.5 h</td><td>Reykjavík or Selfoss</td></tr>
<tr><td>5</td><td>Reykjavík and a lagoon</td><td>short</td><td>Reykjavík or the airport</td></tr>
</tbody></table></div>
<h2>Day 1: How do you drive the Golden Circle?</h2>
<p>Day 1 is the Golden Circle, a loop of about 230 km. Start at <a href="/places/thingvellir">Þingvellir National Park</a>, where Iceland's parliament first met and the continental plates pull apart. Parking is ISK 1,000 for a car.</p>
<p>Drive on to Geysir, where Strokkur erupts every six to ten minutes, usually 15–20 metres high. Then see Gullfoss, which drops 32 metres in two steps into a canyon. Head south to sleep near Selfoss or Hella, an easy start for day 2. For more stops along the loop, see our <a href="/blog/iceland-3-day-itinerary">3 days in Iceland</a> plan.</p>
<h2>Day 2: Which south coast stops should you not miss?</h2>
<p>Day 2 is a short drive with a long list of stops. Walk behind <a href="/places/seljalandsfoss">Seljalandsfoss</a>, which falls 60 metres, then find Gljúfrabúi hidden in a gorge five minutes away. Skógafoss, about 30 km east, is just as tall, with 527 steps to the top.</p>
<p>Next, look at the glacier tongue of Sólheimajökull from the edge of the lagoon; only go onto the ice with a guide. End at the Dyrhólaey headland and Reynisfjara beach before Vík.</p>
<p class="callout"><strong>Reynisfjara is dangerous.</strong> Sneaker waves run far up the beach without warning. Stay well back from the water and never turn your back on the sea.</p>
<h2>Day 3: Is Jökulsárlón worth the drive from Vík?</h2>
<p>Yes. Jökulsárlón is the highlight of the south coast, and from Vík it is about 190 km. Drive east over the Eldhraun lava field, refuel at Kirkjubæjarklaustur, and stop at Fjaðrárgljúfur canyon, about 6 km off Route 1.</p>
<p>At <a href="/places/skaftafell">Skaftafell</a>, walk to Svartifoss and its basalt columns (5.5 km return, 1.5–2 hours). Then drive to Fjallsárlón and <a href="/places/jokulsarlon">Jökulsárlón</a>, about 60 km east of Skaftafell. Walk to Diamond Beach, where icebergs wash up on black sand. Sleep in the farms and hotels near the lagoons, and book early, because there are few beds.</p>
<h2>Day 4: How long is the drive back to Reykjavík?</h2>
<p>From Jökulsárlón to Reykjavík is about 370 km, roughly five hours without stops. Split it by sleeping in Selfoss, or drive it in one go with a coffee stop in Vík. In winter, leave at first light and check road.is before you set off.</p>
<p>Break the drive with a stop you missed on the way out: perhaps Skógafoss in different light, or a coffee in Vík. If you skipped anything on day 2, catch it now. In winter, day 4 is also the day to join a guided ice cave tour from the Jökulsárlón area before driving west.</p>
<h2>Day 5: How should you spend your last day?</h2>
<p>Keep the last day light, especially if you fly home in the afternoon. Keflavík Airport is about 45 minutes from Reykjavík by car, so leave plenty of time to return the rental car. Explore Reykjavík: Hallgrímskirkja, the old harbour and a local geothermal pool. Or soak at a lagoon on the way to the airport.</p>
<p>The Blue Lagoon is on the Reykjanes peninsula near the area of recent eruptions. The Icelandic Met Office reported on 30 September 2026 that no eruption was under way but magma was still building up under Svartsengi. Check vedur.is and safetravel.is before you go.</p>
<h2>Where should you stay on a 5-day trip?</h2>
<p>Use three bases. Spend night 1 near Selfoss or Hella, night 2 in Vík, and night 3 in the farm hotels between Skaftafell and Jökulsárlón. Night 4 can be in Reykjavík or back at Selfoss to shorten the drive. Book the glacier-area night first: there are only a handful of places to stay east of Vík, and they fill early in summer and at New Year. Our guide to <a href="/blog/where-to-stay-in-iceland">where to stay in Iceland</a> covers each area.</p>
<h2>Do you need a 4x4 for this route?</h2>
<p>No. Every stop on this itinerary is on or just off paved Route 1, so a normal car is fine in summer. Guide to Iceland recommends a 4x4 from October to May for extra grip in snow, and rental cars come with winter tyres in the cold months. The short gravel road to Fjaðrárgljúfur is fine in a normal car when dry.</p>
<h2>Can you swap in Snæfellsnes instead?</h2>
<p>Yes. If you prefer coast and mountains to glaciers, replace days 3 and 4 with Snæfellsnes. It is about two to two and a half hours from Reykjavík, with Kirkjufell, lava fields and the Snæfellsjökull glacier volcano. The drives are shorter, but you miss Jökulsárlón.</p>
<p>With an extra day or two, you could also fly to Akureyri for the north. For a full loop, start with our <a href="/blog/iceland-ring-road-7-days">7-day Ring Road itinerary</a>.</p>
<h2>Does this itinerary work in winter?</h2>
<p>It works well in winter, because the south coast is the most reliable region for driving and the sights are close together. Allow for only four to six hours of daylight in December and January, so drive between about 10:00 and 16:00. Rent a car with winter tyres and check road.is and vedur.is every morning.</p>
<p>Winter also adds the northern lights, which you can watch from the dark countryside near Hella, Vík and Skaftafell on clear nights. See our <a href="/northern-lights">northern lights guide</a> and our <a href="/blog/iceland-ring-road-winter">Ring Road in winter</a> advice. For more sights to choose from, browse the <a href="/highlights">Iceland highlights</a> map.</p>
""",
        "checked_note": "Facts checked October 2026. Drive times are approximate and assume good conditions. Reykjanes volcanic activity changes quickly; check vedur.is and safetravel.is before visiting the Blue Lagoon area, and road.is before every drive.",
        "sources": [
            ("South Coast Iceland guide (Slice of Iceland)", "https://sliceoficeland.is/articles/south-coast-iceland-guide"),
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("Strokkur (Wikipedia)", "https://en.wikipedia.org/wiki/Strokkur"),
            ("Gullfoss (Wikipedia)", "https://en.wikipedia.org/wiki/Gullfoss"),
            ("Skógafoss (Wikipedia)", "https://en.wikipedia.org/wiki/Sk%C3%B3gafoss"),
            ("Jökulsárlón (Wikipedia)", "https://en.wikipedia.org/wiki/J%C3%B6kuls%C3%A1rl%C3%B3n"),
            ("Situation on the Reykjanes Peninsula (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/ground-uplift-and-magma-accumulation-continue-beneath-svartsengi"),
            ("Ring Road travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/ring-road"),
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "slug": "iceland-3-day-itinerary",
        "cluster": "ring-road",
        "pillar": False,
        "short": "3 Days in Iceland: A Plan from Reykjavík",
        "title": "3 Days in Iceland: A Reykjavík-Based Itinerary with Golden Circle (2027)",
        "description": "How to spend 3 days in Iceland from Reykjavík: the Golden Circle, the south coast to Vík and back, and a day in the city or a lagoon, with drive times.",
        "category": "Itineraries · Ring Road",
        "teaser": "Golden Circle, the south coast and Reykjavík, all from one base.",
        "image": "hx-gullfoss",
        "image_alt": "Gullfoss waterfall in winter, churning between snow-covered rocks",
        "stats": [
            ("~230 km", "Golden Circle loop from Reykjavík"),
            ("~2.5 h", "Drive from Reykjavík to Vík without stops"),
            ("ISK 1,000", "Daily parking for a car at Þingvellir"),
            ("~45 min", "Keflavík Airport to Reykjavík by car"),
        ],
        "body": """
<p>Three days in Iceland is enough for the Golden Circle, the south coast as far as Vík and a day in Reykjavík. Stay in the capital all three nights and use a hire car or day tours. You will not see the glacier lagoons or the north, but you will see geysers, giant waterfalls, black beaches and a rift valley between two continents.</p>
<!--TOC-->
<h2>Is 3 days in Iceland enough?</h2>
<p>Three days is enough for a good first taste of Iceland, if you stay close to Reykjavík. The Golden Circle and the south coast to Vík are both within a day's return drive. Anything further, such as Jökulsárlón, is a very long day: about 370 km each way.</p>
<p>Do not try to drive the Ring Road. Without stops it takes roughly 17 to 20 hours, and Visit Iceland suggests at least seven days. With five days, our <a href="/blog/iceland-5-day-itinerary">5-day Iceland itinerary</a> reaches the glacier lagoon.</p>
<h2>What does a 3-day Iceland itinerary look like?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>Plan</th><th>Driving</th></tr></thead>
<tbody>
<tr><td>1</td><td>Golden Circle: Þingvellir, Geysir, Gullfoss</td><td>About 230 km loop, 3–3.5 h</td></tr>
<tr><td>2</td><td>South coast: Seljalandsfoss, Skógafoss, Reynisfjara, Vík</td><td>About 370 km return, 5 h</td></tr>
<tr><td>3</td><td>Reykjavík, a lagoon or a short trip</td><td>Little or none</td></tr>
</tbody></table></div>
<p>If you arrive early on day 1, swap days 1 and 3 so the longest drive is not on the morning after an overnight flight. In winter, keep the south coast day for the best forecast of the three.</p>
""" + MAP_GOLDEN.format(
            alt="Map of the Golden Circle route from Reykjavík via Þingvellir, Geysir and Gullfoss",
            cap="The Golden Circle loop from Reykjavík: Þingvellir, Geysir, Gullfoss and nearby stops.",
        ) + """
<h2>Day 1: How long does the Golden Circle take?</h2>
<p>The Golden Circle takes a full day: about 230 km of driving and three to four main stops. Leave Reykjavík by 9 am to beat the tour buses.</p>
<ul>
<li><strong><a href="/places/thingvellir">Þingvellir National Park</a>:</strong> walk down the Almannagjá rift, where the North American and Eurasian plates pull apart, to the site of Iceland's ancient parliament. Parking costs ISK 1,000 for a car for the day.</li>
<li><strong>Geysir:</strong> the old Great Geysir is mostly quiet, but Strokkur erupts every six to ten minutes, usually 15–20 metres high. Stay behind the ropes; the water is boiling.</li>
<li><strong><a href="/places/gullfoss">Gullfoss</a>:</strong> the Hvítá river drops 32 metres in two steps into a canyon. The lower path gets you close to the spray; it can be icy in winter.</li>
</ul>
<p>On the way back, add the Kerið crater lake or a soak at a geothermal pool. For more on stops and timing, see our <a href="/blog/golden-circle-iceland">Golden Circle guide</a>.</p>
<h2>Day 2: Can you see the south coast in a day trip?</h2>
<p>Yes, as far as Vík. Vík is about 180–187 km from Reykjavík, roughly 2.5 hours each way without stops, so this is a long but rewarding day. Turn around at Vík; going further means driving in the dark.</p>
<ol>
<li><strong>Seljalandsfoss</strong> (about 120–130 km, under 2 hours from Reykjavík): a 60-metre waterfall you can walk behind. Pack a waterproof.</li>
<li><strong>Gljúfrabúi:</strong> a waterfall hidden in a gorge, five minutes' walk away.</li>
<li><strong>Skógafoss</strong> (about 30 km further): another 60-metre fall, 25 metres wide, with 527 steps to the top.</li>
<li><strong><a href="/places/reynisfjara">Reynisfjara</a>:</strong> basalt columns, sea stacks and black sand just west of Vík.</li>
<li><strong>Vík:</strong> a coffee and fuel stop before the drive home.</li>
</ol>
<p class="callout"><strong>Safety at Reynisfjara:</strong> sneaker waves can sweep people off the beach with no warning. Keep well back from the water's edge, keep children close and never turn your back to the sea.</p>
<h2>Day 3: What should you do in Reykjavík?</h2>
<p>Spend day 3 in <a href="/places/reykjavik">Reykjavík</a>, or split it between the city and a soak on the way to your flight. Climb the tower of Hallgrímskirkja, walk the old harbour and the shops of Laugavegur, and swim in a neighbourhood geothermal pool, which is how locals relax. Taste fish soup or a hot dog, and visit a museum if the weather turns. The compact centre is easy on foot, so you will not need the car until the evening.</p>
<p>For a bigger outing, choose one of these:</p>
<ul>
<li><strong>A lagoon:</strong> Sky Lagoon is in the capital area. The Blue Lagoon is on the Reykjanes peninsula near the site of recent eruptions. As of the Icelandic Met Office update on 30 September 2026, no eruption was under way, but magma was still accumulating under Svartsengi. Check vedur.is and safetravel.is before you go.</li>
<li><strong>Reykjadalur:</strong> a hike from Hveragerði to a warm river you can bathe in, about 45–60 minutes from Reykjavík.</li>
<li><strong>Whale watching:</strong> boats leave from Reykjavík's Old Harbour.</li>
</ul>
<h2>Should you rent a car or take tours for 3 days?</h2>
<p>Rent a car in summer if you are comfortable driving. You can start early, stop wherever you like and avoid the crowds. Pick it up at Keflavík Airport, about 48 km and 45 minutes from Reykjavík.</p>
<p>In winter, day tours are often the better choice. Snow, ice and only four to six hours of daylight make a self-drive to Vík and back hard work. Guides also know which roads are safe that day. See <a href="/blog/getting-around-iceland">getting around Iceland</a> for bus and transfer options.</p>
<h2>Where should you stay for 3 days in Iceland?</h2>
<p>Stay in Reykjavík for all three nights. You avoid packing up every morning, the city has the most choice of rooms and restaurants, and day tours pick up from the centre. If you are driving and want an earlier start on the south coast, one night in Selfoss or Hella cuts about an hour off day 2. See <a href="/blog/where-to-stay-in-iceland">where to stay in Iceland</a> for the main areas.</p>
<h2>What should you pack for a short trip?</h2>
<p>Pack for wind and rain whatever the season: a waterproof jacket and trousers, warm layers, a hat and gloves, and boots with good grip. Add ice cleats from October to April, because paths at Gullfoss and the waterfalls can be icy. Bring a swimsuit for the pools and lagoons, and a dry bag or plastic bag for your phone at Seljalandsfoss.</p>
<h2>Can you see the northern lights in 3 days?</h2>
<p>From September to April you have a chance, but three nights is a short window. You need clear skies, solar activity and darkness away from city lights. Check the aurora forecast on vedur.is each evening and drive out of town if it is clear. Our <a href="/northern-lights">northern lights guide</a> has the details.</p>
<h2>What if you have a day or two more?</h2>
<p>With a fourth day, add Snæfellsnes or stay a night in Vík and continue to Skaftafell and Jökulsárlón. With a week, drive the full loop with our <a href="/blog/iceland-ring-road-7-days">7-day Ring Road itinerary</a>. All the bigger routes start from our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a>. If you want a compact book for the trip, our <a href="/#guides">Complete Guide to Iceland</a> covers Reykjavík and the south in detail.</p>
""",
        "checked_note": "Facts checked October 2026. Distances and times are approximate. Reykjanes volcanic activity changes quickly; check vedur.is and safetravel.is before visiting the Blue Lagoon area, and road.is before every drive.",
        "sources": [
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("Strokkur (Wikipedia)", "https://en.wikipedia.org/wiki/Strokkur"),
            ("Gullfoss (Wikipedia)", "https://en.wikipedia.org/wiki/Gullfoss"),
            ("South Coast Iceland guide (Slice of Iceland)", "https://sliceoficeland.is/articles/south-coast-iceland-guide"),
            ("Driving distances between hotels (Iceland Hotel Collection by Berjaya)", "https://www.icelandhotelcollectionbyberjaya.com/magazine/blog/driving-distances-mag"),
            ("Situation on the Reykjanes Peninsula (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/ground-uplift-and-magma-accumulation-continue-beneath-svartsengi"),
            ("Iceland Ring Road driving guide (Iceland Tours)", "https://www.icelandtours.is/blog/driving-iceland-ring-road-guide/"),
        ],
    },
    # ------------------------------------------------------------------ 7
    {
        "slug": "westfjords-road-trip",
        "cluster": "ring-road",
        "pillar": False,
        "short": "Westfjords Road Trip: The Detour the Ring Road Skips",
        "title": "Westfjords Road Trip: Route, Stops, Distances and Map (2027)",
        "description": "Plan a Westfjords road trip: the route from Reykjavík, the Baldur ferry, Dynjandi, Látrabjarg, Rauðisandur, Ísafjörður and Strandir, with distances and fuel.",
        "category": "Itineraries · Westfjords",
        "teaser": "Dynjandi, Látrabjarg and empty fjord roads, far from Route 1.",
        "image": "hx-aurora-fjord",
        "image_alt": "Green northern lights over a snowy ridge, reflected in a calm fjord",
        "stats": [
            ("100 m", "Total height of Dynjandi waterfall"),
            ("14 km", "Length of the Látrabjarg bird cliffs"),
            ("~410 km", "Reykjavík to Ísafjörður via Dynjandi"),
            ("5.6 km", "Dýrafjarðargöng tunnel, opened October 2020"),
        ],
        "body": """
<p>A Westfjords road trip takes you to the part of Iceland the Ring Road skips entirely: a ragged peninsula of steep fjords, bird cliffs and tiny fishing villages in the north-west. Plan four to five days from Reykjavík, travel between June and September, and expect slow roads with some gravel. The highlights are Dynjandi waterfall, the Látrabjarg cliffs, Rauðisandur beach and the town of Ísafjörður.</p>
<!--TOC-->
<h2>Is a Westfjords road trip worth it?</h2>
<p>Yes, if you like quiet roads and wild coast more than famous sights. The Westfjords cover 8,842 km² but have only about 7,300 people, so outside Ísafjörður you can drive for an hour and meet a few cars. There are no glacier lagoons or big tour crowds. Instead you get fjord after fjord, seabirds, Arctic foxes and hot pools by the sea.</p>
<p>The cost is time. Roads follow every fjord and cross mountain passes, so distances on the map take longer than you expect. The Westfjords tourist board warns that driving times are often longer than distances suggest.</p>
""" + MAP_WESTFJORDS.format(
            alt="Map of the Westfjords with Dynjandi, Látrabjarg, Rauðisandur, Ísafjörður, Hólmavík, Djúpavík, Krossneslaug and Hornstrandir",
            cap="The Westfjords: Dynjandi, Látrabjarg and Rauðisandur in the south-west, Ísafjörður and Hornstrandir in the north, and the Strandir coast in the east.",
        ) + """
<h2>How do you get to the Westfjords from Reykjavík?</h2>
<p>You can drive all the way or take the Baldur car ferry across Breiðafjörður. Both routes start by leaving the Ring Road north of Borgarnes.</p>
<ul>
<li><strong>By road via Dynjandi:</strong> about 410 km from Reykjavík to Ísafjörður, through the south of the peninsula on Route 60.</li>
<li><strong>By road via Hólmavík:</strong> about 455 km to Ísafjörður on Route 61, following the long Ísafjarðardjúp fjord.</li>
<li><strong>By ferry:</strong> the Baldur sails from Stykkishólmur on Snæfellsnes to Brjánslækur in the southern Westfjords in about 2.5 hours, sometimes stopping at Flatey island. It carries cars, runs year-round with fewer sailings outside summer, and should be booked ahead.</li>
<li><strong>By air:</strong> flights from Reykjavík to Ísafjörður and Bíldudalur take about 40–50 minutes. You can rent a car on arrival.</li>
</ul>
<p>A good loop is to drive in on one route and out on the other, or take the ferry one way and combine the trip with <a href="/places/snaefellsnes">Snæfellsnes</a> and a stop at <a href="/places/kirkjufell">Kirkjufell</a> near Grundarfjörður.</p>
<h2>What does a 5-day Westfjords road trip look like?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>Route</th><th>Highlights</th><th>Overnight</th></tr></thead>
<tbody>
<tr><td>1</td><td>Reykjavík to the south coast of the Westfjords (or the Baldur ferry)</td><td>Fjords of Breiðafjörður, Hellulaug</td><td>Flókalundur or Reykhólar</td></tr>
<tr><td>2</td><td>Látrabjarg and Rauðisandur</td><td>Bird cliffs, red-gold beach, Garðar BA 64</td><td>Patreksfjörður</td></tr>
<tr><td>3</td><td>Patreksfjörður to Ísafjörður</td><td>Dynjandi, Hrafnseyri, Dýrafjarðargöng</td><td>Ísafjörður</td></tr>
<tr><td>4</td><td>Around Ísafjörður</td><td>Bolungarvík, Súðavík, boat trips</td><td>Ísafjörður</td></tr>
<tr><td>5</td><td>Ísafjörður to Hólmavík and Reykjavík</td><td>Ísafjarðardjúp, witchcraft museum</td><td>Reykjavík</td></tr>
</tbody></table></div>
<h2>What are the best stops in the Westfjords?</h2>
<h3>Látrabjarg and Rauðisandur</h3>
<p>Látrabjarg is the westernmost point of Iceland: a line of bird cliffs 14 km long and up to about 440 metres high. Millions of seabirds nest here in summer, including puffins, guillemots and razorbills. Stay back from the edge, which is undercut and crumbly. The last stretch of road is gravel.</p>
<p>Rauðisandur is a wide red-gold beach, about 25 km from Patreksfjörður. The access road drops steeply in tight gravel switchbacks, so drive slowly. On the shore of Patreksfjörður, the rusting Garðar BA 64, launched as a whaling ship in 1912, is described as Iceland's oldest steel ship.</p>
<h3>Dynjandi</h3>
<p>Dynjandi, in Arnarfjörður, is the most famous waterfall in the Westfjords. It spreads over a rock face with a total height of 100 metres, with five smaller falls below it. The walk from the car park up beside the lower falls takes about 15 minutes. From Dynjandi, the road continues past the historic farm of Hrafnseyri and through the Dýrafjarðargöng tunnel. Opened on 25 October 2020, it replaced the Hrafnseyrarheiði mountain road and shortened the trip between Ísafjörður and Reykjavík by 27 km.</p>
<h3>Ísafjörður and around</h3>
<p>Ísafjörður, with about 2,700 people, is the region's main town and the best base for a few nights. Go north to Bolungarvík and the old fishing station at Ósvör, or south to Súðavík for the Arctic Fox Centre, a research centre with an exhibition and café. Boats run from Ísafjörður to the Hornstrandir nature reserve between June and September; there are no roads there.</p>
<h3>Strandir and Hólmavík</h3>
<p>On the way home, stop in Hólmavík for the Museum of Icelandic Sorcery and Witchcraft. With an extra day, follow Route 643 north along the Strandir coast to Djúpavík, where a herring factory built in 1934–35 closed in 1954, and on to Krossneslaug, a geothermal pool on the beach. Route 643 is narrow, slow gravel and is not cleared of snow in winter.</p>
<h2>What are the roads like in the Westfjords?</h2>
<p>The main routes into the Westfjords are paved, but many side roads and the roads to Látrabjarg and Rauðisandur are gravel. A normal car is fine in summer if you drive slowly; you do not need a 4x4 unless you plan to use F-roads. Expect steep passes, single-lane stretches and sheep on the road.</p>
<p>Fuel stations are few. There are stations in Ísafjörður, Patreksfjörður and Hólmavík, and smaller ones in places such as Bíldudalur, Þingeyri and Reykhólar. Never pass a station with less than half a tank.</p>
<p class="callout"><strong>Before every drive:</strong> check road.is for passes such as Dynjandisheiði and Steingrímsfjarðarheiði, and vedur.is for wind. Mountain roads here can be snowy even in early summer.</p>
<h2>When is the best time for a Westfjords road trip?</h2>
<p>June to August is the best time. The days are long, the seabirds are nesting and boats to Hornstrandir run. September is quieter and still usually fine. From October to May, snow, ice and short days make many roads difficult, and some, like Route 643 north of Bjarnarfjörður, are not cleared at all. The main roads into the region are serviced in winter, but this is a summer trip for most visitors.</p>
<h2>How many days do you need for the Westfjords?</h2>
<p>Plan at least four days, and five if you can. Lonely Planet suggests three to five days based in Ísafjörður for the main highlights, and a week or more if you want to hike Hornstrandir or kayak the fjords. The drive from Reykjavík alone is five to six hours each way, so a two-day visit leaves little time at the sights. Distances inside the region are slow too: Ísafjörður to Dynjandi is about 100 km, roughly 1.5 to 2 hours, and Dynjandi to Látrabjarg about 90 km, another two hours.</p>
<h2>How does the Westfjords fit with the Ring Road?</h2>
<p>The Westfjords are a detour from the Ring Road, not a part of it. They fit best into a trip of two weeks or more: drive the full loop, then turn north at Borgarnes or after Holtavörðuheiði for four or five extra days. With less time, choose: a <a href="/blog/iceland-ring-road-10-days">10-day Ring Road trip</a> or a slower week split between Snæfellsnes and the Westfjords.</p>
<p>For planning the main loop, start with our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a>. For more wild places beyond Route 1, see our <a href="/highlights">Iceland highlights</a>. Our <a href="/#guides">printed Summer Guide</a> has a Westfjords chapter for the road.</p>
""",
        "checked_note": "Facts checked October 2026. Road surfaces, ferry timetables and fuel opening hours change by season; check road.is, vedur.is and ferry and airline schedules before you travel.",
        "sources": [
            ("How to travel to the Westfjords (Westfjords tourist board)", "https://www.westfjords.is/en/travel-info/westfjords/how-to-get-here"),
            ("Guide to Iceland's Westfjords (Lonely Planet)", "https://www.lonelyplanet.com/articles/guide-to-westfjords-iceland"),
            ("New tunnel and Ring Road 2 open in West Fjords (Iceland Monitor)", "https://icelandmonitor.mbl.is/news/nature_and_travel/2020/10/27/new_tunnel_and_ring_road_2_open_in_west_fjords"),
            ("Baldur ferry Stykkishólmur to Brjánslækur (Guide to Iceland)", "https://guidetoiceland.is/book-holiday-trips/stykkisholmur-brjanslaekur"),
            ("Látrabjarg (Wikipedia)", "https://en.wikipedia.org/wiki/L%C3%A1trabjarg"),
            ("Dynjandi (Wikipedia)", "https://en.wikipedia.org/wiki/Dynjandi"),
            ("Strandir coast travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/strandir"),
            ("Driving the Westfjords (Iceland Car Guide)", "https://icelandcarguide.com/roads/westfjords"),
        ],
    },
    # ------------------------------------------------------------------ 8
    {
        "slug": "ring-road-driving-times",
        "cluster": "ring-road",
        "pillar": False,
        "short": "Ring Road Driving Times and Distances",
        "title": "Ring Road Driving Times: Distances Stop by Stop Around Iceland (2027)",
        "description": "Ring Road driving times and distances stop by stop: every leg of Route 1 from Reykjavík to Vík, Höfn, Egilsstaðir, Akureyri and back, plus the main detours.",
        "category": "Planning · Ring Road",
        "teaser": "Every leg of Route 1 in kilometres and hours, plus the detours.",
        "image": "hx-braided-rivers",
        "image_alt": "Black meltwater channels branching across a snow-covered plain",
        "stats": [
            ("1,322 km", "Length of Route 1 around Iceland"),
            ("17–20 h", "Rough non-stop driving time for the loop"),
            ("389 km", "Reykjavík to Akureyri, the longest usual one-day drive"),
            ("~70 km", "Distance the Öxi pass saves in summer"),
        ],
        "body": """
<p>Driving the whole Ring Road takes roughly 17 to 20 hours without stops, over about 1,322 km of Route 1. The table below breaks the loop into legs between the main towns and sights, anticlockwise from Reykjavík, with approximate distances and drive times in good summer conditions. Add time for stops, roadworks and weather, and much more in winter.</p>
<!--TOC-->
<h2>How long does it take to drive the Ring Road?</h2>
<p>Without stops, the Ring Road takes about 17 to 20 hours of driving. Nobody does it that way. With sightseeing, plan at least seven days, as Visit Iceland suggests, and ten for a relaxed trip. On a 7-day loop you drive two to five hours a day; on a 10-day loop, one to four.</p>
<p>The speed limit on the Ring Road is 90 km/h, so the average speed over a long leg is lower, around 70–80 km/h once you count towns, bridges, roadworks and slow traffic. The times below assume that average.</p>
""" + MAP_RING.format(
            alt="Map of the Ring Road around Iceland with daily legs and distances between Reykjavík, Hella, Vík, Höfn, Egilsstaðir, Mývatn and Akureyri",
            cap="The Ring Road as a 7-day route, with the approximate distance of each day's leg.",
        ) + """
<h2>What are the Ring Road distances stop by stop?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Leg</th><th>Distance</th><th>Drive time</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Reykjavík to Selfoss</td><td>about 50–55 km</td><td>45 min</td><td>Over the Hellisheiði heath</td></tr>
<tr><td>Selfoss to Hella</td><td>about 40 km</td><td>30 min</td><td>Hella is 94 km from Reykjavík</td></tr>
<tr><td>Hella to <a href="/places/seljalandsfoss">Seljalandsfoss</a></td><td>about 30 km</td><td>25 min</td><td>Waterfall beside Route 1</td></tr>
<tr><td>Seljalandsfoss to Skógafoss</td><td>about 30 km</td><td>25 min</td><td></td></tr>
<tr><td>Skógafoss to Vík</td><td>about 35 km</td><td>30 min</td><td><a href="/places/reynisfjara">Reynisfjara</a> is a short detour</td></tr>
<tr><td>Vík to Kirkjubæjarklaustur</td><td>about 75 km</td><td>1 h</td><td>Next fuel east of Vík</td></tr>
<tr><td>Kirkjubæjarklaustur to <a href="/places/skaftafell">Skaftafell</a></td><td>about 70 km</td><td>1 h</td><td>Across the Skeiðarársandur plain</td></tr>
<tr><td>Skaftafell to <a href="/places/jokulsarlon">Jökulsárlón</a></td><td>about 60 km</td><td>45 min</td><td>Fjallsárlón on the way</td></tr>
<tr><td>Jökulsárlón to Höfn</td><td>about 75–80 km</td><td>1 h</td><td>Höfn is just off Route 1</td></tr>
<tr><td>Höfn to Egilsstaðir (coast)</td><td>about 250–260 km</td><td>3.5–4 h</td><td>Via the East Fjords and Djúpivogur</td></tr>
<tr><td>Höfn to Egilsstaðir (Öxi)</td><td>about 185 km</td><td>3 h</td><td>Summer only; 19 km of steep gravel</td></tr>
<tr><td>Egilsstaðir to Mývatn</td><td>about 165 km</td><td>2 h</td><td>Over the Möðrudalsöræfi plateau</td></tr>
<tr><td>Mývatn to Akureyri</td><td>about 90 km</td><td>1–1.25 h</td><td>Via Goðafoss and the toll tunnel</td></tr>
<tr><td>Akureyri to Blönduós</td><td>about 145 km</td><td>1.75–2 h</td><td>Over Öxnadalsheiði</td></tr>
<tr><td>Blönduós to Borgarnes</td><td>about 170 km</td><td>2–2.25 h</td><td>Over Holtavörðuheiði</td></tr>
<tr><td>Borgarnes to Reykjavík</td><td>about 74 km</td><td>1 h</td><td>Through the Hvalfjörður tunnel</td></tr>
</tbody></table></div>
<p>Adding up the legs gives a little more than the official 1,322 km, because some towns, including Höfn and central Reykjavík, sit just off Route 1. Distances are rounded from several sources and from the official road length; use them for planning, not to the kilometre.</p>
<h2>What are the distances from Reykjavík to the main towns?</h2>
<div class="table-wrap"><table>
<thead><tr><th>From Reykjavík to</th><th>Distance</th><th>Drive time</th></tr></thead>
<tbody>
<tr><td>Keflavík Airport</td><td>48 km</td><td>45 min</td></tr>
<tr><td>Borgarnes</td><td>74 km</td><td>1 h</td></tr>
<tr><td>Hella</td><td>94 km</td><td>1.25 h</td></tr>
<tr><td>Vík</td><td>about 180–187 km</td><td>2.5 h</td></tr>
<tr><td>Blönduós</td><td>about 243 km</td><td>3 h</td></tr>
<tr><td>Skaftafell</td><td>about 327 km</td><td>4.5 h</td></tr>
<tr><td>Jökulsárlón</td><td>about 370 km</td><td>5 h</td></tr>
<tr><td>Akureyri</td><td>389 km</td><td>4.5 h</td></tr>
<tr><td>Höfn</td><td>about 455 km</td><td>6 h</td></tr>
<tr><td>Egilsstaðir (via the north)</td><td>about 654 km</td><td>8 h</td></tr>
</tbody></table></div>
<p>Egilsstaðir is roughly the same distance from Reykjavík either way round. In 2004 the Icelandic Science Web measured the route via the north as 654 km and via the south as 698 km, before newer tunnels shortened both.</p>
<h2>Which legs of the Ring Road are the longest?</h2>
<p>Akureyri to Reykjavík (389 km) is the longest leg most people drive in one day. Vík to Höfn (about 270 km) and Höfn to Egilsstaðir (about 250 km by the coast) come next. On a 7-day trip, these three are your long days. Our <a href="/blog/iceland-ring-road-7-days">7-day Ring Road itinerary</a> puts one on each of days 3, 4 and 7. With more days, split each of them in two.</p>
<h2>How long are the main detours off the Ring Road?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Detour</th><th>Distance or time</th><th>Good to know</th></tr></thead>
<tbody>
<tr><td>Golden Circle loop</td><td>about 230 km from Reykjavík</td><td>Þingvellir, Geysir, Gullfoss</td></tr>
<tr><td>Fjaðrárgljúfur canyon</td><td>about 6 km off Route 1</td><td>Near Kirkjubæjarklaustur</td></tr>
<tr><td>Stokksnes and Vestrahorn</td><td>a short detour before Höfn</td><td>Black dunes below the peaks</td></tr>
<tr><td>Dettifoss (west, Route 862)</td><td>1–1.25 h each way from Mývatn</td><td>Paved; can close in winter</td></tr>
<tr><td>Akureyri to Goðafoss</td><td>about 45 min</td><td>Right on Route 1</td></tr>
<tr><td>Akureyri to Húsavík</td><td>about 1 h</td><td>Whale watching</td></tr>
<tr><td>Snæfellsnes from Reykjavík</td><td>about 2–2.5 h</td><td>Kirkjufell and Snæfellsjökull</td></tr>
<tr><td>Ísafjörður from Reykjavík</td><td>about 410–455 km</td><td>See our <a href="/blog/westfjords-road-trip">Westfjords road trip</a></td></tr>
</tbody></table></div>
<h2>Are there tolls or tunnels that affect drive times?</h2>
<p>Two tunnels save real time. The Hvalfjörður tunnel, 5.8 km long and free since September 2018, cuts out the long drive around the fjord north of Reykjavík. The Vaðlaheiðargöng tunnel near Akureyri, 7.4 km long and opened in December 2018, saves about 16 km. It costs ISK 2,216 per trip for a car (2026), paid online at veggjald.is within 24 hours. The free alternative over Víkurskarð adds about 16 km and can be closed in winter.</p>
<h2>How much longer do drives take in winter?</h2>
<p>Add at least an hour or two to each driving day in winter, and more in snow or wind. You will drive slower on ice, stop to clear windows and wait for snowploughs, and in midwinter you only have about four hours of daylight in Reykjavík. Mountain passes such as Holtavörðuheiði, Öxnadalsheiði and Möðrudalsöræfi can close for hours or days.</p>
<p class="callout"><strong>Plan by daylight, not distance.</strong> In winter, keep each day's drive to two or three hours and finish before dark. Check road.is and vedur.is every morning.</p>
<p>Read our <a href="/blog/iceland-ring-road-winter">Ring Road in winter</a> guide before booking a winter loop, and our <a href="/blog/iceland-ring-road-guide">complete Ring Road guide</a> for the rules of the road. Our <a href="/#guides">printed Complete Guide to Iceland</a> covers each region along the way.</p>
<h2>Where are the longest gaps between services?</h2>
<p>The south-west and the Akureyri area have fuel, food and toilets every few dozen kilometres. The gaps open up in three places. East of Vík, Kirkjubæjarklaustur is the next fuel stop, about 75 km away. Between Höfn and Egilsstaðir, stations are few, so fill up in Höfn. And on the high plateau between Mývatn and Egilsstaðir there is almost nothing for long stretches, and this is also where temperatures run lowest in winter. Keep the tank above half on all three and carry water and snacks.</p>
<h2>How do you plan your own Ring Road days?</h2>
<ul>
<li>Use the leg table above to find natural overnight stops 150–275 km apart.</li>
<li>Add 30–60 minutes for every major stop, and 2 hours for a hike such as Svartifoss.</li>
<li>Book the scarce beds first: Vík to Höfn, then the east.</li>
<li>Keep fuel above half between Höfn and Egilsstaðir and on the plateau east of Mývatn.</li>
<li>Leave one flexible half day for weather.</li>
</ul>
""",
        "checked_note": "Facts checked October 2026. Distances are rounded from several sources and drive times assume about 70–80 km/h average in good conditions. Realignments and new bridges change the figures; check road.is before each journey.",
        "sources": [
            ("The Ring Road – Route Number One (Visit Iceland)", "https://visiticeland.com/article/the-ring-road"),
            ("Driving distances between hotels (Iceland Hotel Collection by Berjaya)", "https://www.icelandhotelcollectionbyberjaya.com/magazine/blog/driving-distances-mag"),
            ("7-day Ring Road itinerary with distances (Dollar Car Rental Iceland)", "https://dollar.is/iceland-travel-guide/self-drive-itineraries/7-day-ring-road-itinerary-your-iceland-adventure"),
            ("South Coast Iceland guide (Slice of Iceland)", "https://sliceoficeland.is/articles/south-coast-iceland-guide"),
            ("Húnaflói: getting there (Frommer's)", "https://www.frommers.com/destinations/hunafloi/planning-a-trip"),
            ("How far is it between Egilsstaðir and Reykjavík? (Vísindavefurinn)", "https://www.visindavefur.is/svar.php?id=4647"),
            ("Öxi Pass, Route 939 (Lonely Planet)", "https://www.lonelyplanet.com/points-of-interest/oxi-pass-route-939/1603264"),
            ("Vaðlaheiðargöng tunnel toll (Go Car Rental)", "https://www.gocarrental.is/driving/driving-tips/iceland-tunnel-toll/"),
        ],
    },
]
