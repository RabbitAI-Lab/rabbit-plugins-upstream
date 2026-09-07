# Region Playbooks — What Each Hazard Actually Demands

The core idea of this skill: **preparedness is regional.** A kit that's
adequate in Kansas is negligent on the Gulf Coast, and money spent on
14-day supplies in Michigan ice country is misallocated from the heat plan
that actually saves lives there. This document explains each profile, why
the day-standards differ, and the reasoning behind the key checklist items.

## Why day-standards differ

The Ready.gov baseline is 1 gal/person/day × 3 days. That covers the
*typical* US outage: under 72 hours, municipal water intact. The profiles
raise that when the regional failure mode is worse:

- **hurricane-gulf (14 days):** Cat 3+ landfalls routinely leave counties
  without grid or potable water for 1-3 weeks (Harvey, Ian, Helene).
  Gulf-coast emergency management agencies explicitly recommend 14 days.
  Water systems lose pressure → boil notices; generators fail on day 4 of
  95°F heat; supply chains restart only when roads clear.
- **hurricane-atlantic (7 days):** inland effects of Atlantic landfalls —
  flooded substations, tree-downed distribution lines — typically restore
  in days, not weeks. 7 days covers the bad tail.
- **atmospheric-river (7 d water / 5 d food):** the water number is high
  for a different reason: flooding *contaminates* supply and triggers boil
  notices even where power survives.
- **tornado (3 days):** the hazard is 13 minutes of warning, not duration.
  Everything important happens BEFORE the storm: safe room chosen, helmets
  and shoes staged, everyone drilled. After a tornado, utilities usually
  restore fast outside the damage path.
- **ice-storm / blizzard (3-7 days):** the killer is indoor cold, not
  supply duration. Budget goes to heat, layers, and CO safety, not to
  stacking more canned goods.
- **wildfire-wui (3 days):** you will not shelter through a WUI fire; you
  will leave in minutes. The kit is a GO kit: documents, meds, N95s,
  devices — in the car before the red-flag warning.

## The P0 logic

Items are P0 (life-safety) when failure directly threatens life, P1 when
it materially worsens a multi-day outage, P2 for comfort. Examples:

- **CO alarm** is P0 if you own ANY fuel-burning device, because carbon
  monoxide is the leading post-storm killer in ice storms and hurricanes.
- **Helmets in tornado country** are P0 because head trauma from flying
  debris is the primary tornado injury mechanism; a bike helmet is the
  cheapest mortality reduction available.
- **Documents go-binder** is P0 (not P2) because insurance recovery after
  total loss depends on it, and it takes a weekend to build once.
- **Closed shoes at each bed** is P0 in wind regions: post-tornado floors
  are glassfields, and people instinctively run to check on family.

## Water purification fallbacks (why three methods)

1. **Boil** — most reliable, kills everything, needs fuel and a container.
2. **Unscented bleach 5-6%** — 8 drops/gal, mix, 30 min wait; chlorine
   smell confirms residual. Bleach degrades: replace yearly, date the
   bottle. Kills most pathogens; poor against cryptosporidium.
3. **Hollow-fiber filter** — bacteria/protozoa excellent (including
   crypto), but NOT viruses (municipal sewage contamination in floods CAN
   be viral — boil or bleach those sources).

Layering all three covers: no-power (filter), no-fuel (bleach), and
viral-risk (boil/bleach) scenarios.

## Power sizing notes

- **Duty cycle:** a modern refrigerator averages ~150 W × 8 h/day
  (compressor cycling), NOT its 600 W nameplate. Freezers similar.
- **Surge:** compressor start draws 3-5× running watts for ~1 s. Cheap
  inverter listings quote running watts; undersized inverters trip or
  die on surge. The plan's PEAK line multiplies compressor loads ×3.5.
- **Usable Wh:** lithium stations deliver ~85% of nameplate through an
  inverter (conversion + depth-of-discharge limits); lead-acid far less
  (50% DoD).
- **Solar reality:** a 100 W panel averages 300-500 Wh/day. That runs
  phones/radio/CPAP indefinitely; it does NOT run a fridge through
  cloudy post-storm days.
- **Medical devices:** register with your utility for priority
  restoration, keep 3× daily-energy in battery, and know your mechanical
  fallback. Oxygen concentrators (~350 W continuous) are in a different
  class than everything else — plan bottled O2 backup.

## Fridge/freezer discipline

Unopened refrigerator: ~4 h above safe temperature. FULL freezer: ~48 h
(half-full: 24 h). The `freeze-bottles` item exists because frozen water
bottles both extend cold-holding and become drinking water. Appliance
thermometers ($5) remove the guesswork — "when in doubt, throw it out"
is expensive guessing without them.

## Evacuation math (hurricane regions)

The checklist puts the evacuation decision at T-24h because of the
logistics curve: contraflow lanes and fuel availability collapse in the
final 12 hours. If you're in a surge zone, the correct answer to "should
we stay?" was decided by FEMA's SLOSH modeling years ago — your zone
assignment is public record. Riding out a surge-zone storm to avoid a
hotel bill is the most expensive decision in this entire document.

## Customizing

- `water_days_override` / `food_days_override` in the profile JSON: for
  medical needs (dialysis, infant formula), rural well properties, or
  island logistics.
- Inventory states: `have` / `partial` / `missing` per checklist ID —
  `audit` prints ✓/~/✗ accordingly and counts P0 prep gaps.
- Add region-agnostic items to the checklist source (`build_checklist`)
  — phases and priorities are plain data.
