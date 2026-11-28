---
name: bs-steel-curve-profile-deck
description: Create an approachable company profile with steel-blue panels, curved image frames, and rounded metric cards. Explain your services and operating model in a presentation you can edit in your browser and export to PowerPoint.
---

# Steel Curve Profile Deck

Use this Skill for company profiles, operating plans, team introductions, training, and partner updates that call for steel-blue framing, rounded white panels, arched picture windows, triple-dot and chevron accents, and calm sentence-case titles with few words.


## Approve the Skillry budget

For Skillry execution, check access and permissions with `prepare_skill_execution`. Verify the model and reference support with `list_media_models`. Upload local reference images with image permission. Quote each final specification using `quote_media` or `skillry media --quote-only`. Show the planned steps, their estimated or maximum credits, and the exact combined budget. Wait for the user to confirm that amount in chat.

After confirmation, use the same credential and API base to create one shared run with `start_skill_run`, or `skillry run start --name "Media task" --skill bs-steel-curve-profile-deck --budget-points <confirmed-total> --run-id <uuid>`. API-key clients can instead POST `id`, `name`, `skill_slug`, and `budget_points` to `/api/relay/runs`. Set `SKILLRY_RUN_ID` to that registered UUID when running bundled scripts, or pass `--run-id` on CLI media commands. Record one request ID per step and use it to recover interrupted jobs. Report settled credits from the job or run status, including any settlement at the approved ceiling when usage evidence is unavailable.

## Generation provider (ask first)

Before generating any new images, present these 3 options upfront and confirm the user's choice:

1. **Skillry API Key (Default)**: Use Skillry (`--provider skillry`, default when omitted) with `SKILLRY_API_KEY`, a logged-in `skillry` CLI session, or Skillry MCP tools (`upload_image_reference`, `quote_media`, `start_skill_run`, `generate_media`, `media_status`, `download_media`).
2. **Codex Built-in Image Generation (Recommended in Codex)**: When running inside a Codex client (`CODEX_THREAD_ID`, `CODEX_SESSION_ID`, or native `image_gen` tool detected), use Codex's built-in `image_gen` tool directly with this Skill's exact prompt, aspect ratio, and reference rules instead of an API key.
3. **Custom FAL API Key (`FAL_KEY`)**: Generate directly through FAL using `--provider fal` and the user's own `FAL_KEY`.
## Shared editor contract

This style always uses the bundled framework in `references/framework/`; never build a separate editor or paging engine. The editor UI is identical across styles: black, white and gray, with localized icon tooltips and independently editable objects. Palettes, fonts, artwork and layouts stay specific to this Skill and come from its style kit. Read [runtime](references/runtime.md) for the editor, saving and export behaviour, and [compose guide](references/compose.md) for the plan format.

## Workflow

1. Confirm the user's topic, audience, source facts, communication language, content language and slide count. Write slide copy in English unless the user asks for another language. Keep this style's art direction, layout proportions and content limits below; do not substitute a generic template.
2. Plan a clear narrative with one job per page, using the agreed number of fixed 16:9 pages and this style's word budgets and evidence rules.
3. Read this package's style references (below). Named palettes are choices for slide content; the shared editor stays unchanged.
4. Compose from the style kit so the deck matches the store example: write `plan.json` picking a recipe from `references/style-kit.json` for each page (recipes may repeat), set the new text, pictures, picture descriptions (`alt`), icons, chart labels and data values by node ID, remove nodes a page does not need, then run `python3 scripts/style-kit.py compose --style-kit references/style-kit.json --plan plan.json --output project.json`. Work through the report: fill every `unfilledImages` slot and replace each `leftoverExample` entry that belongs to the example's topic. The [compose guide](references/compose.md) documents every plan field. Refine `project.json` where needed (add, delete, move or restyle nodes, keeping IDs unique), keep the kit's `contentCSS`, and write `editor-config.json` with the bundled schema.
5. Pictures:
   - Before making any picture, ask the user once (with the step 1 questions when possible) and offer exactly three options. Pictures the user supplies come first in every option. If the user cannot be asked or does not answer, use option 1. Tell the user which option you used.
     1. **Reuse this style's original pictures (recommended)**: use only pictures from this Skill's picture library, with no image credits. A slot with no fitting picture keeps its labeled image frame; list those slots for the user.
     2. **Generate as needed**: reuse library pictures where they fit and generate only the remaining slots.
     3. **Regenerate everything**: generate every picture new for this topic.
   - Library: run `node scripts/embed-library-images.mjs --list`; use `any-topic` pictures freely and `topic-specific` ones only when their topic matches the deck, never show one picture on two pages, and set the plan's `images` value (or an image node `src`) to `library:<id>`. After composing, run `node scripts/embed-library-images.mjs project.json` to inline them; if a download fails, treat those slots as unfilled.
   - Generate pictures following `references/image-prompts.md`, at the `aspect` that `style-kit.json` and the compose report list for each slot. Run `node scripts/fal-image.mjs` defaulting to `--provider skillry` (Skillry API Key/CLI), or use Codex built-in `image_gen` when in Codex, or pass `--provider fal` with the user's `FAL_KEY` (submit once, then `status`/`fetch`). Never use another image provider. Library pictures (`--download <id> --out <dir>`) or pictures already made for this deck can be passed as `--reference` to keep the series consistent.
   - With neither FAL nor a built-in tool, options 2 and 3 fall back to option 1.
6. Set `uiLocale` and `conversationLocale` to the user's communication language and `contentLocale`/`contentDirection` from the brief; compose detects Chinese, Japanese and Korean plans. Arabic and Hebrew right-to-left layout is handled by the framework; do not reverse logical arrays.
7. Build and check: `python3 scripts/build-deck.py --project project.json --config editor-config.json --output presentation.html`, then `python3 scripts/check-deck.py presentation.html --expected-slides N --style-kit references/style-kit.json --report deck-check.json`. Resolve every example string the check still reports. If it warns about size, run `python3 scripts/optimize-images.py presentation.html` and check again.
8. Open the file over local HTTP and inspect every page: typography, pictures, hierarchy, crops, bounds, contrast and spacing. Edit text, add/delete/move a block, change a color or Smart layout, edit notes, undo/redo, save and reopen. Presentation mode must disable editing and its glass navigation must hide after five idle seconds.
9. Deliver the single HTML file. It opens in a page view with an Edit button and works offline. Tell the user that edits stay in the browser until they press Save (Cmd/Ctrl+S), which writes them into the file. On request, export PPTX from the built-in menu, run `python3 scripts/check-pptx.py presentation.pptx --project project.json --report pptx-check.json` and inspect it in PowerPoint, Keynote or WPS. Keynote uses the compatible `.pptx`. Print/PDF gives one page per slide.

## Style references

Read the [style kit](references/style-kit.json), [compose guide](references/compose.md), [palettes](references/themes.md), [layout recipes](references/layouts.md), [image prompts](references/image-prompts.md), [icons](references/icon-library.md), [style reference](references/style-reference.md) and [runtime](references/runtime.md).

## Inputs and outputs

- Inputs: audience, purpose or decision, approximate slide count, source facts, and any approved pictures. Ask only for facts that change the result.
- Outputs: one self-contained presentation HTML (page view, editor, presentation mode, speaker notes, pictures inline), plus an exported PPTX and a PDF via print when requested.

## Restraint rules

- Word budget: headline ≤ 7 words (cover ≤ 5), one supporting line ≤ 18 words, ≤ 3 items (label ≤ 3 words + one line ≤ 10 words, or number + 2–4 word caption), ≤ 45 words per slide. Detail goes into the notes.
- No tag clutter: only the small brand mark top-left (white on the steel field of framed pages); no pills, eyebrows (one small label on the cover only), footers or folios.
- At most 3 content blocks per slide, at least 30% empty; siblings share one style; one accent element per slide.
- One corner radius (`--r`) for cards and panels; photos keep the one signature arch corner. Never overlap photos; a card may sit on a photo only on the workflow archetype.

## Constraints

- English slide copy by default unless the user asks otherwise.
- Keep the light, steel-blue identity; do not add dark pages.
- On the 1280x720 page: body text at least 17px, page titles 59–64px, cover title about 120px, big numbers 64–83px.
- Preserve approved figures; mark invented example numbers as illustrative in the speaker notes.
- Use only fictional organizations and original generated people; never imply real customer proof or reuse third-party logos and photographs.

## Style-specific planning and composition

- Theme: keep the authored Steel Curve Profile preset unless the user picks another from `references/themes.md`. Change only `--ink`, `--paper`, `--accent`. Keep the embedded fonts: Manrope for headlines and numbers (`--font-display`), Hanken Grotesk for body (`--font-body`), both inlined as base64 woff2 so the deck stays offline.

- Layouts: compose the agreed number of pages from the ten archetype recipes in `references/style-kit.json`, using `references/layouts.md` for their geometry, and follow its hard rules. Alternate framed (steel panel) and open (white) pages and keep one focal point per page. Keep node IDs unique and text in independently editable leaves.

- Icons: only where they add meaning (brand mark, contact rows); inline 24-unit Lucide-style SVG from `references/icon-library.md`, same size and stroke, always next to a word. No emoji, dingbats, icon fonts, or glyph arrows.

- Pictures: follow Workflow step 5 (user pictures first, then the library question, then generation) and the scene briefs in `references/image-prompts.md`.

## Package boundary

Keep SKILL.md, scripts and references together. Include the shared runtime and required style resources. Examples, manifests, provider records, migration reports, previews and credentials do not belong in the installation ZIP. Use only references inside this Skill.

---

## More from Skillry

This skill is part of the open-source free skills collection from [Skillry](https://skillry.dev).

- Get a Skillry API key for one-click media generation or explore the full catalog at [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
