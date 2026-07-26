---
name: shiguang-memory-journal
description: "A tool-agnostic workflow and experience pack for turning key frames and source links into 1–5 redrawn keepsake elements, safely learning layout from an optional reference, composing an editable story-led journal, organizing journal/library/memory collections, preserving provenance, supporting semantic recall, and returning to the original content or next real-world action. Use when an agent needs to plan, build, or operate a reusable visual-memory workflow; analyze source images; distinguish content materials from layout references; create or critique scrapbook and guide compositions; write factual artistic copy; search, edit, or delete saved journals and memory assets; design archive/search contracts; or adapt the complete 来源画面 → 元素重绘 → 参考分析 → 可编辑手帐 → 独立整理 → 记忆归档 → 语义找回 → 回到来源/行动 process with its own tools. This skill requires no specific API, local service, token, or bundled runtime."
---

# Shiguang Memory Journal

Apply this playbook with the current agent's own tools. Do not require a Shiguang API, localhost service, bearer token, or bundled executable.

Preserve the product promise:

`关键帧与来源链接 → 1–5 枚元素重绘 → 可选版式参考 → 故事化手帐 → 独立整理 → 记忆归档 → 语义找回 → 回到原内容或行动`

## Load the right knowledge

- Read [references/product-principles.md](references/product-principles.md) before making product, copy, or provenance decisions.
- Read [references/workflow-playbook.md](references/workflow-playbook.md) before running or designing the complete lifecycle.
- Read [references/style-profiles.md](references/style-profiles.md) when choosing among the seven journal types.
- Read [references/prompt-pack.md](references/prompt-pack.md) before delegating visual analysis, redraw, story, copy, background, layout, critique, or recall to a model.
- Read [references/data-contracts.md](references/data-contracts.md) when implementing archive, search, interoperability, or handoff.

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

1. Collect the key frame, original HTTP(S) source link when available, journal type, user intention, output format, and an exact extraction count from 1 to 5. Default to 3 only when the user gives no count.
2. Create a provenance ledger before transformation. Give the source and every derived item stable IDs; copy the source link forward without silently changing it.
3. Inspect the frame and select exactly the requested number of distinct, visible subjects. Favor theme relevance, recognizable silhouettes, visual variety, and complementary story roles.
4. Redraw one subject per generation or editing call. Preserve identity-defining shape and color while removing platform UI, subtitles, watermarks, and unrelated background. Label direct crops honestly; never call them redraws.
5. For composition, let the user approve 1–12 content materials from the current work and reusable library. Keep an optional reference journal in a separate field: it guides layout and must never silently become content.
6. If a reference is present, analyze only transferable structure—reading path, hero strategy, relative scale, text zones, whitespace, overlap rhythm, and optionally abstract paper/palette relationships. Do not copy its photos, people, objects, places, brands, readable text, or factual claims.
7. Plan the story before placing anything. Assign one hero and supporting, transition, detail, or ending roles; define a readable visual path and choose a paper direction that expresses the current intention.
8. Write artful but factual copy. Use multiple text responsibilities—opening, image-linked notes, reflection, marginalia, and closing—rather than a generic title plus one subtitle.
9. Compose with hierarchy and breathing room. Use approved content assets exactly once unless the user requests repetition. Do not scatter equally sized elements into unrelated corners or mechanically clone reference coordinates.
10. Review the rendered whole page, not only its JSON or coordinates. Score story, copy, hierarchy, paper-theme fit, legibility, provenance, factual integrity, and reference safety; revise weak dimensions with focused calls.
11. Save editable structure and expose a journal collection where users can search, filter, sort, preview, quick-edit metadata, reopen for full editing, and explicitly select single or bulk deletion.
12. Archive the source, derived elements, journal, prompts, descriptions, relationships, warnings, and source links in the best durable format available. On confirmed deletion, unlink stale archive records and remove only files no longer referenced.
13. Support natural-language recall by meaning, atmosphere, objects, colors, and vague memory. Return ranked reasons and always surface the original source link or next real-world action.

## Protect quality and trust

- Treat the user's intention as the thematic spine, not permission to invent events, places, prices, dates, relationships, game facts, recipes, health claims, or feelings.
- Let AI organize; do not make the user maintain technical tags or prompts.
- Keep one clear hero, purposeful relationships, legible text, and intentional whitespace.
- Keep content materials and layout references visibly and structurally separate.
- Regenerate the paper direction when the intention changes. Never inherit an unrelated food, travel, or decorative theme.
- Preserve editable structure when the output medium allows it.
- Require explicit selection and confirmation before destructive single or bulk deletion. Preserve source records and unrelated shared assets.
- Distinguish executed results, fallbacks, and proposed artifacts in the final response.
- End every successful recall flow with unique, clickable source links.

## Deliver a reusable result

Return or save these artifacts even when the implementation stack differs:

- `source record`;
- `element plan` and 1–5 element assets or redraw prompts;
- approved `content material manifest` and optional `layout-reference analysis`;
- `story and copy plan`;
- `background art direction`;
- `layout specification` and rendered journal when possible;
- editable `journal record` plus collection search/edit/delete behavior or a handoff specification;
- `memory manifest`;
- `recall index or retrieval plan`;
- `quality report`;
- unique `source links`.

Use the field shapes in [references/data-contracts.md](references/data-contracts.md) so another agent can continue the work without reverse-engineering hidden state.
