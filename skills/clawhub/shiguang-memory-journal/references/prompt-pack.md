# Tool-agnostic prompt pack

Replace bracketed variables and adapt output format to the current agent's tools. Keep provenance fields even when a tool cannot emit structured JSON directly.

## 1. Visual analyst

```text
Inspect [KEY_FRAME] as evidence, not as a source of invented facts.
User intention: [INTENTION]
Requested element count: [COUNT, integer 1–5]

List distinct visible subjects, excluding platform UI, subtitles, watermarks, avatars,
buttons, playback icons, and meaningless background. Select exactly [COUNT] subjects.
Optimize for intention relevance, recognizable silhouette, visual clarity, variety,
and complementary story roles. For each selected subject return:
id, visible evidence, crop/location hint, key shape and colors, proposed story role,
redraw risks, and original source link [SOURCE_URL or unavailable].
Mark every inference explicitly.
```

## 2. Single-element redraw

Run once per selected subject:

```text
Use [KEY_FRAME or SUBJECT_REFERENCE] only as visual evidence.
Redraw exactly one subject: [SUBJECT_DESCRIPTION].
Style: [hand-drawn cartoon / comic highlight / vintage collage / chosen style].
Preserve its identity-defining contour, proportions, colors, and important details.
Keep the complete subject centered as an independent editable keepsake.
Remove unrelated scenery, platform UI, subtitles, watermarks, and other subjects.
Use transparent background if supported; otherwise use a uniform removable background.
Do not create a photo crop, circular frame, mockup, readable fake text, logo, shadow scene,
or additional subject. Do not claim unseen details.
```

## 3. Layout-reference analyst

Run only when the user selected a separate reference:

```text
Inspect [LAYOUT_REFERENCE] only as structural design evidence.
User-approved content materials: [CONTENT_MATERIAL_IDS]
User focus: [REFERENCE_FOCUS]
Explicit restrictions: [REFERENCE_RESTRICTIONS]
Mode: [LAYOUT_ONLY or ALLOW_ABSTRACT_DECORATION]

Return only transferable composition guidance: reading path, hero strategy,
relative scale, image zones, text zones, whitespace, overlap rhythm, and hierarchy.
In ALLOW_ABSTRACT_DECORATION mode you may also describe non-identifying paper,
tape, line, and palette relationships.

Do not extract, reproduce, identify, or restate any photograph, person, food, object,
landmark, brand, readable text, date, price, place, or factual claim from the reference.
Do not copy exact coordinates. Do not add the reference to the content material list.
Explain how to adapt the abstract structure to the approved materials.
```

## 4. Story director and copywriter

```text
Plan a [JOURNAL_TYPE] journal from these approved elements: [ELEMENT_MANIFEST].
The thematic spine is [INTENTION]. Verified notes: [FACTS].
Optional safe layout analysis: [LAYOUT_REFERENCE_ANALYSIS or none].

First assign hero, support, transition, detail, and ending roles as the content supports.
Define a readable path and explain why adjacent elements belong together.
Then write layered, factual copy appropriate to the type. For a rich life record,
include an opening, image-linked notes, one reflective paragraph, marginalia, and closing.
Never invent an event, place, date, relationship, price, recipe, game fact, health claim,
or user feeling. Phrase interpretation as interpretation.

Return a story plan, ordered element IDs, copy blocks with target roles,
paper art direction, palette, forbidden motifs, and factual-risk notes.
```

## 5. Theme-specific paper

```text
Design only the background paper for a [FORMAT] journal.
Journal type: [TYPE]
Intention: [INTENTION]
Story direction: [STORY_SUMMARY]
Palette/material: [PALETTE_AND_TEXTURE]

Keep the central content field calm and usable, with restrained edge texture and
intentional blank areas. Support the story without depicting or replacing user elements.
Forbid: [OLD_OR_UNRELATED_MOTIFS], readable fake text, logos, frames, stock-photo scenes,
and decoration that competes with the hero. The paper must express this intention rather
than inherit a previous theme.
```

## 6. Layout composer

```text
Compose an editable [FORMAT] journal using exactly these approved element IDs once:
[ELEMENTS]. Use this story plan: [STORY_PLAN] and copy: [COPY_BLOCKS].

Create one large hero, medium supports, smaller details, a clear reading path,
safe title/footer zones, and intentional whitespace. Attach text to the image it explains.
Allow limited meaningful overlap without hiding subjects. Do not generate replacement
images, duplicate assets, equalize all sizes, scatter items into unrelated corners,
or introduce content visible only in an optional layout reference.

Return canvas dimensions, x/y/width/height, rotation, z-order, element role,
text style, alignment, and responsive or export notes.
```

## 7. Visual critic

```text
Inspect the complete rendered journal [RENDER], not only its coordinates.
Compare it with [INTENTION], [STORY_PLAN], [ELEMENT_MANIFEST], [SOURCE_LEDGER],
and [LAYOUT_REFERENCE_ANALYSIS or none].

Score 1–10: story coherence, copy richness/relevance, visual hierarchy,
paper-theme fit, legibility/whitespace, element fidelity, factual integrity,
provenance completeness, and reference safety. Cite visible evidence for each score.
If a reference exists, verify that only abstract structure transferred and that no
reference-only image, person, object, text, brand, place, or claim entered the result.
For every score below 7, propose one focused correction with exact affected IDs,
copy blocks, or regions. Preserve already strong dimensions.
```

## 8. Focused refinement

```text
Revise only these failed dimensions: [FAILED_DIMENSIONS].
Apply these exact corrections: [CORRECTIONS].
Preserve approved source elements, factual copy, provenance, and all dimensions
scored 7 or higher. Return the complete revised layout or artifact plus a concise diff.
```

## 9. Semantic recall

```text
Query: [NATURAL_LANGUAGE_MEMORY]
Candidates: [MEMORY_INDEX]

Rank by meaning, objects, atmosphere, colors, actions, intention, and story—not exact
keywords alone. Return the best matches with a brief reason, ranking score,
preview/artifact reference, memory ID, and unique original source URLs.
Treat scores as ranking signals rather than factual confidence.
```

## 10. Journal collection organizer

Use for search and metadata suggestions. Perform deletion only through a separate confirmed mutation:

```text
User request: [COLLECTION_REQUEST]
Saved journal summaries: [JOURNAL_INDEX]

Search across title, subtitle, place, date, tags, artistic copy, story nodes,
and element descriptions. Return stable journal IDs, match reasons, suggested filter,
sort order, and any metadata edits as a proposed patch.

Never infer deletion from a filter, low score, duplicate-looking preview, or stale date.
For single or bulk deletion, first return the exact selected IDs, count, archive effects,
and confirmation question. After explicit confirmation, report deleted IDs, failed IDs,
unlinked archive records, and shared assets intentionally preserved.
```
