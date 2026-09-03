# Seed Crop Library — Data, Defaults, and Derivations

This reference documents the crop parameters used by `scripts/seed_calendar.py`, where the defaults come from, and how to override them for your climate.

## 1. The frost-date anchor

Everything derives from two dates:

- **Last spring frost** — the date with a 50% chance of no frost afterward. Sensitive crops use it with a safety delay; hardy crops deliberately jump it.
- **First fall frost** — 50% chance of no frost before it. Hardy crops keep producing 2–3 weeks past it (`frost_buffer`), tender crops stop at it.

**Finding yours:** NOAA's freeze/frost probability data (via weather.gov and state climate offices) gives dates at 10/50/90% probability. Gardeners who hate gambling use the 10% date (later in spring) for tender crops. Your state extension service publishes county-level tables — always better than a zone guess. Zone (USDA 3–10) maps average annual *minimum* winter temperature and correlates only loosely with frost dates; the built-in `frost --zone` table is a last-resort estimate with ±2 week reality.

## 2. Frost classes

| Class | Tolerates | Direct-sow timing | Fall buffer |
|---|---|---|---|
| hardy | −7°C and colder | 4–6 weeks *before* last frost | +21 days past first frost |
| half-hardy | 0 to −4°C | 0–4 weeks before last frost | +10 days |
| tender | any frost | 1–3 weeks *after* last frost, warm soil | 0 days |

Examples: spinach, pea, kale, onion, leek → hardy. Lettuce, beet, carrot, chard, potato → half-hardy. Tomato, pepper, cucumber, bean, squash, basil → tender.

## 3. Indoor start parameters

`wks_indoor` = weeks before last frost to sow indoors. Defaults (extension-typical):

| Crop | wks | Why |
|---|---|---|
| celery, leek | 10 | painfully slow germination + growth |
| onion | 8 | day-length sensitive, needs head start |
| pepper, eggplant | 9 | germinates slowly, wants 25°C soil |
| tomato | 7 | the classic; more = leggy |
| broccoli, cabbage, cauliflower, kale | 6 | spring + fall crops |
| basil | 5 | warm lover, fast grower |
| lettuce, bok-choy | 4 | quick; often direct-sown instead |
| cucumber, zucchini, squash, melon | 3 | resent root disturbance; peat pots/biodegradable cells |
| okra | 4 | warm soil lover |

`transplant_delay` = days after last frost to set out. Tender warm-soil crops wait: tomato +14, pepper/eggplant/melon/okra +21, cucurbits +7. Hardy transplants *jump* the frost date: brassicas and leeks at −14, lettuce at −7. Sowing indoors earlier than `wks_indoor` produces root-bound, leggy transplants — the classic beginner error this calendar exists to prevent.

**Potting up:** solanaceae (tomato/pepper/eggplant) sown at high density get potted into 4" cells 2 weeks before transplant. The calendar emits a POT-UP event for them.

**Hardening off:** 7 days before transplant, expose seedlings to outdoors 1 hour day 1, doubling daily; the calendar emits HARDEN-OFF as the start of that week.

## 4. Maturity days (`dt`)

`dt` is days-to-harvest measured **from transplant** for indoor-started crops and **from field sow** for direct crops — matching how seed packets label them. Values are mid-range for standard varieties (e.g., tomato 65, pepper 75, eggplant 80, broccoli 65 transplant, carrot 75, lettuce 55, radish 28, bush bean 55, pea 65, winter squash 100, watermelon 85). Cherry-type and fast varieties run 10–15 days shorter; big beefsteak and storage types longer. Override per-variety by editing the crop entry or passing `--json` output into your own tooling.

## 5. Plants-per-person and spacing

`per_person` = plants for steady table supply of one adult (synthesized from extension vegetable-garden planning guides):

- Heavy producers: tomato 3, zucchini 1–2, pepper 3, eggplant 2, winter squash 1–2, cucumber 3 (trellised)
- Cut-and-come-again / pick-many: bush bean 10, pole bean 4–5, pea 15, carrot 30, beet 20, potato 10 (10 ft of row), onion 20
- Single-head: lettuce 10 (succession), cabbage 3, broccoli 3, cauliflower 3, corn 15 (block planting for pollination)
- Herbs: basil 2, parsley 2, cilantro 3 (bolts — succession), dill 2

`spacing_in` (in-row): tomato 24, pepper 18, broccoli 18, cabbage 18–24, lettuce 10, carrot 2, beet 4, bush bean 4, pea 2, corn 9, onion 4, potato 12, zucchini 36, cucumber 12 (trellis), winter squash 48–60.

**Row-feet** = plants × spacing_in ÷ 12. Add ~40% aisle/bed overhead for real garden area; 4×8 ft raised beds ≈ 32 bed-ft ≈ two rows of most crops.

## 6. Succession planting

Crops with `succ` (days between re-sows): lettuce 14, arugula 14, spinach 14 (spring only — bolts; resume in fall), radish 7–10, carrot 21, beet 21, bush bean 21, cilantro 14, bok-choy 14, turnip 14, sweet corn 14 (or varieties with differing `dt`), kale 21 (or once + harvest leaves all season), pea once (spring) + once (mid-July for fall).

Succession chain stops when `sow + dt > first_frost + frost_buffer` — the tool enforces it automatically. Single-planting crops (tomato, pepper, squash, melon, winter squash) get no succession events; indeterminate tomatoes produce all season anyway.

## 7. Fall garden arithmetic

For a fall crop, count *backwards* from first frost:

```
sow_by (direct)   = first_frost + frost_buffer − dt − 7   (harvest/ripening buffer)
transplant_by     = first_frost + frost_buffer − dt
fall indoor sow   = transplant_by − wks_indoor × 7
```

The 7-day buffer covers slow germination in cooling soil and early frosts. Cool-season crops actually *taste better* in fall (sugar production in cold). Garlic is the special case: plant 4–6 weeks *before* first frost, mulch, harvest next July — the calendar emits FALL-PLANT for it instead of spring events.

## 8. Seed tray logistics

Standard flats: 72-cell (small seeds: onion, lettuce), 50-cell (brassicas, tomato), 32-cell (cucurbits that hate transplanting — or use soil blocks/peat pots). The tool computes cells at **plants × 1.2** (20% germination/thinning buffer), then trays at 72/50/32 cells and tray-weeks (shelf occupancy for light planning: a 4-shelf rack holds ~8 flats under 2 fixtures).

Germination heat: peppers/eggplant/celery want 25–29°C bottom heat until emergence; then grow cool-ish (18–21°C) with strong light — 12–14 h under LEDs, 2–3" above canopy. Leggy = light too weak or too far; not "too late at night."

## 9. Moon-phase mode (folklore, optional)

`--moon` annotates each sow date with the lunar phase and whether it matches the traditional rule: *above-ground crops (leaf/fruit) sown in the waxing moon (new→full), below-ground crops (roots) in the waning moon (full→new)*. Phase is computed from the mean synodic month (29.5306 d) referenced to the 2000-01-06 18:14 UTC new moon — accurate to ~±1 day, fine for a 2-week-wide rule. **There is no credible yield evidence for this practice.** It's included because gardeners ask, clearly labeled, never used to shift dates — only to annotate them.

## 10. Troubleshooting quick table

| Symptom | Likely cause | Fix |
|---|---|---|
| Tall pale seedlings falling over | insufficient light | 12–14 h light 2–3" above; don't start earlier than calendar |
| Seeds rot, no germination | cold wet soil | wait for window; use bottom heat indoors |
| Pepper transplants purple + stall | soil < 18°C | respect +21 d transplant delay; plastic mulch |
| Lettuce bitter, bolts | summer heat, full sun | succession gaps; afternoon shade in July–Aug |
| Carrots forked/hairy | fresh manure / rocks | deep sifted bed; sow in window, thin to 2" |
| Zero fall crop | missed sow-by dates | watch SOW-BY-FALL events in July |
