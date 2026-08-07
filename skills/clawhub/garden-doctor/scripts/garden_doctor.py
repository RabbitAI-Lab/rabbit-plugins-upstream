#!/usr/bin/env python3
"""
garden_doctor.py — Plant problem diagnostic tool.

Diagnoses plant health problems from reported symptoms using a built-in
knowledge base of 40+ common plant problems.

Usage:
    python3 garden_doctor.py diagnose --plant "tomato" --symptoms "yellow leaves" "brown spots"
    python3 garden_doctor.py list
    python3 garden_doctor.py info --id spider_mites
    python3 garden_doctor.py search --symptom "yellow leaves"

Standard library only. Python 3.8+.
"""

import argparse
import json
import sys

# ---------------------------------------------------------------------------
# Knowledge Base — 41 common plant problems
# Each entry: id, name, category, symptoms (list of keywords), cause,
#             affected_plants (list or ["all"]), treatment (list), prevention (list)
# ---------------------------------------------------------------------------
KNOWLEDGE_BASE = [
    # --- Watering (3) ---
    {
        "id": "overwatering",
        "name": "Overwatering / Root Rot",
        "category": "watering",
        "symptoms": ["yellow leaves", "yellowing leaves", "wilting", "drooping",
                     "mushy stems", "brown soft spots", "foul smell", "leaf drop",
                     "wet soil", "soggy soil"],
        "cause": "Soil stays waterlogged; roots suffocate, decay, and rot.",
        "affected_plants": ["all"],
        "treatment": [
            "Stop watering immediately.",
            "Remove plant from pot and inspect roots.",
            "Trim brown/mushy roots with sterilized scissors.",
            "Repot in fresh, well-draining soil.",
            "Reduce watering frequency going forward.",
        ],
        "prevention": [
            "Only water when top 2-5 cm of soil is dry.",
            "Ensure pot has drainage holes.",
            "Use well-draining soil mix appropriate for the plant.",
        ],
    },
    {
        "id": "underwatering",
        "name": "Underwatering / Drought Stress",
        "category": "watering",
        "symptoms": ["dry crispy edges", "crispy leaf edges", "wilting", "drooping",
                     "dry soil", "slow growth", "curling leaves", "leaves curling inward"],
        "cause": "Insufficient water; plant is drought-stressed.",
        "affected_plants": ["all"],
        "treatment": [
            "Water thoroughly until water drains from the bottom.",
            "For severely dry plants, bottom-water for 30 minutes.",
            "Establish a regular watering schedule.",
        ],
        "prevention": [
            "Check soil moisture weekly.",
            "Water deeply rather than shallowly.",
            "Use mulch to retain moisture for outdoor plants.",
        ],
    },
    {
        "id": "edema",
        "name": "Edema (Oedema)",
        "category": "watering",
        "symptoms": ["blisters on leaves", "bumps on leaf undersides", "corky patches",
                     "leaf curling", "blisters"],
        "cause": "Plant takes up water faster than it can transpire (overwatering in high humidity).",
        "affected_plants": ["all"],
        "treatment": [
            "Reduce watering frequency.",
            "Improve air circulation around the plant.",
            "Increase light exposure.",
        ],
        "prevention": [
            "Water in the morning.",
            "Ensure good ventilation.",
        ],
    },
    # --- Light (2) ---
    {
        "id": "low_light",
        "name": "Insufficient Light",
        "category": "light",
        "symptoms": ["leggy growth", "stretched growth", "small pale leaves",
                     "slow growth", "leaning toward light", "leaves dropping",
                     "pale leaves"],
        "cause": "Insufficient light for photosynthesis.",
        "affected_plants": ["all"],
        "treatment": [
            "Move to a brighter location with indirect light.",
            "Supplement with grow lights (12-14 hours per day).",
            "Prune leggy growth to encourage bushier regrowth.",
        ],
        "prevention": [
            "Research the light requirements of each plant species.",
            "Rotate pots weekly for even growth.",
        ],
    },
    {
        "id": "sunburn",
        "name": "Sunburn / Light Stress",
        "category": "light",
        "symptoms": ["brown crispy patches", "bleached leaves", "white patches",
                     "leaves curling", "crispy edges", "sunburn", "bleached spots"],
        "cause": "Excessive direct sunlight bleaches and burns leaf tissue.",
        "affected_plants": ["all"],
        "treatment": [
            "Move plant away from direct sunlight.",
            "Filter light with a sheer curtain.",
            "Remove severely damaged leaves.",
        ],
        "prevention": [
            "Acclimate plants gradually to brighter light conditions.",
            "Know each plant's light requirements.",
        ],
    },
    # --- Nutrient (5) ---
    {
        "id": "nitrogen_deficiency",
        "name": "Nitrogen Deficiency",
        "category": "nutrient",
        "symptoms": ["older leaves yellowing", "lower leaves yellow", "uniformly yellow leaves",
                     "stunted growth", "small pale new leaves", "pale leaves"],
        "cause": "Insufficient nitrogen in the soil.",
        "affected_plants": ["all"],
        "treatment": [
            "Apply a balanced fertilizer (NPK 10-10-10) or high-nitrogen fertilizer.",
            "Add compost or worm castings to the soil.",
        ],
        "prevention": [
            "Fertilize every 2-4 weeks during the growing season (spring/summer).",
            "Use fresh potting soil annually.",
        ],
    },
    {
        "id": "iron_deficiency",
        "name": "Iron Deficiency (Chlorosis)",
        "category": "nutrient",
        "symptoms": ["yellow leaves with green veins", "interveinal chlorosis",
                     "yellow new growth", "green veins"],
        "cause": "Iron unavailable to the plant — often due to high soil pH or overwatering.",
        "affected_plants": ["all"],
        "treatment": [
            "Apply an iron chelate supplement.",
            "Check and adjust soil pH to the appropriate range.",
            "Improve soil drainage.",
        ],
        "prevention": [
            "Use soil with the appropriate pH for the plant type.",
            "Avoid overwatering which reduces iron uptake.",
        ],
    },
    {
        "id": "magnesium_deficiency",
        "name": "Magnesium Deficiency",
        "category": "nutrient",
        "symptoms": ["interveinal chlorosis", "yellowing between veins",
                     "reddish purple tint", "purple leaves"],
        "cause": "Insufficient magnesium in the soil.",
        "affected_plants": ["all"],
        "treatment": [
            "Apply Epsom salt (magnesium sulfate) solution: 1 tsp per gallon of water.",
        ],
        "prevention": [
            "Use a balanced fertilizer that includes micronutrients.",
        ],
    },
    {
        "id": "potassium_deficiency",
        "name": "Potassium Deficiency",
        "category": "nutrient",
        "symptoms": ["yellow brown leaf margins", "leaf margin scorch",
                     "weak stems", "poor flowering", "poor fruiting", "brown edges"],
        "cause": "Insufficient potassium in the soil.",
        "affected_plants": ["all"],
        "treatment": [
            "Apply a potassium-rich fertilizer.",
            "Add wood ash (outdoor plants) or kelp extract.",
        ],
        "prevention": [
            "Use a balanced fertilizer.",
            "Test soil nutrient levels periodically.",
        ],
    },
    {
        "id": "nutrient_burn",
        "name": "Nutrient Burn (Over-fertilization)",
        "category": "nutrient",
        "symptoms": ["brown crispy leaf tips", "brown leaf margins", "white crust on soil",
                     "wilting", "leaf curl", "crispy tips"],
        "cause": "Excess fertilizer salts damage roots.",
        "affected_plants": ["all"],
        "treatment": [
            "Flush soil with plenty of clean water (3x pot volume).",
            "Stop fertilizing for 4-6 weeks.",
            "Repot with fresh soil if damage is severe.",
        ],
        "prevention": [
            "Follow fertilizer package rates — never exceed recommendations.",
            "Never fertilize dry soil.",
            "Less is more with fertilizer.",
        ],
    },
    # --- Fungal (10) ---
    {
        "id": "powdery_mildew",
        "name": "Powdery Mildew",
        "category": "fungal",
        "symptoms": ["white powdery spots", "powdery white coating", "white spots",
                     "leaves yellowing", "distorted growth", "white powder"],
        "cause": "Fungal infection that thrives in high humidity with poor airflow.",
        "affected_plants": ["all"],
        "treatment": [
            "Remove and dispose of affected leaves.",
            "Spray with a 1:10 milk-to-water solution or neem oil.",
            "Improve air circulation around plants.",
            "Apply a sulfur-based fungicide if severe.",
        ],
        "prevention": [
            "Space plants for adequate airflow.",
            "Avoid wetting foliage when watering.",
            "Use a fan for indoor plants to improve circulation.",
        ],
    },
    {
        "id": "early_blight",
        "name": "Early Blight",
        "category": "fungal",
        "symptoms": ["brown spots with concentric rings", "target pattern spots",
                     "brown spots", "yellowing around spots", "leaves dropping from bottom",
                     "lower leaves dying"],
        "cause": "Fungal infection (Alternaria solani), common in tomatoes.",
        "affected_plants": ["tomato", "tomatoes", "pepper", "peppers", "potato", "potatoes", "eggplant"],
        "treatment": [
            "Remove infected leaves promptly.",
            "Apply copper fungicide.",
            "Mulch around base to prevent soil splash onto leaves.",
        ],
        "prevention": [
            "Rotate crops annually.",
            "Water at soil level, not overhead.",
            "Space plants for good airflow.",
        ],
    },
    {
        "id": "late_blight",
        "name": "Late Blight",
        "category": "fungal",
        "symptoms": ["large dark brown patches", "black patches on leaves",
                     "white fuzzy growth", "white growth under leaves",
                     "rapid collapse", "dark brown spots", "black stems"],
        "cause": "Fungal infection (Phytophthora infestans), spreads rapidly in cool wet weather.",
        "affected_plants": ["tomato", "tomatoes", "potato", "potatoes"],
        "treatment": [
            "Remove and destroy infected plants (do not compost).",
            "Apply copper fungicide preventatively on remaining plants.",
        ],
        "prevention": [
            "Plant resistant varieties.",
            "Ensure good drainage.",
            "Avoid overhead watering.",
        ],
    },
    {
        "id": "leaf_spot",
        "name": "Leaf Spot (Fungal)",
        "category": "fungal",
        "symptoms": ["brown spots", "black spots", "spots with yellow halos",
                     "spots merging", "leaf drop", "yellow halos around spots"],
        "cause": "Various fungal pathogens (Cercospora, Septoria, etc.).",
        "affected_plants": ["all"],
        "treatment": [
            "Remove affected leaves.",
            "Apply a fungicide (copper-based or neem oil).",
            "Improve airflow around the plant.",
        ],
        "prevention": [
            "Water at soil level.",
            "Space plants properly.",
            "Clean up and dispose of fallen leaves.",
        ],
    },
    {
        "id": "fungal_root_rot",
        "name": "Fungal Root Rot",
        "category": "fungal",
        "symptoms": ["wilting despite moist soil", "wilting", "yellowing",
                     "stunted growth", "brown mushy roots", "black roots"],
        "cause": "Fungal pathogens (Pythium, Rhizoctonia) thriving in waterlogged soil.",
        "affected_plants": ["all"],
        "treatment": [
            "Unpot the plant and inspect roots.",
            "Remove all affected (brown/black/mushy) roots.",
            "Repot in fresh, sterile, well-draining soil.",
            "Apply a biological fungicide (Trichoderma).",
            "Reduce watering significantly.",
        ],
        "prevention": [
            "Use well-draining soil.",
            "Do not overwater.",
            "Sterilize pots between uses.",
        ],
    },
    {
        "id": "anthracnose",
        "name": "Anthracnose",
        "category": "fungal",
        "symptoms": ["dark sunken lesions", "sunken spots", "lesions on fruit",
                     "pinkish spore masses", "sunken spots on leaves"],
        "cause": "Fungal infection (Colletotrichum).",
        "affected_plants": ["all"],
        "treatment": [
            "Remove all infected plant parts.",
            "Apply a copper fungicide.",
            "Improve air circulation.",
        ],
        "prevention": [
            "Remove plant debris.",
            "Avoid overhead watering.",
            "Use disease-free seeds.",
        ],
    },
    {
        "id": "rust",
        "name": "Rust",
        "category": "fungal",
        "symptoms": ["orange pustules", "rust-colored spots", "rust pustules",
                     "yellow spots on top", "orange spots", "leaf drop", "rust spots"],
        "cause": "Fungal infection that requires moisture to spread.",
        "affected_plants": ["all"],
        "treatment": [
            "Remove infected leaves.",
            "Apply sulfur dust or neem oil.",
            "Improve airflow.",
        ],
        "prevention": [
            "Space plants for airflow.",
            "Water at soil level.",
            "Remove and destroy infected debris.",
        ],
    },
    {
        "id": "botrytis",
        "name": "Botrytis (Gray Mold)",
        "category": "fungal",
        "symptoms": ["gray fuzzy mold", "fuzzy gray growth", "brown spots",
                     "rapid decay", "gray mold", "mold on flowers"],
        "cause": "Fungal infection (Botrytis cinerea), thrives in humid conditions.",
        "affected_plants": ["all"],
        "treatment": [
            "Remove all infected or moldy parts immediately.",
            "Improve ventilation.",
            "Reduce ambient humidity.",
        ],
        "prevention": [
            "Remove dead flowers and leaves regularly.",
            "Space plants for airflow.",
            "Use a fan for indoor plants.",
        ],
    },
    {
        "id": "sooty_mold",
        "name": "Sooty Mold",
        "category": "fungal",
        "symptoms": ["black sooty coating", "sooty mold", "black coating on leaves",
                     "sticky residue", "honeydew"],
        "cause": "Fungal growth on honeydew secreted by sap-sucking pests (aphids, scale).",
        "affected_plants": ["all"],
        "treatment": [
            "Treat the underlying pest problem first (aphids, scale, whiteflies).",
            "Wipe leaves with a damp cloth.",
            "Wash leaves with mild soapy water.",
        ],
        "prevention": [
            "Control pest populations that produce honeydew.",
            "Monitor plants regularly for pests.",
        ],
    },
    {
        "id": "black_spot",
        "name": "Black Spot (Rose)",
        "category": "fungal",
        "symptoms": ["black spots on leaves", "black spots", "yellowing leaves",
                     "leaf drop", "spots with yellow halos"],
        "cause": "Fungal infection (Diplocarpon rosae), common on roses.",
        "affected_plants": ["rose", "roses"],
        "treatment": [
            "Remove and destroy infected leaves.",
            "Apply a fungicide labeled for black spot.",
            "Improve airflow by pruning.",
        ],
        "prevention": [
            "Water at soil level — never overhead.",
            "Space roses for airflow.",
            "Plant resistant varieties.",
            "Clean up fallen leaves in autumn.",
        ],
    },
    # --- Bacterial (3) ---
    {
        "id": "bacterial_leaf_spot",
        "name": "Bacterial Leaf Spot",
        "category": "bacterial",
        "symptoms": ["water-soaked spots", "angular spots", "spots between veins",
                     "brown black spots", "yellow halos", "spots on leaves"],
        "cause": "Bacterial infection (Xanthomonas, Pseudomonas).",
        "affected_plants": ["all"],
        "treatment": [
            "Remove infected leaves.",
            "Apply a copper-based bactericide.",
            "Avoid overhead watering.",
        ],
        "prevention": [
            "Space plants properly.",
            "Do not handle plants when wet.",
            "Use clean, sterilized tools.",
        ],
    },
    {
        "id": "bacterial_wilt",
        "name": "Bacterial Wilt",
        "category": "bacterial",
        "symptoms": ["rapid wilting", "wilting without yellowing", "entire plant wilting",
                     "milky ooze from stem", "no recovery at night", "sudden wilt"],
        "cause": "Bacterial infection (Ralstonia solanacearum), common in tomatoes and peppers.",
        "affected_plants": ["tomato", "tomatoes", "pepper", "peppers", "potato", "potatoes", "eggplant"],
        "treatment": [
            "Remove and destroy infected plants — there is no cure.",
            "Focus on prevention for remaining plants.",
        ],
        "prevention": [
            "Rotate crops on a 3-4 year cycle.",
            "Use resistant varieties.",
            "Control nematodes in soil.",
        ],
    },
    {
        "id": "crown_gall",
        "name": "Crown Gall",
        "category": "bacterial",
        "symptoms": ["swollen growths", "tumor-like growths", "swelling at soil line",
                     "galls on roots", "stunted growth"],
        "cause": "Bacterial infection (Agrobacterium tumefaciens).",
        "affected_plants": ["all"],
        "treatment": [
            "Remove and destroy infected plants — no chemical cure available.",
        ],
        "prevention": [
            "Avoid wounding plants during transplanting.",
            "Use disease-free planting stock.",
            "Sterilize soil before replanting.",
        ],
    },
    # --- Pests (9) ---
    {
        "id": "aphids",
        "name": "Aphids",
        "category": "pest",
        "symptoms": ["small insects on new growth", "green insects", "black insects",
                     "white insects", "sticky leaves", "honeydew", "distorted leaves",
                     "curling leaves", "ants on plant"],
        "cause": "Sap-sucking insect infestation.",
        "affected_plants": ["all"],
        "treatment": [
            "Spray off with a strong stream of water.",
            "Apply insecticidal soap or neem oil.",
            "Release ladybugs for outdoor plants.",
        ],
        "prevention": [
            "Inspect new plants before introducing them.",
            "Encourage beneficial insects (ladybugs, lacewings).",
            "Use yellow sticky traps for monitoring.",
        ],
    },
    {
        "id": "spider_mites",
        "name": "Spider Mites",
        "category": "pest",
        "symptoms": ["fine webbing", "webbing on plant", "stippled leaves",
                     "yellow speckled leaves", "tiny moving dots", "dots on leaf undersides",
                     "leaves dropping", "speckled leaves", "webbing"],
        "cause": "Tiny arachnid pests that thrive in hot, dry conditions.",
        "affected_plants": ["all"],
        "treatment": [
            "Spray with water to dislodge mites.",
            "Apply neem oil or a miticide.",
            "Increase humidity around the plant.",
            "Repeat treatment every 5-7 days until gone.",
        ],
        "prevention": [
            "Maintain adequate humidity.",
            "Mist plants regularly.",
            "Inspect the undersides of leaves routinely.",
        ],
    },
    {
        "id": "mealybugs",
        "name": "Mealybugs",
        "category": "pest",
        "symptoms": ["white cottony masses", "white fuzzy masses", "cottony growth",
                     "white growth in leaf joints", "sticky residue", "yellowing",
                     "stunted growth", "white cottony spots"],
        "cause": "Sap-sucking insects covered in white waxy filaments.",
        "affected_plants": ["all"],
        "treatment": [
            "Remove manually with a cotton swab dipped in rubbing alcohol.",
            "Apply insecticidal soap or neem oil.",
            "Use a systemic insecticide for severe infestations.",
        ],
        "prevention": [
            "Inspect new plants thoroughly.",
            "Isolate infested plants immediately.",
            "Monitor regularly, especially in leaf joints.",
        ],
    },
    {
        "id": "scale",
        "name": "Scale Insects",
        "category": "pest",
        "symptoms": ["brown bumps on stems", "yellow bumps", "hard bumps on stems",
                     "soft bumps", "sticky honeydew", "yellowing", "sooty mold",
                     "bumps on leaves"],
        "cause": "Sap-sucking insects with a protective waxy shell.",
        "affected_plants": ["all"],
        "treatment": [
            "Scrape off manually with a fingernail or cotton swab with alcohol.",
            "Apply neem oil or horticultural oil.",
            "Use a systemic insecticide for severe infestations.",
        ],
        "prevention": [
            "Inspect stems regularly.",
            "Quarantine new plants for 2 weeks.",
        ],
    },
    {
        "id": "fungus_gnats",
        "name": "Fungus Gnats",
        "category": "pest",
        "symptoms": ["small black flies", "flies around soil", "black flies",
                     "larvae in soil", "yellowing", "wilting from root damage"],
        "cause": "Small flies whose larvae feed on fungi and roots in wet soil.",
        "affected_plants": ["all"],
        "treatment": [
            "Allow the top layer of soil to dry between waterings.",
            "Apply a Bt (Bacillus thuringiensis) soil drench for larvae.",
            "Use yellow sticky traps to catch adults.",
        ],
        "prevention": [
            "Do not overwater.",
            "Top-dress soil with sand or diatomaceous earth.",
        ],
    },
    {
        "id": "whiteflies",
        "name": "Whiteflies",
        "category": "pest",
        "symptoms": ["tiny white insects", "white flying insects", "white moths",
                     "insects fly up when disturbed", "yellowing leaves",
                     "sticky honeydew", "white flies"],
        "cause": "Sap-sucking insects that multiply rapidly.",
        "affected_plants": ["all"],
        "treatment": [
            "Spray with insecticidal soap.",
            "Apply neem oil to leaf undersides.",
            "Use yellow sticky traps.",
            "Hang reflective mulch near plants (outdoor).",
        ],
        "prevention": [
            "Inspect the undersides of leaves on new plants.",
            "Use row covers outdoors.",
        ],
    },
    {
        "id": "thrips",
        "name": "Thrips",
        "category": "pest",
        "symptoms": ["silvery streaks", "white streaks on leaves", "silvery leaves",
                     "tiny black dots", "distorted flowers", "distorted leaves",
                     "scarred petals", "silver streaks"],
        "cause": "Tiny, slender insects that rasp and feed on plant tissue.",
        "affected_plants": ["all"],
        "treatment": [
            "Apply insecticidal soap or neem oil.",
            "Use blue sticky traps (thrips are attracted to blue).",
            "Release predatory mites for biological control.",
        ],
        "prevention": [
            "Remove weeds near plants.",
            "Inspect new plants very carefully.",
        ],
    },
    {
        "id": "caterpillars",
        "name": "Caterpillars / Cabbage Worms",
        "category": "pest",
        "symptoms": ["large irregular holes", "holes in leaves", "dark green droppings",
                     "leaves stripped", "chewed leaves", "ragged leaves"],
        "cause": "Caterpillar larvae feeding on foliage.",
        "affected_plants": ["all"],
        "treatment": [
            "Hand-pick caterpillars off plants.",
            "Apply Bt (Bacillus thuringiensis) spray.",
            "Use row covers to prevent egg-laying.",
        ],
        "prevention": [
            "Use row covers on brassicas.",
            "Encourage birds and beneficial insects.",
        ],
    },
    {
        "id": "slugs",
        "name": "Slugs and Snails",
        "category": "pest",
        "symptoms": ["large irregular holes", "holes in low leaves", "slimy trails",
                     "damage at night", "ragged holes", "silver trails"],
        "cause": "Mollusks that feed at night.",
        "affected_plants": ["all"],
        "treatment": [
            "Hand-pick slugs/snails at night with a flashlight.",
            "Set beer traps (shallow dish of beer at soil level).",
            "Apply iron phosphate bait (Sluggo).",
            "Create copper tape barriers around pots.",
        ],
        "prevention": [
            "Remove hiding spots (boards, debris, dense mulch).",
            "Water in the morning so the soil surface is dry at night.",
        ],
    },
    # --- Environmental (4) ---
    {
        "id": "cold_stress",
        "name": "Cold Temperature Stress",
        "category": "environmental",
        "symptoms": ["dark water-soaked patches", "dark patches on leaves",
                     "wilting", "leaf drop", "blackened stems", "cold damage"],
        "cause": "Exposure to cold temperatures, frost, or cold drafts.",
        "affected_plants": ["all"],
        "treatment": [
            "Move to a warmer location.",
            "Remove damaged parts once danger of frost has passed.",
            "Do not fertilize until the plant recovers.",
        ],
        "prevention": [
            "Keep plants away from cold windows and drafts.",
            "Move outdoor plants indoors before the first frost.",
            "Use frost cloth for outdoor protection.",
        ],
    },
    {
        "id": "heat_stress",
        "name": "Heat Stress",
        "category": "environmental",
        "symptoms": ["wilting in afternoon sun", "leaf scorch", "flower drop",
                     "fruit drop", "rapid soil drying", "drooping in heat"],
        "cause": "Excessive heat, especially combined with direct sunlight.",
        "affected_plants": ["all"],
        "treatment": [
            "Provide shade cloth during hottest hours.",
            "Water deeply and consistently.",
            "Move container plants to a cooler location.",
        ],
        "prevention": [
            "Apply mulch to keep roots cool.",
            "Provide afternoon shade for sensitive plants.",
            "Choose heat-tolerant varieties for hot climates.",
        ],
    },
    {
        "id": "low_humidity",
        "name": "Low Humidity",
        "category": "environmental",
        "symptoms": ["brown crispy leaf tips", "brown edges", "leaf curling",
                     "flower buds dropping", "slow growth", "crispy edges"],
        "cause": "Air is too dry (common indoors during winter heating, or for tropical plants).",
        "affected_plants": ["all"],
        "treatment": [
            "Use a humidifier near the plant.",
            "Place the pot on a pebble tray with water.",
            "Group plants together to create a microclimate.",
            "Mist plants that tolerate it (not African violets, etc.).",
        ],
        "prevention": [
            "Monitor humidity levels (aim for 40-60%).",
            "Use humidity trays under pots.",
            "Keep plants away from heating and AC vents.",
        ],
    },
    {
        "id": "draft_stress",
        "name": "Draft Stress",
        "category": "environmental",
        "symptoms": ["sudden leaf drop", "brown edges", "wilting despite proper care",
                     "leaves dropping suddenly"],
        "cause": "Hot or cold air from vents, doors, or windows stressing the plant.",
        "affected_plants": ["all"],
        "treatment": [
            "Move the plant away from vents, doors, and windows.",
            "Create a buffer or windbreak.",
        ],
        "prevention": [
            "Identify draft sources in your home.",
            "Relocate sensitive plants to stable-temperature areas.",
        ],
    },
    # --- Salt / Chemical (2) ---
    {
        "id": "salt_buildup",
        "name": "Salt Buildup",
        "category": "chemical",
        "symptoms": ["white crust on soil", "brown leaf tips", "stunted growth",
                     "wilting", "crust on soil surface"],
        "cause": "Accumulated mineral salts from fertilizer or hard water.",
        "affected_plants": ["all"],
        "treatment": [
            "Flush soil thoroughly with clean, room-temperature water.",
            "Repot with fresh soil if the buildup is severe.",
            "Switch to filtered or rain water.",
        ],
        "prevention": [
            "Flush soil quarterly with clean water.",
            "Use filtered or rain water instead of tap water.",
            "Do not over-fertilize.",
        ],
    },
    {
        "id": "herbicide_drift",
        "name": "Herbicide Drift",
        "category": "chemical",
        "symptoms": ["twisted leaves", "cupped leaves", "narrow strap-like growth",
                     "distorted leaves", "sudden widespread damage", "twisted growth",
                     "cupped growth"],
        "cause": "Wind-blown herbicide from nearby lawn or garden spraying.",
        "affected_plants": ["all"],
        "treatment": [
            "Wash the plant thoroughly with clean water.",
            "Prune affected growth.",
            "Wait for new, healthy growth to emerge.",
            "Note: there is no complete cure — some damage may be permanent.",
        ],
        "prevention": [
            "Avoid spraying herbicides on windy days.",
            "Do not use herbicide-treated grass clippings as mulch.",
            "Communicate with neighbors about spraying.",
        ],
    },
    # --- Physiological (3) ---
    {
        "id": "blossom_end_rot",
        "name": "Blossom End Rot",
        "category": "physiological",
        "symptoms": ["dark sunken patch on fruit", "leathery patch on fruit bottom",
                     "rot on bottom of fruit", "sunken fruit", "black bottom on tomato"],
        "cause": "Calcium deficiency in the fruit, usually caused by inconsistent watering.",
        "affected_plants": ["tomato", "tomatoes", "pepper", "peppers", "eggplant", "squash"],
        "treatment": [
            "Maintain consistent soil moisture (water evenly).",
            "Add calcium (agricultural lime or gypsum) to the soil.",
            "Mulch around plants to regulate soil moisture.",
        ],
        "prevention": [
            "Water regularly and deeply — avoid fluctuations.",
            "Add calcium to soil before planting.",
            "Test and adjust soil pH (6.0-6.8 for tomatoes).",
        ],
    },
    {
        "id": "leaf_scorch",
        "name": "Leaf Scorch",
        "category": "physiological",
        "symptoms": ["brown leaf margins", "brown tips", "tissue between veins green",
                     "overall browning of leaf edges"],
        "cause": "Water stress, wind exposure, or salt accumulation causing marginal tissue death.",
        "affected_plants": ["all"],
        "treatment": [
            "Water deeply and consistently.",
            "Apply mulch around the root zone.",
            "Protect the plant from wind.",
        ],
        "prevention": [
            "Maintain consistent watering.",
            "Provide wind protection for sensitive species.",
            "Avoid excessive fertilizer.",
        ],
    },
    {
        "id": "catfacing",
        "name": "Catfacing",
        "category": "physiological",
        "symptoms": ["deformed fruit", "scarred fruit", "puckered fruit",
                     "rough corky areas on fruit", "misshapen fruit"],
        "cause": "Incomplete pollination during cool weather.",
        "affected_plants": ["tomato", "tomatoes", "pepper", "peppers"],
        "treatment": [
            "No treatment needed — affected fruit is still edible.",
            "Wait for warmer weather for properly formed fruit.",
        ],
        "prevention": [
            "Plant after the soil has thoroughly warmed.",
            "Use varieties that are resistant to catfacing.",
            "Protect plants from cool nighttime temperatures.",
        ],
    },
]


# ---------------------------------------------------------------------------
# Diagnosis Engine
# ---------------------------------------------------------------------------
def _normalize(text):
    """Lowercase and strip for matching."""
    return text.strip().lower()


def _symptom_match(reported_symptom, problem_symptoms):
    """
    Check if a reported symptom matches any of a problem's known symptoms.
    Uses bidirectional substring matching with word overlap as fallback.
    """
    rs = _normalize(reported_symptom)
    for ps in problem_symptoms:
        ps_lower = ps.lower()
        # Exact or substring match (either direction)
        if rs in ps_lower or ps_lower in rs:
            return True
    # Word overlap fallback
    rs_words = set(rs.split())
    for ps in problem_symptoms:
        ps_words = set(ps.lower().split())
        overlap = rs_words & ps_words
        # Significant overlap (at least 1 word if reported symptom is 1-2 words,
        # at least 2 words if longer)
        if len(rs_words) <= 2 and len(overlap) >= 1:
            return True
        if len(rs_words) > 2 and len(overlap) >= 2:
            return True
    return False


def diagnose(plant, symptoms):
    """
    Diagnose plant problems from reported symptoms.

    Returns a sorted list of candidate diagnoses with confidence scores.
    """
    plant_lower = _normalize(plant)
    results = []

    for problem in KNOWLEDGE_BASE:
        # Filter by plant if problem is plant-specific
        affected = problem["affected_plants"]
        is_universal = "all" in affected
        plant_relevant = is_universal or any(
            p in plant_lower or plant_lower in p for p in affected
        )

        # Count matched symptoms
        matched = []
        for reported in symptoms:
            if _symptom_match(reported, problem["symptoms"]):
                matched.append(reported)

        if not matched:
            continue

        # Confidence: ratio of matched reported symptoms to total reported symptoms
        symptom_confidence = len(matched) / len(symptoms)

        # Penalize slightly if plant-specific problem doesn't match plant type
        plant_penalty = 0.0 if plant_relevant else 0.15

        confidence = round(max(0.0, symptom_confidence - plant_penalty), 2)

        if confidence > 0:
            results.append({
                "id": problem["id"],
                "name": problem["name"],
                "category": problem["category"],
                "confidence": confidence,
                "matched_symptoms": len(matched),
                "total_reported_symptoms": len(symptoms),
                "cause": problem["cause"],
                "treatment": problem["treatment"],
                "prevention": problem["prevention"],
                "plant_specific": not is_universal,
            })

    # Sort by confidence descending, then by matched symptoms
    results.sort(key=lambda x: (-x["confidence"], -x["matched_symptoms"]))
    return results


def get_by_id(problem_id):
    """Look up a problem by its ID."""
    pid = _normalize(problem_id)
    for problem in KNOWLEDGE_BASE:
        if problem["id"] == pid:
            return problem
    return None


def search_by_symptom(keyword):
    """Find all problems that match a symptom keyword."""
    kw = _normalize(keyword)
    results = []
    for problem in KNOWLEDGE_BASE:
        matched_syms = [s for s in problem["symptoms"] if kw in s.lower()]
        if matched_syms:
            results.append({
                "id": problem["id"],
                "name": problem["name"],
                "category": problem["category"],
                "matched_symptoms": matched_syms,
            })
    return results


def list_all():
    """List all problems in the knowledge base."""
    return [
        {
            "id": p["id"],
            "name": p["name"],
            "category": p["category"],
            "symptom_count": len(p["symptoms"]),
        }
        for p in KNOWLEDGE_BASE
    ]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Plant problem diagnostic tool."
    )
    sub = parser.add_subparsers(dest="command")

    p_diag = sub.add_parser("diagnose", help="Diagnose plant problem from symptoms")
    p_diag.add_argument("--plant", required=True, help="Plant type (e.g., 'tomato')")
    p_diag.add_argument("--symptoms", nargs="+", required=True,
                        help="One or more observed symptoms")

    sub.add_parser("list", help="List all known plant problems")

    p_info = sub.add_parser("info", help="Show details of a specific problem")
    p_info.add_argument("--id", required=True, help="Problem ID (e.g., 'spider_mites')")

    p_search = sub.add_parser("search", help="Search problems by symptom keyword")
    p_search.add_argument("--symptom", required=True, help="Symptom keyword to search")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "diagnose":
        diagnoses = diagnose(args.plant, args.symptoms)
        result = {
            "plant": args.plant,
            "symptoms_reported": args.symptoms,
            "diagnoses": diagnoses,
            "disclaimer": (
                "This tool is for informational and educational purposes only. "
                "For valuable or rare plants, consult a local horticulturist or "
                "agricultural extension service."
            ),
        }
        print(json.dumps(result, indent=2))

    elif args.command == "list":
        problems = list_all()
        print(json.dumps({"total": len(problems), "problems": problems}, indent=2))

    elif args.command == "info":
        problem = get_by_id(args.id)
        if problem:
            print(json.dumps(problem, indent=2))
        else:
            print(json.dumps({"error": f"Problem '{args.id}' not found."}, indent=2))
            sys.exit(1)

    elif args.command == "search":
        results = search_by_symptom(args.symptom)
        print(json.dumps(
            {"keyword": args.symptom, "results": results, "count": len(results)},
            indent=2,
        ))


if __name__ == "__main__":
    main()
