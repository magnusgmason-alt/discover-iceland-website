"""Volcanoes cluster: journal articles (module articles_c7)."""

MAP_VOLCANOES = '<figure class="a-figure a-map"><a href="/assets/img/map-volcanoes-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-volcanoes-1800.jpg" srcset="/assets/img/map-volcanoes-800.jpg 800w, /assets/img/map-volcanoes-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="ALT" loading="lazy" decoding="async"></a><figcaption>CAPTION Tap to open full size.</figcaption></figure>'


def _map(alt, caption):
    return MAP_VOLCANOES.replace("ALT", alt).replace("CAPTION", caption)


ARTICLES = [
    {
        "slug": "volcanoes-in-iceland",
        "cluster": "volcanoes",
        "pillar": True,
        "short": "Iceland's Volcanoes: A Visitor's Map and Guide",
        "title": "Volcanoes in Iceland: A Visitor's Map and Guide to 17 Volcanoes (2027)",
        "description": "Volcanoes in Iceland on one map: Reykjanes, Hekla, Katla, Eyjafjallajökull, Askja, Krafla and more, with what you can visit, the latest status and safety tips.",
        "category": "Nature · Volcanoes",
        "teaser": "Seventeen volcanoes on one map, and which ones you can actually visit.",
        "image": "hx-crater-lakes",
        "image_alt": "A blue crater lake beside a moss-green mountain",
        "stats": [
            ("~30", "Active volcanic systems in Iceland"),
            ("~1/3", "Iceland's share of the world's lava output over the last 500 years"),
            ("12", "Eruptions on the Reykjanes Peninsula since March 2021"),
            ("2,110 m", "Öræfajökull, Iceland's highest volcano"),
        ],
        "body": """
<p>Iceland has around 30 active volcanic systems, and you can visit more of them than you might expect. You can hike to young lava fields near Reykjavík, ride a lift 120 m down into a dormant magma chamber, walk the rim of a tephra crater at Mývatn and drive past the glacier volcano that grounded Europe's planes in 2010. This guide maps 17 volcanoes, explains what each is known for and tells you which ones you can see, and how.</p>
<p>As of mid-October 2026 no eruption is under way in Iceland. Magma is still building up under Svartsengi on the Reykjanes Peninsula, so another eruption there is likely. Check the Icelandic Met Office at vedur.is and SafeTravel at safetravel.is before you go.</p>
<!--TOC-->
<h2>How many volcanoes are there in Iceland?</h2>
<p>Iceland has around 30 active volcanic systems. A volcanic system is a family of craters, fissures and often a central volcano that share the same magma supply, so the number of individual peaks and craters is far higher. Over the last 500 years Iceland's volcanoes have produced about a third of all the lava erupted on Earth.</p>
<p>The reason is geology. Iceland sits on the Mid-Atlantic Ridge, where the North American and Eurasian plates pull apart, and above a hotspot that feeds extra magma from deep below. The plate boundary runs across the island from the Reykjanes Peninsula in the south-west to Krafla in the north-east. You can see the rift itself at <a href="/places/thingvellir">Þingvellir</a>, where the ground has cracked open into long fissures.</p>
""" + _map(
            "Map of Iceland with 17 numbered volcanoes, from the Reykjanes Peninsula to Krafla and Hverfjall",
            "Seventeen of Iceland's best-known volcanoes, numbered from the Reykjanes Peninsula in the south-west to Hverfjall near Mývatn.",
        ) + """
<h2>Which volcanoes are on the map, and can you visit them?</h2>
<p>All 17 volcanoes on the map can be seen in some way, but only a few can be walked on or into. The table follows the map's numbers. Heights and dates are for the volcano or its best-known eruption.</p>
<div class="table-wrap"><table>
<thead><tr><th>#</th><th>Volcano</th><th>Known for</th><th>How visitors see it</th></tr></thead>
<tbody>
<tr><td>1</td><td>Reykjanes Peninsula</td><td>12 eruptions since 2021</td><td>Marked trails to the Fagradalsfjall lava fields</td></tr>
<tr><td>2</td><td>Þríhnúkagígur</td><td>Dormant magma chamber, about 120 m deep</td><td>Guided tour with a lift into the crater, May to October</td></tr>
<tr><td>3</td><td>Snæfellsjökull</td><td>Glacier-capped volcano, 1,446 m</td><td>From the roads around Snæfellsnes</td></tr>
<tr><td>4</td><td>Hekla</td><td>Iceland's most famous volcano, last erupted 2000</td><td>From the south, or a summer hike in settled conditions</td></tr>
<tr><td>5</td><td>Eyjafjallajökull</td><td>The 2010 ash cloud</td><td>From the Ring Road on the south coast</td></tr>
<tr><td>6</td><td>Katla</td><td>Under Mýrdalsjökull, last major eruption 1918</td><td>Glacier hikes on Sólheimajökull, its outlet glacier</td></tr>
<tr><td>7</td><td>Eldfell</td><td>Heimaey eruption, 1973</td><td>A short climb on Heimaey, Westman Islands</td></tr>
<tr><td>8</td><td>Surtsey</td><td>New island, 1963–67</td><td>Only from a boat or plane; landing is for scientists</td></tr>
<tr><td>9</td><td>Laki craters</td><td>The 1783–84 fissure eruption</td><td>Summer only, by 4x4 or highland tour</td></tr>
<tr><td>10</td><td>Öræfajökull</td><td>Highest volcano, 2,110 m; erupted 1727</td><td>From Skaftafell and the Ring Road</td></tr>
<tr><td>11</td><td>Grímsvötn</td><td>Under Vatnajökull, erupted 2011</td><td>Not accessible; under the ice cap</td></tr>
<tr><td>12</td><td>Bárðarbunga</td><td>Under Vatnajökull, 2014–15 unrest</td><td>Not accessible; under the ice cap</td></tr>
<tr><td>13</td><td>Holuhraun</td><td>Lava field from 2014–15</td><td>Highland tours in summer</td></tr>
<tr><td>14</td><td>Askja</td><td>Last erupted 1961, Víti crater</td><td>Summer only, by 4x4 or highland tour</td></tr>
<tr><td>15</td><td>Herðubreið</td><td>Table mountain, 1,682 m</td><td>Seen on the way to Askja</td></tr>
<tr><td>16</td><td>Krafla</td><td>The Krafla Fires, 1975–84</td><td>Paved road from Mývatn; walking trails</td></tr>
<tr><td>17</td><td>Hverfjall</td><td>Tephra ring crater</td><td>Short, steep path to the rim</td></tr>
</tbody></table></div>
<h2>Is a volcano erupting in Iceland right now?</h2>
<p>No. As of mid-October 2026 there is no eruption in Iceland. The most recent one was on the Sundhnúkur crater row near Grindavík, from 16 July to 5 August 2025.</p>
<p>That does not mean the Reykjanes Peninsula is quiet. On 30 September 2026 the Icelandic Met Office said the ground at Svartsengi was still rising slowly, by about 4 cm over three months, and that the most likely next step is a new magma intrusion towards the Sundhnúkur crater row, possibly ending in an eruption. Its August 2026 estimate put the magma stored under Svartsengi at about 29 million m³. The Reykjanes-Svartsengi system was at alert level 2, orange.</p>
<p>Elsewhere, the Met Office reported on 14 August 2026 that the uplift at Askja, under way since 2021, had stopped. Our <a href="/blog/reykjanes-volcano-guide">Reykjanes volcano guide</a> has the full timeline and what you can visit there.</p>
<h2>Which volcanoes can you visit near Reykjavík?</h2>
<p>Two of the most rewarding volcano experiences in Iceland are within an hour or so of the capital.</p>
<h3>The Reykjanes Peninsula (1)</h3>
<p>After about 800 years without an eruption, the Reykjanes Peninsula came alive in March 2021. Three eruptions at Fagradalsfjall in 2021, 2022 and 2023 were followed by nine on the Sundhnúkur crater row between December 2023 and August 2025. Marked hiking trails lead from paid car parks to viewpoints over the new lava, which is now the easiest place in Iceland to stand next to lava that is only a few years old.</p>
<p>Never walk on the new lava. It can stay hot for years under a thin crust. Closures change at short notice, and the town of Grindavík still sits inside the hazard zone.</p>
<h3>Þríhnúkagígur (2)</h3>
<p>In the Bláfjöll hills, about 20 km south-east of Reykjavík, Þríhnúkagígur is a volcano that last erupted about 4,500 years ago. Its magma drained away rather than hardening, which left a huge empty chamber. A guided tour lowers you about 120 m into it in an open lift. Tours run from May to October; see our guide to <a href="/blog/lava-tunnel-thrihnukagigur">lava tunnels and Þríhnúkagígur</a> for prices and the year-round lava caves nearby.</p>
<h2>What are the famous volcanoes of the south coast?</h2>
<p>Hekla, Eyjafjallajökull and Katla are the volcanoes most people have heard of, and all three sit close to the south coast route.</p>
<ul>
<li><strong>Hekla (4)</strong>, 1,491 m, has erupted 23 times in the last thousand years, most recently in February 2000. In the Middle Ages it was known across Europe as a gateway to hell.</li>
<li><strong>Eyjafjallajökull (5)</strong>, 1,666 m, is the glacier volcano above Seljalandsfoss whose 2010 ash cloud closed most of Europe's airspace for several days.</li>
<li><strong>Katla (6)</strong> lies under the Mýrdalsjökull ice cap. It usually erupts every 40 to 80 years, and its last major eruption was in 1918.</li>
</ul>
<p>You see Eyjafjallajökull from the Ring Road as you pass Seljalandsfoss. The guided glacier walks on Sólheimajökull take you onto an outlet glacier of Katla's ice cap, with dark bands of old ash in the ice. Our guide to <a href="/blog/hekla-katla-eyjafjallajokull">Hekla, Katla and Eyjafjallajökull</a> explains each one, including how to say the names.</p>
<h3>Eldfell and Surtsey (7, 8)</h3>
<p>Off the south coast, the Westman Islands have two of the most famous eruptions of the 20th century. In January 1973 a fissure opened on Heimaey, the only inhabited island, and built the cone of Eldfell. About 5,300 people were evacuated by fishing boat within a few hours. Today you can climb Eldfell from the town and look down on the lava that nearly closed the harbour.</p>
<p>Surtsey rose from the sea in an eruption that broke the surface on 14 November 1963 and ended on 5 June 1967. It is a UNESCO World Heritage Site, and only a few scientists may land there, so you see it from a boat or a sightseeing flight.</p>
<h2>Which volcanoes are under Vatnajökull?</h2>
<p>The Vatnajökull ice cap covers several active volcanoes. You cannot visit them, but they shape everything around the <a href="/places/vatnajokull">Vatnajökull</a> area.</p>
<ul>
<li><strong>Laki (9)</strong> is a row of craters south-west of the ice cap. Its 1783–84 eruption released about 15 km³ of lava, and the famine and livestock deaths that followed killed roughly a fifth of Iceland's people. The craters can be reached in summer by 4x4 or on a tour.</li>
<li><strong>Öræfajökull (10)</strong> is Iceland's highest volcano at 2,110 m. Its summit, Hvannadalshnúkur, is the country's highest peak, and its slopes rise straight above <a href="/places/skaftafell">Skaftafell</a>. It last erupted in 1727.</li>
<li><strong>Grímsvötn (11)</strong> lies beneath the middle of the ice cap and is one of Iceland's most active volcanoes. Its May 2011 eruption disrupted about 900 flights at first.</li>
<li><strong>Bárðarbunga (12)</strong> fed the Holuhraun eruption of 2014–15 through a dyke more than 40 km long, while its ice-filled caldera sank.</li>
</ul>
<h2>Which volcanoes can you see in the north and the highlands?</h2>
<p>The north-east has the widest range of volcanic landscapes you can walk through. Some are a short drive from Mývatn; others need a summer 4x4 trip into the highlands.</p>
<h3>Holuhraun, Askja and Herðubreið (13, 14, 15)</h3>
<p>Holuhraun is the lava field from Iceland's largest eruption in about 230 years, which ran for around six months from late summer 2014 into early 2015. It lies about 20 km south of Askja.</p>
<p>Askja is a vast caldera in the central highlands. Its eruption in 1875 left the lake Öskjuvatn, which is 220 m deep and Iceland's second-deepest lake. Beside it is Víti, a smaller crater about 2.5 km on foot from the car park. Askja last erupted from 26 October to 5 December 1961. The roads in are F-roads, usually open only from late June to early October, so most visitors join a tour from Mývatn.</p>
<p>On the way you pass Herðubreið, a 1,682 m table mountain. Its flat top and steep sides formed when it erupted under the thick ice of the last ice age.</p>
<h3>Krafla and Hverfjall (16, 17)</h3>
<p>Krafla is a caldera about 10 km across, east of Mývatn. Between 1975 and 1984 it went through the Krafla Fires: nine eruptions and fifteen rounds of uplift and subsidence. Marked paths cross lava from that period, and you can look into Víti, a crater with a green lake. A geothermal power station has used the heat here since 1977.</p>
<p>Hverfjall is a tephra ring crater about 1 km across that formed in an explosive eruption roughly 2,500 years ago. A short, steep path climbs to the rim, and a loop of about 3 km follows it round, with views over Mývatn. A parking fee applies at the main car park.</p>
<h2>Which volcano is in the west of Iceland?</h2>
<p>Snæfellsjökull (3) is a 1,446 m glacier-capped volcano at the tip of the <a href="/places/snaefellsnes">Snæfellsnes</a> peninsula. On a clear day you can see it across the bay from Reykjavík. It is best known as the entrance to the underworld in Jules Verne's novel <em>Journey to the Centre of the Earth</em>. The roads around the peninsula show it from every side, along with lava fields, craters and black beaches.</p>
<h2>What kinds of volcano does Iceland have?</h2>
<p>Iceland has almost every type of volcano, and knowing them helps you read the landscape.</p>
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>What it looks like</th><th>Examples on the map</th></tr></thead>
<tbody>
<tr><td>Fissure eruption</td><td>A long crack with a row of small craters and fountains of lava</td><td>Reykjanes, Laki, Holuhraun, Krafla</td></tr>
<tr><td>Stratovolcano</td><td>A tall, layered cone or ridge built by many eruptions</td><td>Hekla, Snæfellsjökull, Öræfajökull</td></tr>
<tr><td>Subglacial volcano</td><td>Hidden under ice; eruptions melt the ice and cause floods and ash</td><td>Katla, Grímsvötn, Bárðarbunga, Eyjafjallajökull</td></tr>
<tr><td>Table mountain</td><td>Flat-topped, steep-sided mountain formed under an ice sheet</td><td>Herðubreið</td></tr>
<tr><td>Tephra ring</td><td>A wide, low crater of loose ash and rock from an explosive blast</td><td>Hverfjall</td></tr>
<tr><td>Caldera</td><td>A huge hollow where the ground sank after an eruption</td><td>Askja, Krafla, Katla</td></tr>
</tbody></table></div>
<p>The type matters for travel. Fissure eruptions like those on Reykjanes produce lava but little ash, which is why Keflavík Airport has kept operating through the recent eruptions. Eruptions under glaciers are the ones that can send up ash clouds or flood rivers.</p>
<h2>Is it safe to visit Iceland's volcanoes?</h2>
<p>Yes, if you follow closures and stay on marked paths. Iceland's volcanoes are among the most closely monitored in the world, and authorities close roads and areas quickly when the risk rises. The real dangers near an eruption are local:</p>
<ul>
<li><strong>Volcanic gas</strong> is often invisible and can pool in hollows and valleys. Check the gas forecast before you go.</li>
<li><strong>New lava</strong> looks solid long before it is safe. Never step on it.</li>
<li><strong>New fissures</strong> can open with little warning near an active area.</li>
<li><strong>Glacier volcanoes</strong> can melt ice and send floods down rivers. Respect road closures on the south coast.</li>
</ul>
<p>Our <a href="/blog/iceland-volcano-safety">Iceland volcano safety guide</a> covers gas, flights, closures and the official sources to check.</p>
<p class="callout">Before any volcano trip, check three things: the Icelandic Met Office at vedur.is, alerts and closures at safetravel.is, and road conditions at umferdin.is.</p>
<h2>What are the best volcano experiences in Iceland?</h2>
<p>You do not need an eruption to get close to Iceland's volcanoes. These are the most popular ways in, from easy to more committed.</p>
<ol>
<li><strong>Walk to the Reykjanes lava fields.</strong> Marked trails from paid car parks lead to the 2021–23 Fagradalsfjall lava and viewpoints over the Sundhnúkur craters.</li>
<li><strong>Go underground in a lava tunnel.</strong> Raufarhólshellir, about 30 km from Reykjavík, is open all year on guided tours.</li>
<li><strong>Descend into Þríhnúkagígur.</strong> The only tour of its kind, from May to October.</li>
<li><strong>Visit an exhibition.</strong> The LAVA Centre in Hvolsvöllur explains Iceland's volcanoes, including the 2010 Eyjafjallajökull eruption.</li>
<li><strong>Climb Eldfell on Heimaey.</strong> A short climb up a cone that formed in 1973.</li>
<li><strong>Walk at Krafla and Hverfjall.</strong> Lava, craters and steam vents a short drive from Mývatn.</li>
<li><strong>Join a summer highland tour to Askja.</strong> A long day in a 4x4 for the caldera, Víti and Holuhraun.</li>
</ol>
<h2>When is the best time to visit Iceland's volcanoes?</h2>
<p>Summer is the best time for most volcanoes. From late June to early September the highland roads to Askja, Holuhraun and Laki are usually open, the trails are clear of snow and you have long days. See our guide to the <a href="/blog/best-time-to-visit-iceland">best time to visit Iceland</a> for month-by-month weather.</p>
<p>The Reykjanes trails, the lava tunnels near Reykjavík, Krafla and Hverfjall can be visited much of the year, but winter brings ice, snow and very short days. Þríhnúkagígur runs only from May to October. If an eruption starts, tour operators run trips only when authorities allow it, which is often the safest way to see one.</p>
<p>For the wider picture of what to see between volcanoes, our <a href="/highlights">Iceland highlights map</a> shows the main sights, and our printed <a href="/#guides">Complete Guide to Iceland</a> covers the volcanic regions in more depth.</p>
""",
        "checked_note": "Facts checked October 2026. Volcanic activity changes fast, especially on the Reykjanes Peninsula: check vedur.is and safetravel.is before you travel. Highland road opening dates and tour seasons change every year.",
        "sources": [
            ("Situation on the Reykjanes Peninsula, 30 September 2026 (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/ground-uplift-and-magma-accumulation-continue-beneath-svartsengi"),
            ("News (Icelandic Met Office)", "https://en.vedur.is/about-imo/news"),
            ("Volcanism of Iceland (Wikipedia)", "https://en.wikipedia.org/wiki/Volcanism_of_Iceland"),
            ("Askja (Wikipedia)", "https://en.wikipedia.org/wiki/Askja"),
            ("Krafla (Wikipedia)", "https://en.wikipedia.org/wiki/Krafla"),
            ("Surtsey (Wikipedia)", "https://en.wikipedia.org/wiki/Surtsey"),
            ("Reykjanes eruption timeline 2021–2026 (Volcano Express)", "https://www.volcanoexpress.is/articles/the-reykjanes-eruption-timeline-2021-2026"),
            ("How to visit Hverfjall (Laidback Trip)", "https://www.laidbacktrip.com/posts/guide-hverfjall-crater-iceland"),
        ],
    },
    {
        "slug": "reykjanes-volcano-guide",
        "cluster": "volcanoes",
        "pillar": False,
        "short": "Reykjanes Volcano: Eruption Sites and Status",
        "title": "Reykjanes Volcano: Eruption Sites, Hiking Trails and Latest Status (2027)",
        "description": "Reykjanes volcano guide: status as of October 2026, all 12 eruptions since 2021, hiking trails to Fagradalsfjall, parking, Grindavík and the Blue Lagoon.",
        "category": "Nature · Volcanoes",
        "teaser": "Twelve eruptions since 2021, the trails to the lava and what to check first.",
        "image": "hx-geysir",
        "image_alt": "Steam rising from hot springs on a sunny winter day",
        "stats": [
            ("12", "Eruptions on the Reykjanes Peninsula since March 2021"),
            ("9", "Eruptions on the Sundhnúkur crater row, Dec 2023 to Aug 2025"),
            ("5 Aug 2025", "End of the most recent eruption"),
            ("~29 million m³", "Magma stored under Svartsengi, August 2026 estimate"),
        ],
        "body": """
<p>There is no eruption on the Reykjanes Peninsula as of mid-October 2026, but the volcano is far from finished. The Icelandic Met Office said on 30 September 2026 that magma is still building up under Svartsengi and that a new eruption on the Sundhnúkur crater row, near Grindavík, remains the most likely next step. Meanwhile you can hike to the lava fields of the 2021–23 Fagradalsfjall eruptions on marked trails. Here is the timeline, the trails, and what to check before you go.</p>
<!--TOC-->
<h2>Is the Reykjanes volcano erupting now?</h2>
<p>No. As of the Met Office update of 30 September 2026, and travel updates on 12 October 2026, no eruption is under way. The last one ran from 16 July to 5 August 2025 on the Sundhnúkur crater row.</p>
<p>The system is still active, though. The ground at Svartsengi rose by about 4 cm in the three months to the end of September 2026, and the Met Office's August 2026 estimate put the magma stored beneath it at about 29 million m³. The Reykjanes-Svartsengi system was at alert level 2, orange, and the Met Office saw no evidence that the episode is ending. Past eruptions here have started with as little as 20 minutes' warning.</p>
<p class="callout">Status changes fast. Before you go, check the latest update on vedur.is and closures on safetravel.is, even if you read this page the same week.</p>
<h2>How many times has Reykjanes erupted since 2021?</h2>
<p>Twelve times. After about 800 years without an eruption, three eruptions took place in the Fagradalsfjall area between 2021 and 2023. Then activity moved west to the Sundhnúkur crater row, just north of Grindavík, where nine eruptions followed.</p>
<div class="table-wrap"><table>
<thead><tr><th>#</th><th>Eruption</th><th>Dates</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>1</td><td>Fagradalsfjall (Geldingadalir)</td><td>19 Mar – 18 Sep 2021</td><td>First on the peninsula in about 800 years</td></tr>
<tr><td>2</td><td>Meradalir</td><td>3 – 21 Aug 2022</td><td>About three weeks</td></tr>
<tr><td>3</td><td>Litli-Hrútur</td><td>10 Jul – 5 Aug 2023</td><td>Nearly a month</td></tr>
<tr><td>4</td><td>Sundhnúkur</td><td>18 – 21 Dec 2023</td><td>First of the Sundhnúkur series</td></tr>
<tr><td>5</td><td>Sundhnúkur, by Grindavík</td><td>14 – 16 Jan 2024</td><td>Lava destroyed three homes</td></tr>
<tr><td>6</td><td>Sundhnúkur</td><td>8 Feb 2024</td><td>Cut the hot-water pipeline for several days</td></tr>
<tr><td>7</td><td>Sundhnúkur</td><td>16 Mar – 8 May 2024</td><td>Longest, 54 days</td></tr>
<tr><td>8</td><td>Sundhnúkur</td><td>29 May – 22 Jun 2024</td><td>Largest lava field</td></tr>
<tr><td>9</td><td>Sundhnúkur</td><td>22 Aug – 6 Sep 2024</td><td>Furthest north</td></tr>
<tr><td>10</td><td>Sundhnúkur</td><td>20 Nov – 8 Dec 2024</td><td>Lava covered the Blue Lagoon car park</td></tr>
<tr><td>11</td><td>Sundhnúkur</td><td>1 Apr 2025</td><td>Under 24 hours</td></tr>
<tr><td>12</td><td>Sundhnúkur</td><td>16 Jul – 5 Aug 2025</td><td>Most recent eruption</td></tr>
</tbody></table></div>
<p>The February 2024 eruption lasted about two days. Dates are as reported by the Met Office and compiled in our sources; some end dates were declared a day or two after activity stopped.</p>
""" + _map(
            "Map of Iceland's volcanoes with the Reykjanes Peninsula marked as number 1 near Keflavík Airport",
            "The Reykjanes Peninsula (1) sits between Keflavík Airport and Reykjavík, with Þríhnúkagígur (2) to the east.",
        ) + """
<h2>Can you hike to the Reykjanes eruption sites?</h2>
<p>Yes, to the older Fagradalsfjall lava fields and to viewpoints over the Sundhnúkur lava. Visit Reykjanes, the regional tourist board, lists five marked trails from two official car parks: P1 at Geldingadalir and P2 at Stóri-Leirdalur.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trail</th><th>Goes to</th><th>Distance</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>Path A</td><td>2021 and 2022 eruption sites, Fagradalsfjall</td><td>About 6–8 km one way, 2–2.5 h</td><td>Moderate to hard</td></tr>
<tr><td>Path B</td><td>Edge of the Sundhnúkur lava, with views of the craters</td><td>4.7 km (B1) or 6.1 km (B2) one way from P1</td><td>Moderate</td></tr>
<tr><td>Path C</td><td>Langihryggur viewpoint over the 2021–23 lava</td><td>About 4 km one way</td><td>Moderate</td></tr>
<tr><td>Path E</td><td>July 2023 site near Litli-Hrútur</td><td>About 18–20 km return, 5–6 h</td><td>Hard; last 2 km on rough lava</td></tr>
<tr><td>Nátthagi</td><td>Edge of the 2021 lava field</td><td>About 2 km one way</td><td>Easy</td></tr>
</tbody></table></div>
<p>Parking costs ISK 1,000 per car for 24 hours, paid through Parka.is (checked October 2026). Each car park has its own payment link, and unpaid cars get an extra fee. The paths are rough and exposed, so wear hiking boots and windproof, waterproof layers, and take water and food.</p>
<h2>What are the rules at the eruption sites?</h2>
<p>The main rule is simple: never walk on the new lava. Lava that looks solid can still be dangerously hot under a thin crust, and walking on it is not allowed on Paths C and E. The other rules come from the police and SafeTravel:</p>
<ul>
<li><strong>Stay on marked paths</strong> and keep well back from lava edges, which can collapse or start moving again.</li>
<li><strong>Check the gas forecast</strong> before you set off. Volcanic gas can be invisible and odourless, and it collects in valleys and hollows. Keep to ridges, and leave at once if you feel unwell.</li>
<li><strong>Children under 12</strong> are not advised to visit when gas pollution is present. <strong>Leave dogs at home</strong>: gas and fluorine pollution are unsafe for them.</li>
<li><strong>Respect closures.</strong> Police can close the area without notice, and the Sundhnúkur craters themselves are in the restricted zone.</li>
<li><strong>Do not go in bad weather or the dark.</strong> In winter the trails are icy, daylight is short and there are no lights.</li>
</ul>
<h2>Can you visit Grindavík?</h2>
<p>Yes, at the time of writing, but with restrictions that can change at short notice. Grindavík, a fishing town, was evacuated on 10 November 2023 when magma was found running beneath it. Lava destroyed three houses in January 2024, and large earth barriers now protect the town and the Svartsengi power station.</p>
<p>The town reopened to the public on 18 July 2025. The Met Office's hazard assessment of 30 September 2026 kept Grindavík in the "considerable" (orange) hazard category, slightly lowered after cracks in the ground were repaired. A new risk assessment for people inside the barriers was published on 1 October 2026. Fissures and damaged ground remain, so keep to open streets and obey every sign and closure.</p>
<h2>Is the Blue Lagoon open?</h2>
<p>Usually, but it closes during eruptions and when the risk rises. The Blue Lagoon sits at Svartsengi, right beside the eruption zone. It was evacuated during several eruptions in 2024, and lava covered its car park in November 2024. Check the lagoon's own website on the day of your visit, and have a back-up. Our comparison of the <a href="/blog/blue-lagoon-vs-sky-lagoon">Blue Lagoon and Sky Lagoon</a> covers the closest alternative, in <a href="/places/reykjavik">Reykjavík</a>.</p>
<h2>What happens if it erupts while you are in Iceland?</h2>
<p>For most visitors, very little changes. Keflavík Airport, about 20 km from the eruption zone, has kept a normal schedule through every Reykjanes eruption, because these fissure eruptions release lava and gas but little ash.</p>
<p>Close to the eruption, expect road closures around Grindavík and Svartsengi, a closed Blue Lagoon and changing access to the trails. Authorities decide when and where people may watch. If you want to see an active eruption, the safest way is with a licensed tour operator that runs trips only when the area has been cleared. Sign up for SafeTravel's SMS alerts, and follow our <a href="/blog/iceland-volcano-safety">Iceland volcano safety guide</a> for gas, closures and flights.</p>
<h2>How do you plan a visit to the Reykjanes lava fields?</h2>
<ol>
<li><strong>Check the status</strong> on vedur.is and closures on safetravel.is the evening before and the morning of your visit.</li>
<li><strong>Check the weather and gas forecast.</strong> Wind and rain make the trails hard going; wind direction decides where gas drifts.</li>
<li><strong>Pick a trail that fits your time.</strong> Nátthagi or Path C for a short visit, Path A for the classic 2021 craters, Path E for a full day.</li>
<li><strong>Pay for parking</strong> at P1 or P2 through Parka.is.</li>
<li><strong>Combine it with the rest of the peninsula.</strong> Þríhnúkagígur and the Raufarhólshellir lava tunnel are close by; see our <a href="/blog/lava-tunnel-thrihnukagigur">lava tunnel guide</a>.</li>
</ol>
<p>The Reykjanes eruptions are part of the same plate boundary you can see at <a href="/places/thingvellir">Þingvellir</a> on the Golden Circle. For the rest of Iceland's volcanoes, from Hekla to Krafla, see our <a href="/blog/volcanoes-in-iceland">guide to volcanoes in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026, using the Icelandic Met Office update of 30 September 2026 and travel updates to 12 October 2026. Activity on the Reykjanes Peninsula can change within minutes: always check vedur.is and safetravel.is before you go.",
        "sources": [
            ("Situation on the Reykjanes Peninsula, 30 September 2026 (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/ground-uplift-and-magma-accumulation-continue-beneath-svartsengi"),
            ("News (Icelandic Met Office)", "https://en.vedur.is/about-imo/news"),
            ("Iceland volcano 2026 updates (Icelandic Mountain Guides)", "https://www.mountainguides.is/blog/iceland-volcano-2026"),
            ("Reykjanes eruption timeline 2021–2026 (Volcano Express)", "https://www.volcanoexpress.is/articles/the-reykjanes-eruption-timeline-2021-2026"),
            ("Hiking trails to the eruption sites (Visit Reykjanes)", "https://visitreykjanes.is/en/volcano-eruption/hiking-trails"),
            ("Safety information (Visit Reykjanes)", "https://www.visitreykjanes.is/en/volcano-eruption/safety-information/safety-information"),
            ("Grindavík reopens to public following eruption risk review (Iceland Review)", "https://www.icelandreview.com/news/grindavik-reopens-to-public-following-eruption-risk-review/"),
            ("2023–2025 Sundhnúkur eruptions (Wikipedia)", "https://en.wikipedia.org/wiki/2023%E2%80%932025_Sundhn%C3%BAkur_eruptions"),
        ],
    },
    {
        "slug": "iceland-volcano-safety",
        "cluster": "volcanoes",
        "pillar": False,
        "short": "Iceland Volcano Safety: Is It Safe to Visit?",
        "title": "Iceland Volcano Safety: Is It Safe to Visit During an Eruption? (2027)",
        "description": "Iceland volcano safety explained: whether eruptions affect flights, volcanic gas, closures at Grindavík and the Blue Lagoon, glacier floods, and what to check.",
        "category": "Planning · Safety",
        "teaser": "Gas, closures, flights and the official sources to check before you go.",
        "image": "hx-black-ice",
        "image_alt": "A dark, ash-streaked iceberg rising from choppy grey water",
        "stats": [
            ("~20 km", "Keflavík Airport to the Reykjanes eruption zone"),
            ("15–20 Apr", "Main closure of European airspace in 2010"),
            ("Under 12", "Children advised to stay away when volcanic gas is present"),
            ("112", "Emergency number in Iceland"),
        ],
        "body": """
<p>Yes, it is generally safe to visit Iceland during an eruption. The recent eruptions have all been on the Reykjanes Peninsula, they affect a small area near Grindavík, and Keflavík Airport has kept operating throughout. The risks are local: volcanic gas, fresh lava, sudden closures and, for the glacier volcanoes, floods and ash. This guide explains each one and the official sources to check.</p>
<p>As of mid-October 2026 no eruption is under way in Iceland. The Met Office expects another eruption on the Reykjanes Peninsula at some point, so read this before you travel.</p>
<!--TOC-->
<h2>Is it safe to travel to Iceland during an eruption?</h2>
<p>For almost all visitors, yes. The eruptions since 2021 have been fissure eruptions: long cracks that pour out lava and gas but very little ash. Each one has been confined to a few square kilometres of the Reykjanes Peninsula, south-west of Reykjavík. The rest of the country, from the Golden Circle to the glacier lagoons, carries on as normal.</p>
<p>Iceland's volcanoes are monitored around the clock by the Icelandic Met Office. When magma starts to move, the civil protection authorities close roads and evacuate the area, often before the eruption begins. The people who get hurt are usually those who ignore closures or walk onto new lava.</p>
<h2>Will a volcano affect my flight to Iceland?</h2>
<p>Probably not. Keflavík Airport says it has kept a normal schedule throughout the Reykjanes eruptions, even though it is only about 20 km from the eruption zone. These eruptions produce little ash, which is what grounds aircraft.</p>
<p>Ash-rich eruptions under glaciers are different. When Eyjafjallajökull erupted in April 2010, most European airspace closed from 15 to 20 April and about 10 million travellers were affected. The Grímsvötn eruption in May 2011 disrupted about 900 flights at first. That kind of disruption is rare, but it is why travel insurance that covers natural events and flexible bookings is worth having.</p>
<div class="table-wrap"><table>
<thead><tr><th>Type of eruption</th><th>Example</th><th>Main hazard</th><th>Effect on travellers</th></tr></thead>
<tbody>
<tr><td>Fissure eruption on land</td><td>Reykjanes, 2021–25</td><td>Lava, gas</td><td>Local closures; flights normal</td></tr>
<tr><td>Eruption under a glacier</td><td>Eyjafjallajökull 2010, Grímsvötn 2011</td><td>Ash, glacial floods</td><td>Possible flight disruption; road closures</td></tr>
<tr><td>Explosive stratovolcano</td><td>Hekla 2000</td><td>Ash, sudden onset</td><td>Closures in the area; hikers at risk</td></tr>
<tr><td>Highland fissure eruption</td><td>Holuhraun 2014–15</td><td>Gas over wide areas</td><td>Highland closures; air quality alerts</td></tr>
</tbody></table></div>
""" + _map(
            "Map of 17 Icelandic volcanoes, showing the Reykjanes Peninsula near Keflavík and the glacier volcanoes in the south and under Vatnajökull",
            "The Reykjanes Peninsula (1) is the area of recent eruptions. Katla, Eyjafjallajökull and the Vatnajökull volcanoes lie under ice.",
        ) + """
<h2>How dangerous is volcanic gas?</h2>
<p>Volcanic gas is the most underestimated risk near an eruption. Gases such as sulphur dioxide and carbon dioxide can be invisible and odourless, and they collect quickly in valleys and hollows when the wind drops. They can affect you long before you see any lava.</p>
<ul>
<li><strong>Check the gas forecast</strong> on vedur.is and live air quality at loftgaedi.is before visiting an eruption area.</li>
<li><strong>Stay on high ground</strong>, ridges and hills, and keep the wind at your back.</li>
<li><strong>Children under 12</strong> are not advised to visit when gas pollution is present, and visits should be kept to about 15 minutes when levels exceed safety limits.</li>
<li><strong>Leave dogs behind.</strong> The gas and fluorine pollution is unsafe for them.</li>
<li><strong>If you have asthma or a heart or lung condition</strong>, take extra care and stay indoors if you feel symptoms.</li>
<li><strong>Leave at once</strong> if you get a headache, a sore throat or shortness of breath.</li>
</ul>
<p>Gas can also drift to towns far from the eruption. When the Met Office warns of gas pollution in your area, keep windows closed and limit hard exercise outdoors.</p>
<h2>What are the dangers near fresh lava?</h2>
<p>The biggest danger is walking on it. New lava can look solid while it is still molten beneath a thin crust, and that crust can break without warning. Never step on lava from a recent eruption.</p>
<ul>
<li><strong>Lava edges</strong> can collapse or start moving again, so keep well back.</li>
<li><strong>New fissures</strong> can open with little warning near an active area. On Reykjanes, warning times have been as short as about 20 minutes.</li>
<li><strong>Moss fires</strong> can start where lava meets vegetation, adding smoke to the gas.</li>
<li><strong>Weather</strong> is a hazard in its own right. The trails are exposed, and wind, rain and early darkness make them harder than they look.</li>
</ul>
<p class="callout">Stay on marked paths, never cross a closure, and turn back if the gas, weather or light gets worse. Rescue teams are volunteers who come out to people who ignored the same advice.</p>
<h2>What closes during an eruption on Reykjanes?</h2>
<p>Expect closures around the eruption, not across Iceland. During past eruptions the authorities have closed Grindavík and the roads around it, evacuated the Blue Lagoon and changed access to the hiking trails, sometimes within minutes.</p>
<p>Grindavík was evacuated on 10 November 2023 and reopened to the public in July 2025. In its 30 September 2026 assessment the Met Office kept the town in the "considerable" (orange) hazard category. The Blue Lagoon, beside the Svartsengi power station, has closed temporarily during nearby activity. If either is on your plan, check on the day and book with free cancellation. Our <a href="/blog/reykjanes-volcano-guide">Reykjanes volcano guide</a> has the trails, car parks and full eruption timeline.</p>
<h2>What about Katla, Hekla and the glacier volcanoes?</h2>
<p>The volcanoes under ice bring different risks. When they erupt or when geothermal heat melts the ice, they can send sudden floods, called jökulhlaups, down rivers to the coast.</p>
<ul>
<li><strong>Katla</strong>, under Mýrdalsjökull, has not had a major eruption since 1918. A flood in July 2011 destroyed the Ring Road bridge over the Múlakvísl river. In August 2026 another outburst flood in the Múlakvísl came with raised conductivity and gas near the river, and the Met Office reported on 1 September that it was subsiding.</li>
<li><strong>Sólheimajökull</strong>, Katla's outlet glacier, has changing conditions at the glacier margin; the Met Office warned of increased hazard there in July 2026. Only walk on <a href="/places/solheimajokull">Sólheimajökull</a> with a certified guide.</li>
<li><strong>Hekla</strong> can erupt with less than an hour's warning, and the Met Office says it has been inflated beyond its pre-2000 level. Hikers should check vedur.is first and keep in mind that eruptions can be explosive.</li>
</ul>
<p>On the south coast, obey any road closure or flood warning, even on a sunny day. Our guide to <a href="/blog/hekla-katla-eyjafjallajokull">Hekla, Katla and Eyjafjallajökull</a> explains each volcano.</p>
<h2>Which official sources should you check?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>Icelandic Met Office (en.vedur.is)</td><td>Volcanic and earthquake updates, alert levels, gas forecasts, weather warnings</td></tr>
<tr><td>SafeTravel (safetravel.is)</td><td>Alerts, closures and restricted areas; SMS alerts and travel plans</td></tr>
<tr><td>Civil Protection (almannavarnir.is)</td><td>Official safety advice and evacuation zones</td></tr>
<tr><td>Road conditions (umferdin.is)</td><td>Open and closed roads, live</td></tr>
<tr><td>Air quality (loftgaedi.is)</td><td>Live readings of volcanic gas and other pollution</td></tr>
<tr><td>Visit Reykjanes (visitreykjanes.is)</td><td>Access to the eruption trails and local attractions</td></tr>
</tbody></table></div>
<p>In an emergency, call 112. Leaving a travel plan with SafeTravel helps rescuers find you if something goes wrong.</p>
<h2>How should you plan a trip around volcanic activity?</h2>
<ol>
<li><strong>Book flexibly.</strong> Choose rooms and tours with free cancellation, especially on the Reykjanes Peninsula.</li>
<li><strong>Buy travel insurance</strong> that covers natural events and flight disruption.</li>
<li><strong>Sign up for SafeTravel alerts</strong> before you land, and check the Met Office and SafeTravel every morning.</li>
<li><strong>Keep a back-up plan</strong> for the Blue Lagoon and anything near Grindavík. <a href="/places/reykjavik">Reykjavík</a> has plenty of geothermal pools.</li>
<li><strong>Watch an eruption with a licensed operator</strong>, which only runs trips when the authorities allow it.</li>
<li><strong>Check road conditions</strong> on umferdin.is before each drive, as you would anyway; see our guide to <a href="/blog/getting-around-iceland">getting around Iceland</a>.</li>
</ol>
<p>Iceland's volcanoes are a reason to visit, not to stay away. For an overview of all 17 on our map, from Reykjanes to Krafla, read our <a href="/blog/volcanoes-in-iceland">guide to volcanoes in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Volcanic status, closures and hazard zones change quickly; check en.vedur.is, safetravel.is and umferdin.is before and during your trip.",
        "sources": [
            ("Is it safe to visit Iceland? Volcano update (Keflavík Airport)", "https://www.kefairport.com/news/is-it-safe-to-visit-iceland-volcano"),
            ("Safety information at the eruption sites (Visit Reykjanes)", "https://www.visitreykjanes.is/en/volcano-eruption/safety-information/safety-information"),
            ("Volcanic activity on Reykjanes Peninsula, July 2025 (Icelandic Tourist Board)", "https://www.ferdamalastofa.is/en/news/volcanic-activity-on-reykjanes-peninsula-16-jul-2025"),
            ("Situation on the Reykjanes Peninsula, 30 September 2026 (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/ground-uplift-and-magma-accumulation-continue-beneath-svartsengi"),
            ("News (Icelandic Met Office)", "https://en.vedur.is/about-imo/news"),
            ("Monitoring Hekla (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/monitoring-hekla"),
            ("2010 eruptions of Eyjafjallajökull (Wikipedia)", "https://en.wikipedia.org/wiki/2010_eruptions_of_Eyjafjallaj%C3%B6kull"),
            ("Mýrdalsjökull (Wikipedia)", "https://en.wikipedia.org/wiki/M%C3%BDrdalsj%C3%B6kull"),
        ],
    },
    {
        "slug": "lava-tunnel-thrihnukagigur",
        "cluster": "volcanoes",
        "pillar": False,
        "short": "Inside a Volcano: Þríhnúkagígur and Lava Tunnels",
        "title": "Lava Tunnel Iceland: Þríhnúkagígur, Raufarhólshellir and Víðgelmir (2027)",
        "description": "Lava tunnel Iceland guide: going inside Þríhnúkagígur volcano, Raufarhólshellir near Reykjavík and Víðgelmir in the west, with seasons, prices and what to wear.",
        "category": "Nature · Volcanoes",
        "teaser": "A lift into a magma chamber, and two lava caves you can visit all year.",
        "image": "hx-maelifell",
        "image_alt": "The moss-covered cone of Mælifell rising from black sand plains",
        "stats": [
            ("120 m", "Descent into the Þríhnúkagígur magma chamber"),
            ("~4,500 yrs", "Since Þríhnúkagígur last erupted"),
            ("1,360 m", "Length of the Raufarhólshellir lava tunnel"),
            ("1,585 m", "Length of the Víðgelmir lava cave"),
        ],
        "body": """
<p>You can go inside a volcano in Iceland. At Þríhnúkagígur, near Reykjavík, an open lift lowers you about 120 m into a magma chamber that emptied after an eruption around 4,500 years ago. The tour runs only from May to October. For the rest of the year, and for a shorter, cheaper trip, two lava tunnels are open on guided tours: Raufarhólshellir, about 30 km from Reykjavík, and Víðgelmir in the west. Here is how they compare.</p>
<!--TOC-->
<h2>Can you go inside a volcano in Iceland?</h2>
<p>Yes. Þríhnúkagígur is a dormant volcano whose magma drained away instead of hardening, leaving a huge hollow chamber under a small crater opening of about 4 by 4 m. The chamber is said to be large enough to hold the Statue of Liberty.</p>
<p>The name means "Three Peaks Crater", after the three volcanic peaks in a row; Þríhnúkagígur is the youngest of them. The cave explorer Árni B. Stefánsson was the first person inside, in 1974, lowered on a rope through the opening by his friends.</p>
<h2>How does the Þríhnúkagígur tour work?</h2>
<p>The tour starts at a meeting point in the Bláfjöll hills, about 20 km south-east of the capital area. From there you hike about 3 km across a lava field to the crater, which takes 45–50 minutes each way and ends with a steep climb of about 50 m. At the top you put on a helmet and harness and step into an open cable lift, run by mountaineers, for the six- to seven-minute descent.</p>
<p>If you drive yourself, allow plenty of time to reach Bláfjöll; the road climbs into the hills and can be snowy early and late in the season. At the bottom you have about 30–40 minutes to walk around the chamber floor and look up at the walls of the chamber. Back at base camp, the tour serves Icelandic lamb soup, with a vegetarian option.</p>
<div class="table-wrap"><table>
<thead><tr><th>Þríhnúkagígur tour</th><th>Details (checked October 2026)</th></tr></thead>
<tbody>
<tr><td>Season</td><td>5 May to 30 October</td></tr>
<tr><td>Price</td><td>About ISK 51,000 for adults; ISK 25,000 for children aged 8–12</td></tr>
<tr><td>Pick-up from Reykjavík</td><td>Extra, about ISK 4,500–6,400; or drive to the meeting point</td></tr>
<tr><td>Total time</td><td>5–6 hours with pick-up; about 4 hours from the meeting point</td></tr>
<tr><td>Hike</td><td>About 3 km each way, 45–50 minutes, over uneven lava</td></tr>
<tr><td>Minimum age</td><td>8 years</td></tr>
<tr><td>Included</td><td>Helmet, harness, rain gear, soup, hot drinks, guide</td></tr>
</tbody></table></div>
<p>The 2026 season ends on 30 October, so the next chance is from May 2027. Book ahead in summer, and keep a spare day in case weather cancels your tour.</p>
""" + _map(
            "Map of Iceland's volcanoes with Þríhnúkagígur marked as number 2, south-east of Reykjavík",
            "Þríhnúkagígur (2) lies just south-east of Reykjavík, next to the Reykjanes Peninsula (1).",
        ) + """
<h2>What is a lava tunnel?</h2>
<p>A lava tunnel, or lava tube, is a cave left behind by a river of lava. As a lava flow moves, its surface cools and hardens into a roof, while molten lava keeps flowing underneath. When the eruption stops, the lava drains out and leaves a long, hollow tunnel. Iceland's young lava fields are full of them, and two of the largest are open on guided tours all year.</p>
<h2>What is Raufarhólshellir like?</h2>
<p>Raufarhólshellir is a lava tunnel 1,360 m long, up to 30 m wide and about 10 m high. It formed in a lava flow about 5,200 years ago and is often called the fourth-longest lava tube in Iceland. It is the easiest lava tunnel to visit from Reykjavík: about 30 km away, under 30 minutes' drive. Take Route 1 east for 18 km, then Route 39 for 12 km.</p>
<p>The standard tour takes about an hour and leaves every hour from morning to late afternoon, all year. You walk on built paths, a footbridge and some stairs, so there is no crawling, and children from 3 can join. Prices start from about ISK 8,900 per person (checked October 2026). Longer caving tours of about three hours are also offered. In winter, ice formations grow near the entrance. The tunnel is cold, damp and dark inside all year, so bring a warm layer even on a sunny summer day.</p>
<p>It is close to Hveragerði, so it pairs well with a walk to the <a href="/places/reykjadalur">Reykjadalur hot river</a> or a day on the <a href="/blog/golden-circle-iceland">Golden Circle</a>.</p>
<h2>What is Víðgelmir like?</h2>
<p>Víðgelmir is a lava cave about 1,585 m long at Fljótstunga, in the Borgarfjörður area of West Iceland, about two hours' drive from Reykjavík. It is often called the largest lava cave in Iceland by volume, with sections around 16 m wide and 15 m high, although longer lava tubes exist. It formed in a lava flow about 1,100 years ago, and remains dated to around the year 1100 found inside show people knew it in the Viking Age. Those finds are now in the National Museum in Reykjavík.</p>
<p>Tours run all year and take about 1.5 hours, from about ISK 9,000 per person (checked October 2026). Helmets and headlamps are included. Very young children may need to turn back before the final stop. The cave has been closed by a gate since 1993 to protect it, so the only way in is with a guide. If you are staying in Húsafell, shuttles to the cave run from Húsafell Bistro and are booked separately. It is a good stop on the way to or from <a href="/places/snaefellsnes">Snæfellsnes</a> or the Húsafell area.</p>
<h2>Which should you choose: Þríhnúkagígur, Raufarhólshellir or Víðgelmir?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Þríhnúkagígur</th><th>Raufarhólshellir</th><th>Víðgelmir</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>Empty magma chamber</td><td>Lava tunnel</td><td>Lava cave</td></tr>
<tr><td>From Reykjavík</td><td>About 20 km</td><td>About 30 km</td><td>About 2 h drive</td></tr>
<tr><td>Season</td><td>May to October</td><td>All year</td><td>All year</td></tr>
<tr><td>Tour length</td><td>About 4–6 h</td><td>About 1 h</td><td>About 1.5 h</td></tr>
<tr><td>Price from (2026)</td><td>About ISK 51,000</td><td>About ISK 8,900</td><td>About ISK 9,000</td></tr>
<tr><td>Minimum age</td><td>8</td><td>3</td><td>All ages</td></tr>
</tbody></table></div>
<p>Choose Þríhnúkagígur if you want a once-in-a-lifetime experience and are visiting between May and October. Choose Raufarhólshellir for a short, easy trip from <a href="/places/reykjavik">Reykjavík</a> in any season. Choose Víðgelmir if you are heading west or north and want a bigger cave with fewer people.</p>
<h2>What should you wear in a lava tunnel?</h2>
<p>Dress for cold and damp, even in summer. Lava caves stay cool all year whatever the weather outside, and water drips from the ceiling.</p>
<ul>
<li><strong>Warm layers</strong>: a fleece or wool jumper under a waterproof jacket.</li>
<li><strong>Sturdy shoes or boots</strong> with good grip; floors can be wet, uneven and icy in winter.</li>
<li><strong>Hat and gloves</strong> in the colder months.</li>
<li><strong>Hiking boots</strong> for Þríhnúkagígur, where the 3 km walk to the crater crosses rough lava.</li>
</ul>
<p>Helmets and lights are provided on all three tours. Do not enter lava caves without a guide: many are unlit, have loose rock and are protected because their formations break easily.</p>
<p class="callout">Visiting near the Reykjanes Peninsula? Check vedur.is and safetravel.is before you go. These sites are outside the eruption zone, but roads in the area can close during volcanic activity.</p>
<p>For the lava fields of the recent eruptions, see our <a href="/blog/reykjanes-volcano-guide">Reykjanes volcano guide</a>. For every volcano on our map, read our <a href="/blog/volcanoes-in-iceland">guide to volcanoes in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Tour prices, seasons and departure times are set by the operators and change every year; check their websites before you book. The Þríhnúkagígur season normally runs from May to October.",
        "sources": [
            ("The tour (Inside the Volcano)", "https://insidethevolcano.com/the-tour"),
            ("Inside the Volcano tour (Arctic Adventures)", "https://adventures.is/iceland/day-tours/volcano-tours/inside-the-volcano/"),
            ("Þríhnúkagígur travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/thrihnjukagigur"),
            ("Raufarhólshellir lava tunnel tour (Iceland Travel Guide)", "https://icelandtravelguide.is/tours/raufarholshellir-lava-tunnel-tour"),
            ("Raufarhólshellir lava tunnel entrance ticket (Guide to Iceland)", "https://guidetoiceland.is/book-holiday-trips/standard-lava-tunnel-tour?a=36777"),
            ("Víðgelmir lava cave tour (Iceland Travel Guide)", "https://icelandtravelguide.is/tours/vidgelmir-lava-cave/"),
            ("Hellirinn Víðgelmir (Showcaves)", "https://showcaves.com/english/is/showcaves/Vidgelmir.html"),
        ],
    },
    {
        "slug": "hekla-katla-eyjafjallajokull",
        "cluster": "volcanoes",
        "pillar": False,
        "short": "Eyjafjallajökull, Hekla and Katla Explained",
        "title": "Eyjafjallajökull, Hekla and Katla: Iceland's Famous Volcanoes Explained",
        "description": "Eyjafjallajökull, Hekla and Katla explained: how to say the names, what happened in 2010, whether Katla and Hekla are overdue, and how to see them.",
        "category": "Nature · Volcanoes",
        "teaser": "How to say Eyjafjallajökull, and why Hekla and Katla are watched so closely.",
        "image": "hx-solheimajokull",
        "image_alt": "The ash-streaked ice of Sólheimajökull with a waterfall in the cliffs above",
        "stats": [
            ("1,666 m", "Height of Eyjafjallajökull"),
            ("1,491 m", "Height of Hekla"),
            ("1918", "Katla's last major eruption"),
            ("~10 million", "Travellers affected by the 2010 ash cloud"),
        ],
        "body": """
<p>Eyjafjallajökull, Hekla and Katla are Iceland's three most famous volcanoes, and all three stand within sight of the south coast. Eyjafjallajökull is the glacier volcano whose ash closed Europe's skies in April 2010. Hekla, the "gateway to hell" of medieval legend, last erupted in 2000. Katla hides under the Mýrdalsjökull ice cap and has not had a major eruption since 1918. Here is what each one is, how to say the names and how you can see them.</p>
<!--TOC-->
<h2>How do Eyjafjallajökull, Hekla and Katla compare?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Eyjafjallajökull</th><th>Hekla</th><th>Katla</th></tr></thead>
<tbody>
<tr><td>Height</td><td>1,666 m</td><td>1,491 m</td><td>Under Mýrdalsjökull (ice up to about 1,450–1,490 m)</td></tr>
<tr><td>Type</td><td>Ice-capped stratovolcano</td><td>Ridge volcano on a 40 km volcanic ridge</td><td>Subglacial volcano with a caldera about 10 km across</td></tr>
<tr><td>Last eruption</td><td>2010</td><td>26 Feb – 8 Mar 2000</td><td>1918 (major eruption)</td></tr>
<tr><td>Known for</td><td>The 2010 ash cloud</td><td>Medieval "gateway to hell"</td><td>Huge glacial floods</td></tr>
<tr><td>How to see it</td><td>From the Ring Road at Seljalandsfoss</td><td>From the south; summer hike</td><td>Glacier walks on Sólheimajökull</td></tr>
</tbody></table></div>
<h2>How do you pronounce Eyjafjallajökull, and what does it mean?</h2>
<p>Eyjafjallajökull is roughly "AY-yah-fyah-dlah-YOH-kuh-dl". The double "ll" in Icelandic is not an English "l", which is what trips most people up. Say it in three parts: <strong>Eyja</strong> (islands), <strong>fjalla</strong> (mountains), <strong>jökull</strong> (glacier).</p>
<p>So the name means "the glacier of the island mountains". The islands are the Westman Islands, which you can see from the foot of the volcano, and the mountains are the Eyjafjöll range below the ice.</p>
<h2>What happened when Eyjafjallajökull erupted in 2010?</h2>
<p>The eruption came in two phases. On 20 March 2010 a fissure opened on Fimmvörðuháls, the pass between Eyjafjallajökull and Mýrdalsjökull, with fountains of lava and little ash. About 500 farmers and their families were evacuated overnight and allowed home two days later.</p>
<p>On 14 April the eruption moved under the summit ice. Meltwater mixed with magma and blasted out fine ash, which rose in a plume about 8–9 km high and drifted over Europe. Most European airspace closed from 15 to 20 April, about 20 countries shut their skies to commercial jets and around 10 million travellers were affected. The eruption ejected about 250 million m³ of tephra and was declared over in October 2010.</p>
<p>The two phases were very different. The first, on Fimmvörðuháls, sent ash no higher than about 4 km, and crowds walked up to watch the lava. The second, under the ice, was the one that mattered to the rest of the world. Before 2010, Eyjafjallajökull's most recent major eruptions were in 920, 1612 and 1821–23. You can walk across the 2010 lava on the <a href="/blog/fimmvorduhals-hike">Fimmvörðuháls hike</a>, between Skógar and Þórsmörk.</p>
""" + _map(
            "Map of Icelandic volcanoes with Hekla, Eyjafjallajökull and Katla marked as numbers 4, 5 and 6 in the south",
            "Hekla (4), Eyjafjallajökull (5) and Katla (6) all lie close to the south coast, with Vík below Katla.",
        ) + """
<h2>What is Katla, and is it overdue?</h2>
<p>Katla is one of Iceland's most powerful volcanoes, buried under the Mýrdalsjökull ice cap above Vík. Its caldera is about 10 km across and lies beneath ice that averages about 230 m thick. Katla usually erupts every 40 to 80 years, and 16 eruptions have been documented since 930.</p>
<p>Its last major eruption began on 12 October 1918. Within minutes a glacial flood, or jökulhlaup, poured across the sands to the east with a peak flow of about 300,000 m³ per second. It pushed the coastline temporarily about 4 km out to sea. Three farms near Álftaver were abandoned, and the local population fell by almost a quarter within two years. Most of Katla's big floods since 874, 17 of 20, have run east through the Kötlujökull outlet glacier. More than a century later, Katla is past its usual interval, so it is watched closely.</p>
<p>Smaller events happen more often. In July 2011 a flood destroyed the Ring Road bridge over the Múlakvísl river, east of Vík. In August 2026 another glacial outburst flood came down the Múlakvísl, with raised electrical conductivity and gas pollution near the river, and the Met Office reported on 1 September 2026 that it was subsiding. These floods are why you may see warning signs and occasional road closures between Vík and Kirkjubæjarklaustur.</p>
<h2>Why was Hekla called the gateway to hell?</h2>
<p>Hekla's violent eruption in 1104, after at least 250 quiet years, spread ash over more than half of Iceland and made the volcano famous across Europe. In the Middle Ages, stories spread that its crater was an entrance to hell, a belief that lasted into the 19th century.</p>
<p>Hekla is 1,491 m high and has erupted 23 times in the last thousand years, making it one of Iceland's most active volcanoes. Its 1947 eruption sent a plume about 30 km high. Since 1970 it has erupted roughly every ten years: in 1970, 1980–81, 1991 and from 26 February to 8 March 2000. The 2000 eruption sent a plume 10–12 km high within a couple of hours. Before 1970, though, Hekla sometimes stayed quiet for up to 120 years, so its recent rhythm is no guarantee.</p>
<h2>Is Hekla about to erupt?</h2>
<p>Nobody can say when, but the Met Office says Hekla has been inflated beyond its level before the 2000 eruption since around 2007–09. In 2016 it called the volcano overdue by its recent pattern. Hekla is hard to forecast: the warning before an eruption can be less than an hour.</p>
<p>A path leads most of the way to the summit, and the hike takes about 3–4 hours. If you go, choose a clear summer day, check vedur.is first, and keep in mind that an eruption could start with little warning and be explosive.</p>
<h2>How can you see Hekla, Katla and Eyjafjallajökull?</h2>
<p>You can see all three from the south coast without going anywhere near danger.</p>
<ul>
<li><strong>Eyjafjallajökull:</strong> the ice cap rises above the Ring Road between Hvolsvöllur and Skógar. <a href="/places/seljalandsfoss">Seljalandsfoss</a> falls from the cliffs at its foot.</li>
<li><strong>Katla:</strong> walk onto <a href="/places/solheimajokull">Sólheimajökull</a>, an outlet glacier of Mýrdalsjökull, on a guided glacier hike. The dark bands in the ice are ash from past eruptions. Never go onto the glacier without a certified guide; the Met Office warned of changing conditions at its margin in July 2026.</li>
<li><strong>Hekla:</strong> on a clear day the long, snowy ridge is visible from the Ring Road around Hella and from inland roads to the north.</li>
<li><strong>The LAVA Centre in Hvolsvöllur</strong> has an interactive exhibition on Iceland's volcanoes, including the 2010 eruption.</li>
</ul>
<p>Vík, the village below Katla, is the base for <a href="/places/reynisfjara">Reynisfjara</a> and the black beaches. Our <a href="/blog/south-coast-iceland">South Coast guide</a> puts all of these into one route.</p>
<p class="callout">If Katla, Hekla or Eyjafjallajökull shows signs of unrest, the authorities close roads and areas quickly. Check vedur.is and safetravel.is before you travel along the south coast, and read our <a href="/blog/iceland-volcano-safety">Iceland volcano safety guide</a>.</p>
<p>These three are only part of the story. For Reykjanes, Askja, Krafla and the rest of the 17 volcanoes on our map, see our <a href="/blog/volcanoes-in-iceland">guide to volcanoes in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Volcanic activity under Mýrdalsjökull and at Hekla is monitored continuously; check vedur.is and safetravel.is for current warnings, flood alerts and road closures on the south coast.",
        "sources": [
            ("2010 eruptions of Eyjafjallajökull (Wikipedia)", "https://en.wikipedia.org/wiki/2010_eruptions_of_Eyjafjallaj%C3%B6kull"),
            ("Hekla (Wikipedia)", "https://en.wikipedia.org/wiki/Hekla"),
            ("Monitoring Hekla (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/monitoring-hekla"),
            ("Mýrdalsjökull (Wikipedia)", "https://en.wikipedia.org/wiki/M%C3%BDrdalsj%C3%B6kull"),
            ("1918 eruption of Katla (Wikipedia)", "https://en.wikipedia.org/wiki/1918_eruption_of_Katla"),
            ("News (Icelandic Met Office)", "https://en.vedur.is/about-imo/news"),
            ("Eyjafjallajökull volcanic glacier (Iceland Travel Guide)", "https://icelandtravelguide.is/locations/eyjafjallajokull/"),
            ("How to pronounce Icelandic place names (Bus Travel Iceland)", "https://bustravel.is/iceland-travel-information/how-to-pronounce-icelandic-place-names"),
        ],
    },
]
