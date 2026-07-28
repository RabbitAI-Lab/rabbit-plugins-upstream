# Working File Templates — Recipes

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md`, the collection, and everything they index are what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — Configuration table keys and preference areas alike | `~/Clawic/data/recipe/config.yaml` | Key by key, read-modify-write |
| Kitchen facts, household, sources, prices, collection state, due dates, box index | `~/Clawic/data/recipe/memory.md` | Rewritten in place; stays small |
| **A recipe** | `~/Clawic/data/recipe/recipes/<kebab-title>.md` | Its own file from the first one; never a section of anything |
| The searchable table of the collection | `~/Clawic/data/recipe/index.md` | One row per recipe; splits by `index_grouping` past ~150 rows |
| Dishes actually cooked, with rating and what changed | `~/Clawic/data/recipe/made/<year>.md` | Append-only, cut by year |
| Weekly and event plans, and the list generated from them | `~/Clawic/data/recipe/plans/<year>.md` | Append-only, one section per week or event, cut by year |
| Ingredient unit prices used for costing | `## Prices` in `memory.md`; `~/Clawic/data/recipe/prices.md` once it outgrows the section | One row per ingredient, price with currency and date |
| Trusted and untrusted recipe sources | `## Sources` in `memory.md`; `~/Clawic/data/recipe/sources.md` once it outgrows the section | One row per site, book, or person |
| Allergies, intolerances, diet-relevant conditions | `~/Clawic/data/health/profile.md` (**shared**) | One line per fact, dated |
| People you cook for and their dietary notes | `~/Clawic/data/contacts/contacts.md` (**shared**) | One row per person, note in `Context` |
| A cookbook, supper club, or catering job run as a project — its one-line status only | `~/Clawic/data/projects/<project>.md` (**shared**) | One file per project; the draft and the menus stay in `artifacts/` and are named from there |
| Things you produced that get re-read — a dinner menu with its run-sheet, an oven-calibration note, a family cookbook draft, a print-card layout, a master formula worksheet | `~/Clawic/data/recipe/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| **Anything durable this table does not name** | `~/Clawic/data/recipe/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

Deciding where something unnamed goes, in this order: (1) would another skill want to read it — a person, a health fact, a project, a booking? Then it belongs in the shared box, not here. (2) Is it a text read whole when its subject comes up — a menu, a procedure, a decision with its reasoning, a layout? Then `artifacts/`, its own file from the first one. (3) Is it one more row of something that accumulates? Then a section of `memory.md` until the split threshold.

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A recipe was captured, corrected, or merged with a duplicate | `recipes/<kebab-title>.md` **and** its row in `index.md` |
| A recipe was retired or found unmakeable | Move its row to `## Retired` in `index.md` with the reason; keep or delete the file as the user says |
| A dish was cooked | A row in `made/<year>.md`; bump `Made` and `Rating` in `index.md` |
| A change was cooked twice and worked both times | Promote it into the recipe's `## Ingredients`/`## Method`, move the old line to `## Variations` (`testing.md`) |
| A scaled or substituted version was produced but not yet cooked | `## Variations` in the recipe file, marked `untested` |
| A week or an event was planned | A section in `plans/<year>.md` |
| An ingredient price was read off a receipt, a shelf, or an order | `## Prices` |
| A kitchen fact changed a number — oven offset, tin sizes, hob type, altitude, salt brand, mixer capacity | `## Kitchen` |
| A source proved reliable, or wasted a cook | `## Sources` |
| The user stated an allergy, intolerance, or a condition that constrains food | `~/Clawic/data/health/profile.md` (**shared**) |
| Someone was cooked for, or their restriction was learned | Their row in `~/Clawic/data/contacts/contacts.md` (**shared**) |
| A menu with timings, a calibration note, a cookbook draft, or a print layout was produced | `artifacts/` |
| A cookbook, supper club or catering job moved forward, or was finished or abandoned | Its `status:` line in `~/Clawic/data/projects/<project>.md` (**shared**) |
| A review, price refresh, backup or seasonal pass was scheduled or run | `## Due` |
| The user declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Recipes, plans, make logs and artifacts are born as their own files. Everything else begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/recipe/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite. `## Prices` in `memory.md` becomes `## Prices` in `prices.md`; `## Sources` becomes `## Sources` in `sources.md`.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

`index.md` has its own cut, because it is a box from day one: past ~150 rows it splits along `index_grouping` into `index-<group>.md` (`index-mains.md`, `index-desserts.md`, …), each keeping the same columns, and `index.md` becomes the list of those files with their counts. Recipe files never move when this happens — `recipes/` stays flat, always.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep. A pasted recipe-app export, sync config, or shopping-service order carries tokens and card data: strip each value **before** writing and leave its pointer in place, in this shape: `<kind>:<locator>`.

`env:PAPRIKA_TOKEN` · `keychain:nyt-cooking` · `1password:Personal/Recipes` · `bitwarden:Home/Grocery` · `file:~/.config/recipe-sync/credentials`

In a text, the pointer goes where the value was: `api_key: <env:PAPRIKA_TOKEN>`. Say in one line that you did it.

In this domain — **not secrets, keep them**: recipe text, ingredient names and quantities, source URLs, book titles, editions and page numbers, the name of the relative a recipe came from, shop names, prices, tags, ratings, allergen and diet facts the user asked you to remember, appliance models.

**Secrets, strip them**: recipe-app API keys and sync tokens, subscription logins and passwords, delivery-service accounts, card numbers and the last four on a receipt image, home address on a delivery confirmation, anything in an `.env` or credentials file pasted in with an export.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [recipes/](#recipes) · [index.md](#indexmd) · [made/](#made) · [plans/](#plans) · [artifacts/](#artifacts) · [shared health box](#shared-health-box) · [shared contacts box](#shared-contacts-box) · [shared projects box](#shared-projects-box) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/recipe/` if it does not exist.

```yaml
units: metric
weight_over_volume: true
temperature_scale: celsius
oven_type: fan
altitude_m: 0
default_servings: 4
diet: [vegetarian]
spice_level: hot
currency: EUR
index_grouping: course
pantry_staples: [salt, pepper, olive oil, water, plain flour, sugar, soy sauce]

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
conventions:
  tags: [course, cuisine, effort, season]
  keep_headnote: technique-only
locale:
  ingredient_names: en-GB      # aubergine, coriander, rocket
  hemisphere: north
restrictions:
  no_equipment: [deep fryer, sous vide]
  never_suggest: [offal]
cadence:
  never_made_review: quarter
  price_refresh: quarter
  backup: month
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# Recipe Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- The collection (84 recipes) → `index.md`; read before any search, suggestion, or save
- Recipes cooked (2026) → `made/2026.md`; read before rating, promoting a variation, or asking what to cook again
- Weekly plans and their lists (2026) → `plans/2026.md`; read before planning a week or repeating a menu
- Ingredient prices (22) → `prices.md`; read before any cost-per-serving answer
- Christmas Eve menu and run-sheet → `artifacts/menu-christmas-eve.md`; read when planning a large meal with timings
- Oven calibration → `artifacts/oven-calibration.md`; read before trusting any baking temperature

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Review never-made recipes, retire or schedule | quarter | 2026-05-02 | 2026-08-02 |
| Refresh ingredient prices from a receipt | quarter | 2026-06-14 | 2026-09-14 |
| Export the collection as a backup | month | 2026-07-01 | 2026-08-01 |
| Seasonal shortlist refresh | season | 2026-06-21 | 2026-09-21 |

## Kitchen
Oven: fan, runs ~15 °C hot at 180 (measured with a probe 2026-03-11) — set 165 for anything custard-like.
Tins: 20 cm and 23 cm round, 900 g loaf, one half-sheet (33×45 cm), 26 cm skillet.
Hob: induction, 4 zones; largest pot 5 L — the hard ceiling on any batch scale.
Salt in use: Diamond Crystal kosher (~2.8 g/tsp). Recipes written in table salt must be re-weighed.
No deep fryer, no sous vide. Stand mixer bowl 4.8 L — doubles of bread dough do not fit.
Altitude 12 m — no altitude corrections needed.

## Household
Two adults, one child (6). Child eats separately twice a week; portions ~0.5 adult.
Restrictions live in `~/Clawic/data/health/profile.md` — read it, do not copy it here.
Sunday is the cook-ahead day; weeknight ceiling is ~35 min active.

## Collection
84 recipes, 31 never made. Strong on Italian and Indian mains; thin on fish, breakfast, and anything under 20 minutes.
Tag vocabulary in use: course, cuisine, effort (weeknight/project), season, diet.

## Sources
| Source | Type | Verdict | Notes |
|---|---|---|---|
| Serious Eats | site | reliable | Gram weights given, ratios hold when scaled |
| Grandma Rosa | person | verbatim only | Measures by eye; originals photographed in `recipes/` |
| <recipe aggregator> | site | untrusted | Two failures: leavener out of band, no yield stated |

## Prices
| Ingredient | Unit price | Package | Shop | As of |
|---|---|---|---|---|
| plain flour | 1.10 EUR/kg | 1 kg | local supermarket | 2026-07-12 |
| chicken thighs, bone-in | 6.40 EUR/kg | 1.2 kg tray | butcher | 2026-07-12 |

## How They Work
Wants the grams and the file, not the essay. Cooks from the phone — steps must be short and self-contained.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist. Individual recipe files do **not** get their own lines; `index.md` is their index and gets one line for all of them.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Cadences come from `cadence` in `config.yaml` when the user has declared them.
- **`## Kitchen`**: only facts that changed a number. The oven offset, the largest pot, the mixer bowl and the tin sizes are the four that most often cap a scale — record them with how they were measured.
- **`## Household`**: who eats and how much, plus the weeknight time ceiling. Never copy allergies here; they live in the shared health box and copying them creates two versions of a safety fact.
- **`## Sources`**: `Verdict` is `reliable`, `untrusted`, or `verbatim only`. A source earns `untrusted` after two failures traced to the recipe rather than the cook, and the reason is recorded — otherwise the same site gets re-tried every year.
- **`## Prices`**: unit price with currency in the value (`1.10 EUR/kg`), plus the date it was read. A price older than ~6 months is an estimate and any cost-per-serving built on it says so.
- These headings are exactly the ones `prices.md` and `sources.md` get when their sections outgrow this file, so each split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still learning their kitchen and their taste |
| `complete` | Know the equipment, the household, and what they actually cook |

## recipes/

One file per recipe at `~/Clawic/data/recipe/recipes/<kebab-title>.md`, from the first one, whatever its size — a recipe is read whole and only when it is being cooked. Every recipe gets its `index.md` row in the same turn. Full field rules in `format.md`; this is the shape.

```markdown
---
title: Chicken Tikka Masala
servings: 4
serving_size: ~350 g
prep_min: 25
cook_min: 40
tags: [main, indian, weeknight-project, dairy]
source: https://example.com/tikka — captured 2026-04-02
rating: 4
made: 3
last_made: 2026-07-19
---

Headnote, one or two lines, only if it changes what you do.

## Ingredients
Marinade
- 700 g chicken thigh, boneless, in 4 cm pieces
- 200 g full-fat yoghurt
- 12 g Diamond Crystal kosher salt (1 tbsp) — halve by weight for table salt

Sauce
- 400 g tinned tomato, crushed
- 150 ml double cream *(coconut cream works; untested)*

## Method
1. …one action per step, with its cue: "until the fat separates and the oil pools at the edge, ~8 min".

## Original
As published, unconverted: "1 cup yogurt, 1 tbsp kosher salt, 1 can (14 oz) tomatoes, 350 °F".
Salt brand not stated by the source; assumed Diamond Crystal.

## Variations
- 2026-06-11 — half the cream, +1 tbsp cashew paste. Cooked twice, better. Promoted.
- Scaled ×2 for 8: 5 L pot is at its ceiling, sauce needed 12 extra minutes to reduce. `untested` at ×3.

## Notes
Freezes well before the cream goes in.
```

- `## Original` is never edited after capture (Rule 2). Everything you change goes in `## Ingredients` or `## Variations`.
- `made` and `last_made` in the frontmatter mirror `index.md`; `made/<year>.md` holds the detail. Bump all of them in the same turn.
- A photographed or scanned original lives beside the file as `recipes/<kebab-title>.<ext>` and is linked from `## Original` (`preservation.md`).
- Filename is the dish, kebab-cased, never the date and never the source.

## index.md

The collection is the index; the folder is only storage. One row per recipe, always.

```markdown
# Recipe Index — 84 recipes, 31 never made

| Title | File | Course | Cuisine | Total min | Servings | Tags | Made | Rating |
|---|---|---|---|---|---|---|---|---|
| Chicken Tikka Masala | `recipes/chicken-tikka-masala.md` | main | indian | 65 | 4 | weeknight-project, dairy | 3 | 4 |
| Lentil Soup | `recipes/lentil-soup.md` | main | levantine | 35 | 6 | vegan, freezer | 7 | 5 |

## Retired
| Title | Retired | Why |
|---|---|---|
| Microwave Mug Cake | 2026-05-02 | Made twice, rubbery both times; ratio is out of band |
```

- **`Course`, `Cuisine` and `Total min` are derived, not copied**: the first two are the course and cuisine tags pulled out of `tags`, the third is `prep_min + cook_min`. The frontmatter has no field of any of those three names (`format.md`), and inventing one splits the schema.
- **Search reads this file, never the folder.** Answering "what can I make with chickpeas" by listing the directory is how a 200-recipe collection becomes unusable.
- `Made` is the count of times cooked; `Rating` is the latest, 1-5. Sort by `Made` when suggesting — it predicts what will be cooked again better than the rating does.
- **Duplicate check before every save**: same title, or same dish from a different source. If it is the same dish, merge into the existing file — add the new source under `## Original` and the differing quantities under `## Variations` — and do not create a second row.
- **Retirement**: move the row to `## Retired` with a date and a one-line reason. The reason is what stops the same recipe being re-saved from the same site next year.
- Scale cut: past ~150 rows, split along `index_grouping` into `index-<group>.md` with identical columns; `index.md` keeps the header line, the `## Retired` table, and a pointer to each group file with its count.

## made/

Append-only, one file per year. This is the record that turns a collection into a repertoire.

```markdown
# Cooked — 2026

| Date | Recipe | For | Scale | Rating | What changed | Fix next time |
|---|---|---|---|---|---|---|
| 2026-07-19 | chicken-tikka-masala | family (4) | ×1 | 4 | halved the cream, +cashew paste | reduce 5 min longer |
| 2026-07-21 | lentil-soup | Marco, Aya (see contacts) | ×1.5 | 5 | — | double it, it froze well |
```

- One row per cook, including the failures — a log of successes cannot answer "why did we stop making this".
- `For` names people by name only; the person and their dietary note live in `~/Clawic/data/contacts/contacts.md`.
- `What changed` plus `Fix next time` is the pair that makes the row worth writing. A row that says "good" is a diary entry.
- A change that appears in two rows with the same verdict gets promoted into the recipe file (`testing.md`).

## plans/

```markdown
# Plans — 2026

## Week of 2026-07-20
| Day | Meal | Recipe | Scale | Notes |
|---|---|---|---|---|
| Mon | dinner | lentil-soup | ×1.5 | doubles as Tue lunch |
| Tue | dinner | — | — | leftovers |

Shopping list generated 2026-07-19, aggregated across 4 recipes; `pantry_staples` excluded.
Carried over unused: 200 g yoghurt, half a bunch of coriander → Thu recipe chosen to use them.

## 2026-12-24 — Christmas Eve, 9 people
Menu and timings in `artifacts/menu-christmas-eve.md`.
```

- The value of the file is the carry-over line: what was bought and not used is what should pick next week's recipes.
- An event with timings is a plan row here plus an artifact; the run-sheet does not belong in a table.

## artifacts/

One file per thing, at `~/Clawic/data/recipe/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **a menu with its run-sheet**, **an oven or scale calibration note**, **a family cookbook draft**, **a print-card layout**, **a master formula worksheet** (a bread or cake ratio the user derived and reuses). Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Menu — Christmas Eve, 9 people
*Read when planning a large meal with timings. Written 2026-07-26.*

Menu, with each dish's saved recipe and its scale factor.
Run-sheet backwards from service: T−48h, T−24h, T−4h, T−45min, plate.
Oven contention: only one shelf at 200 °C — the gratin and the roast cannot overlap.
```

```markdown
# Oven calibration
*Read before trusting any baking temperature. Measured 2026-03-11 with a probe thermometer.*

Setting 180 fan → 195 measured at the centre after 20 min preheat. Offset −15 °C.
Back-left runs hottest; rotate trays at the halfway mark.
```

If the user tracks a cookbook or a catering job as a project, its one-line status also belongs in the shared projects box below, with the full draft staying here and referenced by name.

## Shared health box

Lives at `~/Clawic/data/health/profile.md` and is shared with every food, fitness and travel skill — the user may have none of them installed, so the format travels with this skill.

```markdown
# Health Profile

## Allergies
- shellfish — anaphylaxis, carries an adrenaline pen (stated 2026-04-02)
- birch pollen / oral allergy syndrome — raw apple and stone fruit; cooked is fine (stated 2026-05-17)

## Intolerances
- lactose — hard cheese and yoghurt tolerated, milk and cream are not (stated 2026-05-17)

## Conditions
- coeliac disease, diagnosed 2019 — gluten is a hard exclusion, cross-contact matters (stated 2026-04-02)
```

- **Read it before proposing, capturing, adapting, or scaling anything the user will eat.** This is the one shared box this skill reads on the way in, not just on the way out.
- **Identity is the fact plus its date.** Read the file before adding. If the same allergy or condition is already there, update that line in place — never append a second one, and never restate it in `memory.md`.
- **Allergy ≠ intolerance ≠ chosen diet.** An allergy or a condition goes here; a chosen pattern (vegan, low-sodium, halal) is a declaration and goes in `diet` in `config.yaml`. Filing a preference as an allergy makes every future suggestion needlessly narrow; filing an allergy as a preference is a safety failure.
- **Severity and the trigger form belong in the line** — "raw only", "cross-contact matters", "carries a pen". Without them, the substitution advice is guesswork.
- **Removal**: only when the user says it is resolved or was wrong. Delete the line and note the date and who said so in `## Household` of `memory.md`. Never delete or edit a line another skill wrote about medication, vaccines, or a metric.
- **Foreign structure wins.** If `profile.md` already exists with other headings, add under the closest existing heading and never rewrite the file's shape. If it does not exist, create it with only the headings you have content for.
- Never write a metric series here (weight, glucose): those get their own `health/<metric>.md` past ~15 entries, and they are not this skill's to write.

## Shared contacts box

Lives at `~/Clawic/data/contacts/contacts.md`, shared with every skill that deals with people.

```markdown
# Contacts

| Name | Key | Role | Preferred channel | Context | Last contact | File |
|---|---|---|---|---|---|---|
| Marco Ruiz | marco.ruiz@example.com | friend | whatsapp | no pork; loves anything braised | 2026-07-21 | — |
| Aya Tanaka | aya-tanaka | neighbour | in person | vegetarian, no fish sauce | 2026-07-21 | — |
```

- **Identity is `Key`**: lowercase email if there is one, otherwise a handle, otherwise `<kebab-name>` plus a stable disambiguator. Read the file before adding; if the key is there, update that row in place — never a second row for the same person.
- **This skill writes `Context` and `Last contact` only.** Leave `Role`, `Preferred channel` and `File` as you found them; if they are empty and you do not know, leave them empty rather than guessing.
- **Dietary note in `Context`, in a few words.** A medical allergy of someone in the household also goes in the shared health box; a guest's allergy stays here, because the health box is the user's own profile.
- **Removal** is not this skill's job: a person who stops coming to dinner is not a deleted contact. Update `Context` instead.
- **Foreign columns win.** If `contacts.md` exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- Scale cut: one row per person while there are ≤15. Past that, a `~/Clawic/data/contacts/<name>.md` per person, with `contacts.md` as the index and the `File` column pointing at it. If you arrive and the folder already looks like that, follow it.

## Shared projects box

Lives at `~/Clawic/data/projects/<project>.md`, one file per project, shared with every skill that tracks work in flight. Only three things in this domain are projects: a **cookbook or zine** being written, a **supper club or catering job** with a date and people paying or attending, and a **preservation push** with a deadline (a relative's recipes being recorded before a move or a decline). A week's meal plan is not a project — it is a section of `plans/<year>.md`.

```markdown
# Family Cookbook

status: active — 2026-07-26
goal: 40 tested recipes from both grandmothers, printed for Christmas
next: photograph Rosa's remaining cards before September

## Milestones
- 2026-05-02 — 12 recipes captured verbatim, originals scanned
- 2026-07-19 — 9 of them retested and rewritten; drafts in `~/Clawic/data/recipe/artifacts/cookbook-family-draft.md`

## Decisions
- 2026-06-11 — metric first with cups in parentheses; the readers are split across two countries
- 2026-07-04 — print quote 640 EUR for 30 copies (as of 2026-07-04), decided after Christmas
```

- **Identity is the project name, which is the filename** — `family-cookbook.md`, kebab-cased. Read the folder before creating anything: if a file for this project already exists, **update it in place**; a second file for the same project is how two skills end up disagreeing about what was decided.
- **This skill writes `status`, `next`, and the milestones and decisions that came out of cooking work.** Leave every other line as you found it, including lines another skill wrote (a budget, a client, a deadline). Never rewrite the file's shape.
- **The cooking content does not move here.** Recipes stay in `recipes/`, menus and drafts stay in `artifacts/`, and this file names them by path. A project file that grows a recipe inside it has duplicated the collection.
- **A person named here is a pointer only** — the name in a line, their row in `~/Clawic/data/contacts/contacts.md`. Money carries its currency inside the value (`640 EUR`, not `€640`) and an estimate carries the date it was estimated.
- **Closing is not deleting.** A finished or abandoned project gets `status: done — <date>` or `status: cancelled — <date>` at the top and stays: it is the record of what was delivered. Deleting it loses the decisions that the next cookbook will re-litigate.
- **Scale cut**: past ~20 closed projects, move them to `~/Clawic/data/projects/archive/<project>.md` without renaming. Active projects stay flat in `projects/`.
- **Foreign structure wins.** If the folder already uses a single `projects.md` table instead of a file per project, add a row there and follow what exists rather than converting it.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`prices.md` — `## Prices`, plus `## Package Sizes` (the pack the shop actually sells, which is what a shopping list has to round to). This file is why a cost-per-serving answer does not require a shopping trip.

`sources.md` — `## Sources`, plus `## Failures` (date, recipe, what the source got wrong). The failure list is the reason the file exists: a verdict without its evidence gets overturned by the next pretty photograph.
