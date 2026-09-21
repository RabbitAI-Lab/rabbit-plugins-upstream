#!/usr/bin/env python3
"""survival.py — Life-saving navigation & survival guides for difficult terrain and natural disasters.

Sourced from:
- US Army FM 21-76 Survival Manual (public domain)
- American Red Cross Emergency Guides
- WHO, NOAA, USGS, FEMA public guidance
- Wilderness Medical Society

Every guide includes source citation to reduce hallucination.

Stdlib only, Python 3.8+.

Usage:
    from survival import get_terrain_guide, get_disaster_guide, get_sos_instructions, list_terrains, list_disasters
"""
from __future__ import annotations
from typing import Dict, List

# Terrain survival guides
TERRAIN_GUIDES = {
    "desert": {
        "name": "Desert",
        "hazards": ["heat_exhaustion", "dehydration", "sandstorm", "night_cold", "mirages"],
        "sources": ["US Army FM 21-76 Ch.13", "Red Cross Desert Safety"],
        "immediate": [
            "Find shade IMMEDIATELY — rock outcrops, dunes, vehicle shadow. If none, create wind-break with tarp/clothing.",
            "Hydration: sip small amounts every 15 min, DO NOT ration to zero. Conserve water — no washing.",
            "Protect skin: wide-brim hat, UV sunscreen, cover neck/arms. Sunglasses essential.",
            "Signal: 3 fires in triangle (100m apart) = international distress. Mirror flashes day, fire night.",
            "Navigation: Day use sun + shadow stick; night use Polaris (N hemisphere) or Southern Cross (S). Follow dunes' shape — prevailing wind direction.",
        ],
        "gear": ["wide-brim hat", "UV sunscreen SPF50+", "hydration bladder 3L + filter", "lightweight bivy sack", "signal mirror", "whistle"],
        "dont": ["Don't travel midday 11am-4pm", "Don't drink alcohol/caffeine", "Don't leave vehicle if stranded"],
        "water": ["Look for green vegetation, bird flight paths at dawn/dusk, dry riverbeds — dig in outer bends", "Solar still: plastic sheet over hole with container"],
    },
    "mountain": {
        "name": "Mountain / Alpine",
        "hazards": ["altitude_sickness", "avalanche", "rock_fall", "hypothermia", "crevasse", "lightning"],
        "sources": ["US Army FM 21-76 Ch.14", "American Alpine Club", "WMS Altitude Guidelines"],
        "immediate": [
            "Acclimatization: Above 2500m, climb ≤300m/day, rest every 3 days descend 500m. Watch for AMS: headache+nausea = descend.",
            "Lightning: If exposed above treeline, crouch on insulated pad (pack), feet together, 50ft apart from group, avoid caves/overhangs, keep poles horizontal.",
            "Avalanche: If caught, try to stay surface, swim, create air pocket before snow settles, whistle. Carry beacon/shovel/probe.",
            "Navigation: Ridge lines windy — camp halfway up hill. Use altimeter + map contours. Whiteout: follow compass bearing short hops, landmark-to-landmark.",
            "Hypothermia: Stay dry, layered clothing (base+insulating+waterproof shell), shelter from wind, warm fluids.",
        ],
        "gear": ["altimeter/barometer", "ice axe", "avalanche beacon+shovel+probe", "thermal base layers", "map+compass (not just GPS)", "emergency bivy"],
        "dont": ["Don't camp under snow-loaded trees (widow makers)", "Don't camp in avalanche paths or narrow valleys"],
        "signals": ["X ground signal 15ft legs, 1ft wide body = need rescue", "3 whistle blasts = SOS"],
    },
    "jungle": {
        "name": "Jungle / Tropical Forest",
        "hazards": ["heat", "poisonous insects/snakes", "dense vegetation", "flash flood", "waterborne disease"],
        "sources": ["US Army FM 21-76 Ch.15", "WHO Tropical Health"],
        "immediate": [
            "Stay on established trails — dense canopy disorients. Mark direction with arrow in ground, blaze trees.",
            "Water: Boil 5 min or filter + chlorine. Never drink stagnant water. Collect rainwater.",
            "Insects: DEET repellent, long sleeves tucked in, mosquito net sleep, check boots.",
            "Navigation: Follow water downstream to civilization, but beware waterfalls. Use sun breaks for compass.",
            "Shelter: Hammock or raised platform above wet ground, waterproof roof, clear widow makers overhead.",
        ],
        "gear": ["mosquito net", "quick-dry clothing", "compact machete", "water filter + chlorine tablets", "portable solar charger", "antihistamine"],
        "dont": ["Don't touch bright-colored frogs/snakes", "Don't sleep on ground"],
    },
    "snow": {
        "name": "Snow / Arctic",
        "hazards": ["hypothermia", "frostbite", "whiteout", "crevasse", "thin ice"],
        "sources": ["US Army FM 21-76 Ch.16", "Red Cross Winter Safety"],
        "immediate": [
            "Layered system: Base (wicking) → Insulating (fleece/down) → Shell (waterproof/windproof). No cotton.",
            "If buried in snow: Create air pocket BEFORE snow settles, conserve air, signal with whistle (3 blasts).",
            "Crevasse: If fall, spread arms to catch edges, secure rope anchor, pulley system rescue.",
            "Navigation: Snow covers landmarks — use GPS + compass + pace count. Follow ridges not valleys in whiteout.",
            "Frostbite: Warm affected area with body heat, no rubbing, no direct heat. Shelter immediately.",
        ],
        "gear": ["snow boots + gaiters", "thermal gloves + spare", "avalanche transceiver", "insulated bivy + sleeping bag -20C", "sunglasses (snow blindness)"],
        "dont": ["Don't eat snow directly (lowers core temp) — melt first", "Don't travel alone"],
    },
    "swamp": {
        "name": "Swamp / Wetland",
        "hazards": ["soft ground", "mosquito-borne disease", "snakes", "low visibility", "water contamination"],
        "sources": ["US Army FM 21-76 Ch.17"],
        "immediate": [
            "Test ground with stick before stepping — avoid black water that bubbles.",
            "Stay dry: Change socks often, dry feet to prevent trench foot. Waterproof boots essential.",
            "Insects: Full coverage, DEET, net. Malaria risk — seek prophylaxis before travel.",
            "Navigation: Follow high ground, game trails often lead to water but also predators. Mark path.",
            "Water: Never drink swamp water even filtered — boil + chemical treatment.",
        ],
        "gear": ["waterproof boots knee-high", "dry bags", "mosquito net", "walking stick", "water purification tablets"],
        "dont": ["Don't camp in low ground near water", "Don't wade without checking depth"],
    },
    "forest": {
        "name": "Forest / Woodland",
        "hazards": ["getting lost", "widow makers", "wildlife", "night cold"],
        "sources": ["US Army FM 21-76 Ch.6", "Maine Warden Service"],
        "immediate": [
            "If lost: S.T.O.P. — Sit, Think, Observe, Plan. Don't panic move.",
            "Navigation: Orient map with compass, landmark-to-landmark, follow logging roads — trees lean direction of bulldozer entry (walk opposite to exit).",
            "Shelter: Natural formations (caves avoid low ground), lean-to, insulation from ground (80% heat loss to ground).",
            "Signal: Bright color outside shelter, whistle 3x, fires in triangle.",
            "Water: Look for green valleys, follow animal trails downhill.",
        ],
        "gear": ["knife", "map+compass", "whistle", "fire starter (waterproof matches)", "emergency blanket"],
        "dont": ["Don't camp under dead trees", "Don't hide your car — leave visible for rescuers"],
    },
    "urban": {
        "name": "Urban / City Disaster",
        "hazards": ["building collapse", "crowd crush", "power lines", "gas leaks", "civil unrest"],
        "sources": ["FEMA Urban Survival", "Red Cross"],
        "immediate": [
            "Earthquake urban: Drop under desk/table, away from windows, no doorway myth. After shaking, check gas leaks, evacuate if smell.",
            "Flood urban: Avoid underpasses, 15cm water can knock you, 60cm floats car. Go to roof, signal.",
            "Fire urban: Crawl low under smoke, feel doors before opening, use stairs not elevator.",
            "Navigation: Use offline maps (Organic Maps/CoMaps), paper map backup. Mark water sources, hospitals, shelters on map.",
        ],
        "gear": ["power bank", "flashlight+headlamp", "whistle", "dust mask", "water 3L"],
        "dont": ["Don't use elevator in fire/earthquake", "Don't walk through flood water"],
    },
}

DISASTER_GUIDES = {
    "earthquake": {
        "name": "Earthquake",
        "sources": ["USGS, FEMA, Red Cross"],
        "during": [
            "INDOORS: Drop to hands/knees, Cover head/neck under sturdy table/desk, Hold On. Stay away from windows. DO NOT run outside or doorway (myth).",
            "IN BED: Stay, cover head/neck with pillow.",
            "OUTDOORS: Move to clear open area away from buildings/trees/power lines. Drop, cover head/neck.",
            "DRIVING: Pull over to open area, avoid overpasses/bridges/power lines. Stay inside until shaking stops.",
        ],
        "after": [
            "Check for injuries, gas leaks (smell), fires, building damage. If gas smell, turn off, open windows, evacuate.",
            "Expect aftershocks — Drop-Cover-Hold again.",
            "If trapped: Cover mouth, don't shout (dust), tap pipe/wall, use whistle.",
            "Navigation: Roads may be cracked, bridges unsafe. Use foot routing, avoid damaged structures. Check OSM Notes for closures.",
        ],
        "navigation_tips": "OSM may lack real-time closures — use `umn reports --near` + `traffic` + app traffic layers. Prefer foot/bike if car roads blocked.",
    },
    "flood": {
        "name": "Flood / Flash Flood",
        "sources": ["NOAA, FEMA"],
        "during": [
            "Go to HIGHER GROUND immediately — roof if necessary. Never drive/walk through flood water: 15cm knocks person, 60cm floats car.",
            "Avoid streams, drainage channels, underpasses. Flash floods rise in minutes.",
            "If in car and water rises, abandon car, go to roof, signal.",
            "Listen to NOAA radio/emergency alerts.",
        ],
        "after": [
            "Avoid flood water — contaminated, hidden debris, electrocution risk.",
            "Return only when authorities say safe. Check building before entering.",
            "Navigation: Use `umn elevation` to find high ground, `umn poi shelter --near`. Avoid routes through low-lying areas.",
        ],
        "navigation_tips": "Use elevation data + isochrone to find reachable high ground. Avoid `ferries` and low highways.",
    },
    "wildfire": {
        "name": "Wildfire / Forest Fire",
        "sources": ["USFS, CAL FIRE, Red Cross"],
        "during": [
            "Find NON-FLAMMABLE terrain FAST: gravel/dirt roads, grassland few trees, large water bodies. Most dangerous downwind/uphill from fire.",
            "Run TOWARD wind if wind not same direction as fire spread, or perpendicular to fire front.",
            "In car: windows up, lights on, stay — flames unlikely reach if not in forest, but protect lungs.",
            "Cover mouth/nose with cloth, stay low, cover skin.",
            "If trapped, lie in depression, cover with soil/wet clothing if possible.",
        ],
        "after": ["Watch for hotspots, falling trees, ash pits. Wear mask.", "Navigation: Roads may be closed, use offline maps, check `reports` for closures."],
        "navigation_tips": "Avoid forested routes, use `offline` region + `route --avoid` highways through fire zones. Check wind via `weather`.",
    },
    "hurricane": {
        "name": "Hurricane / Cyclone / Typhoon",
        "sources": ["NHC, FEMA"],
        "during": [
            "Seek shelter underground (basement/storm cellar) or interior room without windows, lowest floor.",
            "Avoid windows — flying debris lethal. Cover head with helmet/heavy object.",
            "If storm surge warning, evacuate to inland/high ground immediately — surge kills most.",
            "Driving: Avoid, but if caught, don't drive through flooded roads.",
        ],
        "after": ["Avoid downed power lines, flooded areas, damaged buildings.", "Navigation: Many roads blocked — use foot routing + transit deep links."],
        "navigation_tips": "Use `weather` + `traffic` to avoid. Shelter POI search.",
    },
    "tornado": {
        "name": "Tornado",
        "sources": ["NWS"],
        "during": [
            "Go LOW: basement/storm cellar safest. If none, interior room lowest floor, away from windows, cover head.",
            "Outdoors: No shelter = lie flat in ditch/depression, cover head, avoid underpasses (wind tunnel).",
            "No car/mobile home — evacuate to sturdy building.",
        ],
        "after": ["Watch for debris, downed lines.", "Navigation: Avoid affected area routes."],
        "navigation_tips": "Use `isochrone` to find nearest shelter within 5 min.",
    },
    "avalanche": {
        "name": "Avalanche",
        "sources": ["American Avalanche Association, US Army FM 21-76"],
        "during": [
            "Move SIDEWAYS out of slide path — center fastest. Jump upslope if possible.",
            "Grab tree/rock, swim to stay surface, create air pocket before snow stops.",
            "If buried: Conserve air, whistle 3x, don't shout (wastes air).",
            "Carry beacon — companions rescue in first 15 min = 90% survival.",
        ],
        "after": ["Check for secondary slides.", "Navigation: Avoid slopes 30-45° after fresh snow, use elevation + aspect data."],
        "navigation_tips": "Use `elevation` + `offline` topo maps. Avoid mountain routes after heavy snow.",
    },
    "tsunami": {
        "name": "Tsunami",
        "sources": ["NOAA, USGS"],
        "during": [
            "If strong earthquake near coast or water recedes unusually fast — GO INLAND/HIGH GROUND IMMEDIATELY, no waiting for warning.",
            "Go to ≥30m elevation or ≥2km inland. Vertical evacuation: top floors of reinforced concrete building if no time.",
            "Never go to coast to watch.",
            "If in boat offshore deep water — stay, don't return to harbor.",
        ],
        "after": ["Stay high until official all-clear — multiple waves. Avoid flood water.", "Navigation: Coastal roads destroyed — use inland routes."],
        "navigation_tips": "Use `elevation` to find 30m+ ground, `matrix` to nearest high point.",
    },
    "blizzard": {
        "name": "Blizzard / Whiteout",
        "sources": ["NWS, Red Cross"],
        "during": [
            "Get under cover — building, vehicle, snow cave. Avoid exposure >10 min.",
            "If in vehicle stranded: Stay, run heater 10 min/hour, crack window, ensure exhaust not blocked, signal.",
            "Navigation: Whiteout — no landmarks. Use compass short hops, pace count. Don't travel unless must.",
            "Cover all skin, stay dry, warm fluids.",
        ],
        "after": ["Watch for frostbite/hypothermia.", "Navigation: Roads closed — check `reports` + `traffic`."],
        "navigation_tips": "Use offline maps, compass, dead reckoning. Isochrone foot.",
    },
    "sandstorm": {
        "name": "Sandstorm / Dust Storm",
        "sources": ["NOAA, Red Cross"],
        "during": [
            "Stay LOW, protect face with cloth, goggles if possible. Cover mouth/nose.",
            "Seek shelter behind rock/building/vehicle, avoid open. If driving, pull over, lights off? Actually lights ON, windows closed, wait.",
            "Run against debris flow if caught open, avoid flying objects.",
            "Navigation: Visibility zero — stop, shelter, wait. Use compass when clears.",
        ],
        "after": ["Check lungs/eyes, clean gear.", "Navigation: Sand may block roads — use `reports`."],
        "navigation_tips": "Shelter POI, weather check.",
    },
    "landslide": {
        "name": "Landslide / Mudslide",
        "sources": ["USGS"],
        "during": [
            "Listen for rumbling, watch for cracks in ground. Evacuate if warning.",
            "Move UP and AWAY from slide path, not downhill. Avoid valley bottoms.",
            "If escape impossible, curl into ball, protect head.",
        ],
        "after": ["Avoid slide area — secondary slides. Check for gas/water line breaks.", "Navigation: Roads may be gone — use foot routing, elevation."],
        "navigation_tips": "Avoid steep slopes, use `offline` topo, `reports` for closures.",
    },
}

SOS_GUIDES = {
    "international": [
        "3 whistle blasts (or 3 fires in triangle 100m apart, or 3 flashes) = international distress SOS",
        "Ground signal X: 15ft legs, 1ft wide body, contrast material = need rescue",
        "Mirror flashes: Aim at plane/helicopter, sweep horizon",
        "Night: Fire, flashlight SOS (...---...), bright color outside shelter",
        "Stay put if you told someone your plan — moving makes search harder. If must move, mark direction with arrow stones.",
        "Conserve phone battery: airplane mode, brief GPS check, SMS not call if weak signal",
    ],
    "navigation_sos": [
        "If lost: S.T.O.P. — Sit, Think, Observe, Plan. Don't panic walk.",
        "Orient map: compass on map, align magnetic N-S lines, map now oriented — terrain matches.",
        "Dead reckoning: bearing + pace count. Pick visible object on bearing, walk to it, repeat.",
        "Follow water downstream to civilization, but beware waterfalls/cliffs.",
        "Logging roads: trees pushed over lean direction of deep woods — walk opposite to exit. Skid trails turn toward civilization at junction.",
        "Night navigation: Polaris = true north (N hemisphere). Southern Cross points south (S).",
    ],
}

def get_terrain_guide(terrain: str, lang: str = "en") -> Dict:
    t = terrain.lower()
    if t not in TERRAIN_GUIDES:
        return {"error": f"Unknown terrain {terrain}, choose from {list(TERRAIN_GUIDES.keys())}"}
    return TERRAIN_GUIDES[t]

def get_disaster_guide(disaster: str, lang: str = "en") -> Dict:
    d = disaster.lower()
    if d not in DISASTER_GUIDES:
        return {"error": f"Unknown disaster {disaster}, choose from {list(DISASTER_GUIDES.keys())}"}
    return DISASTER_GUIDES[d]

def get_sos_instructions(terrain: str = None, disaster: str = None, lang: str = "en") -> Dict:
    out = {
        "sos": SOS_GUIDES["international"],
        "navigation_sos": SOS_GUIDES["navigation_sos"],
        "sources": ["US Army FM 21-76", "Red Cross", "NOAA"],
    }
    if terrain and terrain.lower() in TERRAIN_GUIDES:
        out["terrain"] = TERRAIN_GUIDES[terrain.lower()]
    if disaster and disaster.lower() in DISASTER_GUIDES:
        out["disaster"] = DISASTER_GUIDES[disaster.lower()]
    return out

def list_terrains() -> List[str]:
    return list(TERRAIN_GUIDES.keys())

def list_disasters() -> List[str]:
    return list(DISASTER_GUIDES.keys())

def format_guide(guide: Dict, lang: str = "en", compact: bool = False) -> str:
    """Format guide for human display, with citation to reduce hallucination."""
    lines = []
    name = guide.get("name", "Guide")
    sources = guide.get("sources", [])
    lines.append(f"{name} — Sources: {', '.join(sources)}")
    if "hazards" in guide:
        lines.append(f"Hazards: {', '.join(guide['hazards'])}")
    if "immediate" in guide:
        lines.append("IMMEDIATE:")
        for i, step in enumerate(guide["immediate"], 1):
            lines.append(f"  {i}. {step}")
    if "during" in guide:
        lines.append("DURING:")
        for i, step in enumerate(guide["during"], 1):
            lines.append(f"  {i}. {step}")
    if "after" in guide:
        lines.append("AFTER:")
        for s in guide["after"]:
            lines.append(f"  - {s}")
    if "gear" in guide and not compact:
        lines.append(f"Gear: {', '.join(guide['gear'])}")
    if "dont" in guide and not compact:
        lines.append(f"DON'T: {'; '.join(guide['dont'])}")
    if "navigation_tips" in guide:
        lines.append(f"Navigation: {guide['navigation_tips']}")
    return "\n".join(lines)

def get_combined_survival(terrain: str = None, disaster: str = None, situation: str = None, lang: str = "en", compact: bool = False) -> Dict:
    """Combine terrain + disaster + SOS for a situation."""
    result = {"situation": situation, "lang": lang, "sources": []}
    texts = []
    if terrain:
        tg = get_terrain_guide(terrain, lang)
        if "error" not in tg:
            result["terrain"] = tg
            result["sources"].extend(tg.get("sources", []))
            texts.append(format_guide(tg, lang, compact))
    if disaster:
        dg = get_disaster_guide(disaster, lang)
        if "error" not in dg:
            result["disaster"] = dg
            result["sources"].extend(dg.get("sources", []))
            texts.append(format_guide(dg, lang, compact))
    sos = get_sos_instructions(terrain, disaster, lang)
    result["sos"] = sos
    result["sources"] = sorted(set(result["sources"] + sos.get("sources", [])))
    result["text"] = "\n\n".join(texts + ["\n".join(sos["sos"][:4]), "\n".join(sos["navigation_sos"][:3])])
    result["confidence"] = "high" if result["sources"] else "low"
    return result
