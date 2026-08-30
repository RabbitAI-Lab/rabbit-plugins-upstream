---
name: photo-to-disco-elysium
description: 将用户上传的人像或环境照片重构为受《极乐迪斯科》启发的心理绘画与环境概念作品；首轮说明适配性并等待确认。人像默认使用激进概念肖像，可选温和角色肖像；环境保留地点锚点并进行作者化重构。 / Reconstruct user portraits and environments as Disco Elysium-inspired psychological paintings and concept artwork; explain source fit first, use conceptual portraits by default, and preserve essential place anchors while radically redesigning the rendering.
---

# 照片转《极乐迪斯科》风格 / Photo to Disco Elysium

## 概述

将用户上传的照片重构为受《极乐迪斯科》人物肖像与环境概念美术启发的心理绘画作品，而非简单套用油画滤镜。Skill 保留人物的身份关系、姿态与辨识性轮廓，或保留地点的关键地标与空间锚点，同时重新设计色彩、构图、笔触、边缘和叙事氛围。

适合人像、街道、城市、乡镇、建筑、室内、工业场景、港口与遗址等素材。自然风光属于条件适配：在不添加建筑、人物或叙事道具的前提下，以大气、地形、色彩和笔触层级完成重构。

人像在首轮适配说明中可选择两种方式：默认的 `conceptual_portrait` 更接近游戏原始角色肖像的激进概念重绘；可选的 `restrained_character_portrait` 则保留绘画化角色感，但减少象征性和心理性变形。每张源图默认只输出一张独立成品，不生成拼贴或网格图。Skill 不使用游戏角色、UI、Logo、对白框、标题字体或官方素材；游戏名称仅用于说明美术方向，不表示官方关联。

## Overview

Reconstruct user-supplied photographs as psychological paintings inspired by the character portraits and environmental concept art of *Disco Elysium*, rather than applying a simple oil-paint filter. The Skill preserves a person's identity relationships, pose, and recognizable silhouette, or a place's key landmarks and spatial anchors, while redesigning color, composition, brushwork, edges, and narrative atmosphere.

It is best suited to portraits and lived-in environments such as streets, cities, towns, villages, architecture, interiors, industrial sites, harbors, and ruins. Pure natural scenery is a conditional fit: it is reconstructed through atmosphere, terrain, palette, and mark hierarchy without inventing buildings, people, or narrative props.

For portraits, the first suitability reply offers two treatments: the default `conceptual_portrait`, an aggressive reconstruction closer to the game's authored character portraits, or the milder `restrained_character_portrait`, which keeps the designed painterly character treatment with less symbolic and psychic intervention. Each source image produces one independent finished result by default, never a collage or grid. The Skill does not add game characters, UI, logos, dialogue boxes, title typography, or official assets; the game name identifies the requested aesthetic direction only and does not imply official affiliation.

## Required references

Read only the references needed for the current request:

- Always read [visual-language.md](references/visual-language.md) and [transformation-contract.md](references/transformation-contract.md).
- For `portrait` or `environmental portrait`, always read [portrait-art-direction.md](references/portrait-art-direction.md) and [portrait-background-geometry.md](references/portrait-background-geometry.md).
- For `architecture_environment` or `natural_landscape`, always read [environment-art-direction.md](references/environment-art-direction.md).
- Read [analysis-card.md](references/analysis-card.md) for the selected branch.
- Read [prompt-compiler.md](references/prompt-compiler.md) immediately before generating or editing.
- Read [quality-checklist.md](references/quality-checklist.md) after generation and before returning the result.

## Workflow

### 0. Enforce the first-turn suitability gate

On the first Skill-triggered turn for a new photo or batch in the current task, do not call an image-generation tool and do not produce a transformed image. Inspect attached sources only as needed to assess fit, then briefly explain:

- strongest fit: portraits and lived-in environments such as cities, towns, villages, streets, architecture, interiors, industry, harbors, ruins, and other places with visible human traces;
- conditional fit: pure natural scenery such as mountains, forests, meadows, beaches, waterfalls, clouds, or sunsets. These have fewer social and architectural anchors and require concept-art reconstruction, strong atmospheric design, and unequal brush scale to avoid ordinary oil-landscape painting;
- portrait behavior: the face will be repainted while the uploaded background will be distilled into character-bearing color blocks, shapes, and line rhythms rather than preserved as a photographic backdrop. Offer two portrait treatments in the same reply: `conceptual_portrait` (default, aggressive and closest to the game's authored portrait logic) or `restrained_character_portrait` (the earlier, milder character-painting treatment). If the user confirms without naming one, use `conceptual_portrait`.

Classify each source as `recommended`, `conditional`, or `not recommended`, state the likely tradeoff, and ask the user to confirm whether to continue. Continue only after a later user reply confirms. Deliver this gate once per task or batch; do not repeat it after confirmation unless the source type changes materially.

If the user chooses a natural landscape after the caution, proceed on the next turn without inventing buildings, people, or narrative props. Preserve its ecological and geographic identity while using atmosphere, palette, depth, edge hierarchy, and selective natural detail as the authored structure.

### 1. Inspect and classify the source

Require at least one user-supplied photo. Inspect a local target image before editing. If the requested source is missing, ask the user to attach it again rather than inventing it from a description.

Classify the source by its primary promise:

- `portrait`: the person's identity is primary.
- `environmental portrait`: use portrait rules first, then add the place relationship.
- `architecture_environment`: a city, town, village, street, building, interior, industrial site, harbor, ruin, or another human-shaped place whose spatial and landmark identity is primary.
- `natural_landscape`: a primarily natural scene whose geographic forms, atmosphere, water, vegetation, rock, weather, or animal anchors are primary.

Treat visible facts as evidence. Do not invent a person's diagnosis, morality, protected traits, biography, or private state. Base interpretation on visible expression, pose, setting, and narrative supplied by the user.

### 2. Select the portrait treatment and apply the transformation contract

For portraits and environmental portraits, let the user select a treatment during the first-turn suitability gate. Default to `conceptual_portrait` when they confirm without choosing. Use `restrained_character_portrait` only when the user explicitly selects the milder treatment. Apply the environment contract unchanged for non-portrait sources.

For portraits, preserve `identity topology`, not photographic surface:

- keep the constellation of decisive facial landmarks, silhouette, face angle, gaze, hairstyle, accessories, and gesture recognizable;
- replace smooth skin gradients, camera lighting, literal complexion, hair-by-hair detail, photographic depth of field, and beauty-retouch realism;
- reconstruct the face as a character portrait through large designed planes, controlled asymmetry, altered feature hierarchy, broken edges, non-literal color, and character-specific marks.
- after selecting the treatment, choose a presentation: `character_portrait` is a compact head-and-shoulders or bust card when the source permits it; `environmental_portrait` keeps the person primary while retaining a decisive place relationship. The default `conceptual_portrait` treatment may use bounded source-derived symbolic or psychic re-authoring; the restrained treatment may not introduce it unless separately requested.
- reconstruct the uploaded background as one source-derived portrait field grammar, not a literal scene and not an arbitrary collection of geometry. Use one to four painted fields, with an optional restrained line rhythm, whose visual jobs follow visible evidence or user-provided narrative.

For environments, treat the photograph as concept-art source material, not a surface to filter. Apply B2.5 reconstruction: preserve essential place identity and navigable relationships while substantially redesigning atmosphere, palette, depth, edge hierarchy, spatial emphasis, and non-essential proportions. Allocate mark scale by information density and narrative importance: broad low-frequency masses for continuous fields and large structural planes; selective directional precision for identity-bearing architecture, vegetation, animals, and landmarks.

### 3. Build an internal analysis card

Complete the appropriate card from [analysis-card.md](references/analysis-card.md). For a portrait, explicitly separate:

- identity relationships that must survive;
- photographic properties that must disappear;
- facial features to emphasize, compress, partially obscure, or merge;
- one technique thesis that carries the portrait's story;
- one non-natural color event and one mark that moves against the depicted form.
- the selected portrait treatment, presentation, and crop strategy; background facts to distill; one chosen field grammar; and how its masses enter the hair, head, shoulders, or collar.

For an environment, explicitly record:

- the scene narrative, emotional thesis, environmental mood, and worldbuilding interpretation;
- identity anchors and an `identity importance` plus `detail budget` for major elements;
- source color relationships and the reconstructed emotional palette;
- foreground, middle-ground, and background roles plus allowed depth compression;
- sharp-edge anchors, soft-edge zones, and lost-edge zones;
- continuous low-information fields that receive broad marks and high-information or narrative-bearing structures that receive selective precision.

Keep the card internal unless the user asks to see the art direction.

### 4. Compile a visual prompt

Translate the card into visible instructions with [prompt-compiler.md](references/prompt-compiler.md).

For portraits, establish this priority:

`identity topology > selected treatment and portrait presentation > silhouette, gaze, and pose > technique thesis and portrait-field grammar > value and relational color > edge hierarchy and brushwork > photographic surface fidelity`

For environments, establish this priority:

`place identity anchors > scene narrative and visual protagonist > composition and depth redesign > atmosphere and palette reconstruction > semantic detail allocation > edge hierarchy > mark and material language > photographic surface fidelity`

Treat photographic surface fidelity as something to remove, not a quality target. Describe the intended visual behavior rather than depending on the phrase “Disco Elysium style.”

### 5. Generate or edit

Use the available image-generation editing tool with the original photo as the image reference. Produce one finished reinterpretation by default. Keep the source aspect ratio unless the user requests another crop.

For either portrait treatment, prefer a compact vertical head-and-shoulders or bust character-card presentation when the source provides enough information and the user has not asked to preserve the whole composition. Do not silently crop away a pose, garment, or place relationship that is essential to the supplied image. This version does not infer a full-body portrait workflow: preserve the source composition when the user requests it or when it is the image's decisive fact.

Require the portrait edit to transform the facial interior, not just the background or clothing. Preserve identity through relationships while allowing expressive change to pass through the forehead, cheeks, nose, mouth, jaw, hair, and neck.

For portraits, do not preserve the source background as a literal photographic scene unless one object is essential to identity or user narrative. Abstract the remaining setting into one coherent source-derived portrait field: one to four irregular color masses in a single field grammar, plus an optional restrained line rhythm. The field must interact with hair, collar, face, or shoulder rather than sitting behind a cut-out person. Do not substitute generic smoke, decorative splashes, arbitrary geometry, or franchise-like motifs.

Protect these source facts unless explicitly authorized:

- number and identity of people;
- landmark relationships between facial features, distinctive silhouette, accessories, pose, and gesture;
- essential landmark identity, key road or path relationships, principal subject objects, and the minimum spatial structure needed to recognize the place;
- culturally or personally meaningful details identified by the user.

Do not add game characters, skill portraits, dialogue boxes, interface panels, logos, watermarks, captions, or imitation title typography. Do not reuse or embed official game or artbook assets.

### 6. Evaluate and repair

Compare the result with the source using [quality-checklist.md](references/quality-checklist.md). For portraits, both gates must pass:

1. The person remains recognizable through identity topology.
2. The image no longer reads as a realistic person with an oil-paint or color filter.

If either gate fails, make one focused edit that names the failed relationship or insufficient artistic departure while freezing successful properties. Do not regenerate blindly with a longer adjective list.

For environments, both gates must pass:

1. The original place or natural system remains recognizable through its essential anchors.
2. The result reads as an authored environmental concept-art reconstruction, not a photograph with uniform oil texture.

Repair only the failed layer: identity, atmosphere, sky, palette, depth, semantic detail, edge hierarchy, or mark-scale hierarchy.

### Strict evaluation mode

For Skill development, A/B testing, or when the user asks for a traceable test, save six observable artifacts together: `classification`, `analysis-card`, `compiled-prompt`, `generated-image`, `quality-evaluation`, and any `repair-prompt`. Use the complete Skill pipeline; do not substitute an improvised conversation-only prompt. For ordinary user transformations, keep analysis and prompts internal unless requested.

### 7. Deliver

Return the finished image without exposing the full compiled prompt unless requested. Briefly identify the chosen treatment and the main technique or scene-narrative thesis. Do not present multiple candidates unless the user requested variations.

## Rights and reference boundary

Use the game name to identify the requested aesthetic direction, not to imply affiliation or reproduce proprietary assets. Build the result from the user's photo and the original visual rules in this Skill. Use only user-owned, licensed, public-domain, or newly generated source images in distributed examples.
