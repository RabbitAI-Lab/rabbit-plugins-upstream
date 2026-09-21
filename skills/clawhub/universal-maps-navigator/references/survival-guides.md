# Survival Guides — Terrain & Natural Disasters (v2 NEW)

Sourced from public domain authoritative guides to reduce hallucination. Every guide cites source.

## Sources
- US Army FM 21-76 Survival Manual (public domain, 1970, reprinted)
- American Red Cross Emergency Preparedness Guides (public)
- NOAA National Weather Service
- USGS Earthquake Hazards
- FEMA Ready.gov
- WHO, WMS (Wilderness Medical Society)
- American Alpine Club, American Avalanche Association

## Terrain Survival

### Desert (FM 21-76 Ch.13, Red Cross)
- **S.T.O.P.**: Sit, Think, Observe, Plan
- Shade: rock outcrops, dunes, vehicle. Create wind-break tarp/clothing
- Water: sip every 15min, no ration to zero, no washing. Find: green vegetation, bird flight dawn/dusk, outer bends of dry riverbeds, solar still (plastic sheet over hole)
- Navigation: Shadow stick compass day (stick 90cm, mark shadow tip, wait 10min, second mark = E-W line, left of first = N in N hemisphere). Night: Polaris (N) or Southern Cross (S). Dunes shape shows prevailing wind
- Signal: 3 fires triangle 100m apart = international distress. Mirror flashes day, fire night. 3 whistle blasts = SOS
- Gear: wide-brim hat, SPF50+, 3L hydration + filter, bivy, mirror, whistle
- Don't: travel 11am-4pm, alcohol/caffeine, leave vehicle if stranded

### Mountain (FM 21-76 Ch.14, Alpine Club)
- Acclimatization: >2500m climb ≤300m/day, rest 3 days descend 500m. AMS = headache+nausea → descend immediately
- Lightning above treeline: crouch on insulated pad (pack), feet together, 50ft apart group, avoid caves/overhangs, poles horizontal, no single trees
- Avalanche: Move sideways, jump upslope, grab tree, swim, air pocket before snow settles, whistle. Beacon/shovel/probe mandatory
- Whiteout: Compass short hops landmark-to-landmark, pace count, altimeter + contours
- Hypothermia: Stay dry, layers (wicking base + insulating + waterproof shell), no cotton, warm fluids
- Camp: Halfway up hill (ridge windy, valley cold), avoid snow-loaded trees (widow makers), avalanche paths
- Signals: X 15ft legs 1ft wide = need rescue

### Jungle (FM 21-76 Ch.15)
- Stay on trails, blaze trees, arrow in ground for direction
- Water: Boil 5min or filter+chlorine, rainwater best, never stagnant
- Insects: DEET, long sleeves tucked, mosquito net, check boots
- Navigation: Follow water downstream to civilization, beware waterfalls. Sun breaks for compass
- Shelter: Hammock/raised platform, waterproof roof, clear overhead hazards
- Don't touch bright frogs/snakes

### Snow/Arctic (FM 21-76 Ch.16)
- Layers: Base wicking → Insulating fleece/down → Shell waterproof/windproof. No cotton
- Buried: Air pocket BEFORE snow settles, conserve air, whistle 3x, don't shout
- Crevasse: Spread arms to catch, rope anchor, pulley rescue
- Navigation: Snow covers landmarks → GPS+compass+pace count, follow ridges not valleys in whiteout
- Frostbite: Body heat warm, no rubbing/direct heat, shelter
- Don't eat snow directly (lowers core temp) — melt first
- Sunglasses essential (snow blindness)

### Swamp/Wetland (FM 21-76 Ch.17)
- Test ground with stick, avoid black bubbling water
- Stay dry: change socks, dry feet → trench foot prevention, knee-high waterproof boots
- Malaria risk, mosquito full coverage + DEET + net
- Follow high ground, game trails → water but also predators, mark path
- Never drink swamp water even filtered — boil + chemical

### Forest (FM 21-76 Ch.6, Maine Warden Service)
- Lost: S.T.O.P.
- Orient map: compass on map, align magnetic N-S lines
- Logging roads: trees pushed over lean = direction of deep woods → walk opposite to exit. Skid trails turn toward civilization at junction
- Shelter: Natural formations avoid low ground, lean-to, insulation from ground (80% heat loss to ground)
- Signal: Bright color outside shelter, whistle 3x, fires triangle
- Water: Green valleys, animal trails downhill
- Don't hide car — leave visible for rescuers
- Tell someone: where, headed, who with, vehicle description, return time

### Urban Disaster (FEMA)
- Earthquake urban: Drop under desk/table, away windows, no doorway myth. After: gas leaks, evacuate if smell
- Flood urban: Avoid underpasses, 15cm water knocks, 60cm floats car, go roof
- Fire urban: Crawl low under smoke, feel doors, stairs not elevator
- Navigation: Offline maps (Organic Maps/CoMaps), paper map backup, mark water/hospitals/shelters

## Natural Disasters

### Earthquake (USGS, FEMA, Red Cross)
- During INDOORS: Drop to hands/knees, Cover under sturdy table/desk, Hold On. Away windows. NOT run outside or doorway
- IN BED: Stay, pillow over head/neck
- OUTDOORS: Clear open area away buildings/trees/power lines, drop cover head/neck
- DRIVING: Pull over open area, avoid overpasses/bridges/power lines, stay inside until shaking stops
- After: Check injuries, gas leaks, fires, building damage. Gas smell → turn off, open windows, evacuate. Aftershocks → Drop-Cover-Hold again. Trapped: Cover mouth, don't shout (dust), tap pipe/wall, whistle
- Navigation: Roads cracked, bridges unsafe. Foot routing, avoid damaged. Check OSM Notes `umn reports --near` + `traffic` + app traffic layers

### Flood/Flash Flood (NOAA, FEMA)
- Higher ground immediately — roof if necessary. Never drive/walk through flood water: 15cm knocks person, 60cm floats car
- Avoid streams, drainage channels, underpasses. Flash floods rise minutes
- Car water rises → abandon, go roof, signal
- Listen NOAA radio/emergency alerts
- After: Avoid flood water — contaminated, debris, electrocution. Return only when authorities say safe
- Navigation: Use `umn elevation` to find high ground, `umn poi shelter --near`, avoid low highways, `isochrone` to high ground

### Wildfire (USFS, CAL FIRE)
- Non-flammable terrain FAST: gravel/dirt roads, grassland few trees, large water. Most dangerous downwind/uphill from fire
- Run TOWARD wind if wind not same as fire spread, or perpendicular to fire front
- Car: windows up, lights on, stay — flames unlikely reach if not forest, protect lungs
- Cover mouth/nose cloth, stay low, cover skin
- Trapped: lie in depression, cover with soil/wet clothing if possible
- After: hotspots, falling trees, ash pits, wear mask
- Navigation: Avoid forested routes, offline region + `route --avoid`, check wind via `weather`

### Hurricane/Cyclone/Typhoon (NHC, FEMA)
- Underground shelter (basement/storm cellar) or interior room without windows, lowest floor
- Avoid windows — flying debris lethal, cover head helmet/heavy object
- Storm surge warning → evacuate inland/high ground immediately — surge kills most
- Driving: Avoid, but if caught don't drive through flooded roads
- After: Avoid downed power lines, flooded areas, damaged buildings
- Navigation: Many roads blocked — foot routing + transit deep links, `poi shelter`

### Tornado (NWS)
- LOW: basement/storm cellar safest. If none, interior room lowest floor, away windows, cover head
- Outdoors: No shelter = lie flat ditch/depression, cover head, avoid underpasses (wind tunnel)
- No car/mobile home — evacuate to sturdy building
- After: Debris, downed lines
- Navigation: Avoid affected area, `isochrone` nearest shelter 5 min

### Avalanche (American Avalanche Association)
- Move SIDEWAYS out of slide path — center fastest. Jump upslope if possible
- Grab tree/rock, swim to stay surface, air pocket before snow stops
- Buried: Conserve air, whistle 3x, don't shout (wastes air)
- Beacon — companions rescue first 15 min = 90% survival
- After: Secondary slides
- Navigation: Avoid slopes 30-45° after fresh snow, elevation + aspect, `elevation` + `offline` topo

### Tsunami (NOAA, USGS)
- Strong earthquake near coast or water recedes fast → GO INLAND/HIGH GROUND IMMEDIATELY, no waiting
- ≥30m elevation or ≥2km inland. Vertical evacuation: top floors reinforced concrete building if no time
- Never go to coast to watch
- Boat offshore deep water — stay, don't return to harbor
- After: Stay high until official all-clear — multiple waves, avoid flood water
- Navigation: Coastal roads destroyed — inland routes, `elevation` to find 30m+, `matrix` to nearest high point

### Blizzard/Whiteout (NWS)
- Under cover — building, vehicle, snow cave. Avoid exposure >10 min
- Vehicle stranded: Stay, heater 10 min/hour, crack window, ensure exhaust not blocked, signal
- Whiteout: No landmarks, compass short hops, pace count, don't travel unless must
- Cover all skin, stay dry, warm fluids
- After: Frostbite/hypothermia, roads closed — `reports` + `traffic`
- Navigation: Offline maps, compass, dead reckoning, isochrone foot

### Sandstorm/Dust Storm (NOAA)
- LOW, protect face cloth, goggles if possible, cover mouth/nose
- Shelter behind rock/building/vehicle, avoid open. Driving: pull over, lights ON, windows closed, wait
- Run against debris flow if open, avoid flying objects
- Visibility zero — stop, shelter, wait, compass when clears
- After: Check lungs/eyes, clean gear, sand may block roads — `reports`
- Navigation: Shelter POI, weather check

### Landslide/Mudslide (USGS)
- Rumbling, cracks in ground → evacuate if warning
- Move UP and AWAY from slide path, not downhill, avoid valley bottoms
- If escape impossible, curl into ball, protect head
- After: Avoid slide area — secondary slides, check gas/water line breaks
- Navigation: Roads may be gone — foot routing, elevation, offline topo, `reports` for closures

## SOS International Signals

- 3 whistle blasts (or 3 fires triangle 100m apart, or 3 flashes) = international distress SOS
- Ground X: 15ft legs, 1ft wide body, contrast material = need rescue (most visible from air)
- Mirror flashes: Aim at plane/helicopter, sweep horizon
- Night: Fire, flashlight SOS (...---...), bright color outside shelter
- Stay put if you told someone your plan — moving makes search harder. If must move, mark direction with arrow stones
- Conserve phone battery: airplane mode, brief GPS check, SMS not call if weak signal
- Groups of 3: gun shots, whistle blasts, fires = distress

## Navigation SOS (when lost)

- S.T.O.P. — Sit, Think, Observe, Plan. Don't panic walk
- Orient map: compass on map, align magnetic N-S lines, map now oriented — terrain matches
- Dead reckoning: bearing + pace count. Pick visible object on bearing, walk to it, repeat
- Follow water downstream to civilization, but beware waterfalls/cliffs
- Logging roads: trees pushed over lean = direction of deep woods → walk opposite to exit. Skid trails turn toward civilization at junction
- Night: Polaris = true north (N hemisphere). Southern Cross points south (S hemisphere)
- Tell someone: what you're doing, where headed, who with, vehicle description, return time. Don't hide car — leave visible for rescuers
