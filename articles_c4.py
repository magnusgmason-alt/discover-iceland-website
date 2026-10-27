"""Golden Circle cluster: journal articles. Each body uses <h2> question
headings; <!--TOC--> marks where the table of contents and fact tiles go."""

MAP_GC = (
    '<figure class="a-figure a-map"><a href="/assets/img/map-golden-circle-2800.jpg" target="_blank" rel="noopener">'
    '<img src="/assets/img/map-golden-circle-1800.jpg" srcset="/assets/img/map-golden-circle-800.jpg 800w, '
    '/assets/img/map-golden-circle-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" '
    'loading="lazy" decoding="async"></a><figcaption>{cap} Tap to open full size.</figcaption></figure>'
)

ARTICLES = [
    # ------------------------------------------------------------------ 1. PILLAR
    {
        "slug": "golden-circle-iceland",
        "cluster": "golden-circle",
        "pillar": True,
        "short": "The Golden Circle: Self-Drive Guide and Map",
        "title": "Golden Circle Iceland: Self-Drive Guide, Route, Stops and Map (2027)",
        "description": "Golden Circle Iceland self-drive guide for 2027: the 250 km loop from Reykjavík to Þingvellir, Geysir and Gullfoss, with drive times, fees and extra stops.",
        "category": "Itineraries · Golden Circle",
        "teaser": "Þingvellir, Geysir and Gullfoss in one day from Reykjavík, with times, fees and a map.",
        "image": "hx-gullfoss",
        "image_alt": "Gullfoss waterfall in winter, churning between snow-covered rocks",
        "stats": [
            ("~250 km", "The Golden Circle loop from Reykjavík and back"),
            ("32 m", "Total drop of Gullfoss, in two tiers"),
            ("ISK 1,000", "Day parking at Þingvellir for a car with up to 5 seats"),
            ("930", "Year the Alþingi assembly first met at Þingvellir"),
        ],
        "body": """
<p>The Golden Circle is a loop of about 250 km from Reykjavík that links Iceland's three most visited sights: Þingvellir National Park, the Geysir hot spring area and Gullfoss waterfall. It is paved all the way, open all year and needs no 4x4. You can drive it in a single day, with three to four hours behind the wheel and the rest of the day on foot. This guide covers the route, the driving times, what each stop is like, what you pay, and how to make the day better than the coach tours.</p>
<!--TOC-->
<h2>What is the Golden Circle in Iceland?</h2>
<p>The Golden Circle is the name for a round trip from Reykjavík to three sights in the countryside to the east: Þingvellir, Geysir and Gullfoss. It is not one road but a loop of several, and it is Iceland's most popular day trip. Visit Iceland puts the classic loop at about 250 km from Reykjavík and back.</p>
<p>The three stops show three sides of Iceland in a few hours. At Þingvellir you walk through a rift valley where the North American and Eurasian plates are pulling apart, on the site of Iceland's old parliament. At Geysir a hot spring blasts boiling water into the air every few minutes. At Gullfoss a glacial river drops into a deep canyon. Around them is a farming area full of greenhouses, geothermal pools and smaller waterfalls, which is where the day gets interesting.</p>
<h2>How long does the Golden Circle drive take?</h2>
<p>The core loop takes about three to four hours of pure driving, and most people spend six to eight hours on the full day. Allow one to two hours at Þingvellir, 30 to 60 minutes at Geysir and 45 minutes or so at Gullfoss, plus lunch. Add each extra stop on top.</p>
<p>These are the usual legs in summer conditions, driving clockwise. Times are approximate and longer in snow, wind or heavy traffic.</p>
<div class="table-wrap"><table>
<thead><tr><th>Leg</th><th>Roads</th><th>Distance</th><th>Drive time</th></tr></thead>
<tbody>
<tr><td>Reykjavík → Þingvellir</td><td>Route 1, then Route 36</td><td>About 50 km</td><td>About 45 min</td></tr>
<tr><td>Þingvellir → Geysir</td><td>Routes 36, 365 and 37 via Laugarvatn</td><td>About 60 km</td><td>About 50 min</td></tr>
<tr><td>Geysir → Gullfoss</td><td>Route 35</td><td>About 10 km</td><td>About 10 min</td></tr>
<tr><td>Gullfoss → Reykjavík</td><td>Route 35 to Selfoss, then Route 1</td><td>Roughly 120 km</td><td>About 1 h 45 min</td></tr>
</tbody></table></div>
<p>The loop works in either direction. Clockwise, as above, is the classic order and puts Gullfoss in the middle of the day. Anticlockwise reaches Gullfoss first and can help you dodge the morning tour buses at Þingvellir.</p>
""" + MAP_GC.format(
            alt="Map of the Golden Circle route from Reykjavík to Þingvellir, Geysir, Gullfoss and nearby stops",
            cap="The Golden Circle loop: Þingvellir, Geysir and Gullfoss, with the nearby stops around Laugarvatn, Flúðir and Selfoss.",
        ) + """
<h2>What is the best Golden Circle route for a self-drive day?</h2>
<p>Leave Reykjavík early, visit Þingvellir first, then Geysir, then Gullfoss, and come back by the southern road through Selfoss. This keeps the driving smooth and lets you add stops on the way home. Here is a day that works from spring to autumn.</p>
<ol>
<li><strong>8.00 Leave Reykjavík.</strong> Take Route 1 north out of the city and turn onto Route 36 over the Mosfellsheiði moor.</li>
<li><strong>8.45 Þingvellir.</strong> Park at Hakið (P1) by the visitor centre and walk down through the Almannagjá gorge to the Law Rock and Öxarárfoss. Allow 1.5 hours.</li>
<li><strong>10.30 Drive to Laugarvatn.</strong> Route 365 crosses the Lyngdalsheiði heath to the lakeside village of Laugarvatn.</li>
<li><strong>11.30 Geysir.</strong> Watch Strokkur erupt a few times and walk the paths past the Great Geysir. Have lunch at the cafés across the road.</li>
<li><strong>13.30 Gullfoss.</strong> See the falls from the upper viewpoint and walk down to the lower path if it is open.</li>
<li><strong>14.30 The way home.</strong> Pick one or two extras on Route 35: Faxi waterfall, the Friðheimar greenhouse, the Secret Lagoon at Flúðir or Kerið crater.</li>
<li><strong>18.00 Back in Reykjavík,</strong> or stay the night in the countryside for dark skies and an early start on the south coast.</li>
</ol>
<p class="callout">Arrive at Þingvellir before about 9 am or after 4 pm. The big tour coaches arrive mid-morning, and the paths through Almannagjá get crowded.</p>
<h2>What is there to see at Þingvellir National Park?</h2>
<p>Þingvellir is a rift valley where you can walk along the edge of the North American plate, and it is also the birthplace of Iceland's parliament. The Alþingi first met here in 930 and kept gathering on the site for more than eight centuries. Iceland declared its independence from Denmark at Þingvellir on 17 June 1944. The park has been a UNESCO World Heritage Site since 2004.</p>
<p>The main walk runs down through Almannagjá, the largest fault in the park, from the visitor centre at Hakið to the Lögberg (Law Rock) and on to Öxarárfoss, a waterfall that drops over the fault wall. The small Þingvallakirkja church and Þingvallavatn, Iceland's largest natural lake, are a short walk away. Silfra, a fissure of clear glacial water, is where you can snorkel or dive between the plates with a licensed operator.</p>
<p>Parking costs ISK 1,000 a day for a car with up to five seats and covers all three main car parks (P1 Hakið, P2 by Öxarárfoss and P5 by Silfra). Pay at the machines or online at checkit.is. Read our full <a href="/blog/thingvellir-national-park">Þingvellir National Park guide</a> for the walks, Silfra and the history, or see the <a href="/places/thingvellir">Þingvellir place page</a>.</p>
<h2>What happens at Geysir?</h2>
<p>At Geysir you watch Strokkur, a hot spring that erupts every few minutes, throwing boiling water usually 15 to 20 metres into the air. The Great Geysir next to it gave its name to every geyser in the world, but it rarely erupts today. The whole Haukadalur geothermal area is free to enter and open all the time.</p>
<p>A loop of paths leads past steaming vents, bubbling pools and mineral-stained ground. Stay behind the ropes: the water in the vents is close to boiling. Stand upwind of Strokkur unless you want a warm shower. Parking costs about ISK 1,000, paid through the Parka app. The hotel, shops and cafés across Route 35 make Geysir the natural lunch stop. More detail in our guide to <a href="/blog/geysir-strokkur">Geysir and Strokkur</a> and on the <a href="/places/geysir">Geysir place page</a>.</p>
<h2>How big is Gullfoss, and how long do you need there?</h2>
<p>Gullfoss drops a total of 32 metres in two tiers, 11 and 21 metres, into a canyon about 2.5 km long. The river is the glacial Hvítá, and in summer around 140 cubic metres of water pour over every second. You need about 45 minutes to an hour to see it properly.</p>
<p>A short path leads from the car park to the upper viewpoint, and stairs lead down to a lower path that runs out to the edge of the first tier. That lower path is often closed by ice in winter. Expect spray, so bring a waterproof jacket in any season. The site is free to enter, and there is a café and shop at the visitor centre. The falls were protected in 1979; a stone memorial above them honours Sigríður Tómasdóttir, the farmer's daughter credited with fighting to keep them out of foreign hands. See the <a href="/places/gullfoss">Gullfoss place page</a> for photos.</p>
<h2>How much does it cost to visit the Golden Circle?</h2>
<p>The three main sights are free to enter, but you pay for parking at two of them. These were the prices we found in October 2026:</p>
<div class="table-wrap"><table>
<thead><tr><th>Stop</th><th>Entry</th><th>Parking or fee</th></tr></thead>
<tbody>
<tr><td>Þingvellir</td><td>Free</td><td>ISK 1,000 a day per car (up to 5 seats)</td></tr>
<tr><td>Geysir</td><td>Free</td><td>About ISK 1,000 via the Parka app</td></tr>
<tr><td>Gullfoss</td><td>Free</td><td>No parking fee listed in the sources we checked</td></tr>
<tr><td>Kerið crater</td><td>About ISK 700 per person</td><td>Free parking</td></tr>
<tr><td>Faxi waterfall</td><td>Free</td><td>About ISK 700–900</td></tr>
<tr><td>Secret Lagoon</td><td>About ISK 4,200 per adult (2025 price)</td><td>Free parking</td></tr>
<tr><td>Laugarvatn Fontana</td><td>ISK 7,490 per adult</td><td>Free parking</td></tr>
</tbody></table></div>
<p>Add fuel for around 250 km and lunch. Parking machines and apps change, so check the signs on the day. At Þingvellir, cameras read number plates, so pay before you leave.</p>
<h2>Should you self-drive the Golden Circle or take a tour?</h2>
<p>Self-drive is best if you want to set your own pace, beat the crowds and add the smaller stops. A tour is best if you are travelling alone, do not want to drive on Icelandic roads, or are visiting in midwinter. Classic coach tours from Reykjavík cost from about ISK 12,000 per person and take seven to eight hours, with hotel pickup.</p>
<p>For a couple, the cost of a rental car and fuel is roughly the same as two tour tickets. For three or more people, driving is usually cheaper. We compare the two in detail in <a href="/blog/golden-circle-self-drive-or-tour">Golden Circle: self-drive or tour?</a></p>
<h2>What other stops can you add to the Golden Circle?</h2>
<p>The best extra stops are Kerið crater, the Friðheimar tomato greenhouse, the Secret Lagoon at Flúðir, Laugarvatn Fontana, Faxi waterfall and Brúarfoss. Each adds 30 minutes to two hours. Pick two or three rather than trying to fit them all in.</p>
<ul>
<li><strong>Kerið:</strong> a red-walled volcanic crater with a green lake, on Route 35 north of Selfoss. Walk the rim and go down to the water.</li>
<li><strong>Friðheimar:</strong> a geothermal greenhouse at Reykholt where you eat tomato soup among the tomato plants. Book a table.</li>
<li><strong>Secret Lagoon:</strong> a natural hot pool at Flúðir, built in 1891, with water at 38–40°C.</li>
<li><strong>Laugarvatn Fontana:</strong> lakeside steam baths and a geothermal bakery where rye bread is baked in the hot ground.</li>
<li><strong>Faxi:</strong> a wide, low waterfall with a salmon ladder, about 11 km south of Geysir.</li>
<li><strong>Hveragerði and Reykjadalur:</strong> a greenhouse town on Route 1 and the walk to a hot river you can bathe in. See the <a href="/places/reykjadalur">Reykjadalur place page</a>.</li>
</ul>
<p>Prices, opening hours and how long each takes are in our guide to <a href="/blog/golden-circle-extra-stops">the best extra Golden Circle stops</a>.</p>
<h2>Can you drive the Golden Circle in winter?</h2>
<p>Yes. The Golden Circle is open all year, the main roads are cleared, and it is one of the easier winter drives in Iceland. The challenges are short daylight, ice and wind. In late December the sun is up for only about four hours, so you leave Reykjavík in the dark and see Gullfoss in the early afternoon.</p>
<p>Use a car with winter tyres, which rental companies normally fit in the cold months, and carry ice cleats for the paths at Þingvellir, Geysir and Gullfoss. Storms close roads a few days each winter, so check road conditions every morning. On clear winter nights the dark countryside away from Reykjavík is good for the northern lights. Our <a href="/blog/golden-circle-in-winter">Golden Circle in winter guide</a> covers the driving, the closures and the best aurora stops.</p>
<h2>Is the Golden Circle worth it?</h2>
<p>Yes, for most visitors. It packs geology, history and two of Iceland's most famous natural sights into a short, easy drive from the capital. It is also very busy, and if you only see the three headline stops with a coach full of people, it can feel rushed.</p>
<p>The way to make it worth it is to start early, add one or two quieter stops and stay out until the light changes. If you have a whole trip in Iceland, the Golden Circle also makes a natural first day of a Ring Road drive or a trip along the south coast. For more ideas, browse all of Iceland's <a href="/highlights">highlights on the interactive map</a>.</p>
<h2>Can you combine the Golden Circle with the south coast?</h2>
<p>Yes, but it works best over two days. Driving the Golden Circle and the south coast waterfalls in one go adds up to roughly 450–500 km and seven to nine hours behind the wheel, which leaves little time to walk. Split it instead: do the Golden Circle on day one, sleep near Selfoss, Hella or Hvolsvöllur, and drive on to Seljalandsfoss, Skógafoss and Vík on day two.</p>
<p>This is also how most Ring Road trips begin. The Golden Circle makes an easy first day after a long flight, and Route 35 brings you down to Route 1 at Selfoss, where the south coast starts. See our <a href="/blog/iceland-ring-road-guide">Ring Road guide</a> and our <a href="/blog/south-coast-iceland">south coast guide</a> to plan what comes next.</p>
<h2>Where should you stay near the Golden Circle?</h2>
<p>Stay in Reykjavík if the Golden Circle is a day trip, and in the countryside if you want quiet mornings at the sights. Laugarvatn, Flúðir, Reykholt, Selfoss and Hveragerði all have hotels, guesthouses and cabins. Staying overnight lets you reach Þingvellir or Gullfoss before the tour buses, and the dark skies are far better for the northern lights than the city. Selfoss and Hveragerði are on Route 1, so they also make a good start for the south coast. See our guide on <a href="/blog/where-to-stay-in-iceland">where to stay in Iceland</a> for the bigger picture.</p>
<h2>What should you know before driving the Golden Circle?</h2>
<ul>
<li><strong>Never stop on the road.</strong> Pull into a proper car park or lay-by for photos, even on quiet stretches.</li>
<li><strong>Watch your speed.</strong> The limit is 90 km/h on paved rural roads, and speed cameras are common.</li>
<li><strong>Keep to the paths.</strong> At Þingvellir the moss and fissures are fragile, and at Geysir the ground near the vents can be scalding.</li>
<li><strong>Pack a swimsuit.</strong> Several geothermal pools sit right on the route.</li>
<li><strong>Start with a full tank.</strong> Fill up in Reykjavík; the loop passes through villages, but the stops themselves are spread out.</li>
<li><strong>Check conditions.</strong> Look at the road map on umferdin.is and the forecast on vedur.is before you leave, especially from October to April.</li>
</ul>
<p>For general driving rules and car hire, see <a href="/blog/getting-around-iceland">getting around Iceland</a>. If you like having the route on paper, our Complete Guide to Iceland, one of our <a href="/#guides">printed guidebooks</a>, has the Golden Circle with maps and timings.</p>
""",
        "checked_note": "Facts checked October 2026. Parking fees, entry prices and opening hours change, and the Secret Lagoon price is the latest published figure we could find (2025). Driving times are approximate summer times; check umferdin.is and vedur.is before you set off.",
        "sources": [
            ("What is the Golden Circle? (Visit Iceland)", "https://visiticeland.com/article/the-golden-circle"),
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("Gullfoss (Wikipedia)", "https://en.wikipedia.org/wiki/Gullfoss"),
            ("Golden Circle map and driving times (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/golden-circle/map"),
            ("Golden Circle tour prices (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/guides/golden-circle-tour-prices"),
            ("Parking in Iceland (Iceland Tours)", "https://www.icelandtours.is/travel-guide/parking-in-iceland/"),
            ("Golden Circle guide (Campeasy)", "https://campeasy.com/stories/golden-circle"),
        ],
    },
    # ------------------------------------------------------------------ 2. SELF-DRIVE OR TOUR
    {
        "slug": "golden-circle-self-drive-or-tour",
        "cluster": "golden-circle",
        "pillar": False,
        "short": "Golden Circle: Self-Drive or Tour?",
        "title": "Golden Circle Self Drive or Tour: Which Is Better? Costs Compared (2027)",
        "description": "Golden Circle self drive or guided tour? Compare costs, timings, crowds, winter driving and flexibility, with 2026 tour prices and who each option suits best.",
        "category": "Planning · Golden Circle",
        "teaser": "Car or coach? Costs, crowds and winter driving compared.",
        "image": "journal-ring-road",
        "image_alt": "A road winding between snow-covered mountains under a grey sky",
        "stats": [
            ("~250 km", "Classic Golden Circle loop from Reykjavík"),
            ("3–4 h", "Pure driving time for the core loop"),
            ("ISK 11,990", "Example classic coach tour price per person, 2026"),
            ("7–8 h", "Typical length of a classic Golden Circle tour"),
        ],
        "body": """
<p>For most visitors with a driving licence, self-driving the Golden Circle is the better choice. You set your own timing, arrive before the coaches and add the smaller stops tours skip. A guided tour wins if you are travelling alone, if you do not want to drive in Iceland, or if you are visiting in the dark, icy weeks of midwinter. Here is how the two compare on cost, time, crowds and comfort.</p>
<!--TOC-->
<h2>Is it easy to self-drive the Golden Circle?</h2>
<p>Yes. The Golden Circle is one of the easiest drives in Iceland. The roads are paved, the sights are signposted, and the loop is open all year without a 4x4. Visit Iceland puts the classic loop at about 250 km from Reykjavík and back, which takes three to four hours of pure driving.</p>
<p>What makes it harder is the weather and the light, not the roads. From November to February you get short days, ice and occasional storms. In summer, the main challenges are traffic around the car parks and drivers stopping on the road for photos, which is dangerous and not allowed. Read the basics in our guide to <a href="/blog/getting-around-iceland">getting around Iceland</a> before you go.</p>
<h2>How much does a Golden Circle tour cost compared with driving?</h2>
<p>A classic coach tour costs from about ISK 12,000 per person, while that operator estimates a small rental car for the day at about ISK 15,000–25,000 including fuel. That makes tours cheaper for one person, roughly equal for two, and driving cheaper for three or more. These are 2026 prices from one large Reykjavík operator; other operators are in the same range.</p>
<div class="table-wrap"><table>
<thead><tr><th>Tour type</th><th>Length</th><th>Price per person</th></tr></thead>
<tbody>
<tr><td>Classic Golden Circle (coach or minibus)</td><td>7–8 h</td><td>About ISK 11,990</td></tr>
<tr><td>Golden Circle and Friðheimar greenhouse</td><td>8 h</td><td>About ISK 13,000</td></tr>
<tr><td>Golden Circle and Secret Lagoon</td><td>9 h</td><td>About ISK 16,000</td></tr>
<tr><td>Small group with Kerið and Friðheimar</td><td>8.5 h</td><td>About ISK 19,500</td></tr>
<tr><td>Golden Circle and northern lights (winter)</td><td>14–16 h</td><td>About ISK 20,300</td></tr>
<tr><td>Golden Circle and Silfra snorkelling</td><td>9–10 h</td><td>About ISK 49,000</td></tr>
</tbody></table></div>
<p>When you drive, add the parking fees: ISK 1,000 at Þingvellir for a car with up to five seats and about ISK 1,000 at Geysir. Gullfoss had no parking fee in the sources we checked. Tour prices include parking and hotel pickup but usually not lunch or entry to pools.</p>
""" + MAP_GC.format(
            alt="Map of the Golden Circle route from Reykjavík with Þingvellir, Geysir, Gullfoss and nearby stops",
            cap="The Golden Circle loop. Tours stick to the main three stops; a car lets you reach the smaller ones around Flúðir, Laugarvatn and Selfoss.",
        ) + """
<h2>What are the advantages of self-driving the Golden Circle?</h2>
<p>The biggest advantage is control over time. You can be at Þingvellir at 8 am, before the coaches, and stay at Gullfoss for the late light. Tours give you a fixed slot at each stop, often 30 to 60 minutes.</p>
<ul>
<li><strong>Beat the crowds.</strong> The tour coaches reach the big sights mid-morning. Arrive early or late and you see a quieter Almannagjá and fewer people around Strokkur.</li>
<li><strong>Add extra stops.</strong> Faxi waterfall, Brúarfoss, Kerið and the small geothermal pools are easy detours by car and hard to reach without one. See our list of <a href="/blog/golden-circle-extra-stops">extra Golden Circle stops</a>.</li>
<li><strong>Stay overnight.</strong> A car lets you sleep in the countryside and carry on to the south coast the next day.</li>
<li><strong>Chase the weather.</strong> If it rains in the morning, you can swap the order or wait it out in a pool.</li>
</ul>
<h2>What are the advantages of a Golden Circle tour?</h2>
<p>A tour removes the driving, the navigation and the parking, and adds a guide who explains what you are looking at. The history at Þingvellir and the geology of the rift make more sense with someone to tell the story.</p>
<ul>
<li><strong>No winter driving.</strong> Professional drivers know the roads in snow and ice, and operators cancel or reroute when storms hit.</li>
<li><strong>Cheaper for solo travellers.</strong> One tour ticket costs less than a day's car hire plus fuel.</li>
<li><strong>Easy combos.</strong> Tours bundle in things that are hard to arrange alone, such as Silfra snorkelling, a super jeep trip to the glaciers or a northern lights hunt in the evening.</li>
<li><strong>No tiredness.</strong> If you have just landed after an overnight flight, someone else at the wheel is safer.</li>
</ul>
<h2>Which is better in winter: tour or self-drive?</h2>
<p>In midwinter a tour is the safer choice for most first-time visitors, unless you are used to driving on snow and ice. The roads are cleared, but from November to February you get only four to six hours of daylight, black ice in the mornings and strong gusts on the open moors.</p>
<p>If you do drive in winter, make sure the car has winter tyres, check road conditions on umferdin.is every morning and keep a flexible day. Storms close Route 35 and other roads a few days each winter. In March and October, with longer days, self-driving is usually comfortable. Our <a href="/blog/golden-circle-in-winter">Golden Circle in winter</a> guide has the details.</p>
<h2>Who should choose which option?</h2>
<div class="table-wrap"><table>
<thead><tr><th>You are…</th><th>Best choice</th><th>Why</th></tr></thead>
<tbody>
<tr><td>A solo traveller</td><td>Tour</td><td>Cheaper than a car for one person</td></tr>
<tr><td>A couple with a rental car already</td><td>Self-drive</td><td>No extra cost, and far more freedom</td></tr>
<tr><td>A family or group of 3+</td><td>Self-drive</td><td>Much cheaper per person</td></tr>
<tr><td>A nervous or tired driver</td><td>Tour</td><td>No stress on unfamiliar roads</td></tr>
<tr><td>Visiting in December or January</td><td>Tour, or self-drive with experience</td><td>Short days, ice and storms</td></tr>
<tr><td>A keen photographer</td><td>Self-drive</td><td>You can wait for the light</td></tr>
<tr><td>Wanting Silfra or a glacier activity</td><td>Combo tour</td><td>Transport, gear and guides in one booking</td></tr>
</tbody></table></div>
<h2>Is there a middle option?</h2>
<p>Yes. Small-group minibus tours carry fewer people than a coach, often up to about 19, and usually add a stop such as Kerið or Friðheimar. Private tours with a driver-guide let you choose the order and the timing, but they are priced per vehicle and cost far more.</p>
<p>Another option is to self-drive and book one guided activity on the way, such as Silfra snorkelling at Þingvellir, which costs from about ISK 20,000 on its own. You drive yourself to the meeting point and the operator provides the drysuit and guide. Find out more in our <a href="/blog/thingvellir-national-park">Þingvellir National Park guide</a>.</p>
<h2>How do you plan a self-drive day?</h2>
<p>Start in Reykjavík around 8 am and drive Route 36 to <a href="/places/thingvellir">Þingvellir</a>. Continue via Laugarvatn to <a href="/places/geysir">Geysir</a> for lunch, then on to <a href="/places/gullfoss">Gullfoss</a>, and come back along Route 35 through Selfoss. Pick one or two extras on the way home. Our main <a href="/blog/golden-circle-iceland">Golden Circle self-drive guide</a> has the full timed route, every parking fee and what to see at each stop.</p>
<p class="callout">Whichever you choose, check the forecast on vedur.is the night before. In Iceland, the weather decides the day more than the plan does.</p>
""",
        "checked_note": "Facts checked October 2026. Tour prices are 2026 list prices from one operator and vary by season and company; car hire costs depend on the car, season and insurance. Check road conditions on umferdin.is before driving.",
        "sources": [
            ("Golden Circle tour prices (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/guides/golden-circle-tour-prices"),
            ("What is the Golden Circle? (Visit Iceland)", "https://visiticeland.com/article/the-golden-circle"),
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("Parking in Iceland (Iceland Tours)", "https://www.icelandtours.is/travel-guide/parking-in-iceland/"),
            ("Snorkeling and diving in Silfra (Dive.is)", "https://www.dive.is/silfra"),
            ("Gullfoss in winter (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/blog/gullfoss-in-winter"),
        ],
    },
    # ------------------------------------------------------------------ 3. THINGVELLIR
    {
        "slug": "thingvellir-national-park",
        "cluster": "golden-circle",
        "pillar": False,
        "short": "Þingvellir National Park: Between Two Continents",
        "title": "Thingvellir National Park: Almannagjá, Silfra, Parking and Walks (2027)",
        "description": "Thingvellir National Park guide: walk the Almannagjá rift between two continents, snorkel Silfra, see the old Alþingi site, and what parking costs in 2026.",
        "category": "Places · Golden Circle",
        "teaser": "Walk the rift between two plates, on the site of Iceland's first parliament.",
        "image": "hx-thingvellir",
        "image_alt": "The Icelandic flag flying above dark rocks under a wide blue sky",
        "stats": [
            ("930", "Year the Alþingi first met at Þingvellir"),
            ("2004", "Year Þingvellir became a UNESCO World Heritage Site"),
            ("2–4°C", "Water temperature in Silfra all year"),
            ("ISK 1,000", "Day parking for a car with up to 5 seats"),
        ],
        "body": """
<p>Þingvellir National Park, often written Thingvellir, is where you can walk through a rift valley between two tectonic plates, about 40 km northeast of Reykjavík. It is also where Iceland's parliament, the Alþingi, met from 930 for more than 800 years. Plan one to two hours for the main walk through the Almannagjá gorge, longer if you snorkel in Silfra. Parking costs ISK 1,000 for a normal car.</p>
<!--TOC-->
<h2>Can you really walk between two continents at Þingvellir?</h2>
<p>Yes, in a sense. Þingvellir lies in a rift valley about seven kilometres wide where the North American and Eurasian plates are moving apart. The western edge is the Almannagjá fault, the largest in the park, and you walk along the foot of the North American side when you follow the main path.</p>
<p>The valley is not a neat line between continents. It is a zone of cracks, fissures and sunken land. According to the national park, the plates move apart at about 2 cm a year. Since the lava here flowed around 10,000 years ago, the valley floor has sunk about 40 metres and spread by about 70 metres. Even since 930, it has dropped almost four metres.</p>
<h2>What is the Almannagjá walk like?</h2>
<p>The Almannagjá walk is an easy, mostly level path between high rock walls. It starts at the visitor centre at Hakið, where a viewing platform looks out over the valley and the lake. From there a wide path runs down into the gorge.</p>
<ol>
<li><strong>Hakið viewpoint:</strong> the best view of the rift, Þingvallavatn lake and the old assembly site.</li>
<li><strong>Almannagjá:</strong> walk down between the fault walls, with the cliff of the North American plate on your left.</li>
<li><strong>Lögberg (Law Rock):</strong> marked by a flagpole, this is where the Lawspeaker recited the law to the assembly.</li>
<li><strong>Öxarárfoss:</strong> a short walk further north, the Öxará river drops over the Almannagjá cliff.</li>
<li><strong>Þingvallakirkja:</strong> cross the river to the small church and the old farm buildings by the lake.</li>
</ol>
<p>Allow one to two hours for the walk and the viewpoints. In winter the path can be icy, so wear boots with grip or ice cleats. Stay on the marked paths: the moss is fragile and some fissures are deep and hidden.</p>
""" + MAP_GC.format(
            alt="Map of the Golden Circle showing Þingvellir National Park northeast of Reykjavík",
            cap="Þingvellir is the first stop on the Golden Circle, about 45 minutes from Reykjavík by Route 36.",
        ) + """
<h2>Why is Þingvellir important in Iceland's history?</h2>
<p>Þingvellir is where Iceland's national assembly, the Alþingi, was founded in 930. Chieftains and farmers gathered here every summer to pass laws and settle disputes, and the Lawspeaker recited the law from the Law Rock. The assembly met at Þingvellir until the end of the 18th century.</p>
<p>The site stayed a national symbol. Legislation protected it in 1928, and the national park was founded in 1930, the thousandth anniversary of the Alþingi. On 17 June 1944 Iceland declared its independence from Denmark here. UNESCO listed Þingvellir as a World Heritage Site in 2004 for its cultural value.</p>
<h2>What is Silfra, and can you snorkel there?</h2>
<p>Silfra is a water-filled fissure at the edge of Þingvallavatn, and yes, you can snorkel or dive in it with a licensed operator. The water comes from the Langjökull glacier about 50 km north and filters through porous lava for 30 to 100 years. The result is some of the clearest water anywhere, with visibility often quoted at more than 100 metres.</p>
<p>The catch is the cold. Silfra stays at 2–4°C all year, so snorkellers wear thick wetsuits or drysuits with hood, gloves and boots. The park's rules include:</p>
<ul>
<li>Always go with a buddy; entering alone is not allowed.</li>
<li>Divers need a drysuit certification and a recognised diving licence, and the maximum depth is 18 metres.</li>
<li>Caves and overhead areas are off-limits.</li>
<li>Everyone needs a permit and a health declaration; operators include this when you book.</li>
</ul>
<p>Guided snorkelling tours start from about ISK 20,000 with one operator, gear included. Book ahead in summer. Operators screen every participant for health and swimming ability.</p>
<h2>How much is parking at Þingvellir?</h2>
<p>Parking at Þingvellir costs ISK 1,000 a day for a car with up to five seats. One payment covers the three main car parks for the whole day of payment, so you can move between them.</p>
<div class="table-wrap"><table>
<thead><tr><th>Vehicle</th><th>Fee</th></tr></thead>
<tbody>
<tr><td>Motorcycle</td><td>ISK 400</td></tr>
<tr><td>Car, 5 seats or fewer</td><td>ISK 1,000</td></tr>
<tr><td>Car or van, 6–9 seats</td><td>ISK 1,200</td></tr>
<tr><td>Minibus, 10–19 seats</td><td>ISK 2,200</td></tr>
</tbody></table></div>
<p>Pay at the machines at the visitor centre, the toilet building next to it, P2 and P5, or online at checkit.is. Cameras at Hakið read number plates, so do not skip it. Visitors with a disabled parking permit park free but must register their plate at the visitor centre or by email.</p>
<h2>Which car park should you use?</h2>
<ul>
<li><strong>P1 Hakið:</strong> at the top of Almannagjá by the visitor centre. Best for the viewpoint and the walk down the gorge.</li>
<li><strong>P2 Efri-Vellir:</strong> east of and below Öxarárfoss. Good for a short walk to the waterfall.</li>
<li><strong>P5 Valhöll:</strong> nearest to the church and to Silfra. Use this one for snorkelling and diving.</li>
</ul>
<p>A good plan is to park at P1, walk down through the gorge to Öxarárfoss and back, then drive to P5 if you are snorkelling or want the lakeshore.</p>
<h2>When is the best time to visit Þingvellir?</h2>
<p>Go early in the morning or late in the afternoon. The tour coaches arrive from mid-morning, and the path through Almannagjá gets busy around midday in summer. The light is also better low in the sky, when the fault walls throw long shadows.</p>
<p>Þingvellir is open all year. In winter it is quieter and often snowy, and its dark skies, away from the city lights, make it a good place to look for the northern lights. See our <a href="/blog/golden-circle-in-winter">Golden Circle in winter</a> guide.</p>
<h2>Can you camp or swim anywhere else at Þingvellir?</h2>
<p>Yes. The park has two campsites, Leirar and Vatnskot, open mainly in summer with basic facilities. Use them rather than pitching a tent or parking a campervan anywhere else.</p>
<p>Experienced divers can also visit Davíðsgjá, a second rift in the north-eastern part of Þingvallavatn. It lies inside the lake, so you swim some distance from the bank before it deepens and widens. The same permit and safety rules apply as at Silfra.</p>
<h2>How do you get to Þingvellir and where do you go next?</h2>
<p>From Reykjavík, take Route 1 north and turn onto Route 36. The drive is about 45 minutes. Þingvellir is the first stop on the classic loop; from here Route 365 leads over the heath to Laugarvatn, and on to <a href="/places/geysir">Geysir</a> and <a href="/places/gullfoss">Gullfoss</a>. Our <a href="/blog/golden-circle-iceland">Golden Circle self-drive guide</a> has the full route, and the <a href="/places/thingvellir">Þingvellir place page</a> has photos and the map.</p>
<p class="callout">Bring cash or a card for the parking machine, and leave a couple of hours. Þingvellir rewards slow walking more than a quick photo stop.</p>
""",
        "checked_note": "Facts checked October 2026. Parking fees are from the national park's own page; Silfra tour prices and rules change, so check with your operator and the park before booking.",
        "sources": [
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("Diving and snorkelling (Þingvellir National Park)", "https://www.thingvellir.is/en/things-to-do/diving/"),
            ("Tectonic movements (Þingvellir National Park)", "https://thingvellir.is/en/education/nature/tectonic-movements"),
            ("Þingvellir (Wikipedia)", "https://en.wikipedia.org/wiki/%C3%9Eingvellir"),
            ("Silfra (Wikipedia)", "https://en.wikipedia.org/wiki/Silfra"),
            ("Snorkeling and diving in Silfra (Dive.is)", "https://www.dive.is/silfra"),
            ("What is the Golden Circle? (Visit Iceland)", "https://visiticeland.com/article/the-golden-circle"),
        ],
    },
    # ------------------------------------------------------------------ 4. GEYSIR
    {
        "slug": "geysir-strokkur",
        "cluster": "golden-circle",
        "pillar": False,
        "short": "Geysir and Strokkur: What to Expect",
        "title": "Geysir Iceland: What to Expect at Geysir and Strokkur (2027)",
        "description": "Geysir Iceland guide: how often Strokkur erupts, why the Great Geysir is quiet, parking, safety near the hot springs, photo tips and where to eat nearby.",
        "category": "Places · Golden Circle",
        "teaser": "Strokkur erupts every few minutes; here is how to see it well.",
        "image": "hx-geysir",
        "image_alt": "Steam rising from hot springs in the Geysir field on a sunny winter day",
        "stats": [
            ("5–10 min", "Typical gap between Strokkur eruptions"),
            ("15–20 m", "Usual height of a Strokkur eruption"),
            ("1294", "Oldest written account of the Haukadalur hot springs"),
            ("Free", "Entry to the Geysir area, open all year"),
        ],
        "body": """
<p>At Geysir, in the Haukadalur valley on the Golden Circle, you can watch the Strokkur geyser shoot boiling water 15 to 20 metres into the air every few minutes. The famous Great Geysir beside it, which gave its name to geysers everywhere, rarely erupts today. Entry is free and the area is open all the time. Plan 30 to 60 minutes, and stand upwind.</p>
<!--TOC-->
<h2>How often does Strokkur erupt?</h2>
<p>Strokkur usually erupts every five to ten minutes, and sometimes you wait up to 15. Most eruptions reach 15 to 20 metres. Now and then it fires a double or triple burst, and the biggest eruptions have been reported at well over 30 metres.</p>
<p>Watch the pool before it goes. The water sinks and swells, then a turquoise dome of water bulges up from the vent a split second before the blast. That bubble is the moment photographers wait for. Strokkur was first described in 1789, stopped erupting in the early 1900s, and was revived in the 1960s when its vent was cleared.</p>
<h2>Does the Great Geysir still erupt?</h2>
<p>Only rarely. The Great Geysir is the original geyser, and the word comes from its Icelandic name. In its active periods it threw water up to about 60 metres, but its activity has always come and gone, often revived by earthquakes and then fading again.</p>
<p>After earthquakes in 2000 it erupted to a reported 122 metres for two days. Its activity faded again in the following years, and an eruption in 2016 made the news because it was so unusual. Today you see a wide, steaming, blue pool about 50 metres north of Strokkur. Do not expect an eruption, but it is worth seeing.</p>
<h2>What else is there to see at Geysir?</h2>
<p>The Haukadalur geothermal area has about thirty smaller hot springs and pools around the two main geysers. A loop of paths leads past steaming vents, blue pools, bubbling mud and ground stained red and yellow by minerals.</p>
<ul>
<li><strong>Litli Geysir:</strong> "Little Geysir", a small spring that bubbles and splashes constantly.</li>
<li><strong>Blue pools:</strong> clear, steaming pools with vivid blue water, best seen on a sunny day.</li>
<li><strong>The hillside path:</strong> a short climb up the slope of Laugarfjall gives a view down over the field and the valley.</li>
</ul>
<p>The area has been officially protected since 17 June 2020. The land has a long history of private ownership: in 1894 it was sold to a private buyer who charged visitors entry, and in 1935 it was bought and given to the Icelandic people.</p>
""" + MAP_GC.format(
            alt="Map of the Golden Circle with Geysir between Þingvellir and Gullfoss",
            cap="Geysir sits on Route 35, about 10 km from Gullfoss and about 50 minutes' drive from Þingvellir.",
        ) + """
<h2>Is Geysir dangerous?</h2>
<p>It can be if you ignore the ropes. The water at the surface of the vents is around 90–95°C, and much hotter deeper down. The thin crust of ground near the pools can break. Visitors have been burned after stepping off the path or putting a hand in the water.</p>
<ul>
<li>Stay behind the ropes and on the marked paths at all times.</li>
<li>Never touch the water or throw anything into the vents.</li>
<li>Stand on the upwind side of Strokkur. The spray is hot when it leaves the vent and falls as a warm, mineral-heavy shower.</li>
<li>Keep children close, and hold their hands near the rope line.</li>
<li>In winter the paths can be very icy around the vents. Wear ice cleats.</li>
</ul>
<h2>How much does it cost to visit Geysir?</h2>
<p>Entry to the Geysir area is free. You pay for parking, about ISK 1,000 for a normal car, through the Parka app or the signs on site. The area is open day and night, all year.</p>
<p>Across Route 35 is a large visitor complex with a hotel, cafés, a restaurant, a souvenir shop and toilets.</p>
<h2>When is the best time to visit Geysir?</h2>
<p>Early morning or late afternoon is best, when the tour coaches have gone. Geysir is busiest from late morning to mid-afternoon, and a crowd can form a deep ring around Strokkur.</p>
<p>A sunny, cold day is ideal: the steam stands out against a blue sky and the pools look their bluest. In winter, low sun lights the steam from behind, and the field is often white with frost. On calm winter nights, the steam and the dark sky make a strange setting for the northern lights.</p>
<h2>How long should you spend at Geysir?</h2>
<p>Plan 30 to 60 minutes for the hot spring area itself. That is enough to see Strokkur erupt several times, walk the loop past the Great Geysir and the smaller pools, and climb a little way up the hillside for the view. Add 45 minutes to an hour if you are having lunch across the road. If the car park is full and the crowd around Strokkur is deep, walk the outer paths first and come back to the main viewing ring after the next coach leaves.</p>
<p>Geysir is the natural middle of a Golden Circle day. Most people arrive from Þingvellir in the late morning, eat here, and drive the ten minutes to Gullfoss in the early afternoon.</p>
<h2>Can you stay overnight near Geysir?</h2>
<p>Yes. There is a hotel by the geothermal area and a seasonal campsite with electric hook-ups, toilets and showers. Staying close means you can walk over to Strokkur in the early morning or late evening, when the field is almost empty and the light is low. Remember that campervans and tents must use an organised campsite; overnight stays in car parks are not allowed.</p>
<h2>How do you photograph Strokkur?</h2>
<ul>
<li><strong>Use burst mode.</strong> Eruptions last only a couple of seconds. Hold the shutter as the dome rises.</li>
<li><strong>Find the light.</strong> With the sun behind the eruption, the water and steam glow.</li>
<li><strong>Frame wide.</strong> The steam cloud is often bigger than the water column, so leave room above.</li>
<li><strong>Try video.</strong> A short clip often captures the bubble better than a single still.</li>
<li><strong>Protect your lens.</strong> Mineral-rich spray dries into spots. Wipe it off quickly.</li>
</ul>
<h2>How do you get to Geysir, and what is nearby?</h2>
<p>Geysir is about 100 km from Reykjavík, roughly 1 hour 30 minutes by the shortest route. On the Golden Circle loop you usually come from <a href="/places/thingvellir">Þingvellir</a> via Laugarvatn, about 60 km and 50 minutes away. <a href="/places/gullfoss">Gullfoss</a> is only about 10 km further on Route 35.</p>
<p>Nearby extras include Faxi waterfall, about 11 km south, the Friðheimar tomato greenhouse at Reykholt, and the Secret Lagoon at Flúðir, which is fed by its own small geyser. See our guide to <a href="/blog/golden-circle-extra-stops">extra Golden Circle stops</a>, the full <a href="/blog/golden-circle-iceland">Golden Circle self-drive guide</a>, and the <a href="/places/geysir">Geysir place page</a> for photos.</p>
<p class="callout">Give Strokkur three or four eruptions. The first one surprises you; by the fourth you know when to press the shutter.</p>
""",
        "checked_note": "Facts checked October 2026. Strokkur's activity varies over time, and parking charges and payment apps change; check the signs on site.",
        "sources": [
            ("Geysir (Wikipedia)", "https://en.wikipedia.org/wiki/Geysir"),
            ("Strokkur (Arctic Adventures)", "https://adventures.is/iceland/attractions/strokkur"),
            ("What is the Golden Circle? (Visit Iceland)", "https://visiticeland.com/article/the-golden-circle"),
            ("Parking in Iceland (Iceland Tours)", "https://www.icelandtours.is/travel-guide/parking-in-iceland/"),
            ("Parking fees in Iceland (Go Campers)", "https://www.gocampers.is/guides/money/parking-fees-iceland/"),
            ("Golden Circle map and driving times (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/golden-circle/map"),
        ],
    },
    # ------------------------------------------------------------------ 5. WINTER
    {
        "slug": "golden-circle-in-winter",
        "cluster": "golden-circle",
        "pillar": False,
        "short": "The Golden Circle in Winter",
        "title": "Golden Circle Winter Guide: Driving, Daylight and Northern Lights (2027)",
        "description": "Golden Circle winter guide: daylight hours, icy roads and path closures, a timed winter day, and the best dark stops for the northern lights on the way back.",
        "category": "Seasons · Golden Circle",
        "teaser": "Short days, frozen falls and dark skies for the aurora.",
        "image": "hx-aurora-countryside",
        "image_alt": "Bright green northern lights above a dark hillside with two small cabins",
        "stats": [
            ("~4 h", "Daylight in late December in southwest Iceland"),
            ("Nov–Mar", "Months when the lower Gullfoss path often closes"),
            ("All year", "The Golden Circle stays open, no 4x4 needed"),
            ("21:00", "Closing time at Laugarvatn Fontana in winter"),
        ],
        "body": """
<p>The Golden Circle is open all winter, and it is the easiest of Iceland's classic drives in the cold months. The roads are cleared and the sights are close together. The trade-offs are short days, icy paths and the odd storm. The reward is snowy rift walls at Þingvellir, a frozen Gullfoss, steam glowing in the low sun at Geysir and dark skies for the northern lights on the drive home.</p>
<!--TOC-->
<h2>Is it safe to drive the Golden Circle in winter?</h2>
<p>Yes, for a careful driver with the right car, on a day with a good forecast. The main roads on the loop are paved and maintained through the winter, and you do not need a 4x4. Rental companies normally fit winter tyres in the cold months.</p>
<p>The risks are black ice, drifting snow and strong gusts on the open moors, especially on Route 36 over Mosfellsheiði and Route 365 over Lyngdalsheiði. Storms close parts of the route a few days each winter. Check the road map on umferdin.is and the forecast on vedur.is every morning, and do not drive in orange or red weather warnings. If you are not used to snow, a <a href="/blog/golden-circle-self-drive-or-tour">guided tour may be the better choice</a>.</p>
<h2>How much daylight do you get on a winter Golden Circle?</h2>
<p>In late December the sun is up for only about four hours in southwest Iceland, from around 11 am to before 4 pm. Add twilight and you have about six usable hours. By late February and in October, days are much longer and the loop is far more relaxed.</p>
<p>Plan the day around the light. Drive to Þingvellir in the dark and arrive as it gets light, so you reach Gullfoss in the early afternoon. Save the driving home for after dark, when the roads are quieter and the sky may light up.</p>
<h2>What is a good winter Golden Circle itinerary?</h2>
<ol>
<li><strong>9.30 Leave Reykjavík</strong> in the dark, on Route 1 and Route 36.</li>
<li><strong>10.30 Þingvellir</strong> at first light. Walk down Almannagjá from the Hakið visitor centre. Allow an hour.</li>
<li><strong>12.15 Geysir.</strong> Watch Strokkur in the low sun, then have lunch across the road.</li>
<li><strong>13.45 Gullfoss</strong> in the best of the afternoon light. Allow about 45 minutes.</li>
<li><strong>15.00 A warm stop.</strong> Soak at the Secret Lagoon at Flúðir or Laugarvatn Fontana as the light fades.</li>
<li><strong>18.00 onwards: aurora watch.</strong> If the forecast is clear, stop at a dark car park on the way back. Otherwise head to Reykjavík or your countryside hotel.</li>
</ol>
""" + MAP_GC.format(
            alt="Map of the Golden Circle route from Reykjavík with Þingvellir, Geysir, Gullfoss, Laugarvatn and Flúðir",
            cap="The winter loop. Laugarvatn, Flúðir and Þingvellir are dark enough for aurora watching on clear nights.",
        ) + """
<h2>What is closed on the Golden Circle in winter?</h2>
<p>The main sights stay open all year, but some paths close when they ice over. At Gullfoss, the lower path that runs out beside the first tier often closes from November to March, and the closure is enforced. The upper viewpoint stays open in almost all conditions, and the visitor centre café stays open.</p>
<ul>
<li><strong>Gullfoss:</strong> the stairs down from the upper car park are where most falls happen. Use the handrails.</li>
<li><strong>Þingvellir:</strong> the Almannagjá path is open but can be glazed with ice. Some side paths may be closed.</li>
<li><strong>Geysir:</strong> paths stay open, but ice forms around the vents. Keep well behind the ropes.</li>
<li><strong>Kerið:</strong> the rim path and the steps to the lake can be slippery. Visit in daylight only.</li>
<li><strong>Seasonal cafés:</strong> some smaller cafés and restaurants, such as the one at Faxi, open only in summer.</li>
</ul>
<p class="callout">Pack ice cleats that slip over your boots. They cost little, weigh almost nothing and make every path on the loop safer from November to March.</p>
<h2>Where can you see the northern lights on the Golden Circle?</h2>
<p>The best aurora spots on the Golden Circle are anywhere dark, away from Reykjavík's lights, with a proper place to park. The season runs from roughly September to mid-April, and you need a clear sky. Check the aurora and cloud-cover forecast on vedur.is in the afternoon. Our <a href="/northern-lights">northern lights guide</a> explains how to read it.</p>
<ul>
<li><strong>Þingvellir:</strong> the valley is wide, open and dark, and Þingvallavatn gives reflections on calm nights. Use the official car parks, which are paid during the day.</li>
<li><strong>Laugarvatn:</strong> the lakeshore by the village faces south over the water, with little light around it.</li>
<li><strong>Laugarvatn Fontana:</strong> open until 21:00 in winter, so you can soak in the warm pools under a dark sky.</li>
<li><strong>Around Flúðir and Reykholt:</strong> the farmland is dark, but the greenhouses glow orange. Look for spots away from them.</li>
<li><strong>A countryside hotel:</strong> the easiest option of all. Stay the night and step outside whenever the sky clears.</li>
</ul>
<p>Never stop on the road or the hard shoulder to look at the sky. Pull into a proper car park or lay-by, turn off your headlights and give your eyes 15 minutes to adjust. Watch out for other drivers doing the same.</p>
<h2>Does Strokkur erupt in winter?</h2>
<p>Yes. Strokkur erupts all year, every few minutes, whatever the weather. In winter the eruptions often look bigger, because the cold air turns the spray into a tall column of steam. The low sun from the south lights it from behind for much of the short day. Read more in our guide to <a href="/blog/geysir-strokkur">Geysir and Strokkur</a>.</p>
<h2>Can you combine the Golden Circle with a northern lights tour?</h2>
<p>Yes. Several Reykjavík operators run winter combo tours that cover the Golden Circle by day and a northern lights hunt by night. One large operator lists a 14–16 hour combo at about ISK 20,300 per person in 2026. It makes a very long day, so book it early in your trip, when you are fresh, and keep a spare night in case of clouds. Many aurora tours offer a free retry if you see nothing.</p>
<h2>What should you pack for a winter Golden Circle?</h2>
<ul>
<li>A waterproof, windproof jacket and trousers. The spray at Gullfoss freezes on clothes.</li>
<li>Warm layers, a hat, waterproof gloves and a buff or scarf.</li>
<li>Waterproof boots with real soles, plus ice cleats.</li>
<li>A swimsuit and towel for the geothermal pools.</li>
<li>A head torch for dark car parks, and a power bank: phone batteries drain fast in the cold.</li>
<li>Snacks and water in the car, in case a road closes and you have to wait.</li>
</ul>
<h2>Is the Golden Circle worth it in winter?</h2>
<p>Yes. Fewer visitors, snow-covered landscapes and the chance of auroras make winter one of the most atmospheric times to see it. <a href="/places/gullfoss">Gullfoss</a> half-frozen and the steam at <a href="/places/geysir">Geysir</a> in the low sun are among the best winter sights in Iceland. Just keep the day short, flexible and led by the forecast.</p>
<p>For the summer version of the loop, timings and fees, see our main <a href="/blog/golden-circle-iceland">Golden Circle self-drive guide</a>. For more on the season, read <a href="/blog/best-time-to-visit-iceland">the best time to visit Iceland</a>, and if you want everything on paper, our Winter edition is among our <a href="/#guides">printed guidebooks</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Path closures at Gullfoss and other sites depend on ice and are decided on the day; check umferdin.is, vedur.is and safetravel.is before you drive, and confirm tour prices and pool hours when you book.",
        "sources": [
            ("Gullfoss in winter (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/blog/gullfoss-in-winter"),
            ("What is the Golden Circle? (Visit Iceland)", "https://visiticeland.com/article/the-golden-circle"),
            ("Contact and opening hours (Laugarvatn Fontana)", "https://www.fontana.is/en/about-fontana/contact-and-location"),
            ("Golden Circle tour prices (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/guides/golden-circle-tour-prices"),
            ("Parking service (Þingvellir National Park)", "https://www.thingvellir.is/en/service/parking-service/"),
            ("Faxi waterfall (Go Campers)", "https://www.gocampers.is/nature/waterfalls/faxi-waterfall/"),
        ],
    },
    # ------------------------------------------------------------------ 6. EXTRA STOPS
    {
        "slug": "golden-circle-extra-stops",
        "cluster": "golden-circle",
        "pillar": False,
        "short": "The Best Extra Stops on the Golden Circle",
        "title": "Golden Circle Stops: Kerið, Friðheimar, Secret Lagoon and More (2027)",
        "description": "The best extra Golden Circle stops beyond the big three: Kerið, Friðheimar, the Secret Lagoon, Laugarvatn Fontana, Faxi and Brúarfoss, with 2026 prices.",
        "category": "Itineraries · Golden Circle",
        "teaser": "Craters, greenhouses, hot pools and quiet waterfalls along the loop.",
        "image": "hx-reykjadalur",
        "image_alt": "Steam rising from a hot river valley at sunrise",
        "stats": [
            ("ISK 700", "Entry to Kerið crater per person"),
            ("1891", "Year the Secret Lagoon pool at Flúðir was built"),
            ("38–40°C", "Water temperature at the Secret Lagoon"),
            ("~7 m", "Height of the wide Faxi waterfall"),
        ],
        "body": """
<p>The best extra stops on the Golden Circle are Kerið crater, the Friðheimar tomato greenhouse, the Secret Lagoon at Flúðir, Laugarvatn Fontana, Faxi waterfall and Brúarfoss. All sit within a short detour of the classic loop of Þingvellir, Geysir and Gullfoss. Pick two or three, depending on whether you want to eat, soak or walk. Here is what each is like, what it costs and how long it takes, checked in October 2026.</p>
<!--TOC-->
<h2>Which extra Golden Circle stops are worth it?</h2>
<p>Kerið and Faxi are the quickest and cheapest extras. Friðheimar is the best lunch stop, and the Secret Lagoon or Fontana is the best way to end the day. This table sums them up:</p>
<div class="table-wrap"><table>
<thead><tr><th>Stop</th><th>What it is</th><th>Time</th><th>Cost (2026)</th></tr></thead>
<tbody>
<tr><td>Kerið</td><td>Volcanic crater with a lake</td><td>30–45 min</td><td>About ISK 700 per person</td></tr>
<tr><td>Friðheimar</td><td>Greenhouse restaurant</td><td>1–1.5 h</td><td>Price of lunch; book ahead</td></tr>
<tr><td>Secret Lagoon</td><td>Historic natural hot pool</td><td>1.5–2 h</td><td>About ISK 4,200 per adult (2025)</td></tr>
<tr><td>Laugarvatn Fontana</td><td>Lakeside baths and steam rooms</td><td>1.5–2 h</td><td>ISK 7,490 per adult</td></tr>
<tr><td>Faxi</td><td>Wide waterfall with salmon ladder</td><td>20–30 min</td><td>Parking about ISK 700–900</td></tr>
<tr><td>Brúarfoss</td><td>Bright blue waterfall</td><td>30 min to 2 h</td><td>ISK 750 parking at the near lot</td></tr>
<tr><td>Skálholt</td><td>Historic church and bishop's seat</td><td>30 min</td><td>Free to visit the church</td></tr>
</tbody></table></div>
<h2>What is Kerið crater like?</h2>
<p>Kerið is a volcanic crater about 55 metres deep and 170 metres wide, with steep red and black walls and a green-blue lake at the bottom. It sits on Route 35 in the Grímsnes area, north of Selfoss, and is one of the most photographed stops on the loop.</p>
<p>A path runs around the rim, and wooden stairs lead down to the water. The rim loop takes about 20 minutes and the whole visit 30 to 45 minutes. Entry costs about ISK 700 per person, paid at the kiosk, and parking is free. Kerið has been privately owned since 2023, when Arctic Adventures bought the site. The lake is usually 7 to 14 metres deep, depending on the groundwater. In winter the path can be icy, and the site is best visited in daylight.</p>
<h2>Is Friðheimar worth a stop?</h2>
<p>Yes, especially for lunch. Friðheimar is a family farm at Reykholt that grows tomatoes all year in geothermally heated greenhouses, and you eat among the plants. The signature meal is tomato soup with fresh bread, served help-yourself. There are also dishes like tomato ravioli and green tomato and apple pie.</p>
<p>The greenhouse restaurant serves from about 11.30 to 16.00 daily, and the small shop and bar open longer. Book a table online; it is small and tour groups take many of the midday slots, especially from June to August. The farm also breeds Icelandic horses and runs horse shows on a schedule, sold separately. Friðheimar is on Route 35, about 20 minutes from Geysir.</p>
""" + MAP_GC.format(
            alt="Map of the Golden Circle with Kerið, Flúðir, Laugarvatn, Reykholt and other extra stops",
            cap="Most extras sit on Route 35 between Gullfoss and Selfoss, or near Laugarvatn between Þingvellir and Geysir.",
        ) + """
<h2>What is the Secret Lagoon?</h2>
<p>The Secret Lagoon, or Gamla laugin ("the old pool"), is a natural hot pool at the edge of Flúðir, built in 1891. Locals call it Iceland's oldest swimming pool, and it hosted the country's first swimming lessons from 1909 to 1947. It was restored and reopened in 2014.</p>
<p>The water stays at 38–40°C, fed by hot springs around the pool, including a small geyser, Litli Geysir, which bubbles up every few minutes. It is simpler and much cheaper than the big lagoons near Reykjavík. The latest price we could confirm was about ISK 4,200 for adults (2025), with children 14 and under paying a token fee. It is open from 10.00 to 20.00 in summer and 10.00 to 19.00 from October to May. It is about 25 km south of Geysir.</p>
<h2>What is Laugarvatn Fontana?</h2>
<p>Laugarvatn Fontana is a modern spa on the shore of Laugarvatn lake, with warm pools, natural steam rooms built over hot springs, and the lake itself for a cold dip. In the steam rooms, the temperature usually ranges from 40°C to 50°C. It is on the way between Þingvellir and Geysir.</p>
<p>Adult entry costs ISK 7,490 on Fontana's price list, with lower prices for seniors and ages 6–15, and free entry for under-6s. The baths are open daily from 10.00 to 21.00 in summer and 11.00 to 21.00 from October to May. The geothermal bakery tour shows rye bread being dug out of the hot ground, and costs ISK 3,350 for adults. Tours run at set times and often sell out, so book first and plan the baths around it.</p>
<h2>Where are Faxi and Brúarfoss?</h2>
<p><strong>Faxi</strong> (Faxafoss) is a low, wide waterfall on the Tungufljót river, about 11 km south of Geysir and signposted off Route 35. It is only about 7 metres high but around 80 metres across, with a salmon ladder on one side. It is rarely crowded. Parking costs about ISK 700–900, and a seasonal restaurant, Við Faxa, overlooks the falls.</p>
<p><strong>Brúarfoss</strong> is a small waterfall famous for its bright blue water, between Laugarvatn and Geysir. A car park opened in 2023 lets you reach it in about five minutes on foot, for ISK 750, via a rough access road. The alternative is a 3.5 km trail each way from a free lay-by on Route 37, which takes about an hour each way.</p>
<h2>Which stops are on the way back to Reykjavík?</h2>
<p>On the southern half of the loop you pass Skálholt, Kerið, Selfoss and Hveragerði, so these fit naturally at the end of the day.</p>
<ul>
<li><strong>Skálholt:</strong> a historic bishop's seat with a cathedral, open daily from 9.00 to 18.00, with archaeological finds in the cellar.</li>
<li><strong>Selfoss:</strong> the largest town in South Iceland, with supermarkets, fuel and places to eat.</li>
<li><strong>Hveragerði and Reykjadalur:</strong> a greenhouse town about 45 km from Reykjavík on Route 1, and the start of the hike to <a href="/places/reykjadalur">Reykjadalur</a>, a warm river you can bathe in. Read our <a href="/blog/reykjadalur-hot-river">Reykjadalur hot river guide</a>.</li>
</ul>
<h2>How should you fit the extra stops into one day?</h2>
<p>Choose by your priorities. For a classic sightseeing day, add Faxi and Kerið, which take under an hour together. For food, add Friðheimar between Geysir and Gullfoss. For a relaxed end, finish at the Secret Lagoon or Fontana. Trying to add more than three extras to a single day usually means rushing <a href="/places/thingvellir">Þingvellir</a> and <a href="/places/gullfoss">Gullfoss</a>.</p>
<p>A good two-day plan: day one covers Þingvellir, Fontana and a night at Laugarvatn; day two covers Geysir, Gullfoss, Faxi, Friðheimar and Kerið. See our <a href="/blog/golden-circle-iceland">Golden Circle self-drive guide</a> for the main route and timings, and our <a href="/blog/hot-springs-iceland">guide to Iceland's hot springs</a> for more places to swim.</p>
<p class="callout">Book Friðheimar, the Fontana bread tour and any pool in advance in summer. They are small, and the tour groups book early.</p>
""",
        "checked_note": "Facts checked October 2026. Prices and opening hours for Kerið, Friðheimar, the Secret Lagoon, Laugarvatn Fontana and the parking at Faxi and Brúarfoss change often; the Secret Lagoon price is the latest published figure we found (2025). Check each operator's own website before you go.",
        "sources": [
            ("Hours and prices (Laugarvatn Fontana)", "https://fontana.is/hours-and-prices"),
            ("Kerið entrance fee and hours (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/blog/kerid-crater-entrance-fee-hours"),
            ("Kerið (Wikipedia)", "https://en.wikipedia.org/wiki/Keri%C3%B0"),
            ("Friðheimar tomato farm (Golden Circle Day Tours)", "https://www.goldencircledaytours.is/blog/golden-circle-fridheimar-tomato-farm"),
            ("Secret Lagoon (Go Campers)", "https://www.gocampers.is/nature/hot-springs/secret-lagoon/"),
            ("Faxi waterfall (Go Campers)", "https://www.gocampers.is/nature/waterfalls/faxi-waterfall/"),
            ("How to visit Brúarfoss (Earth Trekkers)", "https://www.earthtrekkers.com/how-to-visit-bruarfoss-waterfall"),
            ("Plan your visit to Skálholt (Skálholt)", "https://www.skalholt.is/en/post/plan-your-visit-to-sk%C3%A1lholt"),
        ],
    },
]
