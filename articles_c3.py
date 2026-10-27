"""Glaciers cluster: journal articles. Same format as articles_content.py.
Each body uses <h2> question headings; <!--TOC--> marks where the table of
contents and fact tiles go."""

MAP_GLACIERS = '<figure class="a-figure a-map"><a href="/assets/img/map-glaciers-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-glaciers-1800.jpg" srcset="/assets/img/map-glaciers-800.jpg 800w, /assets/img/map-glaciers-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{caption} Tap to open full size.</figcaption></figure>'


def _map(alt, caption):
    return MAP_GLACIERS.format(alt=alt, caption=caption)


ARTICLES = [
    # ------------------------------------------------------------------
    # 1. PILLAR
    # ------------------------------------------------------------------
    {
        "slug": "glaciers-in-iceland",
        "cluster": "glaciers",
        "pillar": True,
        "short": "Iceland's Glaciers: Where to See, Walk and Explore",
        "title": "Glaciers in Iceland: Where to See, Walk and Explore Them (2027)",
        "description": "Glaciers in Iceland: where to see them from the Ring Road, guided glacier hikes, ice caves, glacier lagoons, the best season, safety and a south coast plan.",
        "category": "Nature · Glaciers",
        "teaser": "Viewpoints, lagoons, guided hikes and ice caves, and how to plan them.",
        "image": "hx-crevasses",
        "image_alt": "Deep blue crevasses running down a glacier, seen from above in mist",
        "stats": [
            ("~10%", "Share of Iceland covered by glaciers in 2019"),
            ("7,720 km²", "Area of Vatnajökull, Iceland's largest ice cap (2019)"),
            ("2,110 m", "Hvannadalshnúkur, Iceland's highest peak, on Öræfajökull"),
            ("284 m", "Maximum depth of Jökulsárlón glacier lagoon"),
        ],
        "body": """
<p>Glaciers in Iceland cover about a tenth of the country, and the easiest place to see them is the south coast. Between Sólheimajökull and Höfn, tongues of ice from the Mýrdalsjökull and Vatnajökull ice caps reach down almost to the Ring Road. You can see them for free from viewpoints and lagoon shores. To walk on the ice or go into an ice cave you need a certified guide. This guide covers where the glaciers are, what you can do on them, when to go and how to stay safe.</p>
<!--TOC-->
<h2>How much of Iceland is covered by glaciers?</h2>
<p>About 10% of Iceland was under glacier ice in 2019, roughly 10,400 km². In 2008 the figure was about 11%. There are more than 400 glaciers, but most are small, and a handful of large ice caps hold nearly all the ice.</p>
<p>Vatnajökull is by far the biggest. It covers about 7,720 km², about three-quarters of all the glacier area in Iceland. These are the largest glaciers by area, from the 2019 figures.</p>
<div class="table-wrap"><table>
<thead><tr><th>Glacier</th><th>Area (2019)</th><th>Where</th><th>How most visitors see it</th></tr></thead>
<tbody>
<tr><td>Vatnajökull</td><td>7,720 km²</td><td>Southeast</td><td>Skaftafell, Jökulsárlón, Fjallsárlón, ice caves</td></tr>
<tr><td>Langjökull</td><td>836 km²</td><td>West highlands</td><td>Ice tunnel and snowmobile tours</td></tr>
<tr><td>Hofsjökull</td><td>810 km²</td><td>Central highlands</td><td>From highland roads in summer</td></tr>
<tr><td>Mýrdalsjökull</td><td>520 km²</td><td>South coast</td><td>Sólheimajökull, Katla ice cave</td></tr>
<tr><td>Drangajökull</td><td>137 km²</td><td>Westfjords</td><td>Remote; seen on long hikes</td></tr>
<tr><td>Eyjafjallajökull</td><td>66 km²</td><td>South coast</td><td>From Route 1 near Seljalandsfoss</td></tr>
<tr><td>Snæfellsjökull</td><td>8.8 km²</td><td>Snæfellsnes</td><td>From the peninsula roads</td></tr>
</tbody></table></div>
<p>Several of Iceland's ice caps sit on active volcanoes. Katla lies under Mýrdalsjökull, and Öræfajökull, the volcano under the southern edge of Vatnajökull, carries Hvannadalshnúkur, the country's highest peak at about 2,110 m.</p>
<h2>Where are the best places to see glaciers in Iceland?</h2>
<p>The best places are on the south coast, along Route 1 from Sólheimajökull to Höfn. Here you can park, walk for 15 to 45 minutes and stand in front of a glacier tongue or a lagoon full of icebergs. These are the main stops from west to east.</p>
<ul>
<li><strong><a href="/places/solheimajokull">Sólheimajökull</a>:</strong> an outlet of Mýrdalsjökull, about 2.5 hours from Reykjavík. A short trail leads from the car park towards the ash-streaked ice. It is the most popular place for guided glacier hikes near the capital.</li>
<li><strong><a href="/places/skaftafell">Skaftafell</a>:</strong> the hiking hub of Vatnajökull National Park, 325 km from Reykjavík. A flat trail of about 1.8 km leads to a viewpoint at Skaftafellsjökull, and guided hikes start at the visitor centre.</li>
<li><strong><a href="/places/fjallsarlon">Fjallsárlón</a>:</strong> a smaller, quieter lagoon about 10 km west of Jökulsárlón, where the glacier wall is close to the shore.</li>
<li><strong><a href="/places/jokulsarlon">Jökulsárlón</a> and Diamond Beach:</strong> Iceland's best-known glacier lagoon, with icebergs that drift under the bridge and wash up on the black sand across the road.</li>
<li><strong>Heinabergslón:</strong> a lagoon at the end of a gravel road about 30 minutes from Höfn, used for summer kayak trips.</li>
</ul>
<p>Away from the south coast, you can see Snæfellsjökull from most of the Snæfellsnes peninsula, and Langjökull from the highland edge beyond Gullfoss. Neither is as easy to get close to without a tour.</p>
""" + _map(
            "Map of Iceland's glaciers, glacier lagoons, ice-cave and glacier-hike areas",
            "Iceland's glaciers and glacier lagoons, with the main ice-cave and glacier-hike areas.",
        ) + """
<h2>Can you walk on a glacier in Iceland?</h2>
<p>Yes, but only on a guided tour. Glacier ice has crevasses hidden under thin snow, deep meltwater channels and edges that collapse without warning. Guides check the route every day, fit you with crampons and a harness, and know when to turn back. Walking onto the ice on your own is dangerous, and rescue is slow and difficult.</p>
<p>The two main areas for glacier hikes are Sólheimajökull on the south coast and Falljökull near Skaftafell. Both run all year, and standard walks of about three to four hours suit most fit people. Most operators accept children from about 8 or 10 years old. Our <a href="/blog/glacier-hiking-iceland">guide to choosing a glacier hike</a> compares them in detail, and our page on <a href="/places/glacier-hikes">glacier hikes</a> shows what the ice looks like.</p>
<p class="callout"><strong>Guided only:</strong> never step onto glacier ice, stranded icebergs or an ice cave without a certified guide. Viewpoints and marked trails let you get close safely.</p>
<h2>When can you visit an ice cave in Iceland?</h2>
<p>The natural blue ice caves in Vatnajökull are a winter activity. Tours run from about October or November to March or April, when the ice is cold and stable, and the caves are closed from May to September. The exact start depends on the weather each year.</p>
<p>If you travel in summer, the Katla ice cave near Vík is open all year, and Into the Glacier on Langjökull is a man-made tunnel you can visit in any season. Our <a href="/blog/iceland-ice-caves">ice cave guide</a> explains the difference, the safety rules and how to choose a tour, and our <a href="/places/ice-caves">ice caves page</a> has photos.</p>
<h2>What are Iceland's glacier lagoons?</h2>
<p>Glacier lagoons are lakes that form in front of a glacier as it melts back. Icebergs break off the glacier front and float in the lagoon, sometimes for years, before drifting out or melting. The south coast has several, all fed by Vatnajökull.</p>
<p>Jökulsárlón is the largest and most visited. It formed in the 1930s and is now about 25 km² and up to 284 m deep, one of the deepest lakes in Iceland. Its ice flows out under the Route 1 bridge and washes up on Diamond Beach. Read our <a href="/blog/jokulsarlon-diamond-beach-guide">complete guide to Jökulsárlón and Diamond Beach</a> for parking, boat tours and the best time to go.</p>
<p>Fjallsárlón, 10 km to the west, is smaller and quieter, and lies right below the steep Fjallsjökull glacier. Breiðárlón and Heinabergslón are further off the main road. Our guide to <a href="/blog/glacier-lagoons-iceland">glacier lagoons beyond Jökulsárlón</a> compares them.</p>
<h2>What else can you do on Iceland's glaciers?</h2>
<p>Beyond hikes and ice caves, these are the main glacier activities. All of them are run by licensed operators, and all depend on the weather on the day.</p>
<ul>
<li><strong>Boat tours:</strong> amphibian boats and Zodiacs sail among the icebergs at Jökulsárlón, roughly from spring to autumn, and Zodiacs run at Fjallsárlón.</li>
<li><strong>Kayaking:</strong> guided kayak trips on Heinabergslón run from June to September and last about three hours.</li>
<li><strong>Ice tunnel:</strong> Into the Glacier takes you about 500 m into Langjökull through a man-made tunnel, all year, from Húsafell or Reykjavík.</li>
<li><strong>Snowmobiles and glacier trucks:</strong> snowmobile tours on Langjökull run from Reykjavík, and monster-truck tours onto the ice leave from near Gullfoss.</li>
<li><strong>Summit climbs:</strong> guided ascents of Hvannadalshnúkur take around 15 hours and need good fitness and a settled forecast.</li>
</ul>
<h2>How do you plan a glacier trip along the south coast?</h2>
<p>Plan at least two nights east of Vík. Sólheimajökull is about 2.5 hours from Reykjavík, but Skaftafell and the lagoons are 325 to 380 km away. Staying near Skaftafell, Jökulsárlón or in Höfn lets you see the lagoons in the early morning and join tours without a long drive first. Our guide to <a href="/blog/where-to-stay-in-iceland">where to stay in Iceland</a> covers the bases.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stop</th><th>Distance or time</th><th>What to do</th><th>Time needed</th></tr></thead>
<tbody>
<tr><td>Sólheimajökull</td><td>About 2.5 h from Reykjavík</td><td>Viewpoint trail, guided hike</td><td>1 h on your own; 3–4 h with a hike</td></tr>
<tr><td>Skaftafell</td><td>325 km from Reykjavík</td><td>Svartifoss, glacier viewpoint, guided hike</td><td>Half a day or more</td></tr>
<tr><td>Fjallsárlón</td><td>About 10 km before Jökulsárlón</td><td>Lagoon shore, Zodiac tour</td><td>30 min to 1.5 h</td></tr>
<tr><td>Jökulsárlón and Diamond Beach</td><td>About 370 km from Reykjavík</td><td>Lagoon, boat tours, ice caves in winter</td><td>2–3 h, more with a tour</td></tr>
<tr><td>Höfn</td><td>About 80 km east of Jökulsárlón</td><td>Base for Heinabergslón and the east</td><td>Overnight</td></tr>
</tbody></table></div>
<p>A good three-day plan from Reykjavík: drive to Vík on day one with a glacier hike at Sólheimajökull. Spend day two at Skaftafell and Fjallsárlón. On day three, visit Jökulsárlón and Diamond Beach early, then take a boat tour or, in winter, an ice cave tour. Our <a href="/blog/south-coast-iceland">south coast guide</a> has the stops in between, and the <a href="/blog/iceland-ring-road-guide">Ring Road guide</a> shows how the glaciers fit into a full loop.</p>
<h2>When is the best time to see Iceland's glaciers?</h2>
<p>You can see glaciers all year, but each season offers different things. Summer gives long days, open roads and boat tours on the lagoons. Winter brings the natural ice caves, more ice on Diamond Beach and the chance of northern lights over the lagoons.</p>
<div class="table-wrap"><table>
<thead><tr><th>Activity</th><th>Season</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Glacier viewpoints and lagoons</td><td>All year</td><td>Winter days are short; check road.is</td></tr>
<tr><td>Guided glacier hikes</td><td>All year</td><td>Tours pause when conditions are unsafe</td></tr>
<tr><td>Natural ice caves (Vatnajökull)</td><td>About Oct/Nov to Mar/Apr</td><td>Closed May to September</td></tr>
<tr><td>Katla ice cave and Into the Glacier</td><td>All year</td><td>The summer options</td></tr>
<tr><td>Jökulsárlón boat tours</td><td>About April/May to October</td><td>Depends on the operator and the ice</td></tr>
<tr><td>Heinabergslón kayaking</td><td>June to September</td><td>Guided only</td></tr>
</tbody></table></div>
<p>For a single trip that covers the most, late September and October, or March, work well. You get reasonable daylight, a chance of auroras and, from autumn, the first ice cave tours. Our guide to the <a href="/blog/best-time-to-visit-iceland">best time to visit Iceland</a> has the monthly weather and daylight.</p>
<h2>Can you visit Iceland's glaciers on your own in winter?</h2>
<p>Yes, you can drive to the glacier viewpoints and lagoons on your own all winter, as long as the roads are open. Route 1 along the south coast is kept open where possible, but storms, ice and strong wind can close it for hours or days. Check road.is and vedur.is every morning and be ready to change plans.</p>
<p>Daylight is the main limit. Around the December solstice Reykjavík gets only about four hours of daylight, so a drive from Vík to Jökulsárlón can use most of the light you have. Short legs and early starts work best. Paths to viewpoints such as Svartifoss and the Skaftafellsjökull trail can be glazed with ice, so carry microspikes and turn back where the path is unsafe.</p>
<p>Winter also has rewards. Diamond Beach usually has the most ice, the lagoons are quiet in the morning, and on clear nights you may see the <a href="/northern-lights">northern lights</a> over the ice. For anything on the glacier itself, from hikes to ice caves, book a guide.</p>
<h2>How do you stay safe around glaciers?</h2>
<p>Stay on marked trails, keep off the ice unless you are with a guide, and respect closures and warning signs. The edge of a glacier is often its most unstable part.</p>
<ul>
<li><strong>Glacier edges change daily.</strong> In July 2026 the Icelandic Met Office warned of an unstable ice ridge, deep lagoons and rockfall at the edge of Sólheimajökull. Access stayed open, but some tours paused while guides found safer routes.</li>
<li><strong>Ice caves can collapse.</strong> On 25 August 2024 part of an ice cave on Breiðamerkurjökull collapsed during a summer tour, killing an American visitor. Tours inside the national park now run only in the cold season, with daily risk checks.</li>
<li><strong>Do not climb icebergs.</strong> Stranded ice on Diamond Beach and floating ice in the lagoons can roll, split or float off without warning.</li>
<li><strong>Keep back from the water.</strong> Waves can run far up Diamond Beach, and the lagoons are deep and close to freezing.</li>
<li><strong>Check before you go.</strong> Look at the forecast on vedur.is, roads on road.is and alerts on safetravel.is every morning. In an emergency, call 112.</li>
</ul>
<h2>Are Iceland's glaciers shrinking?</h2>
<p>Yes. Almost every glacier in Iceland is retreating. Total glacier area has fallen by more than 2,200 km² since the end of the 19th century, and the smaller glaciers have lost the largest share. Snæfellsjökull has lost about 65% of its maximum area, and Drangajökull about half.</p>
<p>Okjökull in the west is the best-known loss. Its ice shrank from about 7.4 km² in the 1940s to almost nothing by 2019, and it no longer counts as a glacier. You can see the change on the south coast too. Jökulsárlón grew from about 8 km² in 1975 to about 25 km² today, and Sólheimajökull retreated 93 m on its western tongue between 2024 and 2025 alone. The lagoons grow as the glaciers shrink, which is also why paths, viewpoints and tour routes move from year to year.</p>
<h2>What should you wear to visit a glacier?</h2>
<p>Dress for cold wind even in summer. The air above the ice is colder than in the car park, and the lagoons are often windy.</p>
<ul>
<li>Waterproof, windproof jacket and trousers.</li>
<li>Warm layers in wool or fleece, not cotton.</li>
<li>Hat, gloves and a buff or scarf.</li>
<li>Waterproof hiking boots with ankle support. Many tour operators rent boots if yours are not stiff enough for crampons.</li>
<li>Sunglasses and sunscreen, because snow and ice reflect a lot of light.</li>
<li>Microspikes for icy paths in winter, on your own walks to viewpoints.</li>
</ul>
<p>Tour operators provide the technical gear: crampons, a helmet, a harness and an ice axe on hikes, and a helmet and crampons in ice caves.</p>
<h2>What is the easiest way to see a glacier from Reykjavík?</h2>
<p>The easiest option is a south coast day tour with a stop or a hike at Sólheimajökull, which is about 2.5 hours away. Into the Glacier and Langjökull snowmobile tours are other full-day options. Jökulsárlón can be done as a very long day trip, but the drive is about 370 km each way, so it is far better with a night on the south coast.</p>
<p>For more ideas, see all our <a href="/highlights">Iceland highlights on one interactive map</a>, including <a href="/places/vatnajokull">Vatnajökull</a> and <a href="/places/breidamerkurjokull">Breiðamerkurjökull</a>. If you want the full route in print, the south coast and glacier chapters of our <a href="/#guides">Complete Guide to Iceland</a> cover every stop in this article. For first-timers heading east, start with our guide to <a href="/blog/vatnajokull-national-park">Vatnajökull National Park</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Glacier areas are 2019 figures; glaciers, paths and lagoon shores change every year. Ice cave seasons, tour availability and parking fees change, so check operators, safetravel.is and vedur.is before you go.",
        "sources": [
            ("List of glaciers in Iceland (Wikipedia)", "https://en.wikipedia.org/wiki/List_of_glaciers_in_Iceland"),
            ("Over 400 glaciers cover more than 10% of Iceland's landmass (Covering Climate Now / CBS News)", "https://coveringclimatenow.org/partner-story/over-400-glaciers-cover-more-than-10-of-icelands-landmass-and-almost-every-one-is-shrinking"),
            ("Vatnajökull National Park (Wikipedia)", "https://en.wikipedia.org/wiki/Vatnaj%C3%B6kull_National_Park"),
            ("Jökulsárlón (Wikipedia)", "https://en.wikipedia.org/wiki/J%C3%B6kuls%C3%A1rl%C3%B3n"),
            ("Increased hazard at the margin of Sólheimajökull glacier (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/increased-hazard-due-to-changing-conditions-at-the-margin-of-solheimajokull-glacier"),
            ("The safest month to visit ice caves in Iceland (Guide to Iceland)", "https://guidetoiceland.is/nature-info/safest-month-to-visit-ice-caves-in-iceland"),
            ("Skaftafell (Icelandia)", "https://www.icelandia.com/attractions/skaftafell"),
            ("Öræfajökull (Wikipedia)", "https://en.wikipedia.org/wiki/%C3%96r%C3%A6faj%C3%B6kull"),
        ],
    },
    # ------------------------------------------------------------------
    # 2. JÖKULSÁRLÓN AND DIAMOND BEACH
    # ------------------------------------------------------------------
    {
        "slug": "jokulsarlon-diamond-beach-guide",
        "cluster": "glaciers",
        "pillar": False,
        "short": "Jökulsárlón and Diamond Beach: Visitor Guide",
        "title": "Jökulsárlón and Diamond Beach: Complete Visitor Guide (2027)",
        "description": "Jökulsárlón and Diamond Beach guide: where they are, parking fees, amphibian and Zodiac boat tours, seals, the best time for ice, safety and where to stay.",
        "category": "Glaciers · South Coast",
        "teaser": "Parking, boat tours, the best light and how to stay safe on the ice beach.",
        "image": "hx-jokulsarlon",
        "image_alt": "Blue and ash-striped icebergs floating in Jökulsárlón glacier lagoon under a stormy sky",
        "stats": [
            ("284 m", "Maximum depth of Jökulsárlón"),
            ("~25 km²", "Area of the lagoon, up from about 8 km² in 1975"),
            ("~370 km", "Driving distance from Reykjavík"),
            ("1934–35", "When the lagoon first formed"),
        ],
        "body": """
<p>Jökulsárlón is a glacier lagoon on Iceland's south coast, and Diamond Beach is the black sand shore across the road where its icebergs wash up. Both sit beside Route 1, about 370 km east of Reykjavík, and both are free to walk around, with a parking fee of about ISK 1,000 per car. Go early or late to avoid the tour buses, take a boat tour between April and October, and never climb on the ice.</p>
<!--TOC-->
<h2>Where are Jökulsárlón and Diamond Beach?</h2>
<p>They are in southeast Iceland, on the Ring Road between Skaftafell and Höfn, inside Vatnajökull National Park. Jökulsárlón is about 370 km from Reykjavík, roughly 4.5 to 5 hours of driving without stops. Höfn is about 80 km further east, around an hour away, and Skaftafell is about 45 minutes to the west.</p>
<p>The lagoon lies on the inland side of Route 1. Diamond Beach lies on the ocean side, either side of the short river that carries the ice out to sea under the bridge. There are car parks at the lagoon and on both sides of the beach, all within two minutes' drive.</p>
<h2>What is Jökulsárlón?</h2>
<p>Jökulsárlón is a lake of meltwater in front of Breiðamerkurjökull, an outlet glacier of Vatnajökull. It began to form around 1934–35, when the glacier tongue pulled back from the coast. Since then it has grown quickly, from about 8 km² in 1975 to about 25 km² today. With a maximum depth of 284 m, it is one of the deepest lakes in Iceland.</p>
<p>Icebergs break off the glacier front and float in the lagoon, some striped black with volcanic ash, some bright blue, and slowly drift towards the outlet. The state bought the land in 2017 and the lagoon became part of <a href="/blog/vatnajokull-national-park">Vatnajökull National Park</a> the same year. The lagoon has also appeared in films including the James Bond films <em>A View to a Kill</em> and <em>Die Another Day</em>, and <em>Batman Begins</em>.</p>
""" + _map(
            "Map of Iceland's glaciers and glacier lagoons, including Jökulsárlón",
            "Jökulsárlón sits beside Route 1 among the southeast glacier lagoons and ice-cave areas.",
        ) + """
<h2>What is Diamond Beach?</h2>
<p>Diamond Beach is the stretch of black sand on both sides of the Jökulsárlón outlet, where chunks of ice from the lagoon wash ashore. The shore is part of Breiðamerkursandur, the wide sand plain built by the glacier's rivers. The waves polish the ice until it shines against the black sand, which gives the beach its name.</p>
<p>The beach has two sides. The east side is bigger and busier. The west side is often quieter and popular with photographers at dawn. You cannot walk between them along the sand, because the river is deep and fast. Drive across the bridge instead, and never wade the river mouth.</p>
<p>How much ice you see changes every day. Winter usually brings the most and largest pieces. In summer the ice is smaller and more scattered, and on some days there is very little.</p>
<h2>Should you take a boat tour on Jökulsárlón?</h2>
<p>A boat tour is the best way to see the icebergs up close, and it is worth it if you have the time. There are two types, both leaving from the lagoon. Prices below are approximate starting prices checked in 2026.</p>
<div class="table-wrap"><table>
<thead><tr><th>Tour</th><th>Season</th><th>Time on the water</th><th>Minimum age</th><th>From about</th></tr></thead>
<tbody>
<tr><td>Amphibian boat</td><td>About May to October</td><td>About 30–40 min</td><td>All ages</td><td>ISK 7,100</td></tr>
<tr><td>Zodiac boat</td><td>About April to October</td><td>About an hour or more</td><td>8 years</td><td>US$135–139</td></tr>
</tbody></table></div>
<p>The amphibian boat drives off the shore into the lagoon and cruises among the icebergs nearest the beach. It suits families and anyone who wants a calm, short trip. The Zodiac is a small, fast boat for up to 12 people that goes much further across the lagoon, towards the glacier front. You wear a floatation suit and need to sit on the side of the boat, so it is more physical.</p>
<p>Book ahead in July and August. Tours can be cancelled in strong wind or when too much ice blocks the lagoon. In winter there are no boat tours, but the lagoon is the meeting point for most ice cave tours. See our <a href="/blog/iceland-ice-caves">Iceland ice cave guide</a> for those.</p>
<h2>Can you see seals at Jökulsárlón?</h2>
<p>Often, yes. Seals come into the lagoon and gather at its mouth to hunt fish, especially in winter. Look for heads in the water near the bridge and for seals resting on the floating ice. Watch them from the shore and keep your distance if one is on the beach.</p>
<h2>When is the best time to visit?</h2>
<p>You can visit Jökulsárlón and Diamond Beach all year, 24 hours a day. Early morning and evening are best. The light is softer, and you avoid the tour buses, which mostly arrive between about 11:00 and 16:00.</p>
<ul>
<li><strong>Summer (June to August):</strong> long days, boat tours and a chance of midnight-sun light. Less ice on the beach.</li>
<li><strong>Autumn (September to October):</strong> fewer people, boat tours still running, and the first dark nights for the <a href="/northern-lights">northern lights</a>.</li>
<li><strong>Winter (November to March):</strong> the most ice on the beach, ice cave tours, and the chance of auroras over the lagoon. Days are short and the road can be icy.</li>
</ul>
<p>The ice on Diamond Beach changes with the tide. A visit in the hours after high tide often finds fresh pieces washed up.</p>
<h2>How much does parking cost at Jökulsárlón?</h2>
<p>Parking costs about ISK 1,000 for a standard car per day, as of 2026, and more for larger vehicles. One payment covers the lagoon and Diamond Beach car parks on the same day. You pay through the Parka app or website, or at machines on site, and number-plate cameras record your visit. The fee runs until midnight.</p>
<p>If you also stop at Skaftafell that day and pay with the same method, the second site is half price. Entry to the lagoon and the beach is free. The fees pay for toilets, rangers, rubbish collection and path upkeep.</p>
<p class="callout"><strong>Never climb on the icebergs.</strong> Ice on the beach and in the lagoon can roll, split or float off with you on it. Keep back from the waterline, never wade the river mouth, and if someone is swept out, do not go in after them. Call 112.</p>
<h2>How do you stay safe at Diamond Beach?</h2>
<p>Treat the beach like any exposed Atlantic shore. Waves can run much further up the sand than the ones before, and the water is close to freezing. Keep children close, do not turn your back on the sea, and stay off the ice blocks, however small and stable they look.</p>
<p>In winter, add a margin for storm surf and icy paths, and wear microspikes if the car parks are glazed. Unlike <a href="/places/reynisfjara">Reynisfjara</a>, there is no warning-light system here, so judge the sea yourself and stay well back.</p>
<h2>How long should you spend at Jökulsárlón?</h2>
<p>Allow at least two hours for the lagoon and both sides of Diamond Beach, and three to four hours with a boat tour. Walking along the lagoon shore east of the café gives you quieter views than the main car park.</p>
<p>There are toilets and cafés by the lagoon car park. Fuel, shops and the nearest wide choice of food are in Höfn. If you have time, stop at <a href="/places/fjallsarlon">Fjallsárlón</a> 10 km to the west, a smaller lagoon right under the glacier wall. Our guide to <a href="/blog/glacier-lagoons-iceland">glacier lagoons beyond Jökulsárlón</a> covers it and others.</p>
<h2>Can you visit Jökulsárlón as a day trip from Reykjavík?</h2>
<p>You can, but it is a very long day. The return drive is about 740 km, at least nine hours at the wheel before any stops. Day tours from Reykjavík exist, but most of the day is spent on the bus, and in winter much of it is in the dark.</p>
<p>A night or two nearby is much better. Stay around Skaftafell, at one of the farm hotels near the lagoon, or in Höfn, and you can see the ice at sunrise before the buses arrive. Our <a href="/blog/glaciers-in-iceland">guide to Iceland's glaciers</a> has a three-day south coast plan, and the <a href="/places/jokulsarlon">Jökulsárlón place page</a> and <a href="/places/breidamerkurjokull">Breiðamerkurjökull</a> page have more photos.</p>
""",
        "checked_note": "Facts checked October 2026. Parking fees, boat tour seasons and prices change every year; check Parka and the tour operators before you go. The amount of ice on Diamond Beach varies daily.",
        "sources": [
            ("Jökulsárlón (Wikipedia)", "https://en.wikipedia.org/wiki/J%C3%B6kuls%C3%A1rl%C3%B3n"),
            ("Diamond Beach guide (Iceland Highlights)", "https://www.iceland-highlights.com/destination/diamond-beach/"),
            ("Diamond Beach travel guide (Guide to Iceland)", "https://guidetoiceland.is/voyage-islande/diamond-beach"),
            ("Visit Jökulsárlón or Skaftafell: area fees (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/news/visit-jokulsarlon-or-skaftafell"),
            ("Parking fees in Iceland (Go Campers)", "https://www.gocampers.is/guides/money/parking-fees-iceland/"),
            ("Pay for parking at Skaftafell (Parka)", "https://parka.is/pay/skaftafell/"),
            ("Jökulsárlón amphibian boat tour (Arctic Adventures)", "https://adventures.is/iceland/day-tours/boat-tours/jokulsarlon-amphibian-boat-tour/"),
            ("Jökulsárlón Zodiac boat tour (Arctic Adventures)", "https://adventures.is/iceland/day-tours/boat-tours/jokulsarlon-glacier-lagoon-zodiac-boat-tour/"),
        ],
    },
    # ------------------------------------------------------------------
    # 3. ICE CAVES
    # ------------------------------------------------------------------
    {
        "slug": "iceland-ice-caves",
        "cluster": "glaciers",
        "pillar": False,
        "short": "Iceland Ice Caves: Season, Safety and Tours",
        "title": "Iceland Ice Cave Tours: Season, Safety and Which Cave to Choose (2027)",
        "description": "Iceland ice cave guide for 2027: when the natural Vatnajökull caves open, year-round options like Katla, safety rules since 2024, tour prices and what to wear.",
        "category": "Glaciers · Winter",
        "teaser": "Natural blue caves in winter, Katla all year, and how to choose a tour.",
        "image": "hx-ice-caves",
        "image_alt": "Light shining through the blue walls of an ice cave inside a glacier",
        "stats": [
            ("Oct–Apr", "Ice cave tour season in Vatnajökull National Park"),
            ("May–Sep", "Months the park's natural ice caves stay closed"),
            ("All year", "Katla ice cave near Vík and the Langjökull ice tunnel"),
            ("8–16", "Guests per guide on park ice cave tours"),
        ],
        "body": """
<p>The classic Iceland ice cave, with walls of glowing blue, is a natural cave inside Vatnajökull, and you can only visit one in winter, roughly from October or November to March. Outside that season, the Katla ice cave near Vík runs all year, and Into the Glacier on Langjökull is a man-made tunnel open in every month. Every ice cave visit must be with a licensed guide. Here is how the options compare, how safe they are and how to choose.</p>
<!--TOC-->
<h2>What kinds of ice cave can you visit in Iceland?</h2>
<p>There are three main types: natural winter caves in Vatnajökull, the year-round Katla cave in Mýrdalsjökull, and the man-made tunnel in Langjökull. They differ in colour, season, distance from Reykjavík and how much walking they need.</p>
<div class="table-wrap"><table>
<thead><tr><th>Cave</th><th>Glacier</th><th>Season</th><th>Starts from</th><th>What it looks like</th></tr></thead>
<tbody>
<tr><td>Vatnajökull natural caves (incl. "Crystal" caves)</td><td>Breiðamerkurjökull and nearby outlets of Vatnajökull</td><td>About Oct/Nov to Mar/Apr</td><td>Jökulsárlón, Skaftafell</td><td>Bright blue, clear ice; changes every year</td></tr>
<tr><td>Katla ice cave</td><td>Kötlujökull, an outlet of Mýrdalsjökull</td><td>All year</td><td>Vík, or day tours from Reykjavík</td><td>Darker ice striped with black volcanic ash</td></tr>
<tr><td>Into the Glacier</td><td>Langjökull</td><td>All year</td><td>Húsafell, or day tours from Reykjavík</td><td>Man-made tunnel about 500 m long, lit inside</td></tr>
</tbody></table></div>
<p>If the bright blue walls in photos are what you want, plan a winter trip and book a Vatnajökull cave. If you travel in summer, or have limited time, Katla or the ice tunnel are the realistic options.</p>
<h2>When is the ice cave season in Iceland?</h2>
<p>The natural ice caves in Vatnajökull National Park open from about October to April, and are closed from May to September. The most reliable months are November to March. The 2025–26 season began in October, but each season starts only when guides judge the caves safe, so early dates are never certain.</p>
<p>The caves form in summer, when meltwater cuts channels through the glacier. As the water drains away in autumn and the ice freezes hard, a hollow is left that people can walk into. Each winter brings different caves, so the one you visit will not look exactly like last year's photos.</p>
<p>Within the season, the coldest months are the most stable. February and January have the most days below freezing. October and March have softer ice and more rain, and heavy rain on the day is the most common reason for a cancellation.</p>
""" + _map(
            "Map of Iceland's glaciers with the main ice-cave and glacier-hike areas marked",
            "The ice-cave areas around Vatnajökull and Mýrdalsjökull, with the glacier lagoons nearby.",
        ) + """
<h2>Are Iceland's ice caves safe?</h2>
<p>Ice caves are safe enough on a licensed tour in the cold season, but they are never risk-free. On 25 August 2024, part of an ice cave on Breiðamerkurjökull collapsed during a summer tour. An American visitor was killed and another person was seriously injured. The Association of Icelandic Mountain Guides warned afterwards that glacier trips in the warmer months can be very dangerous.</p>
<p>The park changed its rules after the accident. These are the main ones now in place:</p>
<ul>
<li>Ice cave tours in Vatnajökull National Park run only in the cold season, and the caves are closed from May to September.</li>
<li>Experienced lead guides assess every cave each day, and any cave judged unsafe stays closed. Companies share their risk assessments.</li>
<li>Each guide may take only 8 to 16 guests, depending on the tour.</li>
<li>Only companies with a park contract may lead tours. About 30 companies received contracts in the current round.</li>
</ul>
<p>The Katla cave lies outside the national park, so the park's rules do not cover it. Operators there run their own risk checks, and guides may switch to another part of the glacier if the usual cave is unsafe.</p>
<p class="callout"><strong>Never enter an ice cave on your own.</strong> Ceilings can thin by several centimetres in a day, meltwater can rise fast, and a cave that looks solid can collapse. Go only with a licensed guide, and accept a cancellation if they call one.</p>
<h2>Which ice cave tour should you choose?</h2>
<p>Choose by where you are staying and the season. These are the main options, with approximate prices checked in 2026.</p>
<ul>
<li><strong>Vatnajökull caves from Jökulsárlón (winter):</strong> most tours meet at the Jökulsárlón car park and drive by super jeep to the glacier. They take about 2.5 to 3 hours, cost from about ISK 22,000–24,000, and usually accept children from about 6 to 8. You need your own car or a multi-day tour, as there is no pickup.</li>
<li><strong>Longer small-group caves (winter):</strong> five-to-six-hour tours visit more remote caves and include more walking on the glacier. They cost from about ISK 37,000.</li>
<li><strong>Ice cave and glacier hike from Skaftafell (winter):</strong> about four hours, combining a hike on the ice with a cave visit, from about ISK 18,500.</li>
<li><strong>Katla ice cave from Vík (all year):</strong> a super jeep drives about 30 minutes across black sand to Kötlujökull. Tours take about three hours and cost from about ISK 24,000, a little more in winter. Full-day tours from Reykjavík take 11 to 12 hours.</li>
<li><strong>Into the Glacier from Húsafell (all year):</strong> about three to four hours, with a glacier truck ride up Langjökull and a guided walk through the tunnel, from about ISK 25,000–28,000. It is about two hours' drive from Reykjavík. The tunnel has flat, prepared floors, so it suits people who cannot manage rough ground.</li>
</ul>
<p>Many visitors combine a winter ice cave with Jökulsárlón and Diamond Beach on the same day. Our <a href="/blog/jokulsarlon-diamond-beach-guide">Jökulsárlón and Diamond Beach guide</a> covers the lagoon, and our <a href="/blog/glacier-hiking-iceland">glacier hiking guide</a> helps if you want time on the ice as well.</p>
<h2>How do you get to the ice caves?</h2>
<p>For the Vatnajökull caves, drive yourself to the meeting point at Jökulsárlón or Skaftafell. Jökulsárlón is about 370 km from Reykjavík, so stay at least one night in the area. Winter roads on the south coast can be icy and closed by storms, so check road.is and vedur.is each morning and leave a margin before your tour time.</p>
<p>For Katla, Vík is about 2.5 hours from Reykjavík, and day tours with pickup run from the capital. For Into the Glacier, you can drive to Húsafell in about two hours or join a full-day tour from Reykjavík.</p>
<h2>What should you wear in an ice cave?</h2>
<p>Wear the same clothes as for a glacier hike. The inside of a cave is around freezing, damp and often dripping, and you walk on the glacier to reach it.</p>
<ul>
<li>Waterproof hiking boots with ankle support. Many operators rent them.</li>
<li>Warm base layer and a wool or fleece mid-layer.</li>
<li>Waterproof jacket and trousers.</li>
<li>Hat, gloves and a buff or scarf.</li>
<li>A small bag with water and a snack.</li>
</ul>
<p>The operator provides a helmet and crampons, and a harness and ice axe on longer tours. Leave large bags in the car.</p>
<h2>Can you visit an ice cave in summer?</h2>
<p>Yes, but not the natural blue caves of Vatnajökull. In summer your options are the Katla ice cave, which runs every month, and the Into the Glacier tunnel on Langjökull. Katla's ash-covered ice melts more slowly, which keeps the cave usable year-round, but expect darker, ash-streaked walls rather than glassy blue ice.</p>
<h2>How far ahead should you book?</h2>
<p>Book a few weeks ahead for December to March, and longer for the Christmas and New Year period. Plan your tour for the first full day in the area, so a weather cancellation can move to the next day, and read the cancellation terms before you pay.</p>
<p>For winter planning, read our <a href="/blog/glaciers-in-iceland">guide to Iceland's glaciers</a>, the <a href="/places/ice-caves">ice caves place page</a>, and our <a href="/northern-lights">northern lights guide</a> for the evenings. Winter visitors also find the <a href="/places/vatnajokull">Vatnajökull</a> page useful for the wider area.</p>
""",
        "checked_note": "Facts checked October 2026. Ice cave seasons depend on the weather each year, and tours are cancelled whenever guides judge a cave unsafe. Prices are approximate 2026 starting prices; check the operator before booking.",
        "sources": [
            ("The safest month to visit ice caves in Iceland (Guide to Iceland)", "https://guidetoiceland.is/nature-info/safest-month-to-visit-ice-caves-in-iceland"),
            ("Ice cave tours in Iceland: which one to choose, 2026–27 (Iceland Travel Guide)", "https://icelandtravelguide.is/blog-posts/ice-cave-tours-in-iceland/"),
            ("Visitor numbers may be limited on Vatnajökull ice cave tours (Reykjavík Grapevine)", "https://grapevine.is/news/2025/09/16/visitor-numbers-may-be-limited-on-vatnajokull-ice-cave-tours/"),
            ("Collapse of ice cave in Iceland (Associated Press via ADN)", "https://www.adn.com/nation-world/2024/08/26/collapse-of-ice-cave-in-iceland-kills-at-least-one-person-two-missing/"),
            ("When is the ice-cave season? (Visit Vatnajökull)", "https://visitvatnajokull.is/faq/when-is-the-ice-cave-season"),
            ("Katla ice cave tour (Iceland Highlights)", "https://www.iceland-highlights.com/katla-ice-cave-tour/"),
            ("Into the Glacier from Húsafell (Iceland Highlights)", "https://www.iceland-highlights.com/tour/into-the-glacier-husafell/"),
        ],
    },
    # ------------------------------------------------------------------
    # 4. GLACIER HIKING
    # ------------------------------------------------------------------
    {
        "slug": "glacier-hiking-iceland",
        "cluster": "glaciers",
        "pillar": False,
        "short": "Glacier Hiking in Iceland: Which Glacier to Choose",
        "title": "Glacier Hike in Iceland: Which Glacier to Choose, Tours and Safety (2027)",
        "description": "Planning a glacier hike in Iceland? Compare Sólheimajökull and Falljökull at Skaftafell, tour lengths, age limits, what to wear and why you must go guided.",
        "category": "Glaciers · Activities",
        "teaser": "Sólheimajökull or Skaftafell, what a hike involves and why it is guided only.",
        "image": "hx-glacier-hikes",
        "image_alt": "A line of hikers crossing a blue-grey glacier under a white sky",
        "stats": [
            ("Guided only", "Never walk onto glacier ice without a certified guide"),
            ("~2.5 h", "Drive from Reykjavík to Sólheimajökull"),
            ("All year", "Season for guided hikes at Sólheimajökull and Falljökull"),
            ("8–10 yrs", "Typical minimum age on standard glacier walks"),
        ],
        "body": """
<p>For a glacier hike in Iceland, choose Sólheimajökull if you are based in Reykjavík or on the western south coast, and Falljökull near Skaftafell if you are travelling further east. Both run all year on guided tours of about three to four hours, with crampons and safety gear provided. Never walk onto a glacier without a certified guide. Here is how the main glaciers compare and what a hike involves.</p>
<!--TOC-->
<h2>Which glacier is best for a hike in Iceland?</h2>
<p>For most visitors the best glacier for a hike is the one on their route. Sólheimajökull is closest to Reykjavík and fits into a south coast day. Falljökull, at Skaftafell in Vatnajökull National Park, has bigger scenery and fewer day-trippers, but it is 325 km from the capital.</p>
<div class="table-wrap"><table>
<thead><tr><th>Glacier</th><th>Ice cap</th><th>From Reykjavík</th><th>Meeting point</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Sólheimajökull</td><td>Mýrdalsjökull</td><td>About 2.5 h</td><td>Sólheimajökull car park</td><td>Short trips, day tours from Reykjavík</td></tr>
<tr><td>Falljökull</td><td>Vatnajökull</td><td>About 325 km</td><td>Skaftafell visitor centre area</td><td>Ring Road trips, steeper icefalls</td></tr>
<tr><td>Hvannadalshnúkur</td><td>Öræfajökull (Vatnajökull)</td><td>Near Skaftafell</td><td>Arranged with the operator</td><td>Fit, experienced hikers; about 15 h</td></tr>
</tbody></table></div>
<p>Both main glaciers also have longer options, such as ice-climbing add-ons and combined hike and ice cave tours from Skaftafell in winter.</p>
<h2>What is a hike on Sólheimajökull like?</h2>
<p>Sólheimajökull is an outlet glacier about 11 km long that flows down from Mýrdalsjökull, the ice cap over the Katla volcano. Its ice is streaked with black ash. Tours meet at the car park, about 2.5 hours from Reykjavík off Route 1 between Skógafoss and Vík.</p>
<p>From the car park you walk about 15 to 20 minutes to the edge of the ice. The walk has grown longer as the glacier has retreated, with 93 m of retreat on its western tongue between 2024 and 2025 alone. At the ice you fit crampons, a harness and a helmet, then walk up among ridges, crevasses and sink holes. A standard walk takes about three to four hours in total, and the standard tour we checked accepts children from 10.</p>
<p>Parking costs ISK 750 per car, paid through Parka. Many south coast day tours from Reykjavík include a Sólheimajökull hike, so it works without a car.</p>
<h3>What changed at Sólheimajökull in 2026?</h3>
<p>On 22 July 2026 the Icelandic Met Office warned of increased hazard at the edge of Sólheimajökull. A new lagoon had thinned the ice ridge used to reach the glacier, there are deep, cold lagoons on either side, and rocks can fall from the slopes above the access route. Some operators cancelled trips while guides looked for safer routes. Officials chose to keep the area open with stronger warnings, and guided tours were running again in August 2026. Conditions there change daily, so expect your guide to adjust the route or, on some days, cancel.</p>
""" + _map(
            "Map of Iceland's glaciers showing the glacier-hike areas at Sólheimajökull and Skaftafell",
            "Glacier-hike areas on the south coast, with the ice caps and glacier lagoons.",
        ) + """
<h2>What is a hike at Skaftafell like?</h2>
<p>Hikes at Skaftafell go onto Falljökull, an outlet glacier of Vatnajökull that drops steeply from the Öræfajökull massif. Tours meet near the Skaftafell visitor centre. Standard walks take about 3.5 to 4 hours and accept children from 8. Operators provide crampons, a harness, an ice axe and other safety gear, and many rent boots.</p>
<p>The ice here is cleaner and bluer than at Sólheimajökull, with big icefalls above you. Until 2018, most tours from Skaftafell used neighbouring Svínafellsjökull, and Falljökull has been the main hiking glacier since. Skaftafell also has excellent marked trails off the ice, including the walk to Svartifoss. Our <a href="/blog/vatnajokull-national-park">Vatnajökull National Park guide</a> covers them.</p>
<p>Parking at Skaftafell costs about ISK 1,110 for a car in 2026. If you pay at Jökulsárlón the same day with the same method, you get half off the second site.</p>
<h2>Why must you hike a glacier with a guide?</h2>
<p>Because glacier ice is moving, cracking and melting all the time, and its dangers are hard to see. Crevasses hide under thin snow, meltwater shafts drop deep into the ice, and the edges of glaciers collapse into lagoons. Iceland's tourism and safety bodies are clear that glacier travel should only be done with certified guides.</p>
<p>A guide checks the route every day, cuts steps where needed, ropes the group on harder ground and knows when to turn back. Rescue on a glacier is slow, and in 2026 an injured visitor at Sólheimajökull had to be lifted out by a Coast Guard helicopter because ground access was so difficult.</p>
<p class="callout"><strong>Guided only:</strong> do not step past the end of the marked path onto the ice, even for a photo. The edge of the glacier is often the most unstable part.</p>
<h2>How fit do you need to be?</h2>
<p>A standard glacier walk suits anyone who can hike for two to three hours on uneven ground. The pace is slow, with frequent stops while the guide explains the ice. Walking in crampons takes a few minutes to learn: keep your feet a little apart and stamp each step flat.</p>
<p>Longer tours of five hours or more go higher and steeper, and ice-climbing add-ons need good upper-body strength. A Hvannadalshnúkur summit climb is a different level: around 15 hours, mostly on snow and ice, for fit hikers only.</p>
<h2>What should you wear for a glacier hike?</h2>
<p>Dress in layers and expect wind, even on a sunny day.</p>
<ul>
<li>Stiff, waterproof hiking boots with ankle support. Trainers will not take crampons; most operators rent boots.</li>
<li>Waterproof jacket and trousers.</li>
<li>A warm mid-layer of wool or fleece, and a thermal base layer in winter.</li>
<li>Hat, gloves and sunglasses. The ice reflects strong light, even under cloud.</li>
<li>A small backpack with water and a snack.</li>
</ul>
<p>The operator provides crampons, a harness, a helmet and an ice axe.</p>
<h2>When is the best time for a glacier hike?</h2>
<p>You can hike both glaciers all year. Summer brings long days, dry ice and grey-white surfaces with dark ash bands. Winter can bring fresh snow, bluer ice and the chance to combine a hike with an ice cave near Skaftafell or Jökulsárlón.</p>
<p>Weather decides more than the season. Tours are cancelled in strong wind and heavy rain, so book your hike early in your stay in the area to leave room for a second try. Check the forecast on vedur.is and alerts on safetravel.is before you set off.</p>
<h2>Sólheimajökull or Skaftafell: which should you book?</h2>
<p>Book Sólheimajökull if you have a short trip, no car, or are only driving as far as Vík. Book Falljökull at Skaftafell if you are driving the Ring Road or staying near the glacier lagoons, and want quieter, more dramatic ice. If you have time, a hike at Skaftafell combined with Jökulsárlón the next morning makes an excellent pair of days.</p>
<p>For the bigger picture, read our <a href="/blog/glaciers-in-iceland">guide to Iceland's glaciers</a>. See the <a href="/places/solheimajokull">Sólheimajökull</a>, <a href="/places/skaftafell">Skaftafell</a> and <a href="/places/glacier-hikes">glacier hikes</a> pages for photos, and our <a href="/blog/iceland-ice-caves">ice cave guide</a> for winter add-ons.</p>
""",
        "checked_note": "Facts checked October 2026. Glacier edges, access routes and tour availability change through the year, and Sólheimajökull has had hazard warnings since July 2026. Check the operator, safetravel.is and vedur.is before your hike.",
        "sources": [
            ("Increased hazard at the margin of Sólheimajökull glacier (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/increased-hazard-due-to-changing-conditions-at-the-margin-of-solheimajokull-glacier"),
            ("Officials agree on new warnings for Sólheimajökull visitors (Iceland Review)", "https://www.icelandreview.com/news/officials-and-agree-on-new-warnings-for-solheimajokull-visitors/"),
            ("Helicopter rescue at Sólheimajökull (Iceland Review)", "https://www.icelandreview.com/news/nature-travel/solheimajokull-helicopter-rescue-glacier-safety/"),
            ("Sólheimajökull glacier (Go Car Rental)", "https://www.gocarrental.is/nature/glaciers/solheimajokull-glacier/"),
            ("Easy glacier hike on Sólheimajökull (Guide to Iceland)", "https://guidetoiceland.is/book-holiday-trips/glacier-discovery-1"),
            ("Easy glacier hiking tour in Skaftafell (Guide to Iceland)", "https://guidetoiceland.is/book-holiday-trips/glacier-wonders-hike-iceland"),
            ("Skaftafell (Wikipedia)", "https://en.wikipedia.org/wiki/Skaftafell"),
            ("Pay for parking at Skaftafell (Parka)", "https://parka.is/pay/skaftafell/"),
        ],
    },
    # ------------------------------------------------------------------
    # 5. VATNAJÖKULL NATIONAL PARK
    # ------------------------------------------------------------------
    {
        "slug": "vatnajokull-national-park",
        "cluster": "glaciers",
        "pillar": False,
        "short": "Vatnajökull National Park: A First-Timer's Guide",
        "title": "Vatnajökull National Park: A First-Timer's Guide (2027)",
        "description": "Vatnajökull National Park for first-timers: what is in it, where to go first, Skaftafell trails, Jökulsárlón, visitor centres, parking fees and the best season.",
        "category": "Glaciers · National parks",
        "teaser": "Iceland's largest park, and the parts first-time visitors should see.",
        "image": "hx-vatnajokull",
        "image_alt": "A glacier spilling from cloud-covered mountains above golden grassland",
        "stats": [
            ("14,967 km²", "Area of the park, about 14% of Iceland"),
            ("2008", "Year the park was founded, on 7 June"),
            ("2019", "Year it became a UNESCO World Heritage Site"),
            ("5.8 km", "Svartifoss loop trail from the Skaftafell visitor centre"),
        ],
        "body": """
<p>Vatnajökull National Park covers about 14% of Iceland, from the ice cap itself to the canyons of the north and the lava fields of the west. For a first visit, focus on the south: Skaftafell for hiking and guided glacier walks, and Fjallsárlón and Jökulsárlón for the glacier lagoons, all on the Ring Road. This guide explains what is in the park, where to start, what it costs and when to go.</p>
<!--TOC-->
<h2>What is Vatnajökull National Park?</h2>
<p>It is Iceland's largest protected area, about 14,967 km², centred on the Vatnajökull ice cap. The park was founded on 7 June 2008, when the older Skaftafell and Jökulsárgljúfur national parks were joined with the ice cap and the land around it. It became a UNESCO World Heritage Site on 5 July 2019, recognised for the geological variety created by the interplay of volcanoes and ice.</p>
<p>The ice cap covers about 7,720 km². The World Heritage area has ten central volcanoes, eight of them under the ice, including Grímsvötn and Bárðarbunga. Hvannadalshnúkur, on the rim of Öræfajökull, is Iceland's highest peak at about 2,110 m. The park is run by the Nature Conservation Agency of Iceland.</p>
<h2>What are the main areas of the park?</h2>
<p>The park is divided into four territories. Only the southern one is on the Ring Road for its whole length.</p>
<div class="table-wrap"><table>
<thead><tr><th>Territory</th><th>Highlights</th><th>Access</th></tr></thead>
<tbody>
<tr><td>South</td><td>Skaftafell, Svartifoss, Falljökull, Fjallsárlón, Jökulsárlón, the Lón area</td><td>Route 1, all year</td></tr>
<tr><td>North</td><td>Ásbyrgi, Jökulsárgljúfur canyon, Dettifoss, Askja</td><td>Paved roads to the canyon; Askja by highland road in summer</td></tr>
<tr><td>East</td><td>Snæfell area, Kverkfjöll</td><td>Highland roads in summer</td></tr>
<tr><td>West</td><td>Laki craters, Langisjór</td><td>Highland roads in summer</td></tr>
</tbody></table></div>
<p>The north, east and west need a 4x4 and summer conditions for most sights, apart from Ásbyrgi and the Jökulsárgljúfur canyon. First-timers get by far the most from the southern territory.</p>
""" + _map(
            "Map of Iceland's glaciers, with Vatnajökull, its lagoons and the main glacier-hike and ice-cave areas",
            "Vatnajökull and the southeast glacier lagoons, with the main glacier-hike and ice-cave areas.",
        ) + """
<h2>Where should first-timers go in Vatnajökull National Park?</h2>
<p>Start at Skaftafell and work east along Route 1 to Jökulsárlón. In one or two days you can walk to a waterfall, stand at a glacier front, join a guided hike and see the lagoons.</p>
<ol>
<li><strong><a href="/places/skaftafell">Skaftafell</a>:</strong> 325 km from Reykjavík. Walk to Svartifoss and the Skaftafellsjökull viewpoint, or join a guided hike on Falljökull.</li>
<li><strong><a href="/places/fjallsarlon">Fjallsárlón</a>:</strong> a short walk from the car park to a lagoon right under the steep Fjallsjökull glacier, with Zodiac tours from spring to autumn.</li>
<li><strong><a href="/places/jokulsarlon">Jökulsárlón</a> and Diamond Beach:</strong> about 10 km further east, the park's most famous sight, with boat tours in summer and ice caves in winter.</li>
<li><strong>Höfn:</strong> about 80 km east of Jökulsárlón, the nearest town with full services and a good base for the eastern part of the park.</li>
</ol>
<p>Our <a href="/blog/jokulsarlon-diamond-beach-guide">Jökulsárlón and Diamond Beach guide</a> has parking, boat tours and safety details for the lagoon.</p>
<h2>What are the best walks at Skaftafell?</h2>
<p>The best first walk is the trail to Svartifoss, the waterfall framed by black basalt columns. It is about 1.5 km each way from the visitor centre, with a climb of about 140 m, and takes about 45 minutes up. These are the main marked trails, from the park's own trail information.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trail</th><th>Distance</th><th>Time</th><th>Level</th></tr></thead>
<tbody>
<tr><td>Svartifoss and back</td><td>About 3 km return</td><td>About 1.5 h</td><td>Easy, some climbing</td></tr>
<tr><td>S2 Svartifoss – Sjónarsker – Sel (loop)</td><td>5.8 km</td><td>2 h</td><td>Easy</td></tr>
<tr><td>Skaftafellsjökull viewpoint</td><td>About 3.6 km return</td><td>About 1 h</td><td>Easy, mostly flat</td></tr>
<tr><td>S6 Svartifoss – Sjónarnípa</td><td>7.1 km</td><td>2.5–3 h</td><td>Challenging</td></tr>
<tr><td>S3 Skaftafellsheiði (loop)</td><td>16.6 km</td><td>5–6 h</td><td>Challenging</td></tr>
<tr><td>S4 Kristínartindar</td><td>18 km</td><td>6–8 h</td><td>Difficult</td></tr>
</tbody></table></div>
<p>The S2 loop passes Svartifoss, the Sjónarsker viewpoint and the old turf farm at Sel. Sjónarnípa looks straight down onto Skaftafellsjökull. Kristínartindar, at 1,126 m, is the big day hike, with views across the ice cap and the sand plains. The paths have steps that get slippery when wet or icy, so wear proper boots, and in winter carry microspikes.</p>
<h2>Where are the visitor centres?</h2>
<p>The main visitor centre for the south is Skaftafellsstofa at Skaftafell, open all year. It has information, toilets and the start of the main trails, and most guided glacier hikes meet nearby. In the north, the visitor centre at Ásbyrgi opens from May to September, as does Skriðuklaustur in the east. The park also runs a centre at Kirkjubæjarklaustur, and there are information points in Höfn and elsewhere around the ice cap.</p>
<h2>How much does it cost to visit?</h2>
<p>Entry to the park is free, but you pay a parking fee at the busiest sites. At Skaftafell a standard car pays about ISK 1,110 in 2026, plus a small transaction fee, and larger vehicles pay more. Jökulsárlón charges about ISK 1,000 for a car. You pay with the Parka app or website, cameras read your number plate, and the fee covers the rest of that day.</p>
<p>If you pay the full fee at one of the two sites and visit the other the same day with the same payment method, the second is half price. Camping at Skaftafell costs about ISK 1,500 per person per night, with showers, toilets and cooking facilities.</p>
<p class="callout"><strong>Stay on the marked trails, and go onto the ice only with a guide.</strong> Glacier fronts, lagoon edges and ice caves inside the park change daily, and some are closed when unsafe. Check safetravel.is and vedur.is before you set out.</p>
<h2>What can you do in the park in each season?</h2>
<p>The southern part of the park is open all year, but what you can do changes with the light and the ice.</p>
<ul>
<li><strong>Summer (June to August):</strong> long days for the Skaftafell trails, boat tours on Jökulsárlón and Fjallsárlón, guided glacier hikes, and highland roads open to Askja and Laki.</li>
<li><strong>Autumn (September to October):</strong> fewer people, autumn colours in the birch woods at Skaftafell, the last boat tours and the first dark nights for the <a href="/northern-lights">northern lights</a>.</li>
<li><strong>Winter (November to March):</strong> natural ice caves on guided tours, the most ice on Diamond Beach, short days and the chance of storms. See our <a href="/blog/iceland-ice-caves">ice cave guide</a>.</li>
<li><strong>Spring (April to May):</strong> longer days return, boat tours start again, and the park is still quiet.</li>
</ul>
<h2>How many days do you need?</h2>
<p>Give the southern part of the park at least two nights. Spend one day at Skaftafell with a walk to Svartifoss and a glacier hike, and the next at Fjallsárlón and Jökulsárlón with a boat tour or, in winter, an ice cave. With a third day, add the Skaftafellsheiði loop or the drive to Höfn and the mountains at <a href="/places/vestrahorn">Vestrahorn</a>.</p>
<p>Accommodation is limited between Kirkjubæjarklaustur and Höfn, so book early, especially for summer. Our guide to <a href="/blog/glaciers-in-iceland">Iceland's glaciers</a> has a three-day south coast plan, and our <a href="/blog/glacier-hiking-iceland">glacier hiking guide</a> helps you choose a tour. For photos, see our <a href="/places/vatnajokull">Vatnajökull</a> page.</p>
""",
        "checked_note": "Facts checked October 2026. Parking fees, visitor centre hours and trail conditions change; check the park website and Parka before you go. Highland roads in the north, east and west open only in summer.",
        "sources": [
            ("Vatnajökull National Park (Wikipedia)", "https://en.wikipedia.org/wiki/Vatnaj%C3%B6kull_National_Park"),
            ("Vatnajökull National Park added to UNESCO's World Heritage List (Government of Iceland)", "https://government.is/news/article/2019/07/10/Vatnajokull-National-Park-added-to-UNESCOs-World-Heritage-List"),
            ("S2 Svartifoss – Sjónarsker – Sel trail (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/svartifoss-sjonarsker-sel-s2"),
            ("Visit Jökulsárlón or Skaftafell: area fees (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/news/visit-jokulsarlon-or-skaftafell"),
            ("Pay for parking at Skaftafell (Parka)", "https://parka.is/pay/skaftafell/"),
            ("A hiker's guide to Skaftafell (isnet.is)", "https://isnet.is/iceland/south-iceland/skaftafell/"),
            ("Skaftafell (Icelandia)", "https://www.icelandia.com/attractions/skaftafell"),
            ("List of glaciers in Iceland (Wikipedia)", "https://en.wikipedia.org/wiki/List_of_glaciers_in_Iceland"),
        ],
    },
    # ------------------------------------------------------------------
    # 6. GLACIER LAGOONS BEYOND JÖKULSÁRLÓN
    # ------------------------------------------------------------------
    {
        "slug": "glacier-lagoons-iceland",
        "cluster": "glaciers",
        "pillar": False,
        "short": "Fjallsárlón and Iceland's Other Glacier Lagoons",
        "title": "Fjallsárlón Glacier Lagoon and Iceland's Other Ice Lagoons (2027)",
        "description": "Fjallsárlón glacier lagoon and the quieter lagoons beyond Jökulsárlón: Breiðárlón, Heinabergslón and Sólheimajökull compared, with access, tours and safety.",
        "category": "Glaciers · South Coast",
        "teaser": "Fjallsárlón, Breiðárlón and Heinabergslón: quieter ice, closer to the glacier.",
        "image": "hx-fjallsarlon",
        "image_alt": "Fjallsárlón glacier lagoon with floating ice below a glacier and blue sky",
        "stats": [
            ("10 km", "Distance from Fjallsárlón to Jökulsárlón along Route 1"),
            ("~45 min", "Time on the water on a Fjallsárlón Zodiac tour"),
            ("~3 km", "Rough track from Route 1 to Breiðárlón"),
            ("Jun–Sep", "Guided kayak season on Heinabergslón"),
        ],
        "body": """
<p>Fjallsárlón glacier lagoon is the best alternative to Jökulsárlón. It lies 10 km to the west on Route 1, it is smaller and quieter, and the glacier wall rises right at the far side of the water. Further off the main road, Breiðárlón and Heinabergslón are wilder still. This guide compares the south coast's glacier lagoons beyond Jökulsárlón, how to reach them and what you can do at each.</p>
<!--TOC-->
<h2>Which glacier lagoons are there besides Jökulsárlón?</h2>
<p>The main ones are Fjallsárlón, Breiðárlón and Heinabergslón, all fed by outlet glaciers of Vatnajökull, plus the young lagoon at Sólheimajökull further west. They are all free to visit, but they differ a lot in access and facilities.</p>
<div class="table-wrap"><table>
<thead><tr><th>Lagoon</th><th>Glacier</th><th>Access</th><th>Facilities</th><th>Tours</th></tr></thead>
<tbody>
<tr><td>Fjallsárlón</td><td>Fjallsjökull</td><td>Short road off Route 1; short walk</td><td>Toilets, café and restaurant</td><td>Zodiac, about April to November</td></tr>
<tr><td>Breiðárlón</td><td>Breiðamerkurjökull</td><td>About 3 km rough track; 4x4 or high clearance advised</td><td>None</td><td>None scheduled</td></tr>
<tr><td>Heinabergslón</td><td>Heinabergsjökull</td><td>Gravel road, about 15 min off Route 1</td><td>Few or none</td><td>Kayaking, June to September</td></tr>
<tr><td>Sólheimajökull lagoon</td><td>Sólheimajökull</td><td>Car park trail, about 15–20 min</td><td>Paid car park</td><td>Glacier hikes only</td></tr>
</tbody></table></div>
<h2>What is Fjallsárlón like?</h2>
<p>Fjallsárlón is a glacier lagoon at the foot of Fjallsjökull, a steep, heavily crevassed outlet of Vatnajökull. Icebergs float close to the shore, and the glacier front is near enough that you can sometimes hear ice break off. The lagoon has grown a great deal since the 1940s as the glacier has retreated, and it is still growing.</p>
<p>It is about 47 km east of Skaftafell and 10 km west of Jökulsárlón, about 4.5 to 5 hours' drive from Reykjavík. From the car park, a short walk over the moraine brings you to the shore. There are toilets and the Frost restaurant by the car park, but no fuel or shop. Fewer tour buses stop here than at Jökulsárlón, so it is usually much quieter.</p>
<p>A Zodiac tour is the way to get close to the glacier wall. Tours run from about April to November, last 75 to 90 minutes in total with about 45 minutes on the water, and accept children from 5. They cost from about US$93 per adult in 2026. Meet at the tour reception behind the Frost restaurant, and book ahead in summer.</p>
""" + _map(
            "Map of Iceland's glaciers and glacier lagoons, including Fjallsárlón, Jökulsárlón and the lagoons near Höfn",
            "The southeast glacier lagoons along Route 1, from Skaftafell to Höfn.",
        ) + """
<h2>How does Fjallsárlón compare with Jökulsárlón?</h2>
<p>Fjallsárlón is smaller, closer to its glacier and much calmer. Jökulsárlón is bigger, has more facilities and has Diamond Beach across the road. If you have time, see both: they are only about 12 minutes apart.</p>
<ul>
<li><strong>Choose Fjallsárlón</strong> for a close view of the glacier front, fewer people and a quieter Zodiac trip.</li>
<li><strong>Choose Jökulsárlón</strong> for the amphibian boat, seals at the lagoon mouth, ice on Diamond Beach and winter ice caves.</li>
</ul>
<p>Our <a href="/blog/jokulsarlon-diamond-beach-guide">Jökulsárlón and Diamond Beach guide</a> covers the bigger lagoon, its parking fee and its boat tours.</p>
<h2>How do you get to Breiðárlón?</h2>
<p>Breiðárlón lies between Fjallsárlón and Jökulsárlón, in front of Breiðamerkurjökull, and is reached by a rough track of about 3 km off Route 1. Expect ruts and deep puddles. A 4x4 or a car with good clearance is advisable, and small two-wheel-drive cars should not try it in ice or heavy rain. You can also walk in along the track, or hike across the moraines from the Fjallsárlón side. The Breiðá river drains from Breiðárlón into Fjallsárlón.</p>
<p>There are no facilities, no marked car park and no scheduled boat tours, so most visitors have the lagoon almost to themselves. The nearest toilets and cafés are at Fjallsárlón and Jökulsárlón. Check your rental terms before driving the track, keep to it, and turn back if it looks worse than your car can handle. Driving off marked tracks is illegal in Iceland.</p>
<h2>What is Heinabergslón like?</h2>
<p>Heinabergslón is a lagoon in front of Heinabergsjökull, another outlet of Vatnajökull, about 30 minutes from Höfn. Turn off Route 1 about 1.5 km after the Kolgríma river bridge, at a small sign for Heinabergsjökull, and follow the gravel road for about 15 minutes to a car park in front of the glacier.</p>
<p>It is best known for guided kayak trips, which run from June to September, take about three hours and go out twice a day. Paddling among the icebergs below the glacier is one of the quietest ways to see the ice in Iceland. Only paddle with a guide: the water is close to freezing, and icebergs can roll without warning.</p>
<h2>What about the lagoon at Sólheimajökull?</h2>
<p>At Sólheimajökull, about 2.5 hours from Reykjavík, a lagoon has been forming in front of the glacier since around 2011 and is about 60 m deep in places. It sits between the car park trail and the ice, and is the main reason the way onto the glacier keeps changing.</p>
<p>In July 2026 the Icelandic Met Office warned that a new lagoon had thinned the ice ridge used to reach the glacier, with deep lagoons on either side and a risk of rockfall above the path. Enjoy the view from the trail, and go onto the ice only on a guided hike. Our <a href="/blog/glacier-hiking-iceland">glacier hiking guide</a> explains the options.</p>
<p class="callout"><strong>Keep off the ice and out of the water.</strong> Do not climb onto icebergs, stranded ice or the glacier front, and do not swim or paddle in any lagoon without a guide. Calving ice can send waves across the water.</p>
<h2>Which lagoon should you visit?</h2>
<p>If you only have time for one stop besides Jökulsárlón, make it Fjallsárlón. It is right on the Ring Road, needs only a short walk, and gives you the closest easy view of a glacier front in the area.</p>
<ul>
<li><strong>Short on time:</strong> Fjallsárlón and Jökulsárlón together, in about three hours.</li>
<li><strong>Want solitude:</strong> Breiðárlón, if your car and the track conditions allow.</li>
<li><strong>Staying in Höfn in summer:</strong> a kayak trip on Heinabergslón.</li>
<li><strong>Coming from Reykjavík for the day:</strong> the Sólheimajökull lagoon from the viewpoint trail, with a guided hike.</li>
</ul>
<h2>What should you bring to the glacier lagoons?</h2>
<p>Bring warm, windproof layers, because cold air drains off the glaciers and the lagoon shores are often much colder than the road. Waterproof boots help on the wet moraine paths at Fjallsárlón and Breiðárlón. Carry food and water for the quieter lagoons, which have no café, and fill the tank before you set off, as there is no fuel at the lagoons themselves. A pair of binoculars is useful for watching the glacier fronts from a safe distance.</p>
<h2>When is the best time to visit the glacier lagoons?</h2>
<p>The lagoons are open all year. Summer gives long days, boat and kayak tours and easier roads. In winter, the lagoons can partly freeze, the tracks to Breiðárlón and Heinabergslón may be icy or impassable, and days are short, but you may see the northern lights over the ice. Early morning is the calmest and quietest time at any season. Check road.is and vedur.is before driving any gravel road.</p>
<p>For the wider picture, read our <a href="/blog/glaciers-in-iceland">guide to Iceland's glaciers</a> and the <a href="/blog/vatnajokull-national-park">Vatnajökull National Park guide</a>. See the <a href="/places/fjallsarlon">Fjallsárlón</a> and <a href="/places/breidamerkurjokull">Breiðamerkurjökull</a> pages for photos.</p>
""",
        "checked_note": "Facts checked October 2026. Lagoon shores, tracks and tour seasons change every year as the glaciers retreat. Check road.is before driving to Breiðárlón or Heinabergslón, and confirm tour dates with the operators.",
        "sources": [
            ("Fjallsárlón Zodiac boat tour (Arctic Adventures)", "https://adventures.is/iceland/day-tours/glacier-tours/glacier-tours-on-vatnajokull/fjallsarlon-zodiac-boat-tour/"),
            ("Fjallsárlón glacier lagoon (Go Car Rental)", "https://www.gocarrental.is/nature/glaciers/fjallsarlon/"),
            ("Jökulsárlón vs Fjallsárlón (isnet.is)", "https://isnet.is/compare/jokulsarlon-vs-fjallsarlon/"),
            ("Breiðárlón glacier lagoon (Iceland Travel Guide)", "https://icelandtravelguide.is/locations/breidarlon-glacier-lagoon"),
            ("Heinabergslón (Adventures.com)", "https://adventures.com/iceland/attractions/glaciers/heinabergslon"),
            ("Sólheimajökull glacier (Go Car Rental)", "https://www.gocarrental.is/nature/glaciers/solheimajokull-glacier/"),
            ("Increased hazard at the margin of Sólheimajökull glacier (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/increased-hazard-due-to-changing-conditions-at-the-margin-of-solheimajokull-glacier"),
        ],
    },
]
