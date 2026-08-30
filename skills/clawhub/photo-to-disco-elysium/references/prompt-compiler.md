# Prompt Compiler

Compile the analysis card into one self-contained image-editing instruction. Prefer concrete visual behavior over theory or adjective piles.

## Contents

- [Prompt order](#prompt-order)
- [Environment compiler order](#environment-compiler-order)
- [Branch emphasis](#branch-emphasis)
- [Repair prompt patterns](#repair-prompt-patterns)

## Prompt order

### 1. Radical reconstruction contract

Open with the task, branch, and source relationship. Use the portrait opening only for `portrait` or `environmental portrait`:

```text
Completely repaint the supplied photograph as an original Disco Elysium-style psychological painting using high abstraction. Reconstruct it from the ground up; do not preserve or filter the photographic surface. Preserve [identity topology or place anchors] and [pose, gesture, silhouette, or spatial structure], while replacing realistic rendering with designed masses, controlled deformation, relational color, edge hierarchy, and character-specific marks.
```

Do not offer generic strength modes. For portraits, honor the two explicit treatment choices made during the first-turn suitability gate; do not stop at the game name.

For `architecture_environment` or `natural_landscape`, open with the concept-art contract instead:

```text
Treat the supplied photograph as source material for an original Disco Elysium-inspired environmental concept painting, not as a surface to filter. Preserve [essential place or natural-system anchors], but redesign atmosphere, palette, depth, edge hierarchy, spatial emphasis, and semantic detail with B2.5 creative freedom so the same place feels authored for this world rather than merely oil-painted.
```

### 2. Source truth and protected relationships

Name only the source relationships that must survive:

- portrait: count, face axis, four to six identity anchors, gaze, expression, silhouette, hairstyle or accessory, pose, and clothing mass;
- architecture environment: core building and landmark identity, decisive silhouettes, key road, path, entrance, and mass relationships, and the minimum perspective structure needed for recognition;
- natural landscape: horizon, terrain or shoreline geometry, water direction, geographic silhouettes, weather mass, characteristic vegetation or rock structure, and any animal anchor;
- environmental portrait: combine only decisive anchors, with the person primary.

For portraits, explicitly state that smooth skin, camera lighting, literal complexion, realistic gradients, hair strands, and photographic depth must not survive. Do not ask for a full-body conversion unless the user explicitly requests it; this baseline portrait branch is optimized for character-card treatment, not inferred whole-body adaptation.

### 3. Portrait redesign block

For `portrait` and `environmental portrait`, include every item below:

1. The selected treatment and presentation: use `conceptual_portrait` by default unless the user explicitly chose `restrained_character_portrait`; then choose `character_portrait` or `environmental_portrait` for the composition. If the source allows, use a compact head-and-shoulders or bust card; otherwise preserve the requested or essential composition.
2. The source pose, face axis, gaze, signature hair or accessory, and head-hair-collar silhouette that must survive.
3. One painting grammar and one technique thesis with visible effects.
4. A five-to-eight-plane reconstruction of head, face, hair, neck, and collar, with one graphic light mass and one or two shadow cavities.
5. Two non-essential features or planes to exaggerate, compress, offset, obscure, flatten, or merge.
6. One small refinement zone and one large abbreviated or lost zone.
7. One motivated non-natural color event passing through the face or collar edge.
8. One family of marks moving against natural hair, skin, clothing, or anatomical direction.
9. One source-derived background field grammar with one to four irregular painted masses, plus an optional restrained line rhythm.
10. At least two ways the field cuts into, merges with, pressures, shelters, divides, or radiates from the head, collar, and shoulders.

Keep the protected landmark constellation collectively recognizable. Do not instruct the model to keep expressive damage away from the whole face; the facial interior must be visibly re-authored.

### 4. Psychological proposition

State one proposition, one tension, and their visible consequence.

Good portrait example:

```text
Make the outward stillness resist inward pressure: compress the forehead and cheek into cold angular planes, pull dark vertical masses toward the shoulders, preserve the long nose and uneven brow relationship, and let a dry warm-red interruption cross the lower face.
```

Good environment example:

```text
Make the wet street feel suspended between neglect and fragile recovery: compress cool buildings into leaning masses while one low warm passage leads the eye toward the distance.
```

Avoid “make it emotional” or “show inner turmoil” without a visible mechanism.

### 5. Composition and value

Describe dominant masses, focal point, viewing path, pressure direction, and three or four large value groups. Keep the image readable at thumbnail size.

For portraits, use value shapes to redesign anatomy rather than model it smoothly. Permit local flattening, abrupt plane changes, and asymmetric shadow logic while protecting the landmark constellation. For environments, protect the horizon and entry path while allowing depth compression and scale shifts.

### 6. Relational color and light

Define a dominant temperature, counter-temperature, darkest or brightest structural accent, one saturation maximum, and how colors contaminate adjacent neutrals. Tie each decision to the proposition.

For portraits, replace literal skin color with a designed color system. A cold forehead, red eye socket, green jaw edge, violet cheek, or yellow-lit nose must function compositionally rather than as franchise decoration.

### 7. Edge, refinement, and material

Specify hard, soft, and lost-edge zones. Name the small refined passage and the large generalized passage. Choose a limited compatible mark family:

- blocky opaque planes;
- cross-grain dry brush;
- scraped or dragged paint;
- broken contour and abrupt corrections;
- translucent scumbling;
- sparse impasto at one accent;
- broad merged pressure fields.

Do not request all materials at once. Place accidents so they reinforce the technique thesis.

### 8. Exclusions

End portraits with source-specific prohibitions plus these defaults:

```text
No added people, no changed identity, no beauty painting, no photoreal skin, no smooth airbrushed gradients, no realistic oil portrait, no unchanged face beneath texture, no generic fantasy costume, no recognizable game characters, no copied portrait composition, no game UI, no skill icons, no logos, no captions, no watermarks, and no uniform filter. Do not make every facial feature equally precise or every region equally detailed. For `restrained_character_portrait`, do not introduce extra faces, psychic anatomy, or icon-like symbolic imagery. For `conceptual_portrait`, allow only bounded source-derived symbolic or psychic re-authoring that preserves identity topology and does not add game imagery, logos, or copied motifs.
```

Remove exclusions only when they conflict with an explicit user request outside this Skill's core scope.

For environments, use branch-specific exclusions:

```text
No uniform oil-paint filter, no equal small-stroke density across the image, no photographic color preservation, no equally sharp edges, no generic fantasy substitution, no unrelated buildings or people, no erased landmark identity, no invented human traces in pure nature, no copied game location or asset, no game UI, no logos, no captions, and no watermarks.
```

## Environment compiler order

For `architecture_environment` and `natural_landscape`, compile in this order. Do not mix these instructions into the portrait redesign block.

### 1. Core preservation anchors

Name three to six essential anchors and the minimum route, horizon, shoreline, entrance, or mass relationship needed to recognize the place. Do not protect every visible object.

### 2. Scene narrative thesis

State the `scene narrative`, `emotional thesis`, `environmental mood`, `worldbuilding interpretation`, and visual protagonist as visible consequences. Describe what mass, weather, light, or structure will express the thesis.

### 3. B2.5 reconstruction freedom

Explicitly permit substantial redesign of weather, light direction, cloud structure, palette, shadow depth, depth compression, sky proportion, horizon emphasis, limited secondary proportions, and peripheral geometry. Freeze the essential anchors so freedom does not become a different place or biome.

### 4. Composition and depth redesign

Assign foreground, middle-ground, and background roles. Define entry path, focal mass, spatial pressure, occlusion, and allowed depth compression. Put the highest semantic information in the middle ground unless the source provides a different visual protagonist.

### 5. Atmosphere and sky redesign

Treat weather, sky, fog, water, glare, snow, or large shadow as an active narrative mass. Merge literal cloudlets and small waves into a few broad directional fields. State the intended light and atmosphere rather than asking for “dramatic mood.”

### 6. Palette reconstruction

Preserve the source's color relationships, not literal hues. Name the target emotional palette, dominant hue, shadow family, light family, limited accent, and how adjacent neutrals become contaminated.

### 7. Large-form mark strategy

Assign the largest viable marks to low-information continuous fields and structural planes: sky, water, fog, snow, road, ordinary walls, roofs, lawns, distance, and broad shadow. Define stroke direction and frequency; do not merely say “large brushstrokes.”

### 8. Semantic detail allocation

For each important element, translate `identity importance` and `detail budget` into visible instructions. Use selective finer lines and directional marks for landmark ornament, structural joints, windows that create identity, signs, railings, lamps, wires, trunks, branches, foliage clusters, flowers, rock ridges, birds, and animals. Compress generic repetition.

### 9. Edge hierarchy

Name primary sharp anchors, secondary broken or soft transitions, and lost-edge zones. Keep the strongest edge contrast at the visual and narrative center. Permit distance, atmosphere, large shadow, and low-importance boundaries to merge.

### 10. Material language

Choose a limited compatible mark family. Make stroke scale vary sharply by the assigned visual job. Avoid requesting every painting material at once.

### 11. Negative constraints

End with the environment exclusions above plus source-specific prohibitions. For natural landscapes, explicitly prohibit invented architecture, people, roads, and symbolic props.

## Branch emphasis

### Portrait

Spend most prompt space on identity topology, portrait presentation, head-hair-collar silhouette, facial mass redesign, controlled feature hierarchy, technique thesis, cross-grain marks, and a source-derived portrait field. Preserve recognition through relationships while visibly departing from the source in surface, local proportion, color, edge, refinement, and backdrop. Require one coherent background-field grammar with one to four irregular masses and an optional line rhythm; do not accept generic smoke, a blurred photograph, or a mechanical collection of shapes.

### Environment

Use the environment compiler order. Spend most prompt space on place identity, scene narrative, B2.5 atmosphere and palette reconstruction, depth roles, semantic detail budgets, and edge hierarchy. Use broad structure with selective precision. Do not individually outline every building, window, tree, leaf, wave, or brick, but do not blur identity-bearing ornament, vegetation, rock, or animal structure into anonymous masses.

### Environmental portrait

Keep the portrait reconstruction primary. Turn the environment into the force acting on the figure rather than a second unrelated subject.

## Repair prompt patterns

### Identity topology drifted

```text
Keep the current abstraction, color system, background pressure, plane design, and rough painterly treatment. Correct only these identity relationships to match the source: [anchors]. Do not restore photoreal skin, smooth lighting, or photographic detail.
```

### Portrait remains too photographic

```text
Keep the person's identity anchors, face angle, gaze, pose, crop, and signature attributes. Repaint the facial interior much more radically: replace realistic skin and camera lighting with [mass design], alter the hierarchy of [features], introduce [color event], lose [edge zone], and drive [cross-grain marks] through the face. Do not merely add texture or change the background.
```

### Environment identity drifted

```text
Keep the current palette, atmosphere, abstraction, and painterly marks. Restore only [horizon, perspective, and landmark anchors] so the place reads again. Do not return to photographic detail.
```

### Environment remains an ordinary oil painting

```text
Keep the essential place anchors and any successful focal detail. Repair only the concept-art direction: strengthen [scene narrative], redesign [atmosphere and palette], increase depth compression, enlarge marks across [continuous fields], concentrate finer directional marks only in [identity-bearing structures], and create distinct primary, secondary, and lost edges. Do not repaint every region with the same stroke scale.
```

### Sky or atmosphere remains too literal

```text
Keep the place anchors, ground structure, and successful detail allocation. Replace only the sky and atmospheric system: merge literal clouds into [large directional masses], establish [target light and weather], reduce internal small strokes, permit [non-literal color relationship], and let selected building, terrain, or vegetation edges dissolve into the atmosphere.
```

### Architecture became too blurry

```text
Keep the successful large building masses, road and sky planes, atmosphere, palette, and depth. Restore only these identity-bearing details with selective directional lines and smaller marks: [ornament, entrance, window rhythm, capital, railing, lamp, sign, roof structure]. Do not reintroduce uniform brick, tile, or window detail elsewhere.
```

### Scene remains too faithful to the photograph

```text
Keep the essential identity anchors and route relationships. Increase only the B2.5 reconstruction: redesign light direction, sky proportion, weather, emotional palette, depth compression, edge loss, and focal emphasis. Do not change the place into another city or biome.
```

### Scene is no longer recognizable

```text
Keep the successful atmosphere, palette, broad mark hierarchy, and edge system. Restore only [core landmark silhouette], [key road, path, shoreline, or entrance relationship], and [principal mass proportion]. Do not return to literal colors, uniform photographic depth, or dense surface detail.
```

### Portrait background remains literal or generic

```text
Keep the person's identity topology, facial mass redesign, pose, crop, technique thesis, and successful face abstraction. Replace only the background: distill [two to four source background facts] into [one chosen field grammar] with [one to four irregular color masses] and [optional line rhythm], then make at least two field actions [press on, shelter, divide, crop, merge with, or radiate from] the head, collar, and shoulders. Remove photographic scenery, generic smoke, random splatter, and decorative symbols unrelated to the source.
```
