# Equipment — Rewriting a Recipe for a Different Device

Each device changes the mechanism, not only the speed. The rewrite has three parts: the time mapping, the liquid correction, and the step that has to move (usually browning).

**Read `## Kitchen` in `~/Clawic/data/recipe/memory.md` first**: what the user owns, what they refuse to use, the oven's measured offset, and the vessel ceilings. Rewriting a recipe for a device that is not in the kitchen is wasted work, and `restrictions.no_equipment` in `config.yaml` says which ones to never propose.

## Device Mapping

| From → To | Time | Liquid | What has to move |
|---|---|---|---|
| Oven braise → pressure cooker | ~⅓ of the oven time at high pressure, plus come-to-pressure (8-15 min) and release | **Minimum 150-250 ml free liquid** or it will not come to pressure; nothing evaporates, so cut the recipe's liquid by ~⅓ beyond that | Sear on sauté mode first; reduce the sauce uncovered after, because a pressure cooker cannot reduce |
| Oven braise → slow cooker | Low ≈ 7-8 h, High ≈ 3-4 h for a 3 h oven braise | Cut liquid by ~⅓-½; a sealed slow cooker loses almost none | Brown separately; add dairy, delicate vegetables and fresh herbs in the last 30 min |
| Slow cooker → pressure cooker | High 4 h ≈ 35-45 min at pressure for tough cuts | Keep the pressure minimum | Natural release for meat (10-15 min), quick release for vegetables — a quick release on meat squeezes the juice out |
| Oven roast → air fryer | Reduce temperature 20 °C and time ~20% | None | Batch size: the basket must be in one layer with gaps. An air fryer is a small convection oven, so a doubled batch is two rounds, not a longer one |
| Deep fry → air fryer | Time roughly doubles at 190-200 °C | Brush with 5-10 ml oil per portion | Battered wet coatings do not transfer at all — breadcrumb or dry coatings only |
| Hob → oven (braise, stew) | 150-160 °C for the same total time | Unchanged | The oven's all-round heat removes the stirring and the scorching risk |
| Oven bread → bread machine | The machine owns the schedule | Follow the machine's flour-to-liquid order and its maximum flour weight | Enriched doughs with >10% butter or sugar need the machine's sweet cycle; a lean 70%+ hydration dough will not knead in most machines |
| Anything → sous vide | Hours at the target internal temperature; time controls texture, not doneness | Bag, none added | Sear before *and* after is optional; sear after is mandatory. Nothing browns in the bath |
| Stand mixer → hand | Kneading ~10-12 min by hand ≈ 6-8 min on speed 2 | None | Windowpane test replaces the timer |
| Wok → domestic hob | The recipe fails at scale | None | Cook in half batches; a domestic burner cannot recover the heat, and the observable is liquid pooling instead of hissing |

## Pressure Cookers

- Time starts when pressure is reached, not when the lid closes. Total elapsed = come-to-pressure (8-15 min, scales with volume and starting temperature) + cook + release.
- **Time does not scale with quantity.** Doubling the meat does not change the pressure time; it changes only the come-to-pressure time. This is the one place where a doubled batch is genuinely free.
- Fill limits: ⅔ full for most foods, **½ for anything that foams** — pulses, grains, pasta, milk. Exceeding it blocks the valve.
- Natural release continues cooking for 10-15 minutes; a recipe that says "10 min then natural release" means ~25 minutes of cooking. Quick release stops it dead and is right for vegetables and seafood.
- At altitude, add ~5% cook time per 300 m above 600 m — a pressure cooker offsets altitude but does not erase it.
- Dairy, thickeners and delicate greens go in after the pressure cook, never before: cornflour scorches on the base and cream splits.

## Slow Cookers

- Low and High reach the same final temperature (~93-100 °C); High just gets there faster. Low is not gentler, it is slower.
- Almost no evaporation: a recipe transferred without cutting the liquid produces a thin, pale sauce. Cut ⅓-½, and reduce on the hob at the end if needed.
- Lifting the lid costs ~20-30 minutes of recovery. Resist it.
- Dried kidney beans must be boiled hard for 10 minutes before they go in — slow-cooker temperatures are inside the range where their lectin is most concentrated. Tinned beans are fine.
- What it is good at: tough collagen-rich cuts, pulses, stocks. What it is bad at: anything that wants texture contrast, and anything under 2 hours.

## Air Fryers and Convection

- It is a small fan oven with a short distance to the element: fast, uneven, and utterly dependent on airflow. One layer, gaps between pieces, shake or turn at the halfway point.
- Preheat 3-5 min for anything that should crisp on contact.
- Capacity is the real constraint, and it is a *surface area*, not a volume — the same rule as a tray (`scaling.md`).
- Small quantities of sugar or marinade drip and burn onto the element; line the basket for anything glazed, but never block the airflow underneath.

## Sous Vide

- Temperature sets doneness; time sets texture. 56 °C for 1 h and 56 °C for 4 h are both medium-rare; the second is more tender.
- Pasteurization is a time-at-temperature pair, not a single number: below 60 °C, hold times run from tens of minutes to hours depending on thickness. Below 54.4 °C, do not hold food for extended periods.
- Chill fast or serve immediately; the danger zone is the same as everywhere else.
- Nothing browns. The sear is a separate step, hot and dry, on a surface patted completely dry.

## Ovens, Hobs, and Tins

- Gas hobs respond instantly, induction responds instantly and holds better, electric coils lag by minutes — a recipe that says "reduce the heat" needs a pan lift on an electric coil.
- Dark metal tins bake hotter and darker than light metal; glass and ceramic lag then hold, so a glass dish wants ~10 °C less and a few minutes more.
- Convection is wrong for custards, soufflés and delicate cakes (`conversion.md`).
- A cast-iron pan carries heat into the oven with it; a thin sheet does not. A recipe built on a preheated pan cannot be transferred to a cold tray without losing the crust.

**Write after any device rewrite**: the rewritten version into the recipe's `## Variations`, naming the device and the mapping used, marked `untested` until cooked. If the session revealed something durable about the kitchen — a machine's real capacity, an air-fryer basket that only fits two portions, a slow cooker that runs hot — one line into `## Kitchen` of `~/Clawic/data/recipe/memory.md`. A device the user does not have or refuses to use goes into `restrictions.no_equipment` in `config.yaml`, because it is a declaration (`memory-template.md`).
