# Migration — Import, Export, Backup, Print

Every migration is two problems wearing one coat: a **field-mapping** problem and a **duplicate** problem. The mapping is mechanical and finishes; the duplicates are what wreck a collection, because an import is the single largest duplicate event it will ever see.

**Read `~/Clawic/data/recipe/index.md` before importing anything** — the whole existing collection is the thing the incoming file has to be matched against, and the match has to happen before the first file is written, not after (`library.md`). Read `format.md` for the target schema you are mapping into.

The markdown collection is the master copy. Anything exported to an app is a copy, and a round trip through an app loses `## Original`, `## Variations` and the make log every time.

## The Four Directions

| Direction | The real work | Finishes when |
|---|---|---|
| One recipe in, from a link or a file | Extraction, not migration (`capture.md`) | The file and its index row exist |
| A whole export file in | Field mapping, then dedup against the index, then a written report of what merged | Every incoming recipe is either a new file with a row, a merge into an existing file, or a named skip |
| Out to an app | Decide what does not survive the target's schema and where to park it | The app has the recipes and the markdown is still the master |
| Backup | Copying plain text, plus one verified restore | A recipe restored from the backup opens and cooks |
| Anything else — a format nobody names, a scrape, a spreadsheet | Map it to schema.org first (below), then treat it as a whole-export import | Same gate as a whole-export import |

## What An Export File Actually Is

Formats verified 2026-07. Read the first bytes rather than trusting the extension — apps change their container between versions, and a renamed `.zip` is the most common "corrupt export".

| Source | Container and payload | Comes across cleanly | Does not survive |
|---|---|---|---|
| Paprika | `.paprikarecipes` = zip of `.paprikarecipe` entries, each gzipped JSON | Title, servings, times, ingredient block, directions, source URL, rating, categories, notes, photo | Ingredient *structure* — quantities are one text blob per line, not parsed numbers |
| Mela | `.melarecipes` = zip of `.melarecipe` entries, plain JSON, schema.org-shaped keys | The same set, plus `yield` and `nutrition` when present | Per-component grouping; groups arrive as heading lines inside the text |
| Crouton | `.crumb` files, JSON | Ingredients with quantities parsed, steps, tags, images | Its own step-timer and inline-link objects |
| Recipe manager exporting HTML or a print page | One file per recipe, sometimes with embedded JSON-LD in the head | Whatever the JSON-LD holds; otherwise you are parsing prose | Everything not in the visible card |
| MasterCook (`.mxp`, `.mx2`), MealMaster (`.mmf`), RecipeML (XML) | Legacy plain text or XML, fixed field order | Title, yield, ingredient lines, directions, categories | Anything added after ~2005: ratings, photos, tags, source URLs |
| Cooklang (`.cook`) | Plain text; metadata as `>> key: value`, ingredients inline as `@flour{120%g}` | Quantities *and* their position in the step — the one format with parsed structure inside the method | Nothing much; it is closer to this collection than any app format |
| A spreadsheet or Notion/Airtable CSV | One row per recipe, ingredients in one cell | The columns that exist | Step order if the cell used commas; check for a delimiter collision before trusting it |
| A service with no export at all (a web-only recipe box) | Nothing | — | Re-capture the ones actually cooked (`capture.md`) and note the rest as an unmigrated source in `## Collection` of `memory.md`, rather than transcribing 300 recipes nobody has made |

## Map Through schema.org, Never App To App

Map every source into schema.org `Recipe` first, then into the frontmatter once. Direct app-to-app mapping is *n*×*n* rules that each rot separately; through the hub it is *n* + 1. The read side — what a live page gives you and its two traps — is in `capture.md`; this is the write side.

| Frontmatter (`format.md`) | schema.org | Typical app key | Mapping rule |
|---|---|---|---|
| `title` | `name` | `name`, `title` | Strip the site's trailing " - Recipe \| SiteName" |
| `servings` / `yield` | `recipeYield` | `servings`, `yield` | A bare number means servings; a number with a noun ("12 muffins") is `yield`. If it is bare and the method says a tin, treat it as servings and mark it `derived` |
| `prep_min` / `cook_min` | `prepTime` / `cookTime` | `prep_time`, `cook_time` | ISO-8601 durations in, integer minutes out. Never store the total — it is derived (`format.md`) |
| `tags` | `recipeCategory` + `recipeCuisine` + `keywords` | `categories`, `tags` | Fold all three into the controlled vocabulary in `index.md`; do not import a 40-tag folksonomy wholesale (`library.md`) |
| `source` | `url` + `author` + `datePublished` | `source`, `source_url` | Add the capture date of the *import*, marked as such: an import date is not a capture date |
| `rating` | `aggregateRating` | `rating` | The app's own 1-5 only. A site's aggregate rating is strangers' opinions and goes in `## Notes`, not in the field |
| `made` / `last_made` | — | `cook_count`, `date_last_cooked` | Import them if they exist; they are the most valuable field in any export and almost never mapped |
| `## Ingredients` | `recipeIngredient[]` | one string per line | Keep the source's own line text; convert to weight after the import lands (`conversion.md`), not during it |
| `## Method` | `recipeInstructions[]` | `directions`, `instructions` | A single blob gets split into steps by hand; `HowToSection` objects become the component groups |
| `## Original` | — | `notes` | Whatever the source's numbers were, verbatim (SKILL.md Rule 2) |
| Anything with no home | — | — | `## Notes`, labelled with the field name it came from. Dropping it unrecorded is what makes the second migration a rewrite |

Emitting JSON-LD for a recipe you own: same table read right to left, `"@context": "https://schema.org"`, `"@type": "Recipe"`, durations back to ISO-8601 (`PT1H15M`). That is also the format most apps and search engines will import from a plain HTML page.

## Duplicate Handling On Merge

Run the whole import in memory, match every incoming recipe, then write. Writing as you go means the 200th duplicate is matched against a collection you have already polluted.

Match ladder, first hit wins:

1. **Same source URL** (normalised: strip `utm_*`, trailing slash, `www.`) — the same recipe, certainly.
2. **Same normalised title** (lowercase, punctuation and articles stripped) **and yield within ±1 serving** — the same recipe, near-certainly.
3. **Ingredient fingerprint**: the sorted set of ingredient head-nouns, ignoring quantities and preparations. ≥80% overlap on a list of ≥6 ingredients is a match worth surfacing; below that it is two similar dishes.
4. No hit → new recipe, new file, new row.

Then, per match: the existing file wins on every field it already has. The import adds its source under `## Original`, its differing quantities as a dated `## Variations` entry, and nothing else. The one exception is `made`/`last_made`/`rating` — take the higher count and the later date, because the import is usually the app the user actually cooked from.

- **Never delete a file during an import.** A wrong merge that only added lines is recoverable; a deletion is not.
- **Stop and ask exactly once**, at the end, and only about the pile the fingerprint rule surfaced as maybes. Everything else is decided by the ladder.
- **Report in one line**: imported, merged, skipped, and the maybes. `"312 in: 268 new, 31 merged, 9 skipped as exact duplicates, 4 for you to look at."`

## Export Out To An App

- Decide first what the target cannot hold — usually `## Original`, `## Variations`, the make log, and the component grouping. Park `## Original` and the current `## Variations` at the top of the app's notes field so nothing is lost at a glance, and accept the rest is gone.
- Export the cooked version, not the source's version: the app is for cooking from.
- Convert once, on the way out, into the units the app's users expect; the markdown keeps its own (`conversion.md`).
- After the export, the app is downstream. Changes made in the app come back only through a fresh import, with the dedup ladder above — which is why sync is not a thing this collection does.

## Backup

- The whole of `~/Clawic/data/recipe/` is plain text plus photos: a copy of the directory is a complete backup, and it needs no export step and no tool.
- Keep the photos of handwritten originals in the same tree (`preservation.md`) — they are irreplaceable and they are the only large files here.
- **A backup nobody has restored is a hypothesis.** Once, on the first backup: restore one recipe file into a scratch location and read it. That is the whole verification.
- A `git init` in the directory gives dated versions of every recipe for free and makes "what did the original say before I edited it" answerable. Only useful if it is committed on the same cadence as the backup.
- No credential ever enters this tree, so a backup carries nothing sensitive — that is what the Secrets rule buys (`memory-template.md`). A sync-service config file, on the other hand, does: keep it outside the tree.

## Print Cards

- One recipe, one side of one page, or it is not a card. Cut the headnote and `## Notes` first; cut the method never.
- Fixed order: title · yield and times · ingredients grouped as in the file · numbered steps. Two columns for the ingredients only if they still fit on one page at ≥10 pt.
- The two things a printed card must keep and screens usually drop: the oven type on every temperature, and the salt brand.
- 10×15 cm index card: the ingredient list and a compressed method, and only for a recipe already cooked three times — a card is a reminder, not an instruction.
- A recurring layout is not re-derived every time: it is an artifact at `~/Clawic/data/recipe/artifacts/<kebab-name>.md`.

**Write at the end of any migration**: every imported recipe as its own file in `~/Clawic/data/recipe/recipes/` with its row in `~/Clawic/data/recipe/index.md`, in the same turn as the import (SKILL.md Rule 1). The import itself — date, source app, counts, and the merge decisions you made — goes as one line into `## Collection` of `~/Clawic/data/recipe/memory.md`, because the next import needs to know what the last one did. A print-card layout or an export-mapping worksheet you will reuse goes to `~/Clawic/data/recipe/artifacts/<kebab-name>.md` with its `## Boxes` line, and a backup cadence gets its row in `## Due` (`memory-template.md`).
