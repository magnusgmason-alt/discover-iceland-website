"""Hot springs cluster: six journal articles (pillar first)."""

MAP_HS = """<figure class="a-figure a-map"><a href="/assets/img/map-hot-springs-2800.jpg" target="_blank" rel="noopener"><img src="/assets/img/map-hot-springs-1800.jpg" srcset="/assets/img/map-hot-springs-800.jpg 800w, /assets/img/map-hot-springs-1800.jpg 1800w" sizes="(min-width: 800px) 760px, 100vw" alt="{alt}" loading="lazy" decoding="async"></a><figcaption>{caption} Tap to open full size.</figcaption></figure>"""


def _map(alt, caption):
    return MAP_HS.format(alt=alt, caption=caption)


ARTICLES = [
    {
        "slug": "hot-springs-iceland",
        "cluster": "hot-springs",
        "pillar": True,
        "short": "Iceland's Hot Springs and Pools: The Complete Map",
        "title": "Hot Springs in Iceland: The Complete Map of 19 Pools and Lagoons (2027)",
        "description": "Hot springs in Iceland on one map: 19 lagoons, pools and natural springs by region, with 2026 prices, what each is like, winter tips, safety and etiquette.",
        "category": "Hot Springs · Map",
        "teaser": "Nineteen lagoons, village pools and wild springs, region by region.",
        "image": "hx-geysir",
        "image_alt": "Steam rising from hot springs in the Geysir geothermal field on a sunny winter day",
        "stats": [
            ("120+", "Public swimming pools across Iceland"),
            ("Dec 2025", "Icelandic pool culture added to UNESCO's heritage list"),
            ("1891", "Year the Secret Lagoon pool at Flúðir was built"),
            ("36–40°C", "Typical water temperature in the big lagoons"),
        ],
        "body": """
<p>Iceland has hot water almost everywhere, and you can bathe in it in three ways: big designed lagoons with bars and saunas, cheap local swimming pools, and natural springs in the countryside. This guide covers 19 of the best, numbered on our map, from the Blue Lagoon near the airport to a remote seaside pool at the end of a gravel road in the Westfjords. For each one you get where it is, what it is like and roughly what it costs in 2026.</p>
<!--TOC-->
<h2>What are the best hot springs in Iceland?</h2>
<p>The best hot spring depends on how you travel. For a first trip with little time, book Sky Lagoon or the Blue Lagoon near Reykjavík. On the Golden Circle, the Secret Lagoon and Laugarvatn Fontana are easy stops, and the free Reykjadalur hot river is the best natural bath within an hour of the city. On a Ring Road trip, the rebuilt Earth Lagoon at Mývatn, the Forest Lagoon by Akureyri and Vök Baths in the east are all worth a stop.</p>
<ul>
<li><strong>Most famous:</strong> the Blue Lagoon, milky blue water in a lava field on the Reykjanes peninsula.</li>
<li><strong>Best view near the city:</strong> Sky Lagoon, with its infinity edge facing the ocean.</li>
<li><strong>Best wild bath:</strong> Reykjadalur, a warm river at the end of a 3 km hike.</li>
<li><strong>Most atmospheric:</strong> Seljavallalaug, a 1923 pool tucked into a mountain valley.</li>
<li><strong>Best in the north:</strong> Earth Lagoon Mývatn, formerly the Mývatn Nature Baths.</li>
<li><strong>Best for meeting locals:</strong> any town swimming pool, for about ISK 1,500 in Reykjavík.</li>
</ul>
""" + _map(
            "Map of Iceland with 19 numbered hot springs, geothermal lagoons and pools",
            "Iceland's hot springs and pools, numbered 1–19. Orange marks lagoons and pools with facilities; green marks natural and wild springs.",
        ) + """
<h2>What is the difference between a lagoon, a pool and a natural hot spring?</h2>
<p>A lagoon is a commercial spa built around geothermal water, with changing rooms, a bar and timed tickets. A pool is a public swimming pool run by the town, with lanes, hot tubs and very low prices. A natural hot spring is a pool or river in the landscape, often with no facilities at all.</p>
<p>The lagoons cost the most, from about ISK 7,500 to more than ISK 18,000 in 2026, and most ask you to book a time slot. The town pools are where Icelanders actually bathe: there are more than 120 across the country, and in December 2025 Iceland's swimming pool culture was added to UNESCO's list of intangible cultural heritage. Natural springs are often free, but more of them now charge a small fee to pay for toilets, parking and upkeep.</p>
<p>In all three, the same basic rule applies: wash thoroughly before you get in. Our guide to <a href="/blog/iceland-swimming-pool-etiquette">Iceland swimming pool rules</a> explains the shower routine.</p>
<h2>Which hot springs are near Reykjavík?</h2>
<p>Four of the pools on the map are within about 90 minutes of the capital. Two of them, the Blue Lagoon and Sky Lagoon, are the most booked baths in the country.</p>
<h3>1. Blue Lagoon</h3>
<p>The Blue Lagoon sits in a lava field about 20 km from Keflavík Airport and roughly 45–50 minutes from <a href="/places/reykjavik">Reykjavík</a>. Its water comes from the Svartsengi geothermal power plant next door and averages 37–39°C. In 2026 the Comfort ticket starts from about ISK 11,990, with a silica mud mask, a towel and a drink included. Prices change with demand.</p>
<p>The lagoon is close to the Sundhnúkur crater row, which has erupted nine times since December 2023. It has closed or been evacuated several times during that series. Read our <a href="/blog/reykjanes-volcano-guide">Reykjanes volcano guide</a> and check the lagoon's own site before you go.</p>
<h3>2. Sky Lagoon</h3>
<p>Sky Lagoon opened in 2021 at Kársnes harbour in Kópavogur, about 15 minutes' drive from central Reykjavík. Its long infinity edge looks straight over the sea, and the ticket includes a seven-step sauna and cold-plunge ritual. Entry starts from about ISK 13,000–14,000 in 2026, and you must be at least 12 years old. We compare the two in <a href="/blog/blue-lagoon-vs-sky-lagoon">Blue Lagoon vs Sky Lagoon</a>.</p>
<h3>3. Hvammsvík</h3>
<p>Hvammsvík is a set of eight natural-style pools on the shore of Hvalfjörður, about 45 minutes north of Reykjavík. It opened in 2022. Some pools mix with seawater, so their level and temperature change with the tide, and there is a cold ocean plunge too. Entry starts from about ISK 7,900.</p>
<h3>4. Krauma</h3>
<p>Krauma is a small spa beside Deildartunguhver in Borgarfjörður, roughly 1.5 hours from Reykjavík. Deildartunguhver is Europe's highest-flow hot spring, producing about 180 litres per second, and you can see it free from a boardwalk. The spa opened in 2017 and has five warm pools at 37–42°C, a cold tub, saunas and a restaurant. Adult entry was about ISK 7,900 in early 2026.</p>
<h2>Which hot springs are on the Golden Circle?</h2>
<p>The Golden Circle has four good bathing stops within easy reach of <a href="/places/thingvellir">Þingvellir</a>, <a href="/places/geysir">Geysir</a> and Gullfoss. See our <a href="/blog/golden-circle-iceland">Golden Circle guide</a> for the full route.</p>
<h3>5. Laugarvatn Fontana</h3>
<p>Fontana sits on the shore of Lake Laugarvatn, between Þingvellir and Geysir. It has steam rooms built over natural vents, warm mineral baths and a sauna, and you can walk into the cold lake between soaks. The spa closed in October 2025 for a full renovation and reopened on 1 August 2026. Its geothermal bakery, where rye bread bakes overnight in hot sand, runs as a separate tour.</p>
<h3>6. Secret Lagoon</h3>
<p>The Secret Lagoon at Flúðir, known locally as Gamla laugin (the old pool), was built in 1891. It is the oldest swimming pool in Iceland. The water stays at about 38–40°C all year, a small geyser bubbles beside it, and a wooden walkway circles the hot spring area. It has changing rooms and a café, and booking ahead is wise.</p>
<h3>7. Reykjadalur hot river</h3>
<p>Reykjadalur, the steam valley, is a warm river above the town of Hveragerði, about 45 minutes from Reykjavík. You hike about 3 km each way to reach the bathing area, where boardwalks and simple screens line the bank. Bathing is free, and the car park charges an hourly fee. Our <a href="/blog/reykjadalur-hot-river">Reykjadalur hot river guide</a> covers the trail, and the <a href="/places/reykjadalur">Reykjadalur place page</a> has the essentials.</p>
<h3>8. Hrunalaug</h3>
<p>Hrunalaug is a set of small stone-edged pools on a family farm near Flúðir, about five minutes' walk from the parking area. There are three pools, from about 32°C to 40°C, two small changing huts and no showers. In 2026 adults pay about ISK 3,000 and children under 10 go free. Visits are limited to 90 minutes, and soap and glass are not allowed.</p>
<h2>Which hot springs are on the South Coast and in the highlands?</h2>
<p>The south has one of Iceland's most photographed pools, and the highlands have two classic summer soaks at the end of rough roads.</p>
<h3>9. Seljavallalaug</h3>
<p>Seljavallalaug was built by local volunteers in 1923 and is 25 m long and 10 m wide. It sits in a narrow valley below Eyjafjallajökull, a 15–20 minute walk from the car park, east of Seljalandsfoss. Entry is free, with a donation box for cleaning. The water is only lukewarm, typically 20–35°C, and there is just a basic changing shed.</p>
<h3>10. Landmannalaugar</h3>
<p>Landmannalaugar means "the people's pools", and the hot stream beneath the Laugahraun lava field is a famous end to a day's hiking. It is reached only in summer by highland F-road, ideally in a 4x4. In recent summers private cars have needed a pre-booked parking slot and a service fee for daytime arrivals from 20 June to mid-September. See our <a href="/blog/landmannalaugar-hiking">Landmannalaugar hiking guide</a>.</p>
<h3>11. Hveravellir</h3>
<p>Hveravellir is a geothermal area on the Kjölur highland route, road 35, between the south and the north. Its bathing pool sits at about 38–40°C next to a summer mountain lodge, campsite and café. The road is generally open from about mid-June to mid-September, and a small service fee covers the pool, showers and toilets.</p>
<h2>Which hot springs are in North Iceland?</h2>
<p>North Iceland has four of the pools on the map, and they make easy stops on a Ring Road trip through Akureyri and Mývatn.</p>
<h3>12. Earth Lagoon Mývatn (Mývatn Nature Baths)</h3>
<p>The Mývatn Nature Baths opened in 2004 and have been rebuilt and renamed Earth Lagoon Mývatn. The new lagoon reopened in July 2026, about 35% larger, with a swim-in steam cave, a waterfall and two hot tubs. The water is cooled to 36–40°C and entry starts from about ISK 7,900. Read our full <a href="/blog/myvatn-nature-baths">Mývatn Nature Baths guide</a>.</p>
<h3>13. GeoSea</h3>
<p>GeoSea opened in 2018 on the headland above Húsavík harbour. Its infinity pools are filled with geothermally heated seawater from boreholes, at about 38–39°C, and look out over Skjálfandi Bay. It pairs well with a whale-watching trip from the town.</p>
<h3>14. Forest Lagoon</h3>
<p>The Forest Lagoon (Skógarböðin) opened in 2022 in the Vaðlaskógur woods, just across the fjord from Akureyri. The hot water was struck while the Vaðlaheiði road tunnel was being dug. Pools are held at about 37°C, with a cold plunge, a sauna and a swim-up bar. Basic entry was about ISK 7,500 in 2026.</p>
<h3>19. Hofsós pool</h3>
<p>Hofsós swimming pool opened in 2010 on the hillside above the village of Hofsós in Skagafjörður. It was designed by Basalt Architects and seems to run straight into the fjord, with Drangey island beyond. It is a public pool, so it is cheap and the locals use it.</p>
<h2>Which hot springs are in East Iceland?</h2>
<p>The east has one designed spa and one simple set of hot tubs, both handy on a Ring Road day.</p>
<h3>15. Vök Baths</h3>
<p>Vök Baths opened in 2019 on Lake Urriðavatn, about five minutes' drive from Egilsstaðir. Its two floating pools sit level with the lake, so you look straight across the water. Adult entry is about ISK 7,690. It is a good stop on the same day as Hengifoss or Stuðlagil.</p>
<h3>16. Hoffell hot tubs</h3>
<p>The Hoffell hot tubs are a handful of geothermal tubs at Hoffell farm, about 10–15 km from Höfn, near an outlet glacier of Vatnajökull. There are changing rooms with showers, a sauna and toilets. Entry was about ISK 3,500 when we checked, with children under 8 free. Temperatures vary from warm to very hot, so test each tub first.</p>
<h2>Which hot springs are in the Westfjords?</h2>
<p>The Westfjords have two of the most memorable soaks in the country, both on long, quiet drives. Plan them as part of a <a href="/blog/westfjords-road-trip">Westfjords road trip</a>.</p>
<h3>17. Hellulaug</h3>
<p>Hellulaug is a small natural pool right beside the sea at Vatnsfjörður, about 1.5 km from the Flókalundur hotel on road 60. It is about 3–4 m across, around 60 cm deep and roughly 38°C. Entry is free, with a donation canister for upkeep. There are no changing rooms or toilets.</p>
<h3>18. Krossneslaug</h3>
<p>Krossneslaug is a small outdoor pool on the shore at the end of road 643 on the Strandir coast, the far edge of the Westfjords. The water is about 38–40°C, and there are simple changing rooms and showers. It is seasonal, roughly mid-May to the end of August, and charges a small fee.</p>
<h2>How much do Iceland's hot springs cost?</h2>
<p>Prices range from free to about ISK 18,500 for a premium lagoon package. These are adult prices from operators and travel guides checked in 2026; most lagoons use dynamic pricing, so expect changes.</p>
<div class="table-wrap"><table>
<thead><tr><th>#</th><th>Pool</th><th>Region</th><th>Type</th><th>Adult price (2026)</th></tr></thead>
<tbody>
<tr><td>1</td><td>Blue Lagoon</td><td>Reykjanes</td><td>Lagoon</td><td>From about ISK 11,990</td></tr>
<tr><td>2</td><td>Sky Lagoon</td><td>Capital area</td><td>Lagoon</td><td>From about ISK 13,000</td></tr>
<tr><td>3</td><td>Hvammsvík</td><td>Hvalfjörður</td><td>Lagoon</td><td>From about ISK 7,900</td></tr>
<tr><td>4</td><td>Krauma</td><td>Borgarfjörður</td><td>Spa</td><td>About ISK 7,900</td></tr>
<tr><td>5</td><td>Laugarvatn Fontana</td><td>Golden Circle</td><td>Spa</td><td>Paid, check site</td></tr>
<tr><td>6</td><td>Secret Lagoon</td><td>Flúðir</td><td>Old pool</td><td>Paid, book ahead</td></tr>
<tr><td>7</td><td>Reykjadalur</td><td>Hveragerði</td><td>Hot river</td><td>Free; paid parking</td></tr>
<tr><td>8</td><td>Hrunalaug</td><td>Flúðir</td><td>Natural pools</td><td>About ISK 3,000</td></tr>
<tr><td>9</td><td>Seljavallalaug</td><td>South Coast</td><td>Old pool</td><td>Free; donation box</td></tr>
<tr><td>10</td><td>Landmannalaugar</td><td>Highlands</td><td>Hot stream</td><td>Car service fee in summer</td></tr>
<tr><td>11</td><td>Hveravellir</td><td>Highlands</td><td>Natural pool</td><td>Small service fee</td></tr>
<tr><td>12</td><td>Earth Lagoon Mývatn</td><td>North</td><td>Lagoon</td><td>From about ISK 7,900</td></tr>
<tr><td>13</td><td>GeoSea</td><td>Húsavík</td><td>Sea baths</td><td>Paid, book ahead</td></tr>
<tr><td>14</td><td>Forest Lagoon</td><td>Akureyri</td><td>Lagoon</td><td>From about ISK 7,500</td></tr>
<tr><td>15</td><td>Vök Baths</td><td>Egilsstaðir</td><td>Lake baths</td><td>About ISK 7,690</td></tr>
<tr><td>16</td><td>Hoffell</td><td>Near Höfn</td><td>Hot tubs</td><td>About ISK 3,500</td></tr>
<tr><td>17</td><td>Hellulaug</td><td>Westfjords</td><td>Natural pool</td><td>Free; donations</td></tr>
<tr><td>18</td><td>Krossneslaug</td><td>Westfjords</td><td>Pool</td><td>Small fee, summer only</td></tr>
<tr><td>19</td><td>Hofsós pool</td><td>Skagafjörður</td><td>Town pool</td><td>Local pool price</td></tr>
</tbody></table></div>
<p>For the full list of pools you can use for free or nearly free, see <a href="/blog/free-hot-springs-iceland">free hot springs in Iceland</a>.</p>
<h2>Can you visit hot springs in Iceland in winter?</h2>
<p>Yes, and many people think winter is the best time. The lagoons, town pools and most spas open all year, and sitting in 38°C water with snow around you is a highlight of a winter trip. On a clear night at a dark spring you may even see the <a href="/northern-lights">northern lights</a> from the water.</p>
<p>Natural springs are harder in winter. Reykjadalur's trail freezes, often from around mid-November, so you need microspikes and a headlamp. Highland springs such as Landmannalaugar and Hveravellir are cut off when the mountain roads close, and Krossneslaug is a summer pool. In the dark months, plan wild bathing around the few hours of daylight.</p>
<h2>How do you stay safe at Iceland's hot springs?</h2>
<p>Geothermal water can be close to boiling at the source, so only bathe where bathing is allowed and the water has been tested. Stay on marked paths in hot spring areas, because the ground can be a thin crust over scalding mud. People have been badly hurt, and some killed, stepping off the trail in geothermal areas.</p>
<ul>
<li><strong>Test before you get in.</strong> Put a hand in first, especially at natural pools where the inflow is hot.</li>
<li><strong>Do not bathe where it is banned.</strong> Grjótagjá, the cave at Mývatn, is too hot and unpredictable for bathing, and its owners ask visitors to stay out.</li>
<li><strong>Keep soaks short.</strong> Limit time in the hottest water, drink water and get out if you feel dizzy.</li>
<li><strong>Check the weather and roads.</strong> Use vedur.is, road.is and safetravel.is, and for the Blue Lagoon check the volcanic situation too.</li>
<li><strong>Watch children closely.</strong> Natural pools have no lifeguards.</li>
</ul>
<p class="callout"><strong>Leave no trace:</strong> at natural springs, take every bit of rubbish home, never use soap or shampoo in the water, and use the toilets at the car park. Several springs on private land have closed in the past because visitors left a mess.</p>
<h2>What should you bring to a hot spring in Iceland?</h2>
<p>Bring a swimsuit, a quick-dry towel and a plastic bag for wet things. Lagoons rent towels and swimwear, but at natural springs you carry everything. Add a warm hat for winter soaks, sandals or water shoes for rocky pools, and a few coins or a card for honesty boxes and parking. Keep your phone in a dry bag, and never take photos in changing rooms.</p>
<p>For more ideas on where to bathe as you travel, browse our <a href="/highlights">Iceland highlights map</a>. If you like having it all on paper, our <a href="/#guides">printed Complete Guide</a> covers the hot springs region by region.</p>
""",
        "checked_note": "Facts checked October 2026. Lagoon prices are dynamic and change by season and time slot. The Blue Lagoon can close at short notice during volcanic unrest on the Reykjanes peninsula; check vedur.is, safetravel.is and the operator's site before you go.",
        "sources": [
            ("Iceland's geothermal lagoons compared (Iceland Highlights, July 2026)", "https://www.iceland-highlights.com/iceland-geothermal-lagoons-compared/"),
            ("Blue Lagoon admissions rate card 2026 (Blue Lagoon)", "https://www.bluelagoon.com/travel-professionals/BL-ratecard2026"),
            ("Icelandic swimming pool culture inscribed on UNESCO's list (Reykjavík City)", "https://reykjavik.is/en/news/2025/icelandic-swimming-pool-culture-inscribed-unescos-list-intangible-cultural-heritage-humanity"),
            ("Fontana: reopened after renovation (Laugarvatn Fontana)", "https://fontana.is/"),
            ("Earth Lagoon Mývatn: new facilities (Earth Lagoon)", "https://www.earthlagoon.is/new-jar%C3%B0bo%C3%B0in-facility"),
            ("Krauma, Hrunalaug, Hoffell, Hellulaug and Krossneslaug listings (Hot Springs Guides)", "https://www.hotspringsguides.com/country/iceland"),
            ("Landmannalaugar FAQ: reservations and service fee (Environment Agency of Iceland)", "https://www.ust.is/english/visiting-iceland/protected-areas/south/fjallabak-nature-reserve/landmannalaugar/faq/"),
            ("Grjótagjá travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/grjotagja"),
        ],
    },
    {
        "slug": "blue-lagoon-vs-sky-lagoon",
        "cluster": "hot-springs",
        "pillar": False,
        "short": "Blue Lagoon vs Sky Lagoon: Which Should You Book?",
        "title": "Blue Lagoon vs Sky Lagoon: Which to Book, Prices and What's Included (2027)",
        "description": "Blue Lagoon vs Sky Lagoon compared: 2026 prices, what each ticket includes, location, age limits, the Sky Lagoon ritual, eruption closures and which to book.",
        "category": "Hot Springs · Lagoons",
        "teaser": "Two famous lagoons, two very different visits: how to choose.",
        "image": "journal-reykjavik",
        "image_alt": "Reykjavík and Hallgrímskirkja church seen across the bay under heavy cloud",
        "stats": [
            ("ISK 11,990", "Blue Lagoon Comfort ticket, from (2026)"),
            ("12+", "Minimum age at Sky Lagoon"),
            ("7 steps", "Sky Lagoon's sauna and cold-plunge ritual"),
            ("37–39°C", "Average water temperature in the Blue Lagoon"),
        ],
        "body": """
<p>Book Sky Lagoon if you are staying in Reykjavík and want an easy, ocean-view soak with a proper sauna ritual. Book the Blue Lagoon if you want the famous milky-blue water in a lava field and can fit it around your airport transfer. Both cost about the same in 2026, but they feel very different. Here is how they compare on price, setting, what is included and practical details, including the Blue Lagoon's closures during the Reykjanes eruptions.</p>
<!--TOC-->
<h2>Which is better, the Blue Lagoon or Sky Lagoon?</h2>
<p>Neither is better for everyone. The Blue Lagoon is bigger, more dramatic and more famous, with silica mud masks and bright blue water among black lava. Sky Lagoon is calmer and closer to the city, with a sea view and a structured seven-step ritual of hot and cold.</p>
<ul>
<li><strong>Choose the Blue Lagoon</strong> if it is your first trip, you are flying in or out of Keflavík, you are travelling with young children, or the landscape matters most.</li>
<li><strong>Choose Sky Lagoon</strong> if you are based in <a href="/places/reykjavik">Reykjavík</a> without a car, want a sunset or evening visit on a short trip, or love saunas and cold plunges.</li>
</ul>
<h2>How do the Blue Lagoon and Sky Lagoon compare?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Blue Lagoon</th><th>Sky Lagoon</th></tr></thead>
<tbody>
<tr><td>Location</td><td>Lava field near Grindavík, Reykjanes</td><td>Kársnes harbour, Kópavogur</td></tr>
<tr><td>From central Reykjavík</td><td>About 45–50 min</td><td>About 15 min</td></tr>
<tr><td>From Keflavík Airport</td><td>About 20 km</td><td>On the far side of Reykjavík</td></tr>
<tr><td>Entry price (2026)</td><td>From about ISK 11,990</td><td>From about ISK 13,000–14,000</td></tr>
<tr><td>Water</td><td>Milky blue, silica-rich, 37–39°C</td><td>Geothermal water, about 38–40°C</td></tr>
<tr><td>Signature feature</td><td>Silica mud mask, in-water bar</td><td>Ocean-view infinity edge, seven-step ritual</td></tr>
<tr><td>Minimum age</td><td>2 years</td><td>12 years</td></tr>
<tr><td>Opened</td><td>1987</td><td>2021</td></tr>
<tr><td>Volcanic risk</td><td>Has closed during Reykjanes eruptions</td><td>Outside the eruption zone</td></tr>
</tbody></table></div>
<p>Prices are dynamic at both lagoons, so the same ticket can cost more at peak times. Book directly on the operators' sites for the current rate.</p>
""" + _map(
            "Map of Iceland hot springs with the Blue Lagoon, Sky Lagoon and Hvammsvík near Reykjavík",
            "The Blue Lagoon (1), Sky Lagoon (2) and Hvammsvík (3) are all within an hour of Reykjavík.",
        ) + """
<h2>What is included in a Blue Lagoon ticket?</h2>
<p>The Blue Lagoon sells three main day packages, all with timed entry. Each includes the lagoon, the steam bath, the sauna, a colder lagoon, a silica mud mask, a towel, shampoo and conditioner, and a locker.</p>
<ul>
<li><strong>Comfort, from about ISK 11,990:</strong> the basics above plus one drink from the included menu.</li>
<li><strong>Premium, from about ISK 14,990:</strong> adds a bathrobe, two extra masks and a drink of your choice at the in-water bar, plus a small skincare gift.</li>
<li><strong>Signature, from about ISK 18,490:</strong> adds a second drink and a larger skincare gift.</li>
</ul>
<p>The separate Retreat Spa costs much more, from about ISK 79,000. Children aged 2 and over are allowed, and under-15s must be with an adult. Bathrobes and swimsuits can be rented if you forget yours.</p>
<h2>What is included in a Sky Lagoon ticket?</h2>
<p>Sky Lagoon has two main passes, and both include the lagoon, a towel and one journey through the Skjól ritual. The difference is the changing room.</p>
<ul>
<li><strong>Saman, from about ISK 13,000–14,000:</strong> shared public changing rooms.</li>
<li><strong>Sér, from about ISK 16,000–17,000:</strong> a private changing suite, plus Sky Lagoon's body lotion.</li>
</ul>
<p>The Skjól ritual runs in a fixed order: a warm soak in the lagoon, a cold plunge, a sauna with a sea view, a cold mist, a body scrub, a steam room, and a final shower before you go back into the lagoon. It is the main reason many people choose Sky Lagoon. Drinks are extra, from the in-water bar. The minimum age is 12, strictly enforced, and ages 12–14 must be with an adult.</p>
<h2>Is the Blue Lagoon open after the volcanic eruptions?</h2>
<p>Yes, as of October 2026 the Blue Lagoon is open. There has been no eruption since the one on the Sundhnúkur crater row from 16 July to 5 August 2025. But the Icelandic Met Office reported on 30 September 2026 that magma is still building up under Svartsengi, and it considers a new intrusion or eruption the most likely scenario, possibly with short warning.</p>
<p>The lagoon has closed several times since late 2023. It shut as a precaution from 9 November 2023 into December, closed again after eruptions in January, February and March 2024 (the March closure lasted until 7 April), and was evacuated when eruptions began in May 2024 and on 16 July 2025. In November 2024 lava flowed over its car park. Closures often last days to weeks.</p>
<p>If you book the Blue Lagoon, read the cancellation terms, keep a back-up plan, and check vedur.is, safetravel.is and the lagoon's site on the day. Our <a href="/blog/reykjanes-volcano-guide">Reykjanes volcano guide</a> explains the eruptions and how to view them safely.</p>
<p class="callout"><strong>Tip:</strong> if a Reykjanes eruption closes the Blue Lagoon, Sky Lagoon is the easiest swap. It is in the capital area, well away from the eruption zone.</p>
<h2>Which lagoon is easier to get to?</h2>
<p>Sky Lagoon is easier from Reykjavík. It is about 15 minutes by car or taxi, and shuttle transfers can be added to a booking. The Blue Lagoon is 45–50 minutes from the city but only about 20 km from Keflavík Airport, so many people visit on the way in or out. See <a href="/blog/getting-around-iceland">getting around Iceland</a> for transfers and car hire.</p>
<h2>Are there good alternatives to the Blue Lagoon and Sky Lagoon?</h2>
<p>Yes. If the big two are full, too expensive or closed, these are worth a look:</p>
<ul>
<li><strong>Hvammsvík:</strong> eight shoreline pools on Hvalfjörður, about 45 minutes north of Reykjavík, from about ISK 7,900. Some pools rise and fall with the tide. It feels wilder than either big lagoon.</li>
<li><strong>Forest Lagoon:</strong> a woodland lagoon just outside Akureyri in the north, from about ISK 7,500, with pools around 37°C and a swim-up bar. Under-12s are not allowed after 8 pm.</li>
<li><strong>Local pools:</strong> Reykjavík's public pools cost ISK 1,500 for an adult in 2026, with hot tubs and steam rooms. Learn the shower routine first in our <a href="/blog/iceland-swimming-pool-etiquette">swimming pool etiquette guide</a>.</li>
</ul>
<p>For all 19 pools on the map, see our pillar guide to <a href="/blog/hot-springs-iceland">hot springs in Iceland</a>.</p>
<h2>How do you get the most out of your lagoon visit?</h2>
<ul>
<li><strong>Book a time slot early.</strong> Both lagoons use timed entry, and evening and summer slots sell out first.</li>
<li><strong>Protect your hair.</strong> The Blue Lagoon's silica water can leave hair stiff. Use the conditioner provided and keep your hair out of the water if you can.</li>
<li><strong>Shower first.</strong> At both lagoons you shower without your swimsuit before getting in. Divided shower cubicles are available.</li>
<li><strong>Go late in winter.</strong> Short winter days mean you can soak in the dark, with a small chance of northern lights on a clear night.</li>
<li><strong>Add a day nearby.</strong> Pair Sky Lagoon with a Golden Circle day to <a href="/places/thingvellir">Þingvellir</a>, or the Blue Lagoon with the Reykjanes coast.</li>
</ul>
""",
        "checked_note": "Facts checked October 2026. Both lagoons use dynamic pricing, and the Blue Lagoon can close at short notice during volcanic unrest; check the Icelandic Met Office (vedur.is) and safetravel.is before you travel.",
        "sources": [
            ("Blue Lagoon admissions rate card 2026 (Blue Lagoon)", "https://www.bluelagoon.com/travel-professionals/BL-ratecard2026"),
            ("Blue Lagoon (geothermal spa) (Wikipedia)", "https://en.wikipedia.org/wiki/Blue_Lagoon_(geothermal_spa)"),
            ("Ground uplift and magma accumulation continue beneath Svartsengi (Icelandic Met Office)", "https://en.vedur.is/about-imo/news/ground-uplift-and-magma-accumulation-continue-beneath-svartsengi"),
            ("2023–2025 Sundhnúkur eruptions (Wikipedia)", "https://en.wikipedia.org/wiki/2023%E2%80%932025_Sundhn%C3%BAkur_eruptions"),
            ("Iceland's geothermal lagoons compared (Iceland Highlights, July 2026)", "https://www.iceland-highlights.com/iceland-geothermal-lagoons-compared/"),
            ("Complete guide to Sky Lagoon (Northbound)", "https://www.northbound.is/blog/306/complete-guide-to-sky-lagoon-in-Iceland"),
            ("Sky Lagoon Iceland complete guide 2026", "https://www.machupicchu.org/sky-lagoon-iceland-complete-guide-2026-everything-you-need-to-know.htm"),
            ("Hvammsvík Hot Springs (Adventures.com)", "https://adventures.com/iceland/tours/activities/wellness/hvammsvik-hot-springs/"),
        ],
    },
    {
        "slug": "free-hot-springs-iceland",
        "cluster": "hot-springs",
        "pillar": False,
        "short": "Free Hot Springs in Iceland: Where to Bathe",
        "title": "Free Hot Springs in Iceland: Natural Pools, Fees and Etiquette (2027)",
        "description": "Free hot springs in Iceland: the natural pools you can legally use for free or a small fee, from Reykjadalur to Hellulaug, plus etiquette and leave-no-trace.",
        "category": "Hot Springs · Natural pools",
        "teaser": "Wild pools that cost nothing or very little, and how to treat them.",
        "image": "hx-highland-rivers",
        "image_alt": "A moss-green mountain above a braided river and black sand in the Icelandic highlands",
        "stats": [
            ("1923", "Year Seljavallalaug was built by local volunteers"),
            ("25 × 10 m", "Size of the Seljavallalaug pool"),
            ("ISK 3,000", "Hrunalaug adult fee in 2026; under-10s free"),
            ("~38°C", "Water temperature at Hellulaug in the Westfjords"),
        ],
        "body": """
<p>Iceland still has natural hot springs you can use for free, but fewer than you might think, and the list is shrinking. Most good springs are on private land, and several have added a small fee to pay for toilets, parking and repairs. These are the free and nearly-free springs that are legal and open to the public in 2026, what each costs, and the etiquette that keeps them open.</p>
<!--TOC-->
<h2>Are there free hot springs in Iceland?</h2>
<p>Yes. Reykjadalur, Seljavallalaug, Hellulaug and Landbrotalaug cost nothing to bathe in, though some ask for donations or charge for parking. Others, such as Hrunalaug, Hoffell and Hveravellir, now charge a fee of a few thousand krónur or less. That is still far cheaper than a lagoon, which costs from about ISK 7,500 in 2026.</p>
<p>The cheapest reliable hot water in Iceland is often the town swimming pool. In Reykjavík an adult ticket costs ISK 1,500, and every pool has hot tubs.</p>
<h2>Which hot springs in Iceland are free or nearly free?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Spring</th><th>Region</th><th>Cost (2026)</th><th>Facilities</th><th>Season</th></tr></thead>
<tbody>
<tr><td>Reykjadalur</td><td>Hveragerði</td><td>Free; paid parking</td><td>Boardwalk, screens</td><td>All year</td></tr>
<tr><td>Seljavallalaug</td><td>South Coast</td><td>Free; donation box</td><td>Changing shed</td><td>All year</td></tr>
<tr><td>Hellulaug</td><td>Westfjords</td><td>Free; donations</td><td>None</td><td>All year, road permitting</td></tr>
<tr><td>Landbrotalaug</td><td>Snæfellsnes</td><td>Free</td><td>None</td><td>Best in summer</td></tr>
<tr><td>Landmannalaugar</td><td>Highlands</td><td>Car service fee in summer</td><td>Toilets, hut</td><td>Summer only</td></tr>
<tr><td>Hrunalaug</td><td>Flúðir</td><td>About ISK 3,000; under-10s free</td><td>Changing huts</td><td>All year</td></tr>
<tr><td>Hveravellir</td><td>Highlands</td><td>Small service fee</td><td>Showers, toilets</td><td>Summer only</td></tr>
<tr><td>Hoffell hot tubs</td><td>Near Höfn</td><td>About ISK 3,500; under-8s free</td><td>Showers, sauna</td><td>All year</td></tr>
<tr><td>Krossneslaug</td><td>Westfjords</td><td>Small fee</td><td>Changing rooms</td><td>Mid-May to August</td></tr>
</tbody></table></div>
<p>Fees and opening rules change. Check each site before you go, and always pay where a fee or honesty box is posted.</p>
""" + _map(
            "Map of Iceland hot springs, with natural and wild springs marked in green",
            "Green numbers mark natural springs, including Reykjadalur (7), Hrunalaug (8), Seljavallalaug (9), Landmannalaugar (10), Hveravellir (11), Hoffell (16), Hellulaug (17) and Krossneslaug (18).",
        ) + """
<h2>Is Reykjadalur free?</h2>
<p>Yes, bathing in the Reykjadalur hot river is free. You pay only for parking at the trailhead above Hveragerði, by the hour, using an app or the card machine. The bathing area is about 3 km up the valley on foot, with boardwalks and simple screens to change behind. It is the most popular free hot spring near Reykjavík, so arrive early in summer. Our <a href="/blog/reykjadalur-hot-river">Reykjadalur hike guide</a> has the details, and the <a href="/places/reykjadalur">Reykjadalur place page</a> has a quick summary.</p>
<h2>Is Seljavallalaug free?</h2>
<p>Yes. Seljavallalaug, built in 1923, has no entry fee, and a donation box helps pay for cleaning. The 25 m pool sits in a valley below Eyjafjallajökull, a 15–20 minute walk from the car park, off Route 1 east of <a href="/places/seljalandsfoss">Seljalandsfoss</a>. Volunteers clean it once a year. After the 2010 Eyjafjallajökull eruption buried it in ash, they dug it out by hand.</p>
<p>Set your expectations: the water is often only 20–35°C and can be cooler in winter, and the walls are green with algae. There is a basic changing shed with no toilets, no showers and no bins, so take everything back with you.</p>
<h2>Where are the free hot springs in the Westfjords and the west?</h2>
<p>Hellulaug is a small natural pool right by the sea at Vatnsfjörður, about 1.5 km from the Flókalundur hotel on road 60. It is about 3–4 m across and roughly 38°C. It is free, with a donation canister for upkeep, and has no facilities, so change discreetly and use the hotel's services.</p>
<p>Landbrotalaug is a tiny pool off road 54 on the eastern Snæfellsnes peninsula, near Eldborg crater. The main pool fits only two or three people at about 38°C. It is on private land, and the owner allows free public access. It was closed for a period and reopened in 2024, so treat it gently and move on if it is busy.</p>
<p>Krossneslaug, on the Strandir coast, is a proper pool with changing rooms rather than a wild spring, but it costs only a small fee. It opens from about mid-May to the end of August. Plan these on a <a href="/blog/westfjords-road-trip">Westfjords road trip</a>.</p>
<h2>Which hot springs now charge a fee?</h2>
<p>Several springs that were once free now charge, usually to fund toilets, parking and staff. The fee is the price of keeping them open.</p>
<ul>
<li><strong>Hrunalaug</strong> near Flúðir is on a family farm. In 2026 adults pay about ISK 3,000, youth about ISK 2,000 and children under 10 go free. Visits are capped at 90 minutes, and in winter payment works on an honesty system.</li>
<li><strong>Landmannalaugar</strong> in the highlands is free to bathe in, but in recent summers private cars arriving in the daytime from 20 June to mid-September needed a booked parking slot and a service fee. The fee pays for wardens and 24-hour toilets. See our <a href="/blog/landmannalaugar-hiking">Landmannalaugar hiking guide</a>.</li>
<li><strong>Hveravellir</strong> on the Kjölur route charges a small service fee that covers the pool, showers and toilets. The road is open only in summer.</li>
<li><strong>Hoffell hot tubs</strong>, near Höfn and an outlet glacier of <a href="/places/vatnajokull">Vatnajökull</a>, charged about ISK 3,500 when we checked, with children under 8 free.</li>
</ul>
<h2>Which hot springs can you not bathe in?</h2>
<p>Some famous springs are closed to bathing, and you should respect that. Grjótagjá, the lava cave at Mývatn, is too hot and unpredictable for bathing since the Krafla eruptions of 1975–1984 heated its water. Its landowners ask visitors only to look. Nearby Kvennagjá was fenced off by its owners in 2018 after visitors left rubbish and human waste and washed dishes in it.</p>
<p>Many hot streams in geothermal areas are far too hot to touch. Never bathe in a pool or stream unless it is clearly used for bathing, and never step off marked paths at places like Geysir or Reykjadalur. The ground can be a thin crust over boiling mud.</p>
<h2>What is the etiquette at natural hot springs?</h2>
<p>At natural springs there are no showers or staff, so the rules are about respect. Locals are relaxed about bodies, but most visitors wear swimsuits.</p>
<ul>
<li><strong>Pay where asked.</strong> Use the honesty box or app, even if no one is watching.</li>
<li><strong>Share the pool.</strong> Small pools fit only a few people. Do not stay for hours if others are waiting.</li>
<li><strong>Keep it quiet.</strong> No music speakers. Many people come for the peace.</li>
<li><strong>Ask before going nude.</strong> Skinny dipping is generally accepted at remote springs, but ask anyone already there first.</li>
<li><strong>No soap, shampoo or glass.</strong> They pollute the water and break on rocks.</li>
<li><strong>Do not camp at the spring.</strong> Use campsites, and do not drive off the road to reach a pool.</li>
</ul>
<h2>How do you leave no trace at a hot spring?</h2>
<p>Leave the spring exactly as you found it. Most closures in Iceland have followed damage and litter, not overcrowding alone.</p>
<ol>
<li><strong>Use the toilet before you arrive.</strong> Most wild springs have none. Never go near the water.</li>
<li><strong>Pack out everything.</strong> Bottles, food wrappers, tissues and even orange peel stay with you until you find a bin.</li>
<li><strong>Stay on paths.</strong> Moss around springs takes decades to recover once crushed.</li>
<li><strong>Do not build or move rocks.</strong> Leave pools and dams as they are.</li>
<li><strong>Change discreetly.</strong> Use the screens or sheds where they exist, and keep clothes off the vegetation.</li>
</ol>
<p class="callout"><strong>Remember:</strong> the free springs stay free because landowners allow it. One bad visit can close a pool for everyone.</p>
<p>For the paid lagoons and every pool on our map, see the full guide to <a href="/blog/hot-springs-iceland">hot springs in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Fees at natural springs change often, and landowners can close access at any time; check before you go and follow local signs. Highland springs are reachable only when the mountain roads are open in summer.",
        "sources": [
            ("Seljavallalaug travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/seljavallalaug"),
            ("Hrunalaug Hot Spring (Hot Springs Guides)", "https://www.hotspringsguides.com/hot-springs/hrunalaug-hot-spring-iceland"),
            ("Hellulaug Hot Spring (Hot Springs Guides)", "https://www.hotspringsguides.com/hot-springs/hellulaug-hot-spring-iceland"),
            ("Landbrotalaug (Hot Springs Guides)", "https://www.hotspringsguides.com/hot-springs/landbrotalaug-iceland"),
            ("Landmannalaugar FAQ: reservations and service fee (Environment Agency of Iceland)", "https://www.ust.is/english/visiting-iceland/protected-areas/south/fjallabak-nature-reserve/landmannalaugar/faq/"),
            ("Hoffell Hot Tubs (Hot Springs Guides)", "https://www.hotspringsguides.com/hot-springs/hoffell-hot-tubs-iceland"),
            ("Landowners close off natural hot pool (Iceland Monitor)", "https://icelandmonitor.mbl.is/news/nature_and_travel/2018/07/11/landowners_close_off_natural_hot_pool_due_to_total_/"),
            ("Nudity in Iceland: when and where (Guide to Iceland)", "https://guidetoiceland.is/es/historia-y-cultura/getting-naked-in-iceland"),
        ],
    },
    {
        "slug": "reykjadalur-hot-river",
        "cluster": "hot-springs",
        "pillar": False,
        "short": "Reykjadalur Hot River: Hike and Bathing Guide",
        "title": "Reykjadalur Hot Spring: Hiking to Iceland's Hot River (2027 Guide)",
        "description": "Reykjadalur hot spring guide: the 3 km hike from Hveragerði, parking fees, where to bathe in the hot river, water temperatures, winter tips and safety rules.",
        "category": "Hot Springs · Hiking",
        "teaser": "A one-hour walk to a warm river you can bathe in, 45 minutes from Reykjavík.",
        "image": "hx-reykjadalur",
        "image_alt": "Steam rising from the Reykjadalur hot river valley at sunrise",
        "stats": [
            ("~3 km", "Hike each way from the car park to the river"),
            ("340–380 m", "Elevation gain to the bathing area"),
            ("~45 min", "Drive from Reykjavík to Hveragerði"),
            ("Free", "Bathing in the river; parking is paid"),
        ],
        "body": """
<p>Reykjadalur, the "steam valley", is a warm river in the hills above Hveragerði where you can bathe in the open countryside for free. It is about 45 minutes' drive from Reykjavík, then a hike of about 3 km each way, which takes most people 45 minutes to an hour on the way up. Here is how to get there, where to bathe, what it costs and how to stay safe in a valley full of boiling springs.</p>
<!--TOC-->
<h2>What is the Reykjadalur hot spring?</h2>
<p>The Reykjadalur hot spring is a stretch of river warmed by geothermal springs higher up the valley. Hot and cold streams meet, so the water is warm enough to sit in all year. The bathing area has wooden boardwalks along the bank and small screens to change behind. There are no showers, lockers or toilets beyond the car park.</p>
<p>The valley itself steams from vents and bubbling mud pools all the way up. That makes the walk beautiful, but it also means you must stay on the path. Our <a href="/places/reykjadalur">Reykjadalur place page</a> has a quick summary.</p>
""" + _map(
            "Map of Iceland hot springs with Reykjadalur hot river near Hveragerði",
            "Reykjadalur (7) is just north of Hveragerði, close to the Golden Circle and about 45 minutes from Reykjavík.",
        ) + """
<h2>How do you get to Reykjadalur?</h2>
<p>Drive east from Reykjavík on Route 1 for about 45 km to Hveragerði, about 45 minutes in good conditions. Drive through the town and follow signs to the Reykjadalur car park and café at the end of the road, about 2 km north of town. The trail starts here.</p>
<p>Without a car, join a tour from Reykjavík. Some operators also offer horse rides up the valley. See <a href="/blog/getting-around-iceland">getting around Iceland</a> for buses and car hire.</p>
<p>A new paid lagoon, Reykjaböð, has opened at the entrance to the valley. It is a separate ticketed spa reached by road, not the free hot river, so do not mix them up when you navigate.</p>
<h2>How long is the Reykjadalur hike?</h2>
<p>The Reykjadalur hike is about 3 km each way, roughly 6 km return, with 340–380 m of climbing. Most people reach the river in 45 minutes to an hour. Allow three to four hours in total, including time in the water. In winter, add an hour each way.</p>
<ol>
<li><strong>Car park to the first climb (0–1 km):</strong> the steepest part comes early. The path climbs in switchbacks, and the first 30–45 minutes are the hardest.</li>
<li><strong>Into the upper valley (1–2 km):</strong> the path gets easier once the first climb is done. Steam rises from vents on both sides; keep to the trail.</li>
<li><strong>To the bathing area (2–3 km):</strong> the trail reaches the river, where the boardwalks and changing screens begin.</li>
<li><strong>Return the same way:</strong> take care on the descent, where loose gravel and mud cause most slips.</li>
</ol>
<p>The path is gravel with rocky and muddy sections. It is moderate rather than hard, but you need sturdy shoes, ideally waterproof boots. It is not suitable for wheelchairs or buggies. For more walks like this, see our <a href="/blog/easy-hikes-iceland">easy hikes in Iceland</a>.</p>
<h2>How much does Reykjadalur cost?</h2>
<p>Bathing in Reykjadalur is free. The only cost is parking at the trailhead, which is paid by the hour. In 2026 a five-hour stay cost roughly ISK 1,000. You pay with a parking app such as Parka or EasyPark, or at the card machine at the café; cash is not accepted.</p>
<p>The café at the car park has toilets, food and drinks, but its winter hours are reduced. Bring your own water and snacks for the hike.</p>
<h2>Where do you bathe in Reykjadalur, and how hot is the water?</h2>
<p>Bathe only in the marked bathing area along the boardwalks. The temperature changes along the river: it is cooler at the lower end, where a cold stream joins, and warmer upstream. Many people find the middle stretch, around 36–40°C, the most comfortable. The highest part can be uncomfortably hot.</p>
<p>The river is shallow, often only 20–30 cm deep, so you lie or sit in it rather than swim. Test the water with your hand before you get in, and move up or down the boardwalk until it feels right.</p>
<p class="callout"><strong>Safety first:</strong> never touch standing water, mud pools or steam vents in the valley. Water near the springs can be over 100°C, and people have been badly hurt stepping off the path.</p>
<h2>Can you visit Reykjadalur in winter?</h2>
<p>Yes, the trail is open all year with no gate or closing time, and bathing in warm water among snow is unforgettable. But winter makes the hike much harder. The path often freezes from around mid-November, so bring microspikes or ice cleats.</p>
<ul>
<li><strong>Start early.</strong> In December you get only about four hours of daylight. Carry a headlamp anyway.</li>
<li><strong>Keep soaks short.</strong> Limit bathing to 20–30 minutes in winter, so you are not chilled for the walk down.</li>
<li><strong>Check the weather.</strong> Storms can make the access road impassable, and the landowner sometimes closes the car park. Check vedur.is and safetravel.is before you set off.</li>
<li><strong>Bring dry layers.</strong> Change quickly into a warm hat, a dry base layer and gloves.</li>
</ul>
<h2>What should you bring to Reykjadalur?</h2>
<ul>
<li>Swimsuit, worn under your clothes to make changing quicker</li>
<li>Quick-dry towel and a dry bag for wet things</li>
<li>Waterproof jacket and hiking boots</li>
<li>Warm layers, hat and gloves, even in summer</li>
<li>Water and snacks</li>
<li>Microspikes and a headlamp from November to March</li>
<li>A bag for all your rubbish, as there are no bins past the trailhead</li>
</ul>
<h2>What are the rules at Reykjadalur?</h2>
<p>Stay on the marked paths, bathe only in the marked area, and leave nothing behind. These rules protect you from scalding ground and protect the moss, which takes decades to recover.</p>
<ul>
<li>No camping, fires or drones in the valley.</li>
<li>Dogs must be on a lead and kept out of the river.</li>
<li>No soap or shampoo in the water.</li>
<li>Watch children closely at all times; there is no lifeguard.</li>
<li>Change behind the screens and keep noise down.</li>
</ul>
<p>The car park fills by mid-morning on summer weekends. For a quieter soak, go early or on a light summer evening.</p>
<h2>What else can you combine with Reykjadalur?</h2>
<p>Reykjadalur fits neatly into a <a href="/blog/golden-circle-iceland">Golden Circle</a> day. Hveragerði is about 45 minutes from Reykjavík, and from there it is a short drive on to <a href="/places/thingvellir">Þingvellir</a>, <a href="/places/geysir">Geysir</a> and Gullfoss. Hike in the morning, then drive the loop in the afternoon, or do it the other way round in summer's long evenings.</p>
<p>If the hike is too much, the Secret Lagoon at Flúðir and Laugarvatn Fontana are easy paid alternatives on the same route. For more free options, read our guide to <a href="/blog/free-hot-springs-iceland">free hot springs in Iceland</a>, and for every pool on the map see <a href="/blog/hot-springs-iceland">hot springs in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Parking charges and café hours change, and the trail and car park can close in bad weather; check safetravel.is and vedur.is before you go.",
        "sources": [
            ("Reykjadalur hot spring hike (Iceland Highlights, updated 2026)", "https://www.iceland-highlights.com/?p=15112"),
            ("Reykjadalur (Icelandia)", "https://www.icelandia.com/attractions/reykjadalur"),
            ("Reykjaböð hot springs (Icelandia)", "https://www.icelandia.com/attractions/reykjabod-hot-springs"),
            ("Hot natural pools: Landmannalaugar and Reykjadalur (Visit South Iceland)", "https://www.south.is/en/experiences/bathing-wellness/hot-natural-pools"),
        ],
    },
    {
        "slug": "myvatn-nature-baths",
        "cluster": "hot-springs",
        "pillar": False,
        "short": "Mývatn Nature Baths, Now Earth Lagoon Mývatn",
        "title": "Mývatn Nature Baths, Now Earth Lagoon Mývatn: Visitor Guide (2027)",
        "description": "Mývatn Nature Baths are now Earth Lagoon Mývatn: the rebuilt lagoon's 2026 prices, tickets, opening hours, water and how it compares with the Blue Lagoon.",
        "category": "Hot Springs · North Iceland",
        "teaser": "The north's famous lagoon, rebuilt, renamed and reopened in July 2026.",
        "image": "hx-aurora-winter",
        "image_alt": "A green aurora curving down to a snowy horizon under a starry sky",
        "stats": [
            ("2004", "Year the original Mývatn Nature Baths opened"),
            ("Jul 2026", "Reopened after rebuilding as Earth Lagoon Mývatn"),
            ("36–40°C", "Lagoon water temperature"),
            ("ISK 7,900", "Earth Essential entry, from (2026)"),
        ],
        "body": """
<p>The Mývatn Nature Baths (Jarðböðin) have been rebuilt and renamed Earth Lagoon Mývatn. The lagoon reopened in July 2026 with a new building, a bigger lagoon, a swim-in steam cave and new ticket types, from about ISK 7,900. It is in the same place, just east of Lake Mývatn on the Ring Road, with the same milky-blue water at 36–40°C. Here is what changed, what it costs and how to plan your visit.</p>
<!--TOC-->
<h2>Are the Mývatn Nature Baths still open?</h2>
<p>Yes, but under a new name. The rebrand to Earth Lagoon Mývatn was announced in October 2025. The old baths stayed open until the end of 2025 and then closed while the new building was finished. The rebuilt lagoon reopened on 9 July 2026, after a short soft-opening period. Many signs, maps and locals still call it Jarðböðin or the Nature Baths.</p>
<p>The address and phone number have not changed: Jarðbaðshólar, 660 Mývatn. If your map app shows the old name, it will still take you to the right place.</p>
<h2>What is new at Earth Lagoon Mývatn?</h2>
<p>The rebuild added a new building of just under 4,000 m², set into the slope with local stone, and a much larger lagoon. The bathing area grew by about 35%, and the lagoon now holds about 580 guests at once.</p>
<ul>
<li><strong>A swim-in steam cave:</strong> a rock steam room you reach through the water, at about 45°C and full humidity.</li>
<li><strong>New lagoon sections:</strong> a passage shaped around a tuff pillar and lava-rock walls leads to a larger, more open part of the lagoon.</li>
<li><strong>A waterfall, two hot tubs and a new lagoon bar.</strong></li>
<li><strong>Walk-in changing rooms:</strong> you step straight from the changing area into the water.</li>
<li><strong>A bistro and café:</strong> local food, with outdoor seating in summer.</li>
</ul>
""" + _map(
            "Map of Iceland hot springs with Earth Lagoon Mývatn, GeoSea and Forest Lagoon in the north",
            "Earth Lagoon Mývatn (12) is in the north, near GeoSea in Húsavík (13), the Forest Lagoon by Akureyri (14) and Vök Baths in the east (15).",
        ) + """
<h2>How much does Earth Lagoon Mývatn cost?</h2>
<p>Entry starts from about ISK 7,900 in 2026 for the basic ticket. Prices vary by time of day and how busy it is, and peak summer slots cost more.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ticket</th><th>From (2026)</th><th>What you get</th></tr></thead>
<tbody>
<tr><td>Earth Essential</td><td>About ISK 7,900</td><td>Lagoon, hot tubs and steam bath; standard changing rooms with private showers; locker</td></tr>
<tr><td>Earth Signature</td><td>About ISK 9,900</td><td>Lava-rock changing rooms, towel, one drink, bistro discount; no private showers</td></tr>
<tr><td>Earth Exclusive</td><td>About ISK 52,000</td><td>Private changing room for two, private lagoon area, robes, Prosecco and a drink, relaxation room; adults 20+</td></tr>
</tbody></table></div>
<p>Children aged 5 and under go free with an adult. Swimsuit rental costs about ISK 1,100 and towel rental about ISK 1,200. Book ahead in summer, and check the cancellation terms when you do.</p>
<h2>What are the opening hours?</h2>
<p>From 1 September 2026 the lagoon is open daily from 12:00 to 22:00, and you must be out of the water by 21:40. Summer hours are longer, with bathing until about 22:40. Hours change by season and around holidays, so check the official site before you drive.</p>
<p>Late visits are a good idea in winter. On clear, dark nights from September to April you have a chance of seeing the <a href="/northern-lights">northern lights</a> over the lagoon, away from city lights.</p>
<h2>What is the water like?</h2>
<p>The water comes from the Bjarnaflag borehole, about 2,500 m deep, at about 130°C and is cooled to 36–40°C. It is fresh water, alkaline and rich in sulphur and minerals, which gives it its cloudy blue colour. No chlorine is added. The lagoon is about 1.2 m deep on average, so most adults can stand everywhere.</p>
<p>Like any Icelandic pool, you must shower without your swimsuit before getting in; our <a href="/blog/iceland-swimming-pool-etiquette">swimming pool rules guide</a> explains how.</p>
<h2>How do you get to Earth Lagoon Mývatn?</h2>
<p>The lagoon sits just off Route 1, the Ring Road, on the east side of Lake Mývatn, near the village of Reykjahlíð. It is about an hour's drive east of Akureyri and about two hours west of Egilsstaðir. From Reykjavík it is around six hours by car, so most visitors stop on a Ring Road trip or fly to Akureyri.</p>
<p>It works well at the end of a day's driving from the east, after <a href="/places/studlagil">Stuðlagil canyon</a> or <a href="/places/hengifoss">Hengifoss</a>. See our <a href="/blog/iceland-ring-road-guide">Ring Road guide</a> for the full route.</p>
<h2>Is Earth Lagoon Mývatn better than the Blue Lagoon?</h2>
<p>It is cheaper, quieter and set in wider open landscape, but it is far from Reykjavík. The Blue Lagoon is more polished and easier to reach from the airport. If your route passes Mývatn, the northern lagoon is the better value.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Earth Lagoon Mývatn</th><th>Blue Lagoon</th></tr></thead>
<tbody>
<tr><td>Entry from (2026)</td><td>About ISK 7,900</td><td>About ISK 11,990</td></tr>
<tr><td>Water temperature</td><td>36–40°C</td><td>37–39°C on average</td></tr>
<tr><td>Region</td><td>North Iceland, on the Ring Road</td><td>Reykjanes, near Keflavík Airport</td></tr>
<tr><td>Children</td><td>All ages; 5 and under free</td><td>From age 2</td></tr>
<tr><td>Volcanic closures</td><td>None reported</td><td>Several since 2023</td></tr>
</tbody></table></div>
<p>For a full head-to-head of the southern lagoons, read <a href="/blog/blue-lagoon-vs-sky-lagoon">Blue Lagoon vs Sky Lagoon</a>.</p>
<h2>Can you visit Earth Lagoon Mývatn with children?</h2>
<p>Yes. All ages are welcome at the main lagoon, and children aged 5 and under go free with a paying adult. The lagoon averages about 1.2 m deep, with a maximum of about 1.3 m, so small children need to be held or wear arm bands. Watch them closely near the hot tubs and the steam cave, which are much hotter than the lagoon. The Earth Exclusive area is for adults aged 20 and over.</p>
<h2>What should you bring?</h2>
<p>Bring a swimsuit and a towel to avoid rental fees, though both can be rented at the desk. Take a warm hat for winter evenings, when the air can be well below freezing while the water stays at 36–40°C. Lock your phone away in the changing room, and do not take photos there. If you plan to eat afterwards, the Signature ticket includes a bistro discount and a drink, which can make it better value than the basic ticket.</p>
<h2>What else is there to see near the lagoon?</h2>
<p>The Mývatn area is full of volcanic sights, many within a short drive of the lagoon. Hverfjall's huge tephra crater, the Krafla volcanic area and the lava formations around the lake are all close by. The lake itself is famous for its ducks in summer.</p>
<p>Do not try to bathe in Grjótagjá, the hot-water cave a few minutes away. The water there has been too hot and unpredictable since the Krafla eruptions of 1975–1984, and the owners ask visitors only to look.</p>
<p>For more hot water in the north, the Forest Lagoon near Akureyri and GeoSea's sea baths in Húsavík are each about an hour away. Our <a href="/blog/north-iceland-guide">North Iceland guide</a> covers the region, and our <a href="/blog/hot-springs-iceland">hot springs in Iceland</a> map shows all 19 pools.</p>
<p class="callout"><strong>Tip:</strong> book an evening slot after a day of sightseeing around the lake. You avoid the midday tour groups and finish the day warm.</p>
""",
        "checked_note": "Facts checked October 2026. Earth Lagoon Mývatn reopened in July 2026 and its hours, prices and ticket types may still change; check earthlagoon.is before you go. Prices vary by time slot and season.",
        "sources": [
            ("New facilities (Earth Lagoon Mývatn)", "https://www.earthlagoon.is/new-jar%C3%B0bo%C3%B0in-facility"),
            ("Earth Lagoon Mývatn: prices and opening hours (Earth Lagoon)", "https://www.earthlagoon.is/"),
            ("Earth Lagoon (Visit North Iceland)", "https://www.northiceland.is/en/service/myvatn-nature-baths"),
            ("Mývatn Nature Baths to reopen as Earth Lagoon in 2026 (Construction.is)", "https://construction.is/myvatn-nature-baths-to-reopen-as-earth-lagoon-in-2026/"),
            ("Mývatn Nature Baths (now Earth Lagoon): guide (Arctic Adventures)", "https://adventures.is/iceland/attractions/myvatn-nature-baths/"),
            ("Earth Lagoon Mývatn, reopened 2026 (Iceland Travel Information)", "https://icelandtravelinformation.com/hot-springs-in-iceland/earth-lagoon-myvatn/"),
            ("Grjótagjá travel guide (Guide to Iceland)", "https://guidetoiceland.is/travel-iceland/drive/grjotagja"),
        ],
    },
    {
        "slug": "iceland-swimming-pool-etiquette",
        "cluster": "hot-springs",
        "pillar": False,
        "short": "Iceland Swimming Pool Rules and Etiquette",
        "title": "Iceland Swimming Pool Rules: Shower Etiquette and Local Customs Explained",
        "description": "Iceland swimming pool rules explained: why you shower without a swimsuit, step-by-step changing room etiquette, phones, children, hot tubs and prices.",
        "category": "Hot Springs · Culture",
        "teaser": "The naked shower, the hot tub chat and the other rules locals expect.",
        "image": "hx-reykjavik",
        "image_alt": "Reykjavík and Hallgrímskirkja across the bay under heavy cloud",
        "stats": [
            ("ISK 1,500", "Adult entry at Reykjavík city pools (2026)"),
            ("8", "Swimming pools run by the City of Reykjavík"),
            ("Under 10", "Must swim with someone aged 15 or older"),
            ("Dec 2025", "Pool culture added to UNESCO's heritage list"),
        ],
        "body": """
<p>The most important Iceland swimming pool rule is simple: you must shower thoroughly, without your swimsuit, before you get in the water. It applies at every public pool and at lagoons such as the Blue Lagoon and Sky Lagoon. Everyone shares the same warm water, so hygiene depends on everyone washing first. Here are the rules, the unwritten customs and a step-by-step guide so you walk in like a local.</p>
<!--TOC-->
<h2>What are the rules at Icelandic swimming pools?</h2>
<p>Icelandic pools have clear, enforced rules. These are the main ones, from the City of Reykjavík's official rules for its pools:</p>
<ul>
<li><strong>Shower without swimwear</strong> before entering the pool, and wash thoroughly.</li>
<li><strong>Wear clean swimwear</strong> in the pool. Swimming naked is not allowed.</li>
<li><strong>No phones or cameras</strong> in changing rooms or pool areas. This is strictly enforced.</li>
<li><strong>No alcohol, tobacco, vapes or nicotine pouches</strong> anywhere in the building, and no entry if you are drunk.</li>
<li><strong>No glass</strong> in pool areas or changing rooms.</li>
<li><strong>Follow staff instructions.</strong> Staff can remove anyone who breaks the rules, without warning for serious cases.</li>
</ul>
<h2>Do you really have to shower naked in Iceland?</h2>
<p>Yes. Showering without your swimsuit, with soap, is required, not optional. Staff can send you back if you skip it, and at the Blue Lagoon attendants check the showers. Illustrated signs on the shower walls show which parts of the body to wash with special care.</p>
<p>Locker rooms and showers are separated by gender, and nudity there is completely normal. Locals do not stare or judge. If you are shy, some pools have a few showers with curtains, and many have private changing rooms you can ask for. Larger lagoons such as the Blue Lagoon and Sky Lagoon have divided shower cubicles.</p>
<p class="callout"><strong>Why it matters:</strong> washing first keeps the shared water clean for everyone, which is why locals take the shower rule so seriously and staff can ask you to go back.</p>
<h2>How do you use an Icelandic pool, step by step?</h2>
<ol>
<li><strong>Take your shoes off</strong> before you enter the changing room. Leave them on the racks at the entrance.</li>
<li><strong>Undress at your locker</strong> and lock your valuables away.</li>
<li><strong>Carry your swimsuit and towel</strong> to the shower area.</li>
<li><strong>Leave your towel</strong> on the racks or shelves by the showers.</li>
<li><strong>Shower naked with soap,</strong> washing thoroughly as the signs show.</li>
<li><strong>Put your swimsuit on</strong> and go out to the pool.</li>
<li><strong>After swimming, shower again</strong> and dry off in the shower area before you walk back to the lockers, so the changing-room floor stays dry.</li>
</ol>
""" + _map(
            "Map of Iceland hot springs and pools, including Krossneslaug and Hofsós pool",
            "Our 19 pools and springs include two public pools, Krossneslaug (18) and Hofsós (19), as well as lagoons and natural springs.",
        ) + """
<h2>What is the etiquette in the hot tubs?</h2>
<p>The hot tubs, called heitur pottur, are the social heart of an Icelandic pool. People come to relax and talk, so keep it calm. Quiet conversation is normal, and locals often chat about the weather, the news or politics. Loud groups, shouting and splashing belong in the children's pool.</p>
<ul>
<li>Tubs are labelled with their temperature, usually from warm to very hot. Start with a cooler one.</li>
<li>Many pools have a cold tub too. Locals switch between hot and cold.</li>
<li>Do not bring drinks or food into the tubs.</li>
<li>Make room when someone arrives; tubs are shared.</li>
</ul>
<h2>What are the rules in the lanes, saunas and steam rooms?</h2>
<p>In the lap pool, watch the lane for a moment before you join, and pick one that matches your pace. Some lanes are fast lanes or reserved for training. Floats and toys belong in the shallow pool.</p>
<p>In Reykjavík's saunas you sit on a towel and must not use scented oils, and children under 16 need an adult with them. Steam rooms are usually towel-free, so they are the easy option if you did not bring a towel.</p>
<h2>What are the rules for children?</h2>
<p>At Reykjavík's pools, children under 10 must be accompanied by a swimmer aged 15 or older. One adult can supervise at most two children, unless they are the child's parent or guardian. From 1 June of the year a child turns 10, they may swim on their own.</p>
<p>Children who are 6 or older use the changing room for their own gender, with private changing rooms if needed. Non-swimmers must wear approved arm bands or a swim vest; inflatable rings count as toys.</p>
<h2>How much does a swimming pool cost in Iceland?</h2>
<p>Public pools are one of the cheapest things to do in Iceland. From 5 May 2026, Reykjavík city pools charge:</p>
<div class="table-wrap"><table>
<thead><tr><th>Ticket</th><th>Price</th></tr></thead>
<tbody>
<tr><td>Adult, single entry</td><td>ISK 1,500</td></tr>
<tr><td>Children aged 10–17</td><td>ISK 400</td></tr>
<tr><td>Children under 10 with a guardian</td><td>Free</td></tr>
<tr><td>Adult 10-visit card</td><td>ISK 7,000</td></tr>
<tr><td>Towel rental</td><td>ISK 860</td></tr>
<tr><td>Swimsuit rental</td><td>ISK 1,270</td></tr>
<tr><td>Swim, towel and swimsuit package</td><td>ISK 2,770</td></tr>
</tbody></table></div>
<p>Pools in other towns charge similar or lower prices. Compare that with a lagoon, which costs from about ISK 7,500 to more than ISK 18,000. See <a href="/blog/blue-lagoon-vs-sky-lagoon">Blue Lagoon vs Sky Lagoon</a> if you want the spa experience as well.</p>
<h2>Which pools should you try in Reykjavík?</h2>
<p>The City of Reykjavík runs eight pools, and each neighbourhood has its favourite. Three are good places to start in <a href="/places/reykjavik">Reykjavík</a>:</p>
<ul>
<li><strong>Laugardalslaug:</strong> the largest, with indoor and outdoor pools, several hot tubs and a water slide. Good for families.</li>
<li><strong>Vesturbæjarlaug:</strong> a neighbourhood favourite in the west of the city, with hot tubs, a steam room and outdoor changing areas.</li>
<li><strong>Sundhöll Reykjavíkur:</strong> a historic indoor pool hall in the centre, with a newer outdoor section and hot tubs.</li>
</ul>
<p>Outside the capital, small country pools are just as good. Hofsós pool in Skagafjörður looks out across the fjord, and Krossneslaug sits on a beach at the far end of the Westfjords.</p>
<h2>Why are swimming pools so important in Iceland?</h2>
<p>Pools are where Icelanders meet, relax and talk, all year and in every kind of weather. There are more than 120 public pools across the country, heated by geothermal water. In December 2025 UNESCO added Iceland's swimming pool culture to its list of the intangible cultural heritage of humanity, Iceland's first entry of its own on the list.</p>
<p>Going to the local pool is one of the easiest ways to see everyday Icelandic life. Visit in the early morning or after work, when locals fill the hot tubs.</p>
<h2>Do the same rules apply at lagoons and natural hot springs?</h2>
<p>At lagoons, yes. The Blue Lagoon, Sky Lagoon and other spas follow the same shower rule, and staff check it. They also add their own rules, such as minimum ages: Sky Lagoon admits only those 12 and over.</p>
<p>Natural hot springs have no showers or staff, so the rules are about respect instead. Bathe only where bathing is allowed, use no soap in the water, take all your rubbish home and stay on the paths. At remote springs nudity is generally accepted, but ask anyone already there first. Read our guides to <a href="/blog/free-hot-springs-iceland">free hot springs in Iceland</a> and the <a href="/places/reykjadalur">Reykjadalur hot river</a>, or see every pool on our map in <a href="/blog/hot-springs-iceland">hot springs in Iceland</a>.</p>
""",
        "checked_note": "Facts checked October 2026. Rules and prices are from the City of Reykjavík's pools; other towns and private lagoons set their own prices and may add rules. Check each pool's website for opening hours.",
        "sources": [
            ("Safety and conduct rules for Reykjavík swimming pools (City of Reykjavík)", "https://reykjavik.is/en/swimming-pools/rules-on-safety-and-conduct"),
            ("Fees for swimming pools (City of Reykjavík)", "https://reykjavik.is/en/swimming-pools/fees"),
            ("Icelandic swimming pool culture inscribed on UNESCO's list (City of Reykjavík)", "https://reykjavik.is/en/news/2025/icelandic-swimming-pool-culture-inscribed-unescos-list-intangible-cultural-heritage-humanity"),
            ("A guide to Reykjavík's swimming pools (PLAY)", "https://www.flyplay.com/blog/a-guide-to-reykjaviks-swimming-pools"),
            ("Nudity in Iceland: when and where (Guide to Iceland)", "https://guidetoiceland.is/es/historia-y-cultura/getting-naked-in-iceland"),
            ("Hofsós swimming pool (Hot Springs Guides)", "https://www.hotspringsguides.com/hot-springs/hofsos-swimming-pool-iceland"),
        ],
    },
]
