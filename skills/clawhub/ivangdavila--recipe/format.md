# Format — The Recipe File Itself

The file has one job: someone cooks from it with wet hands on a phone and gets the same dish twice. Every rule below serves that.

The shape lives in `memory-template.md` under `recipes/`; this file is the grammar of what goes inside it.

## Frontmatter Fields

| Field | Type | Required | Rule |
|---|---|---|---|
| `title` | text | yes | The dish as a person would say it. The filename is this, kebab-cased |
| `servings` | number | yes | The base for every scale and every cost (SKILL.md Rule 6) |
| `serving_size` | text | when servings alone is vague | `~350 g`, `2 pieces`, `250 ml` — this is what makes `servings` verifiable |
| `yield` | text | for baked and preserved goods | `12 muffins`, `1 × 900 g loaf`, `4 × 500 ml jars` — use instead of `servings` when the output is countable |
| `prep_min` / `cook_min` | number | yes | Active and unattended, separately. One `total` number hides whether a 3-hour recipe is 20 minutes of work or 180 |
| `tags` | list | yes | From the vocabulary in `index.md`; course, cuisine, effort, season, diet |
| `source` | text | yes | URL plus capture date, or book plus edition and page, or person plus year |
| `rating` | 1-5 | after the first cook | Latest, not an average |
| `made` / `last_made` | number / date | after the first cook | Mirrors `index.md`; the detail lives in `made/<year>.md` |
| `allergens` | list | when present | Written from the ingredient list, not inferred from the cuisine: dairy, egg, gluten, nuts, peanut, soy, shellfish, fish, sesame |
| `equipment` | list | when a specific tool is mandatory | Only what the recipe fails without: `stand mixer`, `pressure cooker`, `23 cm springform`, `probe thermometer` |

## The Ingredient Line

`<quantity> <unit> <ingredient>, <preparation>` — with weight leading when `weight_over_volume` is true.

- `700 g chicken thigh, boneless, in 4 cm pieces`
- `120 g plain flour (1 cup, spoon-and-level)`
- `12 g Diamond Crystal kosher salt (1 tbsp)`
- `150 ml double cream *(coconut cream works; untested)*`

Rules:

- **Preparation goes after the comma, and its position changes the quantity.** `100 g walnuts, chopped` and `100 g chopped walnuts` are the same mass; `1 cup walnuts, chopped` and `1 cup chopped walnuts` are not. Weight makes this ambiguity disappear, which is the main reason for Rule 3.
- **Group by component** when the method uses them at different times: `Marinade`, `Sauce`, `To finish`. A flat list of 22 ingredients for a three-component dish guarantees something goes in at the wrong moment.
- **Order within a group follows the method**, first used first.
- **Optional is marked at the start of the line**, not buried: `*optional* — 1 tbsp toasted sesame oil`.
- **Divided ingredients say so and say how**: `12 g salt, divided (8 g in the dough, 4 g on top)`. "Divided" alone is a bug report waiting to happen.
- **Brand matters exactly three times**: salt (`Measures That Change The Dish`), chocolate percentage, and anything where a specific product behaves differently (Dutched vs natural cocoa, instant vs active-dry yeast). Name it there and nowhere else.
- **A substitution note is inline and marked untested until the make log clears it** (SKILL.md Rule 8).

## The Method Step

One action per numbered step, each ending in a cue.

- Bad: `Cook the onions for 8 minutes.`
- Good: `Cook the onions in the oil over medium heat until translucent and just starting to colour at the edges, 8-10 min.`
- The pattern is **action → sensory cue → time as a range**. Time is the estimate; the cue is the instruction. Every step where they conflict is resolved by the cue.
- Temperatures inside steps repeat the oven type: `200 °C fan`. The reader is not going to scroll up.
- A step that says "meanwhile" gets its own number and names what it runs alongside.
- Hard stops get their own line: `Do not stir from this point — it will crystallize.`
- Long unattended periods are stated as a range with what happens at each end: `Rise 8-12 h at 20 °C; at 8 h the dough is domed, at 12 h it is flat and sour.`
- Steps end at the plate, not at the pan: plating, resting time, and how to hold it warm are steps.

## The Standard Sections

| Heading | Contains | Rule |
|---|---|---|
| Headnote (no heading, first lines) | One or two lines, only if they change what you do | Delete rather than pad. "A weeknight favourite" is noise |
| `## Ingredients` | The version you cook, in the user's units | This is the only section that gets edited by a promotion |
| `## Method` | Numbered steps with cues | — |
| `## Original` | The source's own numbers and phrasing, unconverted | **Never edited after capture** (SKILL.md Rule 2), including for a family original's odd measures |
| `## Variations` | Dated changes, scales, substitutions, each with a verdict or `untested` | Promoted into `## Ingredients` after two good cooks (`testing.md`) |
| `## Notes` | Make-ahead, storage, freezing, what it goes with, vetting findings | Storage gets a time and a temperature, never "keeps well" |

Omit any section with nothing in it. An empty `## Variations` on a new recipe is scaffolding, and scaffolding is what makes a collection feel dead.

## Storage and Make-Ahead Lines

Write them as `<state> · <container> · <temperature> · <duration> · <how to bring it back>`:

`Sauce only, no cream · airtight · fridge 4 °C · 3 days · reheat to a simmer, then add cream off the heat`

Freezer lines say what to freeze *before*: most dairy-finished sauces freeze badly after the cream goes in and perfectly before it. That sentence is worth more than the recipe's photograph.

## Naming Files

- `<dish>.md`, kebab-cased, in the user's own words: `chicken-tikka-masala.md`, `grandma-rosa-sunday-sauce.md`.
- Never the date, never the source, never a version number. A second version of a dish is a `## Variations` entry, or — if it is genuinely a different dish — its own name (`lentil-soup.md` and `red-lentil-dal.md`, not `lentil-soup-2.md`).
- The photograph or scan of an original sits beside the file with the same stem (`preservation.md`).

**Write whenever the file changes shape or content**: the recipe at `~/Clawic/data/recipe/recipes/<kebab-title>.md`, and every index column it feeds, updated in its row in `~/Clawic/data/recipe/index.md` in the same turn. Three of those columns are **derived, not mirrored** — there is no `course`, `cuisine` or `total` field in the frontmatter above: `Course` and `Cuisine` are the course and cuisine tags lifted out of `tags`, and `Total min` is `prep_min + cook_min`. `Title`, `Servings` and `Tags` are mirrored as they stand. A frontmatter field and its index cell that disagree make the search lie (`memory-template.md`).
