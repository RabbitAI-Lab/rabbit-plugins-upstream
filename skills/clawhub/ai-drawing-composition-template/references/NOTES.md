# Workbook Notes — Supplementary Material for the 12 Sheets

The 12 CSV files in this folder are flat tables so that GitHub renders them cleanly.
This file restores the explanatory content removed in the restructure: section
descriptions, reference tables, supplementary rules, and usage notes.

---

## Usage.csv

### Section ② — Weight semantics master table (SD/MJ numeric baseline)

| Weight range | Semantics | Applies to | Example | Corresponding action |
|---|---|---|---|---|
| 1.6 - 2.0 | Hard anchor: absolutely immutable | Identity anchors / signature features | Mole below left eye (1.8) | Force-keep in every scene; add opposites to negative prompts |
| 1.3 - 1.5 | Core feature: kept in all scenes | Face / hairstyle / core outfit | Light mint cotton plain dress (1.4) | Cross-scene consistency baseline; validated as P0 |
| 1.0 - 1.2 | Baseline feature: default strength | Natural-language main description / auxiliary elements | Gentle, quiet temperament (1.0) | Fine-tune per scene; fluctuation ≤ 0.2 |
| 0.7 - 0.9 | Atmosphere aid: adjustable per scene | Scene elements / decor / weather | Spring garden (0.8) | Replaceable when the scene changes |
| <0.7 | Weak prompt: easily ignored by models | Minor modifiers | Breeze (0.5) | Atmosphere only; must not carry key information |

### Section ③ — Weight → narrative intensity mapping (new in v2.2)

Natural-language models have no numeric weights; express them via this table.

| Numeric weight | Semantics | How to express in natural-language models | MJ/Niji expression | Description precision requirement |
|---|---|---|---|---|
| 1.6 - 2.0 | Hard anchor: absolutely immutable | Standalone short sentence + sentence-initial priority + high-precision description (position/material/relative quantifier) | First 10 tokens + repeated keywords | Must be concrete enough to draw: tiny / in the hair / below the left eye corner |
| 1.3 - 1.5 | Core feature: kept in all scenes | Standalone short sentence placed early in the character description block | First 20 tokens | Concrete and drawable; abstract adjectives forbidden |
| 1.0 - 1.2 | Baseline feature: default strength | Regular clause carried naturally by the main sentence | Middle section | Plain description is enough |
| 0.7 - 0.9 | Atmosphere aid: adjustable per scene | Environment sentence placed at the very end | Mid-late section | Keywords suffice |
| <0.7 | Weak prompt: may be omitted | Do not write | Do not write | — |

### Section ④ — Validation priority (P0 mandatory / P1 recommended / P2 optional)

| Priority | Definition | Failure handling |
|---|---|---|
| P0 | Core character settings; failure = discard the image | Must adjust and regenerate |
| P1 | Image quality and proportions; affects usability | Fix first; one retry acceptable |
| P2 | Aesthetics and details; icing on the cake | Log the issue; improve next round |

### Section ⑤ — Cross-model syntax red lines (must read)

| Red line | Explanation |
|---|---|
| Weight syntax | `(word:1.3)` works only on SD; MJ relies on token position and repetition; natural-language models forbid bracket weights — rely on narrative structure |
| Negative prompts | MJ `--no` limited to 4-6 short words; SD uses the Negative Prompt box; Flux/DALL-E/GPT-4o/Gemini have no negative box → write affirmatively first, negate as fallback; domestic API negative-word support per official docs |
| Reference images | MJ `--cref`; SD LoRA; Flux Kontext/Redux; GPT-4o/Gemini native reference images; DALL-E 3 has none → description-led, recommended deprecated; domestic API reference capabilities per official docs — see the Reference Image Capability Matrix |
| Anchor reuse | Natural-language models: anchor sentences must be reused verbatim across images; synonym rewriting forbidden (e.g. "mole" must not become "tache" or "little spot") |

### Section ⑥ — Multi-character scenes

Reference Character A/B anchors in the two-character interaction block of Composition & Shots; the spatial-relation fields must be filled — do not just write the two character names.

---

## CharacterAnchors.csv

### Adding a character / image version

- When adding a character: copy this sheet's structure.
- When adding an image version: append a row and fill in the version reference (master version, differences).
- A character may have multiple image versions (Plain-Dress Garden Version / Winter Version / Battle Version...); derived versions must reference the master version and note the differences.

---

## CompositionAndShots.csv

### Section B — Composition type reference table

Apply the sentence template; avoid writing bare "rule of thirds".

| Composition type | Applicable scenes | Description sentence template | Negative prompts | Common failures |
|---|---|---|---|---|
| Centered composition | Avatar close-up / illustration subject | [subject] centered in the frame with balanced margins | Subject off-center, edge cropping | Subject too large, filling the frame |
| Rule of thirds | Two-character interaction / scene narrative | [subject] at the left/right third of the frame, with the gaze leading to the other side | Rigid centered subject, stiff composition | Unbalanced background; subject too small |
| Leading lines | Deep scenes / roads and corridors | The road/fence/river guides the eye from near to far toward [subject] | No depth, broken perspective | Leading line cutting off the subject |
| Framing composition | Windows / doors / tree gaps / arched bridges | [subject] inside a [window frame/door frame], with the frame occluding part of the background | Frame covering the face, deformed frame | Frame too heavy, stealing the subject |
| Diagonal composition | Dynamic scenes / running / combat | [subject] distributed along the frame diagonal; the action direction aligns with the diagonal | Horizontal rigid subject, excessive imbalance | Over-tilting loses stability |
| Negative-space composition | Mood / emotion / emotional close-up | [subject] in a corner of the frame with large negative space | Full-bleed, no breathing room | Subject too small to recognize |

### Section C — Two-character interaction spatial relations (mandatory for multi-character scenes)

| Field | Description | Example |
|---|---|---|
| Character A / Character B | Reference the version tags in Character Anchors | Nanwang · Plain-Dress Garden Version / Song Jiuning · Aloof Detached Version |
| Positional relation | Left-right / front-back / encircling... | Nanwang front-left; Song Jiuning back-right |
| Height difference / distance | Relative height and spacing between the two | Song Jiuning is half a head taller; one arm's length apart |
| Gaze line | Who looks at whom and where | Song Jiuning lowers her gaze; Nanwang looks up at her |
| Interaction contact point | Holding hands / side by side / passing by... | No contact; only a meeting of gazes |
| Posture difference (new in v2.4) | Each one's standing/sitting/dynamic posture; reference the Posture-Emotion Mapping Reference Table below | Nanwang stands with a slight side turn; Song Jiuning stands upright |

### Section D — Posture-Emotion Mapping Reference Table (new in v2.4)

Fixes the v1.0 posture zone that was only empty fill-in boxes; linked to the temperament tags in Character Anchors.
Before use: check the temperament tag and weight in Character Anchors, pick the posture combination from the matching temperament row, and fill it back into the four Section A fields: Posture / Gaze / Center of gravity / Garment dynamics. Free-hand writing is forbidden.

| Temperament type | Required anchor weight | Recommended stance / seated pose | Gaze direction | Center of gravity / hand gesture | Garment dynamics suggestions | Forbidden postures | Common failure modes |
|---|---|---|---|---|---|---|---|
| Gentle, quiet, slightly timid | ≥1.3 | Standing slightly side-on or seated quietly · limbs gathered | Subtly lowered or looking at the ground · not facing the camera | Weight on one leg · hands naturally at rest or lightly clasped at the chest | Skirt drifting slightly · garment subdued · weak direction | Chest out / hands on hips / staring at the camera / large open movements | Stiff puppet-like posture · wandering gaze · overly active expression |
| Aloof, detached, restrained | ≥1.3 | Standing upright or leaning · straight body lines | Level gaze into the distance or slightly lowered · eyes not on the camera | Weight centered · hands at rest or crossed | Static or barely moving garment · as if windless | Smiles / open dynamics / lively limbs / direct gaze | Too relaxed · warm expression · body leaning visibly |
| Lively, outgoing, spirited | ≥1.0 | Light hop or forward lean or half turn · clear dynamic lines | Looking at the camera or angled with the motion | Weight shifted forward · hands pointing or swinging naturally | Skirt lifted · hair flying · hem pulled straight | Stiff attention / dull gaze / gathered limbs / blank face | Excessive movement distorting the body · unstable center of gravity |
| Dignified, solemn, grave | ≥1.5 | Sitting upright or standing straight · no slouching | Level gaze or slight downward gaze · steady unmoving eyes | Weight centered · hands clasped behind the back or on armrests | Garment static · robe hem touching the ground · windless | Slouching / looseness / fidgeting / wandering gaze | Body too stiff losing presence · head-to-body ratio off |
| Sorrowful, introverted, deep | ≥1.0 | Slightly hunched or seated low or hugging the knees | Lowered or closed eyes or side glance · avoiding direct gaze | Weight lowered · arms wrapped or face covered · limbs drawn in | Garment static · hair covering the face · dark mood | Standing tall / large open postures / bright expression | Overly curled posture making the subject unrecognizable |
| Cold, sharp, alert | ≥1.3 | Side stance or half-crouch or combat stance | Sharp direct gaze or scanning · locked eyes | Weight lowered · hand on a weapon or loosely gripped · wary | Garment taut · snapping in the wind · clear direction | Relaxed posture / soft gaze / asymmetric slouch | Stiff limbs without power · unstable center of gravity |

---

## FeatureDetails.csv

### Weight ordering rule

When adding a character/feature, append rows following Category → Feature → Description → Weight → Negative prompts → Negative weight → Syntax strategy.
Weight ordering must satisfy: **hard anchor (1.6+) > core (1.3-1.5) > baseline (1.0-1.2) > atmosphere (<1.0)**.

---

## NaturalLanguagePromptTemplate.csv

### Universal assembly priority (all models)

**Hard anchor → core features → baseline description → atmosphere elements.**
Natural-language models realize the "hard anchor" as an independent sentence-initial clause; MJ as the first 20 tokens; SD as the highest-weight tag.

---

## ModelsAndReferences.csv

### Section A — Generation config

| Field | Description | Example | Notes |
|---|---|---|---|
| Recommended model | Choose the best model by character style | Niji V6 (anime characters) | Use SDXL / Flux for realistic styles |
| Model-specific parameters | Special parameters of the model | Niji V6: --style cute --niji 6 | — |
| --ar aspect ratio | Must match the standard ratio in Composition & Shots | --ar 3:4 | Avatar 1:1 / storyboard 16:9 |
| --stylize | Artistic strength; higher drifts the features more | --s 100 (medium-low) | Use ≤100 for character consistency |
| --chaos | Composition variation; keep low when reproducibility is needed | --chaos 5 | 30-50 for exploring compositions |
| --seed | Key to locking the composition; must be recorded | Seed: 20260807 | Log it in the Generation Iteration Log |

### Section B — Reference anchoring

| Field | Description | Example | Notes |
|---|---|---|---|
| Reference image URL | Baseline image of the character | https://.../nanwang_v12.png | The closer to the target version, the better |
| --cref (MJ character reference) | Core character-consistency parameter; pair with --cw to control strength | --cref URL --cw 100 | 80-100 recommended for portraits |
| --sref (style reference) | Style consistency parameter | --sref URL | Use when the visual style drifts |
| Flux Kontext/Redux | Native reference-image solution for the natural-language flow | Flux Kontext + baseline image | Kontext for reference / Redux for variants |
| Conversational model reference | GPT-4o / Gemini upload the first image or previous version as the anchor | First image as anchor; fix via conversation | Fix failures directly in conversation |
| seed strategy | Reuse / new random | Reuse 20260807 | Reuse the seed for iterative fine-tuning |
| Upscale / fix tools | Post-generation pipeline | Upscale 2x → inpaint to fix hands | Route hand failures here |

### Section D — Parameter interaction rules

| Parameter change | Linked impact | Recommended action |
|---|---|---|
| --stylize up | More artistic but character features drift | Also raise the feature weights 0.2-0.3 |
| --ar widened | Composition spreads automatically; negative-space and subject ratio change | Add "on the left/right side" positioning to the subject words |
| --chaos up | Composition varies a lot; hard to reproduce | Keep chaos 0-5 when reproducibility is needed |
| --cw up | Stronger cref features but lower pose freedom | 80-100 for portraits; 30-50 for varied poses |
| seed fixed | Same prompt reproduces the composition | Keep the seed during iteration; tweak the prompt |

---

## NegativeWordBank.csv

### Natural-language models (Flux/DALL-E/GPT-4o/Gemini)

Do not translate the exclusions in the sheet into the prompt as "no X"; convert them into affirmative writing of the corresponding features (e.g. "red dress" → lock the dress sentence as light mint cotton).

### Assembly rules

- SD: concatenate the full list.
- MJ: pick only the 4-6 highest-weight words into `--no`.
- Natural-language models: convert to affirmative writing.

---

## AspectRatioBaselines.csv

### Supplementary rule

Head-to-body ratios must not be mixed across a character's multiple versions (teen/adult); when crossing versions, create a new image-version row in Character Anchors and note the differences.

---

## ReferenceImageCapabilityMatrix.csv

### Cross-image consistency strength ranking (weak → strong)

**DALL-E 3 < Flux < GPT-4o/Gemini (reference) < SD (LoRA) < MJ/Niji (--cref)**

Strength correlates with external anchoring tools; models with weak tools must compensate with verbatim anchor-sentence reuse.

### Usage rule

Before creating a character: fix the target model → check this sheet for its consistency method → for models without strong methods (DALL-E 3), lock them down with the P0 "anchor-description reuse" check in the Checklist.

---

## GenerationIterationLog.csv

### Stats tip

After 10+ rows, analyze horizontally — which category the failures cluster in, and which weight class to raise; three consecutive occurrences of the same problem means the current model/parameter route needs a switch.
