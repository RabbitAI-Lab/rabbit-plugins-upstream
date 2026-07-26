# Workflow playbook

## Contents

1. Intake and capability mapping
2. Source ledger
3. Element planning and redraw
4. Content materials and optional layout reference
5. Story, copy, paper, and layout
6. Multi-pass review
7. Journal and collection management
8. Archive, recall, and return
9. Degraded modes

## 1. Intake and capability mapping

Collect only what changes the result:

| Input | Rule |
| --- | --- |
| Key frame or images | Required for visual execution; otherwise produce an implementation template |
| Source link | Preserve HTTP(S) links; mark unavailable rather than inventing one |
| Element count | User-controlled integer 1–5; default 3 only when omitted |
| Journal type | `portrait`, `pet`, `travel`, `game`, `life`, `fashion`, or `food` |
| Intention | A short thematic spine such as “诗与远方” |
| Factual notes | Optional verified places, dates, prices, steps, names, or feelings |
| Composition materials | 1–12 user-approved images or reusable elements |
| Layout reference | Optional; structural inspiration only, never an implicit content asset |
| Collection action | Optional search, filter, quick edit, reopen, single delete, or bulk delete |
| Output | Editable canvas, image, document, web page, JSON plan, or agent handoff |

Map the current environment to seven capability roles: inspect, redraw, compose, persist, retrieve, manage collections, and present source links. Prefer tools already available to the agent. Do not require a particular vendor or API.

Choose an execution mode:

- **Full execution:** all six roles are available.
- **Creative execution:** inspect, redraw, and compose are available; also output a portable archive manifest.
- **Planning mode:** visual or layout tools are missing; output exact prompts, element plan, story plan, and layout specification.
- **Recall-only mode:** archive data already exists; rank it and surface source links.
- **Management-only mode:** saved records already exist; search or mutate them by stable ID without invoking visual generation.

## 2. Source ledger

Create the source record first. Assign stable IDs before generating derived items.

For each transformation, keep:

- parent source ID;
- original source URL;
- operation (`inspect`, `redraw`, `crop`, `reference-analyze`, `compose`, `edit`, `delete`, `archive`, or `recall`);
- prompt or decision summary;
- tool/model when known;
- warnings and missing facts.

Never replace the source link with the generated image URL. The first supports “return to original”; the second only locates a derivative.

## 3. Element planning and redraw

### Select subjects

Rank visible candidates by:

1. relevance to intention;
2. recognizable silhouette;
3. visual clarity;
4. difference from already selected subjects;
5. contribution to hero, support, transition, detail, or ending.

Select exactly the requested count. Do not pad the set with platform UI, subtitles, watermarks, generic background, or duplicate views of the same subject.

### Redraw

Use one visual generation/editing call per subject when possible. This preserves independent assets and makes later layout editing reliable.

Keep:

- identity-defining contour and colors;
- complete subject rather than arbitrary circular crops;
- coherent style across the set;
- transparent background when supported, otherwise a removable flat background.

Reject outputs that introduce extra subjects, readable fake text, platform logos, frames, mockups, or unrelated scenery. If only cropping is possible, record `generationMode: crop`.

## 4. Content materials and optional layout reference

### Approve content materials

For automatic composition, let the user choose 1–12 content materials from the current task, canvas, or reusable library. Record stable IDs and provenance before layout. Use only approved materials and do not silently import visually similar items.

### Isolate the reference

Store an optional reference journal under `layoutReference`, never inside `elements` or `contentMaterials`. Analyze:

- composition model and reading path;
- hero placement and relative scale;
- image and text zones;
- whitespace strategy;
- overlap, tape, line, or rhythm relationships;
- abstract paper and palette relationships only when explicitly allowed.

Do not extract or copy the reference's photographs, people, food, objects, landmarks, brands, readable text, captions, dates, prices, or factual claims. Do not recreate exact coordinates. Convert the analysis into constraints for the user's approved materials.

Record both:

- `focus`: what the user wants to learn from the reference;
- `restrictions`: what must not transfer.

If the reference is unavailable to the visual tool, continue with the chosen style profile and disclose that no reference analysis was executed.

## 5. Story, copy, paper, and layout

### Story pass

Before coordinates, assign:

- `hero`: the page's first visual answer;
- `support`: evidence or context;
- `transition`: movement between moments;
- `detail`: texture and intimacy;
- `ending`: a quiet return, decision, or next step.

With fewer elements, combine roles. With five elements, use all roles only when the content supports them. Define a top-to-bottom, diagonal, S-shaped, timeline, or grid reading path according to the journal type. When a layout reference exists, adapt its abstract reading logic to the current story rather than cloning positions.

### Copy pass

For rich life records, aim for 6–10 blocks:

- 30–70 Chinese characters for the opening;
- 18–55 near each important image;
- 55–130 for one reflective paragraph;
- 20–60 for the closing;
- one or two short marginal notes.

Use fewer blocks for portrait pages and more structured labels for guides. Copy may interpret visible mood and user-provided intention, but must not fabricate personal experience. Use explicit uncertainty such as “画面让人想到” when the meaning is inferred.

### Paper pass

Describe paper independently from the images:

- material and texture;
- palette;
- edge decoration;
- reserved blank areas;
- forbidden motifs;
- relation to the intention.

The center should support content rather than compete with it. When “诗与远方” involves mountains, sky, roads, or distance, prefer mist blue, mountain green, warm dawn white, fine route lines, and restrained horizon texture—not food-table remnants.

### Layout pass

Use a mobile-first 3:4 portrait canvas unless the user requests another format. Establish:

- one large hero;
- two medium supports when assets allow;
- smaller details;
- at least 20% breathing room for a life record;
- text attached to the images it explains;
- safe title and footer zones;
- purposeful overlap without hiding subjects.

Never place all items at nearly equal size or distribute them evenly into four corners. Never replace an approved content material with an object seen only in the reference.

## 6. Multi-pass review

Use separate calls or roles when available:

1. **Visual analyst:** candidate subjects and factual observations.
2. **Story director:** roles, sequence, art direction, and copy responsibilities.
3. **Element artist:** independent redraws.
4. **Paper artist:** theme-specific background.
5. **Layout composer:** editable coordinates and render.
6. **Visual critic:** direct inspection of the complete render.
7. **Refiner:** focused correction of failed dimensions.

Score each dimension from 1–10:

- story coherence;
- richness and relevance of copy;
- visual hierarchy;
- paper-theme fit;
- legibility and whitespace;
- element fidelity;
- factual integrity;
- provenance completeness.
- reference safety and content/reference separation.

Revise any dimension below 7. Prefer one focused revision and at most two critique cycles unless the user requests deeper exploration. Preserve the latest valid result if a later call fails.

## 7. Journal and collection management

Keep the rendered preview and editable journal record together. Support:

1. browse with faithful thumbnails;
2. full-text search across title, subtitle, place, date, tags, artistic copy, story nodes, and element descriptions;
3. type filters plus clear “all” and “unclassified” states;
4. sorting by recent/oldest update, title, or content count;
5. quick edit of title, subtitle, place, date, tags, and journal type;
6. reopen for full image, text, layout, and source-link editing;
7. explicit single and bulk deletion.

For deletion:

- resolve stable IDs, not visible indexes;
- preview or state the number of selected records;
- require confirmation immediately before mutation;
- remove journal records and stale archive links;
- remove archived JSON, snapshots, and backgrounds only when no surviving journal references them;
- keep unrelated source frames and derived elements unless explicitly selected;
- record deleted IDs and failures;
- use tombstones or equivalent suppression when automatic backfill could recreate intentionally deleted records.

Apply the same trust model to library and memory collections: text edits should refresh searchable content, and batch deletion should affect only explicit selections.

## 8. Archive, recall, and return

Archive a portable manifest beside the rendered result. Include the source record, elements, prompts, story, layout, warnings, and source links.

Build searchable text from:

- user intention and verified notes;
- visible subjects, colors, atmosphere, and actions;
- story and captions;
- journal type and style;
- source title or domain when known.

For recall, accept natural language such as “雨后骑车去山里的那一页”. Rank by semantic relevance, explain the match, and do not treat similarity as proof.

The final result should show:

1. remembered item and preview;
2. why it matched;
3. related journal or elements;
4. unique original source links;
5. a clear return action.

## 9. Degraded modes

| Missing role | Deliver instead |
| --- | --- |
| Visual inspection | Ask for descriptions or provide an analysis checklist |
| Image generation/editing | Provide one redraw prompt per planned element |
| Layout renderer | Provide coordinates, z-order, typography, and responsive rules |
| Durable storage | Return a portable manifest and recommended folder structure |
| Semantic engine | Use weighted keyword/fuzzy matching and disclose the fallback |
| Collection manager | Return stable-ID edit/delete commands or a dry-run mutation plan; do not claim persistence |
| Link navigation | Print validated source links without opening them |

Always distinguish a completed artifact from a handoff specification.
