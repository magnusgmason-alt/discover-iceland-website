"""Hiking cluster articles (cluster c5). Same format as articles_content.py."""

MAP_HIKING = '<figure class="a-figure a-map"><a href="/assets/img/map-hiking-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-hiking-1800.jpg" srcset="/assets/img/map-hiking-800.jpg 800w, /assets/img/map-hiking-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{caption} Tap to open full size.</figcaption></figure>'


def _map(alt, caption):
    return MAP_HIKING.format(alt=alt, caption=caption)


ARTICLES = [
    # ------------------------------------------------------------------
    # 1. PILLAR
    # ------------------------------------------------------------------
    {
        "slug": "hiking-in-iceland",
        "cluster": "hiking",
        "pillar": True,
        "short": "Hiking in Iceland: The Best Day Hikes and Treks",
        "title": "Hiking in Iceland: Best Day Hikes and Multi-Day Treks (2027)",
        "description": "Hiking in Iceland: the best day hikes and multi-day treks, from Laugavegur and Landmannalaugar to Skaftafell and Glymur, with seasons, huts, buses and safety.",
        "category": "Hiking · Planning",
        "teaser": "From short waterfall walks to four days across the highlands.",
        "image": "hx-skaftafell",
        "image_alt": "A walker sitting by a boulder looking out at a glacier tongue between dark mountains",
        "stats": [
            ("55 km", "Laugavegur Trail, Landmannalaugar to Þórsmörk"),
            ("198 m", "Glymur, Iceland's second-highest waterfall"),
            ("32 km", "Canyon trail from Ásbyrgi to Dettifoss"),
            ("112", "Emergency number, including mountain rescue"),
        ],
        "body": """
<p>Hiking in Iceland ranges from a 20-minute walk to a waterfall to four days across the highlands with your bed on your back. The best-known trek is the 55 km Laugavegur Trail from Landmannalaugar to Þórsmörk. The best day hikes include Skaftafell, Glymur, Mount Esja, Reykjadalur and the colourful mountains around Landmannalaugar. Most highland trails open only from late June to mid-September, while many lowland walks work all year.</p>
<p>This guide covers the best hikes by length, when to go, how to reach the trailheads, where to sleep and how to stay safe.</p>
<!--TOC-->
<h2>What are the best hikes in Iceland?</h2>
<p>The best hikes in Iceland are the Laugavegur Trail, the day trails around Landmannalaugar and Skaftafell, Glymur, and the canyon trail from Ásbyrgi to Dettifoss. For an easy start, the walks to Svartifoss and the Reykjadalur hot river are hard to beat. The table gives a quick comparison.</p>
<div class="table-wrap"><table>
<thead><tr><th>Hike</th><th>Region</th><th>Distance</th><th>Time</th><th>Level</th></tr></thead>
<tbody>
<tr><td>Laugavegur Trail</td><td>Southern highlands</td><td>55 km</td><td>3–4 days</td><td>Challenging</td></tr>
<tr><td>Ásbyrgi to Dettifoss</td><td>North, Vatnajökull NP</td><td>32 km</td><td>2 days</td><td>Challenging</td></tr>
<tr><td>Fimmvörðuháls</td><td>South, Skógar to Þórsmörk</td><td>About 25 km</td><td>1–2 days</td><td>Challenging; see warning below</td></tr>
<tr><td>Bláhnúkur</td><td>Landmannalaugar</td><td>About 4 km</td><td>About 3 h</td><td>Moderate, steep</td></tr>
<tr><td>Glymur loop</td><td>Hvalfjörður, west</td><td>About 7 km</td><td>3–4 h</td><td>Moderate, exposed</td></tr>
<tr><td>Svartifoss–Sjónarsker–Sel</td><td>Skaftafell</td><td>5.8 km loop</td><td>About 2 h</td><td>Easy</td></tr>
<tr><td>Reykjadalur hot river</td><td>Hveragerði</td><td>About 7 km return</td><td>2–3 h with a bath</td><td>Easy to moderate</td></tr>
<tr><td>Hengifoss</td><td>East Iceland</td><td>About 2 h return</td><td>About 2 h</td><td>Moderate, 300 m climb</td></tr>
</tbody></table></div>
<p>Times are walking times in good conditions. In wind, rain or fog, add time, and turn back early rather than late.</p>
""" + _map(
            "Map of Iceland hiking trails including Laugavegur, Fimmvörðuháls, Glymur, Esja, Skaftafell and Hornstrandir",
            "Iceland's main hiking areas: Laugavegur and Fimmvörðuháls in the south, the canyon trail in the north, Hornstrandir in the Westfjords and day hikes near Reykjavík.",
        ) + """
<h2>When is the hiking season in Iceland?</h2>
<p>The main hiking season in Iceland runs from late June to mid-September. That is when the highland roads are open, the buses run and the mountain huts are staffed. Ferðafélag Íslands (FÍ), the Iceland Touring Association, gives the Laugavegur Trail an average open season of 25 June to 15 September, though the exact dates depend on snow and when the roads open.</p>
<p>Lowland trails are different. Skaftafell, Reykjadalur, Þingvellir and the waterfall walks along the south coast can be hiked all year. In winter they are often icy, the days are short and some paths close for repairs or to protect the ground in the spring thaw. July and August give the most reliable trail conditions and almost endless daylight. Our guide to the <a href="/blog/best-time-to-visit-iceland">best time to visit Iceland</a> covers the weather month by month.</p>
<h2>What are the best multi-day treks in Iceland?</h2>
<p>The best multi-day treks in Iceland are the Laugavegur Trail, the canyon trail from Ásbyrgi to Dettifoss, and the coastal routes of the Hornstrandir nature reserve. Fimmvörðuháls is a classic one or two-day crossing, but it is under a safety warning as of autumn 2026.</p>
<h3>Laugavegur Trail</h3>
<p>The Laugavegur runs 55 km from the hot springs of Landmannalaugar to the green valley of Þórsmörk. Most people take four days, sleeping in FÍ huts or campsites at Hrafntinnusker, Álftavatn or Hvanngil, and Emstrur. You cross rhyolite mountains, obsidian fields, black sand deserts and at least three rivers you must wade. Our <a href="/blog/laugavegur-trail">Laugavegur Trail guide</a> has every stage, hut and bus.</p>
<h3>Fimmvörðuháls</h3>
<p>Fimmvörðuháls climbs about 1,000 m from Skógafoss to a pass between the Eyjafjallajökull and Mýrdalsjökull glaciers, then drops into Þórsmörk. On the way you pass the Magni and Móði craters from the 2010 eruption. On 25 August 2026 FÍ, Útivist and the Dagrenning rescue team strongly advised against crossing it, because glacier retreat had opened ravines and crevasses near the huts on the pass. Read our <a href="/blog/fimmvorduhals-hike">Fimmvörðuháls guide</a> before you plan it.</p>
<h3>Ásbyrgi to Dettifoss</h3>
<p>In the north of Vatnajökull National Park, a 32 km trail follows the Jökulsárgljúfur canyon from the horseshoe-shaped Ásbyrgi to Dettifoss. The park recommends two days, with a night at the Vesturdalur campsite. There are no huts, and camping is allowed only at the official sites at Ásbyrgi, Vesturdalur and Dettifoss. The middle stage includes wading the Stallá river.</p>
<h3>Hornstrandir</h3>
<p>Hornstrandir, at the northern tip of the Westfjords, has no roads at all. Boats from Ísafjörður, Bolungarvík and Norðurfjörður drop hikers off between June and August. It has been a nature reserve since 1975 and is one of the best places in Iceland to see Arctic foxes. Book your return boat in advance, because that is how rescuers know if you fail to arrive. Camp only at the designated campgrounds, and consider a guide unless you have real wilderness experience.</p>
<h2>What are the best day hikes in Iceland?</h2>
<p>The best day hikes in Iceland are in Skaftafell, around Landmannalaugar, at Glymur in Hvalfjörður and on Mount Esja above Reykjavík. Each gives a different side of the country: glaciers, coloured rhyolite, a deep canyon and a view over the capital.</p>
<ul>
<li><strong>Skaftafell:</strong> the hiking hub of <a href="/places/skaftafell">Skaftafell</a> in Vatnajökull National Park has marked trails from the visitor centre. The easy 5.8 km Svartifoss–Sjónarsker–Sel loop takes about two hours. Sjónarnípa (6.5 km, 2–2.5 hours) looks straight onto Skaftafellsjökull, and the 16.6 km Skaftafellsheiði loop takes 5–6 hours.</li>
<li><strong>Landmannalaugar:</strong> short, steep climbs to Bláhnúkur (about 945 m) and Brennisteinsalda give views over striped rhyolite mountains and steaming vents. You need a 4x4 or the highland bus to get there. See our <a href="/blog/landmannalaugar-hiking">Landmannalaugar hiking guide</a>.</li>
<li><strong>Glymur:</strong> Iceland's second-highest waterfall drops 198 m into a canyon in Hvalfjörður, north of Reykjavík. The loop is about 7 km with 425 m of climbing and takes 3–4 hours. It follows the canyon edge and crosses the river on a log, which is usually only in place from spring to autumn.</li>
<li><strong>Mount Esja:</strong> about 10 km north of Reykjavík, Esja is the capital's home mountain. The marked path climbs roughly 600 m to Steinn, a large rock where most people turn round. Experienced hikers continue to Þverfellshorn at 780 m.</li>
<li><strong>Hengifoss:</strong> in the east, a steep path climbs about 300 m past the basalt columns of Litlanesfoss to <a href="/places/hengifoss">Hengifoss</a>, a 128 m waterfall in a gorge banded with red clay. Allow about two hours return.</li>
</ul>
<h2>What are the easiest hikes in Iceland?</h2>
<p>The easiest hikes in Iceland are short, well-made paths to waterfalls, canyons and craters. Good examples are the stairs beside Skógafoss, the rim path at Fjaðrárgljúfur, the walk to Svartifoss, the 20 to 30-minute climb up Hverfjall crater at Mývatn and the walk to the <a href="/places/reykjadalur">Reykjadalur</a> hot river. Most take under two hours and start from a car park on or near the Ring Road. Our list of <a href="/blog/easy-hikes-iceland">easy hikes in Iceland</a> has times and tips for each.</p>
<h2>Can you hike on a glacier in Iceland on your own?</h2>
<p>No, you should only walk on a glacier with a qualified guide. Glacier ice hides crevasses and meltwater channels that change from week to week, and you need crampons, an ice axe and the skills to use them. Guided hikes run all year at Sólheimajökull and in Skaftafell. You can walk to the edge of <a href="/places/solheimajokull">Sólheimajökull</a> on your own, but stop at the ice. Our <a href="/blog/glacier-hiking-iceland">glacier hiking guide</a> explains how the tours work, Most tours start from the Skaftafell visitor centre or the Sólheimajökull car park.</p>
<p class="callout"><strong>Stay on the path.</strong> Iceland's moss and soil take decades to recover from footprints. Stay on marked trails, camp only where it is allowed, and carry out all your rubbish, including food scraps and toilet paper.</p>
<h2>How do you get to Iceland's hiking trails?</h2>
<p>Most lowland trailheads have a car park beside a paved or gravel road, and a normal car is fine in summer. Many charge a parking fee, usually paid by app or by camera number-plate reading. The highland trailheads, including Landmannalaugar, are reached by F-roads that only 4x4 vehicles may use, often with unbridged rivers.</p>
<p>If you do not want to drive in the highlands, take the summer highland buses. They run from the BSÍ bus terminal in Reykjavík to Landmannalaugar, Þórsmörk and Skógar, roughly from late June to early September. They are also how most Laugavegur hikers get to the start and home from the end. For the wider picture, see <a href="/blog/getting-around-iceland">getting around Iceland</a>.</p>
<p>At Landmannalaugar, anyone driving their own car and arriving between 9:00 and 16:00 must book a parking slot in advance. In 2026 the rule applied from 20 June to 13 September, and the fee was ISK 1,500 for a car with up to five seats. Bus passengers do not need to book.</p>
<h2>Where do you sleep on a multi-day hike in Iceland?</h2>
<p>On the main trails you sleep in mountain huts or at the campsites beside them. FÍ runs the huts on the Laugavegur and many others across the highlands, and Útivist runs huts at Básar in Þórsmörk and on Fimmvörðuháls. The huts have bunks, kitchens with gas stoves and, at most sites, showers, but you bring your own sleeping bag and food.</p>
<p>Huts fill up months ahead for July and August. FÍ sells its Laugavegur nights as route packages, and in 2026 a three-night hut package cost ISK 54,000. Camping is cheaper and easier to book, but you carry more weight and need a tent that stands up to strong wind. On the Laugavegur, camp only at the hut sites.</p>
<h2>How do you stay safe hiking in Iceland?</h2>
<p>To stay safe hiking in Iceland, check the weather every day, leave a travel plan, stay on marked trails and turn back when conditions turn. The weather changes fast, even in summer. Fog can hide the trail markers within minutes, and wind is the biggest danger on exposed passes.</p>
<ul>
<li><strong>Check the forecast</strong> at vedur.is once or twice a day, and ask hut wardens and rangers, who know the local conditions.</li>
<li><strong>Leave a travel plan</strong> at safetravel.is and with someone at home, and update it if your plans change.</li>
<li><strong>Carry navigation:</strong> a GPS or phone with offline maps, a paper map and compass, and a power bank.</li>
<li><strong>Know about rivers:</strong> glacial rivers are lowest in the morning and rise after rain and on warm afternoons. Cross in groups of two or three with linked arms, in sandals or old trainers, and never cross if you are unsure.</li>
<li><strong>Watch for hypothermia:</strong> SafeTravel says it is common in Iceland even in summer. Change into dry layers early and keep eating.</li>
<li><strong>Call 112 in an emergency.</strong> Phone coverage in the highlands is patchy, so for remote routes consider renting a personal locator beacon or satellite messenger.</li>
</ul>
<h2>How fit do you need to be to hike in Iceland?</h2>
<p>You need average fitness for the short walks and good fitness for the full-day hikes and treks. The easy trails in this guide suit most people who can walk for an hour or two on uneven ground. A day like Glymur or Bláhnúkur needs you to climb 300 to 400 m on steep, loose paths. The Laugavegur asks for four days in a row of four to seven hours' walking with a full pack, often in wind and rain.</p>
<p>SafeTravel's advice is simple: be honest about your experience, fitness and equipment, start with easier routes, and keep daily distances reasonable. If you have never carried a pack for several days, try a weekend trek at home first, or join a guided group.</p>
<h2>Can you hike in Iceland in winter?</h2>
<p>Yes, but only on lowland trails, and with winter gear. From about November to April, paths at places like Fjaðrárgljúfur and Skaftafell are often icy, so microspikes or crampons are essential. Daylight is short, and around the December solstice Reykjavík has only about four hours of it. Some trails close in the spring thaw, roughly March to May, to protect the wet ground.</p>
<p>The highland trails are a different matter. The huts are locked, the F-roads are closed and FÍ says winter crossings of routes like the Laugavegur need expert skills and full winter equipment. In winter, the best way into the mountains is a guided tour: glacier hikes and ice caves run with qualified guides through the cold months.</p>
<h2>Do you need a guide to hike in Iceland?</h2>
<p>You do not need a guide for marked trails in summer, and many people walk the Laugavegur on their own each summer. A guide makes sense on glaciers, where it is essential, on remote routes like Hornstrandir if you lack wilderness experience, and on any route under a warning, such as Fimmvörðuháls in 2026. Guided treks also solve the logistics, with huts, food and transport booked for you.</p>
<h2>What should you pack for hiking in Iceland?</h2>
<p>Pack for wind, rain and cold on every hike, whatever the season. That means a waterproof jacket and trousers, warm wool or fleece layers, a hat and gloves, sturdy waterproof boots and enough food and water. For hut trips, add a sleeping bag; for river crossings, light shoes you can wade in. Our full <a href="/blog/iceland-hiking-packing-list">Iceland hiking packing list</a> covers day hikes, hut treks and camping.</p>
<h2>How should you plan your first hiking trip in Iceland?</h2>
<p>Start with day hikes from a car or a base, then add a highland trek once you know how you handle the weather. A good first week combines the south coast walks with a few days in Skaftafell, or a day trip to Landmannalaugar by bus. Book huts and buses for July and August as early as you can, and keep a spare day in case a storm closes a pass.</p>
<p>For more ideas beyond the trails, browse our <a href="/highlights">Iceland highlights</a> with their interactive map. Our printed <a href="/#guides">Summer guidebook</a> brings the main hikes, huts and highland roads together in one place for the trip.</p>
""",
        "checked_note": "Facts checked October 2026. Hut prices, bus timetables and parking rules change every year, and highland trails open only when the snow and roads allow. The Fimmvörðuháls warning was issued on 25 August 2026; check fi.is and safetravel.is for its current status.",
        "sources": [
            ("Trails: Laugavegur (Ferðafélag Íslands)", "https://www.fi.is/en/hiking-trails/trails/view/laugavegur"),
            ("Warning: dangerous conditions on the Fimmvörðuháls hiking trail (Icelandic Tourist Board)", "https://www.ferdamalastofa.is/en/news/category/1/warning-dangerous-conditions-on-the-fimmvorduhals-hiking-trail"),
            ("Svartifoss and Skaftafell trails (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/destination-svartifoss"),
            ("Ásbyrgi to Dettifoss: Canyon Trail (Vatnajökull National Park)", "https://vatnajokulsthjodgardur.is/en/asbyrgi-dettifoss"),
            ("The ultimate guide to Hornstrandir (Westfjords.is)", "https://www.westfjords.is/en/moya/news/the-ultimate-guide-to-hornstrandir-europes-last-wilderness"),
            ("Hiking and trekking (SafeTravel)", "https://safetravel.is/outdoors/hiking-trekking/"),
            ("Glymur waterfall hike guide (Earth Trekkers)", "https://www.earthtrekkers.com/glymur-waterfall-hike-complete-guide/"),
            ("Landmannalaugar parking (Parka)", "https://parka.is/parking/landmannalaugar/"),
        ],
    },
    # ------------------------------------------------------------------
    # 2. LAUGAVEGUR
    # ------------------------------------------------------------------
    {
        "slug": "laugavegur-trail",
        "cluster": "hiking",
        "pillar": False,
        "short": "Laugavegur Trail: Stage-by-Stage Guide",
        "title": "Laugavegur Trail: Stages, Huts, Season, Booking and Buses (2027)",
        "description": "The Laugavegur Trail stage by stage: the 55 km route from Landmannalaugar to Þórsmörk, huts, distances, river crossings, season, booking and highland buses.",
        "category": "Hiking · Multi-day treks",
        "teaser": "55 km from Landmannalaugar to Þórsmörk, hut by hut.",
        "image": "hx-highland-rivers",
        "image_alt": "A moss-green mountain above a braided river and black sand in the Icelandic highlands",
        "stats": [
            ("55 km", "Landmannalaugar to Þórsmörk"),
            ("4 days", "Standard itinerary in four stages"),
            ("25 Jun–15 Sep", "Average open season, depending on snow"),
            ("3 rivers", "Crossings you must wade"),
        ],
        "body": """
<p>The Laugavegur Trail is a 54–55 km hike from Landmannalaugar to Þórsmörk in Iceland's southern highlands. Most people walk it in four days, north to south, sleeping in mountain huts or at the campsites beside them. The trail is normally open from late June to mid-September. You need to book huts and buses well ahead for July and August.</p>
<!--TOC-->
<h2>How long is the Laugavegur Trail?</h2>
<p>Ferðafélag Íslands (FÍ), which runs most of the huts, gives the Laugavegur as 54 to 55 km. The standard plan splits it into four stages of 12 to 16 km, each taking four to seven hours. Fit hikers can walk it in three days or even two, but the long days leave little margin for bad weather.</p>
<p>The route climbs from Landmannalaugar over the high ground around Hrafntinnusker, then descends gradually to the birch woods of Þórsmörk. Many hikers add Fimmvörðuháls to continue to Skógar on the south coast; see our <a href="/blog/fimmvorduhals-hike">Fimmvörðuháls guide</a> for the current warning on that route.</p>
<h2>What are the stages of the Laugavegur Trail?</h2>
<p>The four standard stages, with FÍ's distances and times, are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Distance</th><th>Time</th><th>Height change</th></tr></thead>
<tbody>
<tr><td>1. Landmannalaugar to Hrafntinnusker</td><td>12 km</td><td>4–5 h</td><td>About 470 m up</td></tr>
<tr><td>2. Hrafntinnusker to Álftavatn</td><td>12 km</td><td>4–5 h</td><td>About 490 m down</td></tr>
<tr><td>3. Álftavatn to Emstrur</td><td>16 km</td><td>6–7 h</td><td>Mostly level</td></tr>
<tr><td>4. Emstrur to Þórsmörk</td><td>15 km</td><td>6–7 h</td><td>About 300 m down</td></tr>
</tbody></table></div>
<p>FÍ also suggests a three-day version (Landmannalaugar to Álftavatn, 24 km; Álftavatn to Emstrur; Emstrur to Þórsmörk) and a two-day version via Hvanngil, with two days of about 28 km.</p>
<h3>Stage 1: Landmannalaugar to Hrafntinnusker</h3>
<p>The first day is the steepest climb. You leave the Laugahraun lava field, pass steaming vents and climb through orange, green and grey rhyolite hills to Hrafntinnusker, named after its black obsidian. Snow can lie here well into summer, and fog is common.</p>
<h3>Stage 2: Hrafntinnusker to Álftavatn</h3>
<p>The trail crosses high ground with views of the glaciers, then drops steeply to the lake at Álftavatn. FÍ warns that fog can cut visibility to almost nothing between Landmannalaugar and Álftavatn, so follow the trail markers closely.</p>
<h3>Stage 3: Álftavatn to Emstrur</h3>
<p>This is the longest stage. Soon after Álftavatn you reach Hvanngil, an alternative overnight stop about 4 km further on. Then comes a long walk across black sand plains below Mýrdalsjökull. Several of the trail's river crossings come on this stage, so ask the warden about water levels before you leave.</p>
<h3>Stage 4: Emstrur to Þórsmörk</h3>
<p>The last day starts near the canyons of the Markarfljót river at Emstrur and ends in the birch woods of Þórsmörk. The final river, Þröngá, must be waded before you reach the woods. The trail ends at the Langidalur hut in Þórsmörk.</p>
""" + _map(
            "Map of Iceland hiking trails with the Laugavegur Trail from Landmannalaugar to Þórsmörk marked",
            "The Laugavegur Trail runs about 55 km south from Landmannalaugar to Þórsmörk, with Fimmvörðuháls continuing to Skógar.",
        ) + """
<h2>Where do you sleep on the Laugavegur?</h2>
<p>You sleep in FÍ mountain huts or camp at the campsites next to them. The huts have bunks, gas stoves, cooking equipment and toilets, and most have showers you pay for. You must bring your own sleeping bag and food. FÍ's hut capacities are:</p>
<ul>
<li><strong>Landmannalaugar:</strong> 78 beds, beside the hot spring.</li>
<li><strong>Hrafntinnusker (Höskuldsskáli):</strong> 52 beds, the highest and coldest stop.</li>
<li><strong>Álftavatn:</strong> two huts, 72 beds, by the lake.</li>
<li><strong>Hvanngil:</strong> 60 beds, a quieter alternative to Álftavatn.</li>
<li><strong>Emstrur (Botnar):</strong> three huts, 60 beds, at about 465 m.</li>
<li><strong>Þórsmörk (Langidalur, Skagfjörðsskáli):</strong> 73 beds.</li>
</ul>
<p>Útivist runs a separate hut at Básar in the Goðaland part of Þórsmörk, about 2 km from Langidalur across the Krossá footbridge. Wardens staff the huts in summer and can tell you about weather and rivers.</p>
<h2>How do you book the Laugavegur huts?</h2>
<p>Book on the FÍ website, as early as you can. For 2026 FÍ sold hut nights on the Laugavegur as route packages rather than single nights. A three-night hut package (for example Landmannalaugar, Álftavatn and Þórsmörk) cost ISK 54,000, and a five-night package with every stop cost ISK 90,000. Packages that combine huts with a rented tent were cheaper. Individual hut nights on other FÍ routes cost about ISK 16,000–18,000.</p>
<p>FÍ says you should have confirmed bookings before you start, whether in a hut or at a campsite. In October 2026 FÍ's booking system already listed 2027 dates.</p>
<p class="callout"><strong>Plan around the weather.</strong> Keep a spare day at the end of your trip. Storms can close the trail, and wardens may advise you to wait at a hut rather than continue.</p>
<h2>When can you hike the Laugavegur Trail?</h2>
<p>The Laugavegur is open on average from 25 June to 15 September, according to FÍ. The exact opening depends on snow and on when the road authority opens the highland roads to Landmannalaugar. In June and early July expect snowfields, especially around Hrafntinnusker. July and August are the busiest months, with the most daylight. Outside the season the huts are locked, and FÍ says winter crossings need expert skills and full winter equipment.</p>
<h2>How do you get to and from the Laugavegur?</h2>
<p>Most hikers take the summer highland buses. They run from the BSÍ bus terminal in Reykjavík to Landmannalaugar from late June to early September, and from Þórsmörk back to Reykjavík. Reykjavík Excursions (Icelandia) and other operators sell one-way and return tickets, and the ride to Landmannalaugar takes about four hours.</p>
<p>If you drive, you need a 4x4 that your rental company allows on F-roads. Driving your own car to Landmannalaugar between 9:00 and 16:00 requires a parking reservation; in summer 2026 the rule applied from 20 June to 13 September and cost ISK 1,500 for a car with up to five seats. Remember that the trail ends far from where it starts, so a bus is usually simpler. Our <a href="/blog/landmannalaugar-hiking">Landmannalaugar hiking guide</a> covers the roads and the day hikes at the start of the trail.</p>
<h2>How hard is the Laugavegur Trail?</h2>
<p>The Laugavegur is a moderate to challenging trek for fit hikers with some experience. The paths are well marked, and the daily climbs are modest. The difficulty comes from the conditions: cold wind, rain, fog, snow and river crossings, often all in one day.</p>
<p>At least three rivers have no bridge: Grashagakvísl (sometimes snow-bridged in early summer), Bláfjallakvísl and Þröngá. Others, including Kaldaklofskvísl, Fremri-Emstruá and Ljósá, have footbridges. Bring sandals or light shoes for wading, cross in the morning when levels are lower, and ask the wardens before you set off. FÍ notes that phone signal is unreliable along the route, sometimes only on hilltops, and the huts have no wifi. In an emergency call 112.</p>
<h2>What should you pack for the Laugavegur?</h2>
<p>Pack full waterproofs, warm layers, a hat and gloves, sturdy boots, wading shoes, a sleeping bag and all your food. Campers need a tent that can handle strong wind. Carry a map and a GPS or phone with offline maps, plus a power bank. Our <a href="/blog/iceland-hiking-packing-list">Iceland hiking packing list</a> has the full checklist.</p>
<h2>What else is near the Laugavegur?</h2>
<p>Spend an extra day at Landmannalaugar to climb Bláhnúkur and Brennisteinsalda before you start. At the other end, Þórsmörk has short walks among birch woods and glacier views. Back on the Ring Road, <a href="/places/seljalandsfoss">Seljalandsfoss</a> and <a href="/places/solheimajokull">Sólheimajökull</a> are close to the road into Þórsmörk. For more treks and day walks, see our guide to <a href="/blog/hiking-in-iceland">hiking in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Hut and package prices are FÍ's 2026 rates, and the trail's opening depends on snow and road openings each year. Bus timetables and Landmannalaugar parking rules are set each spring; check fi.is, the bus operators and safetravel.is before you go.",
        "sources": [
            ("Trails: Laugavegur (Ferðafélag Íslands)", "https://www.fi.is/en/hiking-trails/trails/view/laugavegur"),
            ("Online booking: huts and packages (Ferðafélag Íslands)", "https://vinna.fi.is/en/boka/"),
            ("Hut: Emstrur (Ferðafélag Íslands)", "https://www.fi.is/en/mountain-huts/all-mountain-huts/emstrur"),
            ("Trails: Fimmvörðuháls, with Þórsmörk huts (Ferðafélag Íslands)", "https://www.fi.is/en/moya/adverts/429"),
            ("Highland Bus: Reykjavík to Landmannalaugar (Icelandia)", "https://www.icelandia.com/tours/highland-bus-landmannalaugar"),
            ("Landmannalaugar parking (Parka)", "https://parka.is/parking/landmannalaugar/"),
            ("Hiking and trekking (SafeTravel)", "https://safetravel.is/outdoors/hiking-trekking/"),
        ],
    },
    # ------------------------------------------------------------------
    # 3. FIMMVÖRÐUHÁLS
    # ------------------------------------------------------------------
    {
        "slug": "fimmvorduhals-hike",
        "cluster": "hiking",
        "pillar": False,
        "short": "Fimmvörðuháls: Hiking Between Two Glaciers",
        "title": "Fimmvörðuháls Hike: Skógar to Þórsmörk Between Two Glaciers (2027)",
        "description": "The Fimmvörðuháls hike from Skógar to Þórsmörk: route, distance, huts, the 2010 craters, season, safety and the August 2026 warning about new crevasses.",
        "category": "Hiking · Multi-day treks",
        "teaser": "Waterfalls, new lava and a pass between two glaciers.",
        "image": "hx-solheimajokull",
        "image_alt": "The ash-streaked ice of Sólheimajökull, an outlet of Mýrdalsjökull, with a waterfall in the cliffs above",
        "stats": [
            ("~25 km", "Skógar to Þórsmörk, FÍ's figure"),
            ("~1,000 m", "Climb from Skógar to the pass"),
            ("2010", "Eruption that formed Magni and Móði"),
            ("25 Aug 2026", "Safety warning issued for the route"),
        ],
        "body": """
<p>The Fimmvörðuháls hike crosses a high pass between the Eyjafjallajökull and Mýrdalsjökull glaciers, from Skógafoss on the south coast to the valley of Þórsmörk. It is about 25 km with roughly 1,000 m of climbing, and takes one long day or two shorter ones with a night in a hut. On the way you pass dozens of waterfalls and the craters of the 2010 eruption.</p>
<p class="callout"><strong>Safety warning, August 2026:</strong> on 25 August 2026 Ferðafélag Íslands, Útivist and the Dagrenning rescue team strongly advised against hiking Fimmvörðuháls. Glacier retreat had opened ravines and crevasses between the two huts on the pass. Check fi.is and safetravel.is for the latest before you plan this hike.</p>
<!--TOC-->
<h2>Is it safe to hike Fimmvörðuháls right now?</h2>
<p>As of late October 2026, the last official word is a warning against crossing. The Icelandic Tourist Board passed on the warning on 25 August 2026. It said glacier retreat had opened new ravines and crevasses on the section between Baldvinsskáli and Fimmvörðuhálsskáli, where hikers used to cross snow and ice. Steep scree slopes had formed, and heavy rain had made parts of the trail impassable.</p>
<p>Iceland Review reported that snow bridges over glacial streams were singled out as especially dangerous. The organisations said they were looking for a new, safer route around the affected section. We found no notice that the warning had been lifted. Before the 2027 season, check whether a new route has been marked, and treat the crossing as a serious mountain journey, not a maintained path.</p>
<h2>How long is the Fimmvörðuháls hike?</h2>
<p>FÍ gives the route as 25 km in two stages: 12 km from Skógar to the Baldvinsskáli hut and 13 km from there to Þórsmörk. Other sources give 22 to 24 km, depending on where you start and finish in Þórsmörk. Fit hikers walk it in one day of about 8 to 11 hours. Splitting it with a night at the hut on the pass makes it far more relaxed.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Distance</th><th>Time</th><th>What to expect</th></tr></thead>
<tbody>
<tr><td>Skógar to Baldvinsskáli</td><td>12 km</td><td>4–5 h</td><td>About 1,000 m up past the Skógá waterfalls</td></tr>
<tr><td>Baldvinsskáli to Þórsmörk</td><td>13 km</td><td>4–6 h</td><td>Over the pass, craters, ridges, steep descent</td></tr>
</tbody></table></div>
""" + _map(
            "Map of Iceland hiking trails showing Fimmvörðuháls between Skógar and Þórsmörk and the Laugavegur Trail",
            "Fimmvörðuháls links Skógar on the south coast with Þórsmörk, where the Laugavegur Trail ends.",
        ) + """
<h2>What do you see on the Fimmvörðuháls trail?</h2>
<p>The first half is a waterfall walk. A steep staircase of about 370 steps climbs beside Skógafoss, and the path then follows the Skógá river upstream past more than 20 waterfalls. About 8 km in, a footbridge crosses the river and is a good place to fill water bottles. The last 4 km to the hut are mostly on a gravel track.</p>
<p>The second half crosses the pass. About 3 km beyond Baldvinsskáli you reach Goðahraun, the lava field from the 2010 eruption. The eruption began on the night of 20 March 2010 on the northern part of the pass. Its two new craters were named Magni and Móði, after the sons of Thor, a fitting name so close to Þórsmörk.</p>
<p>From the craters the trail passes a memorial to three travellers who died in a snowstorm on the pass in May 1970. It then descends the steep slope of Brattafönn and crosses Heljarkambur, a narrow ridge with a chain on the most exposed part. After the views from Morinsheiði comes Kattarhryggir, another narrow ridge, and finally the steep path down Strákagil into the green birch woods of Goðaland.</p>
<h2>Which direction should you hike Fimmvörðuháls?</h2>
<p>Most people walk from Skógar to Þórsmörk. The climb is more gradual from the south, and you have the waterfalls in front of you all the way up. Hikers who have just finished the <a href="/blog/laugavegur-trail">Laugavegur Trail</a> often walk it the other way, from Þórsmörk to Skógar, to reach the Ring Road and the bus.</p>
<h2>Where do you sleep on Fimmvörðuháls?</h2>
<p>There are two huts near the top of the pass. Baldvinsskáli, run by FÍ, sits at about 900 m and sleeps 16 in a dormitory. It has a small kitchen with gas stoves, but FÍ says there is no fresh water at the hut, so you must carry enough for the hike and your stay. A night cost about ISK 17,000–18,000 in 2026. Útivist runs Fimmvörðuhálsskáli nearby.</p>
<p>Camping near Baldvinsskáli is possible, but FÍ warns the ground is poor for tent pegs and there is no shelter, so it is not an option in bad weather. In Þórsmörk you can stay at Útivist's hut at Básar in Goðaland or FÍ's Langidalur hut, 2 km further across the Krossá footbridge.</p>
<h2>When can you hike Fimmvörðuháls?</h2>
<p>The trail is generally passable from about late June to mid-September. FÍ gives an average season of 20 or 25 June to 15 September, depending on snow. In summer, daytime temperatures are typically 5–14°C, but it can freeze at night on the pass. The pass is often snow-covered well into summer, and Brattafönn can stay snowy and slippery. Outside summer the huts are unstaffed and the crossing is for experienced winter mountaineers only.</p>
<h2>How hard is the Fimmvörðuháls hike?</h2>
<p>Fimmvörðuháls is a demanding hike even in good conditions. The climb is long, the descent into Þórsmörk is steep, and the two ridges are exposed, so take care if you dislike heights. The weather near the pass changes quickly. FÍ notes that wind above about 10–12 m/s makes hiking difficult, and fog can make the markers hard to follow.</p>
<ul>
<li>Check the forecast at vedur.is and leave a travel plan at safetravel.is.</li>
<li>Carry a map, GPS or phone with offline maps, waterproofs, warm layers, a first-aid kit and spare dry clothes.</li>
<li>Do not hike alone, and consider a guide while the warning stands.</li>
<li>Phone coverage is patchy; in an emergency call 112.</li>
</ul>
<p>Never cross a snow bridge over a stream or step onto glacier ice. If you want to walk on a glacier, join a guided tour at nearby <a href="/places/solheimajokull">Sólheimajökull</a>; our <a href="/blog/glacier-hiking-iceland">glacier hiking guide</a> explains the options.</p>
<h2>How do you get to Skógar and Þórsmörk?</h2>
<p>Skógar is on the Ring Road east of <a href="/places/seljalandsfoss">Seljalandsfoss</a>, with a car park at the foot of Skógafoss. Summer highland buses and public Strætó buses link Skógar with Reykjavík, and highland buses also run between Þórsmörk and Reykjavík. Þórsmörk is reached only by a rough highland track with unbridged rivers, so most hikers leave the car behind and use the bus.</p>
<p>If the crossing stays closed, you can still enjoy the lower half: walk up the Skógá river as far as the footbridge and back, about 16 km return. For other routes, see our guide to <a href="/blog/hiking-in-iceland">hiking in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. The warning against crossing Fimmvörðuháls was issued on 25 August 2026 and we found no notice that it had been lifted; the route may be changed for 2027. Check fi.is, utivist.is and safetravel.is before you go.",
        "sources": [
            ("Warning: dangerous conditions on the Fimmvörðuháls hiking trail (Icelandic Tourist Board)", "https://www.ferdamalastofa.is/en/news/category/1/warning-dangerous-conditions-on-the-fimmvorduhals-hiking-trail"),
            ("Fimmvörðuháls dangerous conditions warning (Iceland Review)", "https://www.icelandreview.com/travel/safety/fimmvorduhals-dangerous-conditions-hiking-warning-2026/"),
            ("Trails: Fimmvörðuháls (Ferðafélag Íslands)", "https://www.fi.is/en/moya/adverts/429"),
            ("Hut: Fimmvörðuháls / Baldvinsskáli (Ferðafélag Íslands)", "https://fi.is/en/mountain-huts/all-mountain-huts/fimmvorduhals-baldvinsskali"),
            ("Fimmvörðuháls (Wikipedia)", "https://en.wikipedia.org/wiki/Fimmv%C3%B6r%C3%B0uh%C3%A1ls"),
            ("Skógafoss waterfall guide (Perlan)", "https://perlan.is/articles/skogafoss-waterfall-iceland-guide"),
            ("Online booking: huts and packages (Ferðafélag Íslands)", "https://vinna.fi.is/en/boka/"),
        ],
    },
    # ------------------------------------------------------------------
    # 4. EASY HIKES
    # ------------------------------------------------------------------
    {
        "slug": "easy-hikes-iceland",
        "cluster": "hiking",
        "pillar": False,
        "short": "Easy Hikes in Iceland Under 3 Hours",
        "title": "Easy Hikes in Iceland: 10 Short Walks Under 3 Hours (2027)",
        "description": "Easy hikes in Iceland under three hours: Svartifoss, Reykjadalur, Fjaðrárgljúfur, Skógafoss, Hverfjall, Hengifoss and more, with distances, times and tips.",
        "category": "Hiking · Day hikes",
        "teaser": "Waterfalls, canyons, craters and a hot river, all in an afternoon.",
        "image": "hx-reykjadalur",
        "image_alt": "Steam rising from the Reykjadalur hot river valley at sunrise",
        "stats": [
            ("~370", "Steps up beside Skógafoss"),
            ("5.8 km", "Svartifoss loop in Skaftafell, about 2 h"),
            ("~3 km", "Each way to the Reykjadalur hot river"),
            ("128 m", "Height of Hengifoss in East Iceland"),
        ],
        "body": """
<p>The best easy hikes in Iceland are short walks to waterfalls, canyons, craters and hot rivers that take under three hours and start from a car park. Svartifoss in Skaftafell, the Reykjadalur hot river, the rim of Fjaðrárgljúfur canyon, the stairs beside Skógafoss and the climb up Hverfjall crater are all good choices. Most are on or near the Ring Road and open in summer without special gear.</p>
<!--TOC-->
<h2>Which easy hikes in Iceland are best?</h2>
<p>These ten walks give the most reward for the least effort. Times are return walking times in good summer conditions.</p>
<div class="table-wrap"><table>
<thead><tr><th>Hike</th><th>Region</th><th>Distance</th><th>Time</th></tr></thead>
<tbody>
<tr><td>Skógafoss stairs</td><td>South coast</td><td>About 370 steps</td><td>10–15 min up</td></tr>
<tr><td>Sólheimajökull glacier front</td><td>South coast</td><td>Short path</td><td>15–20 min each way</td></tr>
<tr><td>Hverfjall crater</td><td>Mývatn, north</td><td>Short, steep path</td><td>20–30 min up</td></tr>
<tr><td>Fjaðrárgljúfur canyon rim</td><td>South, near Kirkjubæjarklaustur</td><td>About 2 km return</td><td>45–60 min</td></tr>
<tr><td>Almannagjá, Þingvellir</td><td>Golden Circle</td><td>Short walk</td><td>Under 1 h</td></tr>
<tr><td>Svartifoss</td><td>Skaftafell</td><td>Short return path</td><td>About 1.5 h</td></tr>
<tr><td>Svartifoss–Sjónarsker–Sel loop</td><td>Skaftafell</td><td>5.8 km</td><td>About 2 h</td></tr>
<tr><td>Laugahraun lava loop</td><td>Landmannalaugar</td><td>4.3 km</td><td>1.5–2 h</td></tr>
<tr><td>Hengifoss</td><td>East Iceland</td><td>About 300 m climb</td><td>About 2 h</td></tr>
<tr><td>Reykjadalur hot river</td><td>Hveragerði</td><td>About 7 km return</td><td>2–3 h with a bath</td></tr>
</tbody></table></div>
""" + _map(
            "Map of Iceland hiking trails including Reykjadalur, Skaftafell and Svartifoss, Hverfjall and Stuðlagil",
            "Short hikes marked on the map include the Reykjadalur hot river, Skaftafell and Svartifoss, Hverfjall crater at Mývatn and Stuðlagil canyon.",
        ) + """
<h2>What are the easiest hikes on the south coast?</h2>
<p>The easiest south coast hikes are the Skógafoss stairs, the walk to Sólheimajökull and the rim of Fjaðrárgljúfur. All three sit just off the Ring Road and fit easily into a day of driving.</p>
<h3>Skógafoss stairs and the Skógá river</h3>
<p>Skógafoss drops 60 m from a cliff right beside the car park. A staircase of about 370 steps climbs to a viewing platform at the top, which takes 10 to 15 minutes. From there a path follows the river upstream past more than 20 smaller waterfalls. Walk 30 minutes and turn back, or keep going as long as you like. This is the start of the Fimmvörðuháls trail, so do not continue onto the high pass; our <a href="/blog/fimmvorduhals-hike">Fimmvörðuháls guide</a> explains why.</p>
<h3>Sólheimajökull glacier front</h3>
<p>From the car park at <a href="/places/solheimajokull">Sólheimajökull</a>, an easy path of about 15 to 20 minutes leads to the front of the glacier and its small lagoon. Stop at the edge. Walking on the ice is only safe with a guide, crampons and an ice axe.</p>
<h3>Fjaðrárgljúfur canyon</h3>
<p>Fjaðrárgljúfur is a mossy canyon about 2 km long and up to about 100 m deep, near Kirkjubæjarklaustur. A marked path of about 2 km return runs along the rim from the lower car park, with viewing platforms over the gorge. Allow 45 to 60 minutes. Parking at the lower lot cost ISK 1,000 for a small car in 2026, paid by app. The path can close in the spring thaw, roughly March to May, to protect the ground, and it is icy in winter.</p>
<h2>What are the best short hikes in Skaftafell?</h2>
<p>The best short hike in <a href="/places/skaftafell">Skaftafell</a> is the walk to Svartifoss, a waterfall framed by dark basalt columns that formed about 300,000 years ago. The return walk from the visitor centre takes about 1.5 hours with a steady climb. For a little more, the Svartifoss–Sjónarsker–Sel loop is 5.8 km and about two hours. Vatnajökull National Park rates it easy. It passes the waterfalls Hundafoss and Magnúsarfoss, a viewpoint at Sjónarsker and an old turf house at Sel.</p>
<h2>Which easy hikes are near Reykjavík?</h2>
<p>Near Reykjavík, the walk to the Reykjadalur hot river and a stroll through Almannagjá at Þingvellir are the best easy options.</p>
<h3>Reykjadalur hot river</h3>
<p>The trail starts at a car park north of Hveragerði, about 45 minutes from Reykjavík. It is about 3 km each way to the bathing area of <a href="/places/reykjadalur">Reykjadalur</a>, with a fairly steep climb at the start. Most people take 45 minutes to an hour each way, so allow about three hours with a bath. Boardwalks and simple screens line the bathing area, but there are no changing rooms. Bathe only in the marked section: some springs in the valley are close to boiling.</p>
<h3>Almannagjá, Þingvellir</h3>
<p>At Þingvellir, a path leads down from the Hakið visitor centre through the Almannagjá rift, between walls of rock pulled apart by the separating tectonic plates. It is an easy walk, and you can extend it to the Öxarárfoss waterfall. It works all year, but wear grips in winter.</p>
<p class="callout"><strong>Easy is relative in Iceland.</strong> Even a one-hour walk can turn cold and wet in minutes. Wear a waterproof jacket, take a warm layer and gloves, and check the weather before you set off.</p>
<h2>What are the best easy hikes in the north and east?</h2>
<p>In the north, Hverfjall crater at Mývatn is the classic short climb. In the east, Hengifoss and the viewpoints at Stuðlagil are the best options.</p>
<h3>Hverfjall crater</h3>
<p>Hverfjall is a tephra ring crater about 1 km across, formed around 2,800 years ago. A clear path climbs to the rim in about 20 to 30 minutes from the car park, and you can walk part or all of the way round. The loose gravel is steep, so wear shoes with good grip.</p>
<h3>Hengifoss</h3>
<p><a href="/places/hengifoss">Hengifoss</a> falls about 128 m into a gorge banded with red clay. The path climbs about 300 m, fairly steeply, passing Litlanesfoss and its basalt columns halfway. Allow about two hours return. It is the most strenuous walk on this list, but still easy to fit into a morning.</p>
<h3>Stuðlagil</h3>
<p>At Stuðlagil canyon, a short path from the car park on the west side leads to viewing platforms over the basalt columns. The east side needs a much longer walk of about 5 km each way, so pick the west side for a quick visit.</p>
<h2>Is there an easy hike in the highlands?</h2>
<p>Yes. At Landmannalaugar, the Laugahraun lava loop is about 4.3 km with only about 115 m of climbing and takes 1.5 to 2 hours. It crosses a lava field of black obsidian between coloured rhyolite mountains. Getting there is the hard part: you need a 4x4 on the F-roads or the summer highland bus. See our <a href="/blog/landmannalaugar-hiking">Landmannalaugar hiking guide</a> for details.</p>
<h2>What should you know before an easy hike in Iceland?</h2>
<ul>
<li><strong>Parking:</strong> many popular trailheads now charge for parking, usually by app with number-plate cameras.</li>
<li><strong>Footwear:</strong> paths are often gravel, mud or rock. Wear waterproof walking shoes or boots.</li>
<li><strong>Winter:</strong> short days and ice change everything. Bring microspikes from about November to April.</li>
<li><strong>Stay on the path:</strong> rope lines protect fragile moss, and leaving the path harms it for decades.</li>
<li><strong>Tell someone:</strong> SafeTravel suggests leaving a note in your car window saying where you have gone and for how long.</li>
</ul>
<p>Ready for something longer? Our guide to <a href="/blog/hiking-in-iceland">hiking in Iceland</a> covers full-day hikes and multi-day treks, and our <a href="/blog/iceland-hiking-packing-list">hiking packing list</a> tells you what to bring.</p>
""",
        "checked_note": "Facts checked October 2026. Parking fees and seasonal path closures change, especially at Fjaðrárgljúfur in spring. Check conditions with the national park or landowner and the weather at vedur.is before you go.",
        "sources": [
            ("Svartifoss and Skaftafell trails (Vatnajökull National Park)", "https://www.vatnajokulsthjodgardur.is/en/destination-svartifoss"),
            ("Fjaðrárgljúfur Canyon travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/Fjadrargljufur"),
            ("Skógafoss waterfall guide (Perlan)", "https://perlan.is/articles/skogafoss-waterfall-iceland-guide"),
            ("Hverfjall crater (Perlan)", "https://perlan.is/articles/hverfjall-crater-volcano"),
            ("Hengifossárgil gorge (Visit East Iceland)", "https://east.is/en/unsorted/nature/hengifossargil-gorge"),
            ("Reykjadalur hot spring hike (Happy Campers)", "https://happycampers.is/reykjadalur/"),
            ("Landmannalaugar hiking guide (Arctic Adventures)", "https://adventures.is/blog/landmannalaugar-hiking-guide/"),
            ("Hiking and trekking (SafeTravel)", "https://safetravel.is/outdoors/hiking-trekking/"),
        ],
    },
    # ------------------------------------------------------------------
    # 5. LANDMANNALAUGAR
    # ------------------------------------------------------------------
    {
        "slug": "landmannalaugar-hiking",
        "cluster": "hiking",
        "pillar": False,
        "short": "Landmannalaugar Hiking: Trails, Roads and Tips",
        "title": "Landmannalaugar Hiking: Best Trails, F-Roads, Parking and Buses (2027)",
        "description": "Landmannalaugar hiking guide: Bláhnúkur, Brennisteinsalda, Laugahraun and more, plus F-roads, highland buses, parking rules and the hot spring.",
        "category": "Hiking · Highlands",
        "teaser": "Coloured mountains, steaming vents and a hot spring at the trailhead.",
        "image": "hx-crater-lakes",
        "image_alt": "A blue crater lake beside a moss-green mountain in Iceland's southern highlands",
        "stats": [
            ("~945 m", "Summit of Bláhnúkur, the classic climb"),
            ("~1477", "Year the Laugahraun lava field erupted"),
            ("ISK 1,500", "Parking for a car up to 5 seats, 2026"),
            ("36–40°C", "Water in the Landmannalaugar hot spring"),
        ],
        "body": """
<p>Landmannalaugar is the best place for hiking in Iceland's highlands: a valley of coloured rhyolite mountains, black lava and steaming vents, with a natural hot spring next to the trailhead. The classic day hikes are Bláhnúkur, Brennisteinsalda and the Laugahraun lava loop. You can only get there in summer, roughly late June to September, by 4x4 on the F-roads or by highland bus.</p>
<!--TOC-->
<h2>What are the best hikes in Landmannalaugar?</h2>
<p>The best hikes in Landmannalaugar are Bláhnúkur for the view, Brennisteinsalda for the colours and steam, and the Laugahraun loop for an easy introduction. All start from the hut and campsite. Distances and times vary a little between sources, depending on the exact route.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trail</th><th>Return distance</th><th>Time</th><th>Climb</th><th>Level</th></tr></thead>
<tbody>
<tr><td>Grænagil canyon</td><td>About 2 km</td><td>About 1 h</td><td>Minimal</td><td>Easy</td></tr>
<tr><td>Laugahraun lava loop</td><td>About 4.3 km</td><td>1.5–2 h</td><td>About 115 m</td><td>Easy</td></tr>
<tr><td>Brennisteinsalda</td><td>About 6.5–8 km</td><td>2–3 h</td><td>About 255–300 m</td><td>Moderate</td></tr>
<tr><td>Bláhnúkur</td><td>About 4–5.7 km</td><td>2.5–3.5 h</td><td>About 300–320 m</td><td>Steep</td></tr>
<tr><td>Brennisteinsalda–Bláhnúkur loop</td><td>About 11 km</td><td>4–6 h</td><td>About 620 m</td><td>Challenging</td></tr>
<tr><td>Suðurnámur ridge</td><td>About 9.3 km</td><td>3–4.5 h</td><td>About 440 m</td><td>Challenging</td></tr>
<tr><td>Ljótipollur crater lake</td><td>About 13.3 km</td><td>4–6 h</td><td>About 340 m</td><td>Moderate</td></tr>
</tbody></table></div>
<h3>Bláhnúkur</h3>
<p>Bláhnúkur, the "blue peak", rises to about 945 m just south of the hut. FÍ describes a route of about 4 km with a climb of just over 300 m, taking about three hours. Cross the stream from Grænagil near the hut, and the path climbs steadily up grey scree to a summit with views over the whole coloured valley. You can go down the same way or take the steeper marked path west into Grænagil.</p>
<h3>Brennisteinsalda</h3>
<p>Brennisteinsalda, about 855 m, means roughly "sulphur wave", and its slopes are streaked with yellow, red and green. The trail crosses the Laugahraun lava field, passes active fumaroles and climbs steeply up the back of the mountain to a broad top. Plan on two to three hours. It is also the first climb of the <a href="/blog/laugavegur-trail">Laugavegur Trail</a>, which continues south to Hrafntinnusker.</p>
<h3>Laugahraun</h3>
<p>The Laugahraun lava field, formed in an eruption around 1477, lies right behind the hut. The loop across it is the easiest good walk here: about 4.3 km over black obsidian and moss, with views of the rhyolite slopes. Combine it with Brennisteinsalda or Bláhnúkur for a full day.</p>
<h3>Longer day hikes</h3>
<p>For a bigger day, the Brennisteinsalda–Bláhnúkur loop links both summits in about 11 km. Suðurnámur follows a high ridge west of the valley. Ljótipollur, the "ugly puddle", is in fact a striking red crater lake to the north. Higher routes can hold snow into early July.</p>
""" + _map(
            "Map of Iceland hiking trails showing Landmannalaugar at the start of the Laugavegur Trail",
            "Landmannalaugar sits at the northern end of the Laugavegur Trail, inland from the south coast.",
        ) + """
<h2>How do you get to Landmannalaugar?</h2>
<p>You get to Landmannalaugar by highland bus or by driving a 4x4 on the F-roads. There is no route for normal cars.</p>
<h3>By highland bus</h3>
<p>Summer highland buses run daily from the BSÍ terminal in Reykjavík, roughly from late June to early September. The ride takes about four hours, arriving around midday. Buses usually leave again mid-afternoon, which gives you time for a short hike and a bath, but not for the longer trails. For a full day of hiking, stay overnight. Bus passengers do not need a parking reservation.</p>
<h3>By 4x4 on the F-roads</h3>
<p>Three F-roads lead in. The F208 from the north is the easiest approach, with no river crossings until the final stretch. The F208 from the south and the F225 both cross rivers. The last 2.5 km into Landmannalaugar are on the F224, which has two fords just before the hut area.</p>
<p>Small SUVs are not recommended through those fords, even if they are 4x4s. Park at the northern car park (P1) instead and walk over the footbridge. Rental insurance usually does not cover water damage, so never cross a river you are unsure about. The roads usually open between mid and late June, and some open later, so check the road map at umferdin.is before you go.</p>
<h2>Do you need to book parking at Landmannalaugar?</h2>
<p>Yes, if you drive your own car and arrive between 9:00 and 16:00 in summer. In 2026 the rule applied from 20 June to 13 September, and bookings opened on 1 April. A car with up to five seats paid ISK 1,500, a car with six to nine seats ISK 2,450 and a motorcycle ISK 750.</p>
<p>Book through the Parka app or website, or via the Environment Agency. Outside 9:00 to 16:00 you need no booking, but every vehicle still pays the fee, and cameras read number plates. The agency says the daily slots sold out on most days in 2024, so book as soon as you know your date. Hiking elsewhere in the Fjallabak Nature Reserve needs no reservation.</p>
<p class="callout"><strong>Arrive early.</strong> The buses arrive around midday. Reach Landmannalaugar before 9:00 and you will have the trails, the parking and the hot spring almost to yourself.</p>
<h2>Can you bathe in the hot spring at Landmannalaugar?</h2>
<p>Yes. A natural pool next to the campsite, where hot water from under the lava mixes with cold streams, is open to everyone. The water is usually about 36–40°C. The toilets, open around the clock, are covered by the parking or service fee. Bathe after your hike, not before.</p>
<h2>Where can you stay at Landmannalaugar?</h2>
<p>You can stay in the FÍ hut, which sleeps 78, or at the campsite beside it. Both fill up in July and August, so book early on the FÍ website. The hut has a kitchen and bunks; bring your own sleeping bag and food.</p>
<h2>When is the best time to hike in Landmannalaugar?</h2>
<p>July and August are the best months for hiking in Landmannalaugar. All trails are normally open and you have very long days. In late June the lower trails open first, while Suðurnámur and other high routes can hold snow into July. September is quieter, but rain is more likely and early snow can close high trails. Outside summer the huts are locked and the F-roads are closed to normal traffic.</p>
<h2>How do you stay safe hiking in Landmannalaugar?</h2>
<ul>
<li>Stay on marked paths. The ground near the vents is hot and unstable, and the moss is fragile.</li>
<li>Expect cold even in summer, and carry waterproofs, a warm layer, a hat and gloves.</li>
<li>Glacial streams rise in the afternoon and after rain. Do not wade water above your knees if you have no experience.</li>
<li>Check the forecast at vedur.is, talk to the hut warden, and leave a travel plan at safetravel.is.</li>
<li>Phone coverage is limited. In an emergency call 112.</li>
</ul>
<h2>What else is near Landmannalaugar?</h2>
<p>Landmannalaugar is the start of the Laugavegur Trail. On the highland roads around it you can also reach the <a href="/places/crater-lakes">crater lakes</a> of Veiðivötn and, further south-east, <a href="/places/maelifell">Mælifell</a> on its black sand plain. For more trails across the country, see our guide to <a href="/blog/hiking-in-iceland">hiking in Iceland</a>, and check our <a href="/blog/iceland-hiking-packing-list">packing list</a> before you go.</p>
""",
        "checked_note": "Facts checked October 2026. Parking rules and fees are the 2026 figures and are set again each spring. F-road opening dates change every year; check umferdin.is, vedur.is and safetravel.is before you travel.",
        "sources": [
            ("Trails: Bláhnúkur í Laugum (Ferðafélag Íslands)", "https://www.fi.is/en/hiking-trails/trails/blahnukur-i-laugum"),
            ("Landmannalaugar hiking guide (Arctic Adventures)", "https://adventures.is/blog/landmannalaugar-hiking-guide/"),
            ("The Brennisteinsalda hike (The Photo Hikes)", "https://thephotohikes.com/the-brennisteinsalda-hike-in-landmannalaugar/"),
            ("Landmannalaugar FAQ: reservations and access (Environment Agency of Iceland)", "https://ust.is/english/visiting-iceland/protected-areas/south/fjallabak-nature-reserve/landmannalaugar/faq"),
            ("Landmannalaugar parking (Parka)", "https://parka.is/parking/landmannalaugar/"),
            ("Trails: Laugavegur, with hut capacities (Ferðafélag Íslands)", "https://www.fi.is/en/hiking-trails/trails/view/laugavegur"),
            ("Landmannalaugar (Wikipedia)", "https://en.wikipedia.org/wiki/Landmannalaugar"),
        ],
    },
    # ------------------------------------------------------------------
    # 6. PACKING LIST
    # ------------------------------------------------------------------
    {
        "slug": "iceland-hiking-packing-list",
        "cluster": "hiking",
        "pillar": False,
        "short": "Iceland Hiking Packing List: What to Bring",
        "title": "Iceland Hiking Packing List: Day Hikes, Hut Treks and Camping (2027)",
        "description": "Iceland hiking packing list: clothing layers, boots, rain gear, navigation, river-crossing shoes, hut and camping kit, and safety items for day hikes and treks.",
        "category": "Hiking · Planning",
        "teaser": "The checklist for wind, rain, rivers and long highland days.",
        "image": "hx-vestrahorn",
        "image_alt": "A walker in a blue jacket crossing black dunes below the jagged peaks of Vestrahorn",
        "stats": [
            ("5–14°C", "Typical summer daytime range on Fimmvörðuháls"),
            ("112", "Emergency number, including mountain rescue"),
            ("2–3", "Hikers linking arms to wade a river"),
            ("Own bag", "Sleeping bag and food needed in FÍ huts"),
        ],
        "body": """
<p>Your Iceland hiking packing list should start with a waterproof jacket and trousers, warm layers, a hat and gloves, sturdy waterproof boots, a map and navigation, and enough food and water. Bring these on every hike, in every season. For hut treks add a sleeping bag and cooking food; for camping add a strong tent; for highland routes add light shoes for wading rivers. Below are checklists for each type of trip.</p>
<!--TOC-->
<h2>What should you pack for hiking in Iceland?</h2>
<p>Pack for cold, wind and rain, whatever the forecast. Ferðafélag Íslands (FÍ) says every hiker should always carry navigation tools and wind- and waterproof clothing, regardless of season, weather or trip length. In summer, daytime temperatures on the high passes are often only about 5–14°C, and it can freeze at night. SafeTravel warns that hypothermia is common in Iceland even in summer.</p>
<p>The trick is layers. A base layer that wicks sweat, a warm mid layer and a waterproof shell let you adjust as the weather swings from sun to sleet. Avoid cotton, which stays wet and cold.</p>
<h2>What is on the day hike checklist?</h2>
<p>For a day hike of up to six or seven hours, pack:</p>
<ul>
<li><strong>Waterproof, windproof jacket</strong> with a hood that fits over a hat.</li>
<li><strong>Waterproof overtrousers</strong>, ideally with side zips to pull on over boots.</li>
<li><strong>Base layer</strong> of merino wool or synthetic fabric.</li>
<li><strong>Warm mid layer:</strong> a fleece or light insulated jacket.</li>
<li><strong>Hiking trousers</strong> that dry quickly; no jeans.</li>
<li><strong>Warm hat and gloves</strong>, even in July.</li>
<li><strong>Waterproof hiking boots</strong> with ankle support and good grip, already broken in.</li>
<li><strong>Wool hiking socks</strong>, plus a spare pair.</li>
<li><strong>Daypack</strong> of about 20–30 litres with a rain cover or a liner bag.</li>
<li><strong>Water</strong>, at least 1–1.5 litres, and a bottle you can refill from clear streams where it is safe.</li>
<li><strong>Food:</strong> lunch and high-energy snacks.</li>
<li><strong>Navigation:</strong> phone with offline maps and the route downloaded, plus a paper map.</li>
<li><strong>Charged phone and power bank.</strong></li>
<li><strong>Small first-aid kit</strong> with blister plasters.</li>
<li><strong>Sunglasses and sunscreen:</strong> the sun is low and bright, and snow reflects it.</li>
<li><strong>Swimsuit and small towel</strong> if you are walking to a hot spring such as <a href="/places/reykjadalur">Reykjadalur</a>.</li>
</ul>
<p>SafeTravel also suggests leaving a note in your car window saying where you have gone and when you expect to be back.</p>
""" + _map(
            "Map of Iceland hiking trails from day hikes near Reykjavík to multi-day treks in the highlands",
            "Iceland's main hiking routes, from day hikes near Reykjavík to the Laugavegur and Hornstrandir. Pack for the route you choose.",
        ) + """
<h2>What extra should you pack for a hut-to-hut trek?</h2>
<p>For a hut trek such as the <a href="/blog/laugavegur-trail">Laugavegur Trail</a>, take everything on the day hike list, plus:</p>
<ul>
<li><strong>Backpack</strong> of about 40–55 litres with a waterproof liner.</li>
<li><strong>Sleeping bag:</strong> FÍ huts provide bunks, but you must bring your own bag.</li>
<li><strong>All your food:</strong> huts have kitchens with gas stoves and pans, but FÍ notes they do not sell hot meals.</li>
<li><strong>River-crossing shoes:</strong> sandals with straps or old trainers. SafeTravel says these are better than crossing barefoot.</li>
<li><strong>Quick-dry towel</strong> for river crossings and showers.</li>
<li><strong>Spare dry clothes</strong> in a waterproof bag, kept for the hut.</li>
<li><strong>Warm hut layer:</strong> a down or synthetic jacket for evenings.</li>
<li><strong>Trekking poles</strong>, useful on descents and in rivers.</li>
<li><strong>Headtorch</strong> for early or late-season trips, when nights get dark.</li>
<li><strong>Earplugs</strong> for busy dormitories.</li>
<li><strong>Rubbish bags:</strong> you carry out everything you bring in.</li>
<li><strong>Cash or card</strong> for paid showers at the huts.</li>
</ul>
<p>Check your water plan for each stop. FÍ says there is no fresh water at the Baldvinsskáli hut on Fimmvörðuháls, for example, so you must carry enough for the hike and the night. See our <a href="/blog/fimmvorduhals-hike">Fimmvörðuháls guide</a> for the current warning on that route.</p>
<h2>What extra should you pack for camping?</h2>
<p>Camping cuts costs and gives you more freedom, but adds weight. On top of the hut list, pack:</p>
<ul>
<li><strong>Tent built for strong wind</strong>, with plenty of strong pegs. Practise pitching it before the trip.</li>
<li><strong>Warm sleeping bag</strong> rated for night temperatures around freezing.</li>
<li><strong>Insulated sleeping mat.</strong></li>
<li><strong>Stove, fuel and pot:</strong> you cannot fly with gas canisters, so buy them in Iceland.</li>
<li><strong>Lighter and spare.</strong></li>
<li><strong>Eye mask</strong> for the bright summer nights.</li>
</ul>
<p>Camp only at designated campsites, which on the main trails are next to the huts. Book them ahead in July and August.</p>
<h2>What safety gear do you need for hiking in Iceland?</h2>
<ul>
<li><strong>Travel plan:</strong> leave one at safetravel.is and with someone at home.</li>
<li><strong>Navigation:</strong> GPS or phone, map and compass, and the skills to use them. Markers can vanish in fog.</li>
<li><strong>Power bank</strong> with enough charge for several days.</li>
<li><strong>Emergency shelter or foil blanket.</strong></li>
<li><strong>Whistle</strong> to attract attention.</li>
<li><strong>Personal locator beacon or satellite messenger</strong> for remote highland routes, as SafeTravel suggests.</li>
<li><strong>Emergency numbers:</strong> 112 by phone, or 00 354 570 2112 from a satellite phone.</li>
</ul>
<p class="callout"><strong>Cross rivers together.</strong> SafeTravel advises crossing in groups of two or three with arms linked at the elbows, with backpack straps loosened, and in the morning when the water is usually lower. If in doubt, ask the warden or wait.</p>
<h2>What changes in spring, autumn and winter?</h2>
<p>Outside summer you need warmer and more specialist kit. Add a thicker insulated jacket, warmer gloves and a spare pair, a buff or balaclava, and a headtorch for the short days. Bring microspikes or crampons for icy paths; many popular trails, including Fjaðrárgljúfur and the paths in <a href="/places/skaftafell">Skaftafell</a>, are icy from about November to April. Pack a spare power bank too, because batteries drain fast in the cold. Do not walk onto glaciers on your own at any time of year. Join a guided tour instead; our <a href="/blog/glacier-hiking-iceland">glacier hiking guide</a> explains what the operators provide.</p>
<h2>How do you keep your gear dry?</h2>
<p>Keep your gear dry by packing it in layers of waterproofing, not by trusting the backpack. Rain in Iceland often blows sideways, and a pack cover alone will not stop it.</p>
<ul>
<li><strong>Pack liner:</strong> a large waterproof bag inside your backpack.</li>
<li><strong>Dry bags:</strong> separate bags for your sleeping bag, spare clothes and electronics.</li>
<li><strong>Zip bags</strong> for your phone, map and documents.</li>
<li><strong>Dry hut clothes:</strong> keep one set that never leaves its bag on the trail.</li>
</ul>
<h2>What should you leave at home?</h2>
<ul>
<li><strong>Cotton clothing and jeans</strong>, which stay wet and cold.</li>
<li><strong>An umbrella</strong>: the wind makes it useless.</li>
<li><strong>Brand-new boots</strong> you have not walked in.</li>
<li><strong>Heavy extras.</strong> SafeTravel warns that an overloaded backpack can ruin a trip.</li>
</ul>
<h2>Where can you buy or rent hiking gear in Iceland?</h2>
<p>Reykjavík has outdoor shops where you can buy stove fuel, and some companies rent camping gear. Prices in Iceland are high, so bring your boots and clothing from home and consider renting only bulky items such as a tent. Before you go, read our guide to <a href="/blog/hiking-in-iceland">hiking in Iceland</a> to choose your route, and our <a href="/blog/easy-hikes-iceland">easy hikes</a> if you are starting small. For more general packing tips, see the <a href="/blog/best-time-to-visit-iceland">best time to visit Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Hut facilities and rules vary by route and year; check the hut operator's page before you go, and check vedur.is and safetravel.is before every hike.",
        "sources": [
            ("Hiking and trekking (SafeTravel)", "https://safetravel.is/outdoors/hiking-trekking/"),
            ("What to bring (Ferðafélag Íslands)", "https://www.fi.is/en/hiking-trails/what-to-bring"),
            ("Trails: Fimmvörðuháls (Ferðafélag Íslands)", "https://www.fi.is/en/moya/adverts/429"),
            ("Hut: Fimmvörðuháls / Baldvinsskáli (Ferðafélag Íslands)", "https://fi.is/en/mountain-huts/all-mountain-huts/fimmvorduhals-baldvinsskali"),
            ("Fjaðrárgljúfur Canyon travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/Fjadrargljufur"),
        ],
    },
]
