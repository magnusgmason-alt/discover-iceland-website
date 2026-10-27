"""Long-form content for the place pages at /places/<slug>.

Keys match the slugs in highlights_content.py (entries that have "ll").
Each entry: intro (list of paragraphs), facts (label, value) pairs,
getting (getting there), when (best time), tips (list).
"""

PLACES = {
    "jokulsarlon": {
        "intro": [
            "Jökulsárlón is Iceland's most famous glacier lagoon. Icebergs break off the front of Breiðamerkurjökull, an outlet glacier of Vatnajökull, and drift slowly across the lagoon towards a short river that carries them out to the sea.",
            "The lagoon has grown quickly as the glacier has retreated, and it is now one of the deepest lakes in Iceland. Seals often swim between the icebergs, and the ice changes shape and colour every day, from milky white to deep blue and ash-striped black.",
            "Across the Ring Road bridge is Diamond Beach, where chunks of ice wash up on black sand and glitter in the low sun.",
        ],
        "facts": [("Region", "South-east, Vatnajökull"), ("From Reykjavík", "About 370 km, 4.5–5 hours"), ("Road", "Right beside Route 1"), ("Best for", "Icebergs, seals, Diamond Beach")],
        "getting": "Jökulsárlón sits directly on Route 1, about an hour west of Höfn and 50 minutes east of Skaftafell. There is a large car park, a café and toilets. Most visitors stay nearby rather than doing it as a day trip from Reykjavík.",
        "when": "Any time of year. Boat tours on the lagoon usually run from spring to autumn. Winter brings fewer people, frozen edges and the chance of northern lights over the ice.",
        "tips": ["Walk along the shore away from the car park for quieter views.", "Cross to Diamond Beach at sunrise or sunset.", "Never climb onto icebergs, on the shore or in the water: they can roll without warning."],
    },
    "breidamerkurjokull": {
        "intro": [
            "Breiðamerkurjökull is the outlet glacier that feeds Jökulsárlón. It flows down from Vatnajökull in a wide tongue striped with dark moraine, the rock and ash the ice has carried for centuries.",
            "From the lagoon shore you can follow those dark bands back up towards the ice cap. In winter, natural ice caves form inside the glacier, and they are the reason many tours start here.",
        ],
        "facts": [("Region", "South-east, Vatnajökull"), ("From Reykjavík", "About 370 km, 4.5–5 hours"), ("Access", "View from Jökulsárlón; on the ice only with a guide"), ("Best for", "Glacier views, winter ice caves")],
        "getting": "Park at Jökulsárlón on Route 1 and walk along the lagoon's western shore for views of the glacier front. Ice cave and glacier tours meet nearby and use super jeeps to reach the ice.",
        "when": "The views work all year. Ice cave tours run in the cold months, usually from about November to March.",
        "tips": ["Do not walk onto the glacier on your own: crevasses and thin ice are hidden.", "Bring binoculars for the glacier front.", "Book winter ice cave tours early."],
    },
    "fjallsarlon": {
        "intro": [
            "Fjallsárlón is a smaller, quieter glacier lagoon about ten minutes west of Jökulsárlón. Here the glacier, Fjallsjökull, comes right down to the water, so you get a much closer look at the ice front itself.",
            "It is a good stop if Jökulsárlón is busy, and many people prefer its wilder feel.",
        ],
        "facts": [("Region", "South-east, Vatnajökull"), ("From Reykjavík", "About 360 km, 4.5 hours"), ("Road", "Short gravel road off Route 1"), ("Best for", "Close-up glacier front, fewer crowds")],
        "getting": "Turn off Route 1 at the sign for Fjallsárlón, about 10 km west of Jökulsárlón. A short track leads to the car park and a café; the lagoon is a few minutes' walk.",
        "when": "All year. Boat tours to the glacier front run in the warmer months.",
        "tips": ["Combine it with Jökulsárlón on the same stop.", "The light on the ice is best early and late in the day.", "Stay on the shore; the lagoon edges can be soft."],
    },
    "ice-caves": {
        "intro": [
            "Every winter, meltwater carves natural ice caves inside Vatnajökull's outlet glaciers. Inside, the old, dense ice glows deep blue, and no two seasons are the same: the caves form, change and collapse each year.",
            "They can only be visited with a licensed glacier guide, who checks each cave's safety daily and provides helmets and crampons.",
        ],
        "facts": [("Region", "South-east, Vatnajökull"), ("Season", "Usually about November to March"), ("Access", "Guided tours only"), ("Best for", "Blue ice, winter adventure")],
        "getting": "Most tours meet near Jökulsárlón on Route 1 and drive to the ice in super jeeps. A few operators also run summer ice cave tours in other glaciers, such as Katla's ice cave near Vík.",
        "when": "The natural Vatnajökull caves are a winter experience, when the ice is cold and stable. Tours can be cancelled at short notice for weather or safety.",
        "tips": ["Book well ahead for December to February.", "Wear warm, waterproof layers and sturdy boots.", "Never enter an ice cave without a guide."],
    },
    "glacier-hikes": {
        "intro": [
            "A guided glacier hike is one of the best ways to feel the scale of Iceland's ice. With crampons and an ice axe, you walk among ridges, crevasses and meltwater channels on a living glacier.",
            "Skaftafell's glacier tongues and Sólheimajökull on the south coast are the most popular places to go.",
        ],
        "facts": [("Region", "Skaftafell and the South Coast"), ("Season", "All year"), ("Access", "Guided tours only"), ("Best for", "Walking on the ice")],
        "getting": "Tours meet at Skaftafell visitor centre or at the Sólheimajökull car park, both just off Route 1. Some also offer pick-ups from Reykjavík for Sólheimajökull.",
        "when": "Glacier hikes run all year. Summer brings longer days; in winter the ice is often bluer and the crowds smaller.",
        "tips": ["Wear waterproof hiking boots that take crampons.", "Choose a longer tour if you want to see deeper ice formations.", "Never walk onto a glacier without a guide."],
    },
    "skaftafell": {
        "intro": [
            "Skaftafell is the hiking heart of Vatnajökull National Park: a green oasis between black sand plains and glacier tongues. Trails lead to waterfalls, viewpoints and the edge of the ice.",
            "The most popular walk climbs to Svartifoss, a waterfall framed by dark basalt columns. Another easy trail leads to the front of Skaftafellsjökull.",
        ],
        "facts": [("Region", "Vatnajökull National Park"), ("From Reykjavík", "About 330 km, 4 hours"), ("Facilities", "Visitor centre, campsite, café"), ("Best for", "Hikes, Svartifoss, glacier views")],
        "getting": "Skaftafell is signposted off Route 1, about 50 minutes west of Jökulsárlón. All trails start from the visitor centre car park.",
        "when": "Summer for the full range of trails; winter for glacier tours and quiet, snowy walks on the main paths.",
        "tips": ["Allow about 1.5 hours return for Svartifoss.", "Many glacier hikes and ice cave tours start here.", "Check trail conditions at the visitor centre in winter."],
    },
    "vatnajokull": {
        "intro": [
            "Vatnajökull is the largest ice cap in Iceland and covers about 8 percent of the country. Beneath it lie active volcanoes, and from its edges dozens of outlet glaciers spill down towards the lowlands.",
            "Vatnajökull National Park, a UNESCO World Heritage Site, protects the ice cap and the land around it, from Skaftafell in the south to Jökulsárgljúfur and Dettifoss in the north.",
        ],
        "facts": [("Region", "South-east and the interior"), ("Protected", "Vatnajökull National Park, UNESCO"), ("Best bases", "Skaftafell, Jökulsárlón, Höfn"), ("Best for", "Glaciers, lagoons, ice caves")],
        "getting": "You see Vatnajökull's outlet glaciers from Route 1 for hours between Skaftafell and Höfn. The ice cap itself is reached only on guided tours, such as snowmobile or super jeep trips.",
        "when": "The southern edge is accessible all year. Highland parts of the park open only in summer.",
        "tips": ["Base yourself near Skaftafell or Höfn for a few nights.", "Combine a glacier hike, a lagoon and an ice cave in winter.", "Watch for wind warnings on this stretch of road."],
    },
    "solheimajokull": {
        "intro": [
            "Sólheimajökull is an outlet glacier of Mýrdalsjökull and the easiest glacier to reach from Reykjavík. Its ash-streaked tongue ends in a small lagoon just a short walk from the car park.",
            "It is the most popular place in Iceland for a first glacier hike, and the retreating ice shows clearly how fast glaciers are changing.",
        ],
        "facts": [("Region", "South Coast"), ("From Reykjavík", "About 160 km, 2 hours"), ("Road", "Short road off Route 1"), ("Best for", "First glacier hike, easy access")],
        "getting": "Turn off Route 1 onto road 221 between Skógafoss and Vík. From the car park it is an easy walk of about 15–20 minutes to the glacier front.",
        "when": "All year. Guided hikes run daily in most weather.",
        "tips": ["Walk to the viewpoint without a guide, but go onto the ice only with one.", "Combine with Skógafoss and Seljalandsfoss on a south coast day.", "Wear sturdy shoes; the path can be muddy or icy."],
    },
    "gullfoss": {
        "intro": [
            "Gullfoss, the 'golden falls', is one of Iceland's most powerful waterfalls. The Hvítá river drops in two steps, about 32 metres in total, into a narrow canyon, throwing up clouds of spray that often catch a rainbow.",
            "It is a highlight of the Golden Circle, together with Geysir and Þingvellir. In the early 1900s, plans to dam the river were fought by Sigríður Tómasdóttir, whose story is told on a plaque at the falls.",
        ],
        "facts": [("Region", "Golden Circle"), ("From Reykjavík", "About 120 km, 1.5–2 hours"), ("Height", "About 32 m in two steps"), ("Best for", "Power, rainbows, winter ice")],
        "getting": "Follow the Golden Circle route via Þingvellir and Geysir; Gullfoss is about 10 km past Geysir on road 35. There is a visitor centre with a café and toilets above the falls.",
        "when": "All year. Summer brings the most water; in winter the canyon fills with ice and snow.",
        "tips": ["Walk both the upper and lower paths for different views.", "Expect spray: bring a rain jacket.", "Paths close in icy conditions; respect the barriers."],
    },
    "seljalandsfoss": {
        "intro": [
            "Seljalandsfoss is the waterfall you can walk behind. The stream drops about 60 metres from an old sea cliff, and a path loops around the back of the curtain of water.",
            "A short walk north along the cliffs leads to Gljúfrabúi, a smaller waterfall hidden inside a narrow canyon.",
        ],
        "facts": [("Region", "South Coast"), ("From Reykjavík", "About 130 km, 1.5–2 hours"), ("Height", "About 60 m"), ("Best for", "Walking behind a waterfall")],
        "getting": "Seljalandsfoss is just off Route 1 on road 249, clearly visible from the main road. There is a car park with paid parking and toilets.",
        "when": "All year, but the path behind the falls usually closes when it is icy in winter. Summer evenings bring golden light from the west.",
        "tips": ["Wear a waterproof jacket and shoes with grip.", "Don't miss Gljúfrabúi, a few minutes' walk away.", "Come early or late to avoid the tour buses."],
    },
    "hengifoss": {
        "intro": [
            "Hengifoss is one of Iceland's tallest waterfalls, at about 128 metres. It plunges into a gorge whose walls are banded with thin red clay layers between dark basalt, a striking sight in any weather.",
            "On the way up, the trail passes Litlanesfoss, a smaller waterfall framed by tall basalt columns.",
        ],
        "facts": [("Region", "East Iceland"), ("From Egilsstaðir", "About 35 km, 30–40 minutes"), ("Height", "About 128 m"), ("Hike", "40–60 minutes each way")],
        "getting": "Drive south from Egilsstaðir along Lake Lagarfljót to the car park on road 933. The trail climbs steadily up the gorge to the falls.",
        "when": "Best from late spring to autumn. In winter the path can be icy and snowy.",
        "tips": ["Wear hiking boots; the path is steep in places.", "Stop at Litlanesfoss on the way.", "Combine with a drive around Lagarfljót."],
    },
    "kirkjufell": {
        "intro": [
            "Kirkjufell, the 'church mountain', rises above Grundarfjörður on the north coast of Snæfellsnes. With the small Kirkjufellsfoss waterfall in front, it is one of the most photographed views in Iceland.",
            "In winter, photographers line up by the falls hoping for northern lights over the peak.",
        ],
        "facts": [("Region", "Snæfellsnes, West Iceland"), ("From Reykjavík", "About 180 km, 2.5 hours"), ("Height", "About 463 m"), ("Best for", "Photography, northern lights")],
        "getting": "Follow road 54 around Snæfellsnes to Grundarfjörður. The car park for Kirkjufellsfoss is just west of town.",
        "when": "All year. Summer for green slopes and long evenings, winter for snow and aurora.",
        "tips": ["Climbing the mountain is steep and dangerous; enjoy it from below.", "Stay on the paths around the waterfall.", "Combine with a full loop of the Snæfellsnes peninsula."],
    },
    "reynisfjara": {
        "intro": [
            "Reynisfjara is the black sand beach near Vík, with tall basalt columns, a sea cave and the Reynisdrangar sea stacks rising from the surf.",
            "It is also one of the most dangerous beaches in Iceland. Sudden 'sneaker waves' surge far up the sand without warning and have swept people into the sea.",
        ],
        "facts": [("Region", "South Coast, near Vík"), ("From Reykjavík", "About 185 km, 2.5 hours"), ("Danger", "Sneaker waves, strong currents"), ("Best for", "Basalt columns, sea stacks")],
        "getting": "Turn off Route 1 onto road 215 just west of Vík. There is a car park, toilets and a café.",
        "when": "All year. Follow the warning lights at the entrance; on red days, stay off the beach.",
        "tips": ["Stay well back from the water and never turn your back on the waves.", "Keep children close.", "See the sea stacks from Vík's own beach too."],
    },
    "stokksnes": {
        "intro": [
            "Stokksnes is a black sand peninsula near Höfn, with grass-tufted dunes and the jagged Vestrahorn mountain rising behind. It is one of the most photographed coastal landscapes in Iceland.",
            "The land is private, and a small entry fee is paid at the Viking Café at the start of the road.",
        ],
        "facts": [("Region", "South-east, near Höfn"), ("From Höfn", "About 15 minutes"), ("Access", "Entry fee at the Viking Café"), ("Best for", "Dunes, Vestrahorn, reflections")],
        "getting": "Turn off Route 1 about 10 km east of Höfn and follow the gravel road to the Viking Café, then on to the dunes and the beach.",
        "when": "All year. Calm days at low tide give reflections of Vestrahorn in the wet sand.",
        "tips": ["Check the tide for mirror reflections.", "Visit at sunrise or sunset for golden light on the grass.", "Stay off fragile dune grass where marked."],
    },
    "snaefellsnes": {
        "intro": [
            "Snæfellsnes is often called 'Iceland in miniature': in one peninsula you find lava fields, black and golden beaches, fishing villages, sea cliffs and the Snæfellsjökull glacier.",
            "The western tip is protected as Snæfellsjökull National Park, with stops like Arnarstapi, Hellnar and Djúpalónssandur.",
        ],
        "facts": [("Region", "West Iceland"), ("From Reykjavík", "About 2–2.5 hours"), ("Loop", "Road 54 around the peninsula"), ("Best for", "A varied 1–2 day trip")],
        "getting": "Drive north from Reykjavík on Route 1 to Borgarnes, then take road 54 west. A full loop of the peninsula makes a long day; two days is more relaxed.",
        "when": "All year. Summer is greener; winter brings snow and the chance of northern lights.",
        "tips": ["Stay overnight in Stykkishólmur or Grundarfjörður.", "Walk the coastal path between Arnarstapi and Hellnar.", "Check road conditions in winter on the mountain passes."],
    },
    "vestrahorn": {
        "intro": [
            "Vestrahorn is a dramatic mountain of gabbro and granophyre rising straight from the black sands of Stokksnes. Its jagged ridges change by the minute as cloud pours over the top.",
            "Seen across the grass-topped dunes, it is one of the great views of the south-east.",
        ],
        "facts": [("Region", "South-east, near Höfn"), ("From Höfn", "About 15 minutes"), ("Access", "Via Stokksnes; entry fee at the Viking Café"), ("Best for", "Mountain views, photography")],
        "getting": "Follow the Stokksnes road from Route 1, east of Höfn. Viewpoints are all along the beach and the dunes.",
        "when": "All year. Calm, clear mornings and evenings give the best light and reflections.",
        "tips": ["Wait out the clouds: they often lift.", "Low tide gives the best reflections.", "Bring a wide-angle lens or phone setting."],
    },
    "maelifell": {
        "intro": [
            "Mælifell is a near-perfect volcanic cone covered in bright green moss, standing alone on the black Mælifellssandur desert north of Mýrdalsjökull.",
            "It is one of the highlands' most striking sights, and one of the hardest to reach.",
        ],
        "facts": [("Region", "Southern highlands"), ("Access", "F-roads, 4x4 only, summer"), ("Rivers", "Unbridged river crossings"), ("Best for", "Highland adventure")],
        "getting": "Mælifell lies on highland F-roads that open only in summer. You need a 4x4 and experience with river crossings, or join a guided super jeep tour.",
        "when": "Only in the summer highland season, usually July to early September, once the F-roads are open.",
        "tips": ["Check road.is for F-road status before you go.", "Cross rivers early in the day, when the water is lower.", "A guided tour is the safest way to visit."],
    },
    "east-fjords-road": {
        "intro": [
            "In the East Fjords the Ring Road and the coast road wind in and out of long fjords, past steep mountains, small fishing villages and very little traffic.",
            "It is one of the quietest and most scenic drives in Iceland, with stops like Fáskrúðsfjörður, Stöðvarfjörður and Djúpivogur, and a detour to colourful Seyðisfjörður.",
        ],
        "facts": [("Region", "East Iceland"), ("Main roads", "Route 1 and road 96"), ("Bases", "Egilsstaðir, Seyðisfjörður, Djúpivogur"), ("Best for", "Quiet scenic driving")],
        "getting": "Drive between Höfn and Egilsstaðir along the coast. Allow extra time: the fjords add many kilometres, and you will want to stop.",
        "when": "Best from late spring to autumn. In winter, mountain passes such as the road to Seyðisfjörður can close in snow.",
        "tips": ["Fill up on fuel when you can; stations are spread out.", "Look for reindeer in winter and spring.", "Check road.is for pass closures."],
    },
    "studlagil": {
        "intro": [
            "Stuðlagil is a canyon lined with tall basalt columns, with a blue-green river running through it. The columns were hidden under the river until a hydropower dam upstream lowered the water level in the 2000s.",
            "It quickly became one of East Iceland's top sights.",
        ],
        "facts": [("Region", "East Iceland, Jökuldalur"), ("From Egilsstaðir", "About 70 km, around 1 hour"), ("Access", "Viewpoint (west) or riverbed walk (east)"), ("Best for", "Basalt columns, blue water")],
        "getting": "Take road 923 off Route 1 into Jökuldalur. On the west side, a short path from the Grund farm car park leads to viewing platforms. On the east side, a walk of about 5 km each way from near Klaustursel, passing Stuðlafoss, brings you down to the river.",
        "when": "Late June to late July usually has the bluest water. From August, overflow from the reservoir upstream can turn the river grey.",
        "tips": ["Choose the east side if you want to walk among the columns.", "Arrive early in summer to avoid crowds.", "Parking is paid on both sides."],
    },
    "geysir": {
        "intro": [
            "The Geysir geothermal area gave its name to every geyser in the world. The Great Geysir itself is mostly quiet now, but its neighbour Strokkur erupts every few minutes, shooting boiling water high into the air.",
            "Around them, hot pools, steaming vents and coloured clay make it one of the easiest places to see Iceland's geothermal power up close.",
        ],
        "facts": [("Region", "Golden Circle"), ("From Reykjavík", "About 110 km, 1.5 hours"), ("Strokkur", "Erupts every 5–10 minutes"), ("Best for", "Geysers, hot springs")],
        "getting": "Geysir is on road 35, between Þingvellir and Gullfoss on the Golden Circle. There is a large visitor centre across the road.",
        "when": "All year. Winter eruptions against the cold air look especially dramatic.",
        "tips": ["Stand upwind of Strokkur to avoid the spray.", "Stay on the paths: the ground and water are scalding.", "Wait for a few eruptions to time your photo."],
    },
    "reykjadalur": {
        "intro": [
            "Reykjadalur, the 'steam valley', is a hike to a warm river where you can bathe in the open countryside. Steam rises from vents and pools all along the valley.",
            "Wooden boardwalks and simple changing screens line the bathing area, but there are no facilities beyond the car park.",
        ],
        "facts": [("Region", "Hveragerði, South Iceland"), ("From Reykjavík", "About 45 minutes"), ("Hike", "About 3 km each way, 45–75 min up"), ("Best for", "Bathing in a hot river")],
        "getting": "Drive to Hveragerði on Route 1, then follow signs to the Reykjadalur car park and café at the end of the road. The trail climbs into the valley to the bathing area.",
        "when": "All year, but winter brings snow, ice and short days, and the car park can close in storms.",
        "tips": ["Bathe only in the marked river area; other streams are dangerously hot.", "Bring a towel and wear a swimsuit under your clothes.", "Carry out all your rubbish."],
    },
    "crater-lakes": {
        "intro": [
            "In Iceland's southern highlands, old volcanic craters have filled with bright blue water. Around Veiðivötn there are dozens of lakes in a landscape of black sand, moss and lava.",
            "It is remote, quiet and only reachable in summer.",
        ],
        "facts": [("Region", "Southern highlands"), ("Access", "F-roads, 4x4 only, summer"), ("Bases", "Highland huts, Landmannalaugar"), ("Best for", "Remote landscapes")],
        "getting": "The crater lakes are reached by highland F-roads that require a 4x4. Check which roads are open before setting out, or join a guided highland tour.",
        "when": "Summer only, usually July to early September.",
        "tips": ["Carry extra food, water and fuel.", "Check road.is and vedur.is before you go.", "Leave a travel plan on SafeTravel."],
    },
    "reykjavik": {
        "intro": [
            "Reykjavík is the world's northernmost capital and home to about two thirds of Iceland's people, counting the capital area. It is small, walkable and full of colour.",
            "Hallgrímskirkja church, the Harpa concert hall, the old harbour and the Sun Voyager sculpture are all close together, and every neighbourhood has a geothermal swimming pool.",
        ],
        "facts": [("Region", "Capital area"), ("From Keflavík Airport", "About 45–50 minutes"), ("Getting around", "Walk, bus, or bike"), ("Best for", "Food, culture, pools")],
        "getting": "The Flybus and public bus 55 run from Keflavík Airport to the city. Most sights are within walking distance of the centre.",
        "when": "All year. Summer for long bright nights and festivals; winter for cosy cafés, pools and northern lights trips.",
        "tips": ["Visit a local pool, the Icelandic way to relax.", "Climb Hallgrímskirkja's tower for the view.", "Many day tours pick up from central hotels."],
    },
    "thingvellir": {
        "intro": [
            "Þingvellir is where Iceland's parliament, the Althing, first met in the year 930. The national park, a UNESCO World Heritage Site, lies in a rift valley where the North American and Eurasian plates are slowly pulling apart.",
            "You can walk through the Almannagjá gorge, see the Öxarárfoss waterfall and even snorkel between the plates in the crystal-clear Silfra fissure.",
        ],
        "facts": [("Region", "Golden Circle"), ("From Reykjavík", "About 45 minutes"), ("Protected", "National park, UNESCO"), ("Best for", "History, geology, Silfra")],
        "getting": "Drive north-east from Reykjavík on road 36. There are several car parks with paid parking; the main visitor centre is at Hakið above Almannagjá.",
        "when": "All year. Quiet winter days are beautiful, and the dark skies are good for northern lights.",
        "tips": ["Walk down through Almannagjá from the visitor centre.", "Book Silfra snorkelling in advance.", "Start the Golden Circle here early to beat the buses."],
    },
}
