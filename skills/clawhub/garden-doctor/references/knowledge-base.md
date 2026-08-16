# Plant Problem Knowledge Base

Full catalog of 40+ common plant problems covered by `garden_doctor.py`.

## How to Read This Document

Each entry has:
- **ID** — unique identifier for the `info` command
- **Name** — common name of the problem
- **Category** — watering, light, nutrient, pest, fungal, bacterial, environmental, temperature
- **Symptoms** — observable signs (what the user reports)
- **Cause** — underlying cause
- **Affected plants** — plant types most commonly affected (or "all" for universal)
- **Treatment** — actionable steps to fix
- **Prevention** — long-term care adjustments

---

## Watering Problems

### Overwatering / Root Rot
- **ID:** `overwatering`
- **Symptoms:** Yellowing leaves (especially lower), wilting despite wet soil, mushy stems, brown soft spots, foul smell from soil, leaf drop
- **Cause:** Soil stays waterlogged; roots suffocate, decay, and rot
- **Treatment:** Stop watering immediately. Remove plant from pot, inspect roots. Trim brown/mushy roots with sterilized scissors. Repot in fresh, well-draining soil. Reduce watering frequency.
- **Prevention:** Only water when top 2-5 cm of soil is dry. Ensure pot has drainage holes. Use well-draining soil mix.

### Underwatering
- **ID:** `underwatering`
- **Symptoms:** Dry crispy leaf edges, wilting/drooping, dry soil pulling from pot edges, slow growth, leaves curling inward
- **Cause:** Insufficient water; plant is drought-stressed
- **Treatment:** Water thoroughly until water drains from bottom. For severely dry plants, bottom-water for 30 minutes. Establish regular watering schedule.
- **Prevention:** Check soil moisture weekly. Water deeply rather than shallowly. Use mulch to retain moisture (outdoor plants).

### Edema
- **ID:** `edema`
- **Symptoms:** Blisters/bumps on underside of leaves, corky patches, leaf curling
- **Cause:** Plant takes up water faster than it can transpire (usually from overwatering in high humidity)
- **Treatment:** Reduce watering. Improve air circulation. Increase light.
- **Prevention:** Water in morning. Ensure good ventilation.

---

## Light Problems

### Too Little Light
- **ID:** `low_light`
- **Symptoms:** Leggy/stretched growth, small pale leaves, slow growth, leaning toward light, leaves dropping
- **Cause:** Insufficient light for photosynthesis
- **Treatment:** Move to brighter location (indirect light). Supplement with grow lights (12-14 hours). Prune leggy growth.
- **Prevention:** Research light needs of each plant. Rotate pots weekly for even growth.

### Too Much Light / Sunburn
- **ID:** `sunburn`
- **Symptoms:** Brown crispy patches on leaves (often white/bleached), leaves curling, crispy edges, spots on the side facing the sun
- **Cause:** Excessive direct sunlight bleaches and burns leaf tissue
- **Treatment:** Move plant away from direct sun. Filter light with sheer curtain. Remove severely damaged leaves.
- **Prevention:** Acclimate plants gradually to brighter light. Know your plant's light requirements.

---

## Nutrient Problems

### Nitrogen Deficiency
- **ID:** `nitrogen_deficiency`
- **Symptoms:** Older/lower leaves turning uniformly yellow, stunted growth, small pale new leaves
- **Cause:** Insufficient nitrogen in soil
- **Treatment:** Apply balanced fertilizer (NPK 10-10-10) or high-nitrogen fertilizer. Add compost or worm castings.
- **Prevention:** Fertilize every 2-4 weeks during growing season (spring/summer). Use fresh potting soil annually.

### Iron Deficiency (Chlorosis)
- **ID:** `iron_deficiency`
- **Symptoms:** Yellow leaves with green veins (especially new growth), interveinal chlorosis
- **Cause:** Iron unavailable — often due to high soil pH or overwatering
- **Treatment:** Apply iron chelate supplement. Check and adjust soil pH. Improve drainage.
- **Prevention:** Use appropriate soil pH for plant type. Avoid overwatering.

### Magnesium Deficiency
- **ID:** `magnesium_deficiency`
- **Symptoms:** Interveinal chlorosis on older leaves, leaves may develop reddish/purple tint
- **Cause:** Insufficient magnesium
- **Treatment:** Apply Epsom salt (magnesium sulfate) solution: 1 tsp per gallon water.
- **Prevention:** Use balanced fertilizer with micronutrients.

### Potassium Deficiency
- **ID:** `potassium_deficiency`
- **Symptoms:** Yellow/brown leaf margins (scorch), weak stems, poor flowering/fruiting
- **Cause:** Insufficient potassium
- **Treatment:** Apply potassium-rich fertilizer. Add wood ash (outdoor) or kelp extract.
- **Prevention:** Use balanced fertilizer. Test soil periodically.

### Nutrient Burn (Over-fertilization)
- **ID:** `nutrient_burn`
- **Symptoms:** Brown crispy leaf tips and margins, white crust on soil surface, wilting, leaf curl
- **Cause:** Excess fertilizer salts damage roots
- **Treatment:** Flush soil with plenty of water (3x pot volume). Stop fertilizing for 4-6 weeks. Repot if severe.
- **Prevention:** Follow fertilizer package rates. Never fertilize dry soil. Less is more.

---

## Fungal Diseases

### Powdery Mildew
- **ID:** `powdery_mildew`
- **Symptoms:** White powdery spots on leaves and stems, leaves yellowing and drying, distorted growth
- **Cause:** Fungal infection (favors high humidity + poor airflow)
- **Treatment:** Remove affected leaves. Spray with 1:10 milk-to-water solution or neem oil. Improve air circulation. Apply sulfur-based fungicide.
- **Prevention:** Space plants for airflow. Avoid wetting foliage when watering. Use fan for indoor plants.

### Early Blight
- **ID:** `early_blight`
- **Symptoms:** Brown spots with concentric rings (target pattern) on lower leaves, yellowing around spots, leaves drop from bottom up
- **Cause:** Fungal infection (Alternaria solani) — common in tomatoes
- **Treatment:** Remove infected leaves. Apply copper fungicide. Mulch to prevent soil splash.
- **Prevention:** Rotate crops. Water at soil level. Space plants for airflow.

### Late Blight
- **ID:** `late_blight`
- **Symptoms:** Large dark brown/black patches on leaves and stems, white fuzzy growth underneath, rapid collapse
- **Cause:** Fungal infection (Phytophthora infestans) — spreads fast in cool wet weather
- **Treatment:** Remove and destroy infected plants (do not compost). Apply copper fungicide preventatively on remaining plants.
- **Prevention:** Plant resistant varieties. Ensure good drainage. Avoid overhead watering.

### Leaf Spot (Fungal)
- **ID:** `leaf_spot`
- **Symptoms:** Brown/black spots on leaves, sometimes with yellow halos, spots may merge, leaf drop
- **Cause:** Various fungal pathogens (Cercospora, Septoria, etc.)
- **Treatment:** Remove affected leaves. Apply fungicide (copper or neem). Improve airflow.
- **Prevention:** Water at soil level. Space plants. Clean up fallen leaves.

### Root Rot (Fungal)
- **ID:** `fungal_root_rot`
- **Symptoms:** Wilting despite moist soil, yellowing, stunted growth, brown/black mushy roots
- **Cause:** Fungal pathogens (Pythium, Rhizoctonia) thriving in waterlogged soil
- **Treatment:** Unpot, remove all affected roots, repot in fresh sterile soil. Apply biological fungicide (Trichoderma). Reduce watering.
- **Prevention:** Well-draining soil. Don't overwater. Sterilize pots between uses.

### Anthracnose
- **ID:** `anthracnose`
- **Symptoms:** Dark sunken lesions on leaves, stems, or fruit, pinkish spore masses
- **Cause:** Fungal infection (Colletotrichum)
- **Treatment:** Remove infected parts. Apply copper fungicide. Improve airflow.
- **Prevention:** Remove plant debris. Avoid overhead watering. Use disease-free seed.

### Rust
- **ID:** `rust`
- **Symptoms:** Orange/rust-colored pustules on leaf undersides, yellow spots on top, leaf drop
- **Cause:** Fungal infection (requires moisture to spread)
- **Treatment:** Remove infected leaves. Apply sulfur or neem oil. Improve airflow.
- **Prevention:** Space plants. Water at soil level. Remove infected debris.

### Botrytis (Gray Mold)
- **ID:** `botrytis`
- **Symptoms:** Gray fuzzy mold on leaves/flowers/stems, brown spots, rapid decay in humid conditions
- **Cause:** Fungal infection (Botrytis cinerea)
- **Treatment:** Remove all infected/moldy parts immediately. Improve ventilation. Reduce humidity.
- **Prevention:** Remove dead flowers/leaves. Space plants. Use fan indoors.

### Sooty Mold
- **ID:** `sooty_mold`
- **Symptoms:** Black sooty coating on leaves, sticky residue (honeydew) underneath
- **Cause:** Fungal growth on honeydew secreted by sap-sucking pests (aphids, scale)
- **Treatment:** Treat the pest problem first. Wipe leaves with damp cloth. Wash with mild soapy water.
- **Prevention:** Control pest populations. Monitor regularly.

---

## Bacterial Diseases

### Bacterial Leaf Spot
- **ID:** `bacterial_leaf_spot`
- **Symptoms:** Water-soaked spots that turn brown/black, spots often angular (between leaf veins), yellow halos
- **Cause:** Bacterial infection (Xanthomonas, Pseudomonas)
- **Treatment:** Remove infected leaves. Apply copper bactericide. Avoid overhead watering.
- **Prevention:** Space plants. Don't work with wet plants. Use clean tools.

### Bacterial Wilt
- **ID:** `bacterial_wilt`
- **Symptoms:** Rapid wilting of entire plant without yellowing, plants don't recover at night, milky ooze from cut stem
- **Cause:** Bacterial infection (Ralstonia solanacearum) — common in tomatoes/peppers
- **Treatment:** Remove and destroy infected plants. No cure — focus on prevention.
- **Prevention:** Rotate crops. Use resistant varieties. Control nematodes.

### Crown Gall
- **ID:** `crown_gall`
- **Symptoms:** Swollen tumor-like growths at soil line or on roots, stunted growth
- **Cause:** Bacterial infection (Agrobacterium tumefaciens)
- **Treatment:** Remove and destroy infected plants. No chemical cure.
- **Prevention:** Avoid wounding plants. Use disease-free stock. Sterilize soil.

---

## Pests

### Aphids
- **ID:** `aphids`
- **Symptoms:** Small green/black/white insects on new growth, sticky leaves (honeydew), distorted/curling leaves, ants on plant
- **Cause:** Sap-sucking insect infestation
- **Treatment:** Spray with strong water stream. Apply insecticidal soap or neem oil. Release ladybugs (outdoor).
- **Prevention:** Inspect new plants. Encourage beneficial insects. Use yellow sticky traps.

### Spider Mites
- **ID:** `spider_mites`
- **Symptoms:** Fine webbing on plant, stippled/yellow speckled leaves, tiny moving dots on leaf undersides, leaves dropping
- **Cause:** Tiny arachnid pests thriving in hot dry conditions
- **Treatment:** Spray with water to dislodge. Apply neem oil or miticide. Increase humidity. Repeat every 5-7 days.
- **Prevention:** Maintain humidity. Mist regularly. Inspect undersides of leaves.

### Mealybugs
- **ID:** `mealybugs`
- **Symptoms:** White cottony masses in leaf joints and undersides, sticky residue, yellowing, stunted growth
- **Cause:** Sap-sucking insect covered in white waxy filaments
- **Treatment:** Remove with cotton swab dipped in alcohol. Apply insecticidal soap or neem oil. Systemic insecticide for severe cases.
- **Prevention:** Inspect new plants. Isolate infested plants. Regular monitoring.

### Scale Insects
- **ID:** `scale`
- **Symptoms:** Brown/yellow hard or soft bumps on stems and leaves, sticky honeydew, yellowing, sooty mold
- **Cause:** Sap-sucking insect with protective shell
- **Treatment:** Scrape off with fingernail or cotton swab with alcohol. Apply neem oil or horticultural oil. Systemic insecticide for severe cases.
- **Prevention:** Inspect stems regularly. Quarantine new plants.

### Fungus Gnats
- **ID:** `fungus_gnats`
- **Symptoms:** Small black flies around soil, larvae in topsoil, yellowing, wilting (if larvae damage roots)
- **Cause:** Small flies whose larvae feed on fungi and roots in wet soil
- **Treatment:** Allow top layer of soil to dry between watering. Apply Bt (Bacillus thuringiensis) drench. Use yellow sticky traps for adults.
- **Prevention:** Don't overwater. Top-dress soil with sand or diatomaceous earth.

### Whiteflies
- **ID:** `whiteflies`
- **Symptoms:** Tiny white moth-like insects that fly up when plant is disturbed, yellowing leaves, sticky honeydew
- **Cause:** Sap-sucking insect that multiplies rapidly
- **Treatment:** Spray with insecticidal soap. Apply neem oil. Use yellow sticky traps. Hang reflective mulch.
- **Prevention:** Inspect undersides of leaves. Use row covers outdoors.

### Thrips
- **ID:** `thrips`
- **Symptoms:** Silvery/white streaks on leaves/flowers, tiny black dots (feces), distorted flowers/leaves
- **Cause:** Tiny slender insects that rasp plant tissue
- **Treatment:** Apply insecticidal soap or neem oil. Use blue sticky traps. Release predatory mites.
- **Prevention:** Remove weeds near plants. Inspect new plants carefully.

### Caterpillars / Cabbage Worms
- **ID:** `caterpillars`
- **Symptoms:** Large irregular holes in leaves, dark green droppings (frass), leaves stripped to stems
- **Cause:** Caterpillar larvae feeding on foliage
- **Treatment:** Hand-pick caterpillars. Apply Bt spray. Use row covers.
- **Prevention:** Use row covers on brassicas. Encourage birds and beneficial insects.

### Slugs and Snails
- **ID:** `slugs`
- **Symptoms:** Large irregular holes in leaves (especially low leaves), slimy trails, damage at night
- **Cause:** Mollusks feeding at night
- **Treatment:** Hand-pick at night. Set beer traps. Apply iron phosphate bait. Create copper barriers.
- **Prevention:** Remove hiding spots (boards, debris). Water in morning so soil is dry at night.

---

## Environmental Problems

### Temperature Stress (Cold)
- **ID:** `cold_stress`
- **Symptoms:** Dark water-soaked patches on leaves, wilting, leaf drop, blackened stems
- **Cause:** Exposure to cold temperatures or drafts
- **Treatment:** Move to warmer location. Remove damaged parts. Don't fertilize until recovery.
- **Prevention:** Keep away from cold windows/drafts. Move plants indoors before frost.

### Temperature Stress (Heat)
- **ID:** `heat_stress`
- **Symptoms:** Wilting in hot afternoon sun, leaf scorch, flower/fruit drop, rapid soil drying
- **Cause:** Excessive heat, especially combined with direct sun
- **Treatment:** Provide shade cloth. Water deeply. Move container plants to cooler spot.
- **Prevention:** Use mulch. Provide afternoon shade. Choose heat-tolerant varieties.

### Low Humidity
- **ID:** `low_humidity`
- **Symptoms:** Brown crispy leaf tips and edges, leaf curling, flower buds dropping, slow growth
- **Cause:** Air too dry (common indoors in winter, or for tropical plants)
- **Treatment:** Use humidifier or pebble tray. Group plants together. Mist (for some plants).
- **Prevention:** Monitor humidity (aim for 40-60%). Use humidity trays. Avoid heating/AC vents.

### Draft Stress
- **ID:** `draft_stress`
- **Symptoms:** Sudden leaf drop, brown edges, wilting despite proper care
- **Cause:** Hot or cold air from vents, doors, or windows
- **Treatment:** Move plant away from vents/doors. Create buffer.
- **Prevention:** Identify draft sources. Relocate sensitive plants.

---

## Salt / Chemical Damage

### Salt Buildup / Fertilizer Salt
- **ID:** `salt_buildup`
- **Symptoms:** White crust on soil surface, brown leaf tips, stunted growth, wilting
- **Cause:** Accumulated mineral salts from fertilizer or hard water
- **Treatment:** Flush soil thoroughly with clean water. Repot with fresh soil if severe. Use filtered water.
- **Prevention:** Flush soil quarterly. Use filtered/rain water. Don't over-fertilize.

### Herbicide Drift
- **ID:** `herbicide_drift`
- **Symptoms:** Twisted/cupped distorted leaves, narrowed strap-like growth, sudden widespread damage
- **Cause:** Wind-blown herbicide from lawn/garden spraying
- **Treatment:** Wash plant with water. Prune affected growth. Wait for new growth. (No full cure)
- **Prevention:** Avoid spraying on windy days. Don't use herbicide-treated grass clippings as mulch.

---

## Physiological Problems

### Blossom End Rot
- **ID:** `blossom_end_rot`
- **Symptoms:** Dark sunken leathery patch on bottom (blossom end) of fruit (tomatoes, peppers)
- **Cause:** Calcium deficiency in fruit — usually from inconsistent watering
- **Treatment:** Maintain consistent soil moisture. Add calcium (lime, gypsum). Mulch to regulate moisture.
- **Prevention:** Water regularly and deeply. Add calcium to soil before planting. Test soil pH.

### Leaf Scorch
- **ID:** `leaf_scorch`
- **Symptoms:** Brown margins and tips on leaves, tissue between veins stays green longer, overall browning
- **Cause:** Water stress, wind, or salt accumulation causing marginal tissue death
- **Treatment:** Water deeply and consistently. Mulch roots. Protect from wind.
- **Prevention:** Consistent watering. Wind protection for sensitive species.

### Catfacing
- **ID:** `catfacing`
- **Symptoms:** Deformed, scarred, puckered fruit (tomatoes, peppers) with rough corky areas
- **Cause:** Incomplete pollination during cool weather
- **Treatment:** No treatment — affected fruit still edible. Wait for warmer weather.
- **Prevention:** Plant after soil warms. Use varieties resistant to catfacing. Protect from cool nights.

---

## Summary Statistics

| Category | Count |
|---|---|
| Watering | 3 |
| Light | 2 |
| Nutrient | 5 |
| Fungal | 10 |
| Bacterial | 3 |
| Pests | 9 |
| Environmental | 4 |
| Salt/Chemical | 2 |
| Physiological | 3 |
| **Total** | **41** |
