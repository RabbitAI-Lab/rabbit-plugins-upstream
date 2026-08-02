---
name: shiguang-memory-journal
description: "A tool-agnostic workflow for turning video links/files, key frames, user stories, and optional reference posters into evidence-grounded传播海报 or editable memory journals. It builds a NarrativeBrief, retrieves story-bearing frames, competes identity/contrast/emotion concepts, separates source content from reference style, audits title–visual–intent alignment, preserves provenance and editable structure, and supports archive and semantic recall. Use for short-video poster generation, video-to-poster pipelines, reference-poster adaptation, key-frame redraw, scrapbook composition, visual-memory archive/search, or adversarial quality review. Requires no specific API, local service, token, or bundled runtime."
---

# Shiguang Memory Journal

Apply this playbook with the current agent's own tools. Do not require a Shiguang API, localhost service, bearer token, or bundled executable.

Capability revision: `2.0.0`. See the version evolution and release rules in [references/video-poster-workflow.md](references/video-poster-workflow.md#version-evolution); the registry/package version is the authoritative published version.

Preserve the product promise:

`关键帧与可选来源链接 → 默认 1 枚（可调至 1–5 枚）元素重绘 → 逐元素画面范围 → 可选版式参考 → 故事化手帐 → 独立整理 → 记忆归档 → 语义找回 → 回到原内容或行动`

For video posters, preserve the parallel promise:

`视频链接或文件 → 证据索引与 NarrativeBrief → 故事关键帧 → 三类传播概念竞赛 → 主辅画面海报 → 对抗审计 → 可编辑交付与反馈`

## Load the right knowledge

- Read [references/product-principles.md](references/product-principles.md) before making product, copy, or provenance decisions.
- Read [references/workflow-playbook.md](references/workflow-playbook.md) before running or designing the complete lifecycle.
- Read [references/style-profiles.md](references/style-profiles.md) when choosing among the seven journal types.
- Read [references/prompt-pack.md](references/prompt-pack.md) before delegating visual analysis, redraw, story, copy, background, layout, critique, or recall to a model.
- Read [references/data-contracts.md](references/data-contracts.md) when implementing archive, search, interoperability, or handoff.
- Read [references/video-poster-workflow.md](references/video-poster-workflow.md) whenever the input is a video, the requested output is a poster/cover, or a reference poster is supplied. It defines inputs, outputs, model-call conditions, failure handling, adversarial gates, reuse, and version evolution.

## Choose the workflow branch

- Use the video-poster branch for a video URL/file, a request for a short-video poster/cover, or evaluation of whether a poster expresses a video's story and intent.
- Use the memory-journal branch below for frame extraction/redraw, scrapbook composition, collection management, archive, or recall.
- Run both only when the user asks to turn the generated poster or its source frames into an editable journal/memory record. Keep their outputs separately identifiable.

For the video-poster branch, require a source video and desired output. Treat a source link, upload, user intention, channel/ratio, and reference poster as optional constraints. Use one multimodal understanding call after evidence-aware candidate retrieval when such a model is available; do not add a second summarization call merely to create the poster. Generate or compose pixels only after a candidate passes the concept tournament. When AI, ASR, OCR, downloading, or rendering is unavailable, follow the explicit degradation matrix in the reference and never label metadata-only inference as semantic understanding.

## Map available capabilities

Inventory the current agent's tools and map them to these roles:

1. visual inspection;
2. image generation or editing;
3. layout composition or document/canvas creation;
4. durable file, database, or knowledge storage;
5. semantic retrieval or best available text search;
6. collection management with safe edit and delete operations;
7. source-link presentation or navigation.

Use available tools rather than assuming product-specific names. If a role is unavailable, produce the corresponding structured plan, prompt, manifest, or layout specification for another agent or tool. Never claim an image, archive, or search index was created when only a proposal was produced.

## Run the lifecycle

1. Collect the key frame, optional original HTTP(S) source link, extraction style (`handdrawn`, `comic`, `collage`, or `realistic`), journal type, user intention, output format, task-level background strategy (`subject-only`, `preserve-context`, or `mixed`), and an exact extraction count from 1 to 5. Default to 1 when the user gives no count. A missing source link must never block extraction. `mixed` requires at least two elements and should use the user's element-by-element intent when supplied.
2. Create a provenance ledger before transformation. Give the source and every derived item stable IDs; copy the source link forward without silently changing it.
3. Inspect the frame and select exactly the requested number of distinct, visible subjects or meaningful environment regions. Favor intention relevance, recognizable silhouettes, visual variety, and complementary story roles.
4. Redraw one planned element per generation or editing call and record its own element-level mode. In `subject-only`, preserve identity-defining shape and color while removing unrelated background. In `preserve-context`, keep the subject together with the visible environment that directly explains its spatial, action, or narrative relationship. In `background-only`, keep a meaningful environment region and remove foreground people or objects the user excluded. For a `mixed` task, assign at least two different element-level modes from the user's detailed intent, falling back to a balanced AI plan only when that intent is absent. Label direct crops honestly; never call them redraws.
   Treat `realistic` as a photographic rendering profile, not an illustration preset: preserve natural light, skin, fabric, surfaces, lens perspective, identity, count, pose, and scene relationships; allow only restrained composition, exposure, and color refinement. Reject plastic skin, face replacement, body reshaping, aggressive HDR, 3D-rendered surfaces, invented people, or stylization that erases material truth.
   Preserve a valid generated image's natural portrait, landscape, or square canvas unless the user explicitly requested an aspect ratio. Do not reject or pad an otherwise valid element merely because it is not 1:1.
5. For composition, let the user approve 1–12 content materials from the current work and reusable library. Keep an optional reference journal in a separate field: it guides layout and must never silently become content.
6. If a reference is present, analyze only transferable structure—reading path, hero strategy, relative scale, text zones, whitespace, overlap rhythm, and optionally abstract paper/palette relationships. Do not copy its photos, people, objects, places, brands, readable text, or factual claims.
7. Plan the story before placing anything. When the user supplies a story, treat it as the first-priority factual and narrative axis: score factual fidelity, narrative structure, and sentence selection, then remove repetition, refine, and compress without replacing it with generic template copy. Assign one hero and supporting, transition, detail, or ending roles; define a readable visual path and choose a paper direction that expresses the current intention.
8. Write artful but factual copy. Use multiple text responsibilities—opening, image-linked notes, reflection, marginalia, and closing—rather than a generic title plus one subtitle. Select at most two verbatim highlight phrases per block when real numbers, distances, people counts, achievements, turns, or distinctive original wording deserve emphasis. Design font family, size, weight, tracking, leading, alignment, container, and contrast as one typography system.
9. Compose with hierarchy and breathing room. Use approved content assets exactly once unless the user requests repetition. Do not scatter equally sized elements into unrelated corners or mechanically clone reference coordinates. Derive the canvas ratio from an explicit target or reference before considering material count; more assets do not justify an unsupported long page. Build 3–4 narrative groups with one dominant hero and a lower-page emotional anchor. Use paper or Polaroid frames on contextual images and reserve tape for roughly 1–3 accents. Let transparent people overlap contextual images by about 4%–16% to connect groups, but never cover people, essential scenery, or text.
   When the user supplies a specific finished journal as the target effect, switch from loose reference adaptation to target reconstruction: derive the canvas ratio from that target, inventory every independent content layer, keep original sources, remove those layers from a clean base, and place them back at measured coordinates. Assign overlapping pixels to the visible top layer so one element does not carry a duplicate person or neighboring card. Preserve titles or doodles as base decoration only when they do not need independent editing.
10. Review the rendered whole page, not only its JSON or coordinates. Score story, copy, typography, hierarchy, whitespace, paper-theme fit, provenance, factual integrity, and reference safety; reject pages that still read as uniform photo walls. If the structure is already strong and only a small overlap or text collision fails, apply the smallest local movement and revalidate instead of discarding the entire AI composition. Fall back to a full safe layout only for missing content, identity errors, collapsed hierarchy, or unresolved structural failure. When the user requests interactive creation, pause after reference analysis, story, layout, and rendered review so they can approve or revise the current stage.
11. Save editable structure and expose a journal collection where users can search, filter, sort, preview, quick-edit metadata, reopen for full editing, import a portable editable journal as a new record, export that structure again, and explicitly select single or bulk deletion.
12. Archive the source, derived elements, journal, prompts, descriptions, relationships, warnings, and source links in the best durable format available. On confirmed deletion, unlink stale archive records and remove only files no longer referenced.
13. Support natural-language recall by meaning, atmosphere, objects, colors, and vague memory. Return ranked reasons and surface the original source link when available; otherwise state that the link is unavailable and provide the next real-world action.

## Protect quality and trust

- Treat the user's intention as the thematic spine, not permission to invent events, places, prices, dates, relationships, game facts, recipes, health claims, or feelings.
- Let AI organize; do not make the user maintain technical tags or prompts.
- Keep one clear hero, purposeful relationships, legible text, and intentional whitespace.
- Protect a strong AI composition from all-or-nothing fallback: repair isolated geometry and text collisions locally, then rerun the deterministic quality gate.
- Treat user-provided story text as the first-priority factual source. Always score, refine, and select it before placing copy; never let template prose replace its key facts, turns, relationships, actions, or closing meaning.
- Keep content materials and layout references visibly and structurally separate.
- Regenerate the paper direction when the intention changes. Never inherit an unrelated food, travel, or decorative theme.
- Preserve editable structure when the output medium allows it.
- Preserve every visible person unless the user explicitly requests removal. Before delivery, audit the expected people count on both the independent person assets and the composed page; a person hidden by overlap still counts as missing.
- Do not force a square or default journal ratio onto a valid target. Store explicit canvas width and height when the target or user specifies another format, and verify editor, thumbnail, mobile fit, PNG export, and portable project export against that size.
- Never imply that a flattened PNG, JPG, WebP, PDF, or screenshot can recover its original layers. Import it honestly as one editable visual or a background. Use a portable structured journal package with embedded or resolvable assets when independent images, text, positions, rotations, layers, and source links must survive a round trip.
- Require explicit selection and confirmation before destructive single or bulk deletion. Preserve source records and unrelated shared assets.
- Distinguish executed results, fallbacks, and proposed artifacts in the final response.
- End every successful recall flow with unique, clickable source links when available; never fabricate a link to satisfy the format.

## Deliver a reusable result

Return or save these artifacts even when the implementation stack differs:

- `source record`;
- `element plan` and 1–5 element assets or redraw prompts;
- approved `content material manifest` and optional `layout-reference analysis`;
- `story and copy plan`;
- `background art direction`;
- `layout specification` and rendered journal when possible;
- editable `journal record`, a portable import/export package when supported, plus collection search/edit/delete behavior or a handoff specification;
- `memory manifest`;
- `recall index or retrieval plan`;
- `quality report`;
- interactive checkpoint summaries and revision feedback when staged review is enabled;
- target-reconstruction process data when used: clean base, independent elements, extraction manifest, production/layout manifest, story, reference analysis, reconstructed preview, browser regression result, and people audit;
- unique `source links` when available, otherwise an explicit unavailable status and next action.

Use the field shapes in [references/data-contracts.md](references/data-contracts.md) so another agent can continue the work without reverse-engineering hidden state.
