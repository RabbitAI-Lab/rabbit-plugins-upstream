---
name: ai-drawing-composition-template
slug: ai-drawing-composition-template
displayName: AI Drawing Composition Template
description: Build high-consistency AI character prompts across five model syntax families (natural-language / conversational / MJ-Niji / SD / domestic API) and multi-format outputs (image / storyboard / comic panel / video / 3D) using a weight & ratio precision-control workbench. Ships character-anchor sheets, composition & shots references, posture-emotion mapping, reference-image capability matrix, multi-character spatial relations, storyboard/panel layout rules, speech-bubble positioning, LoRA management, temporal-consistency checklist, 3D generation matrix, video prompt template, conversational edit chain, negative-word bank, and a P0/P1/P2 validation checklist.
version: 2.6.0
metadata:
  openclaw:
    requires: {}
    homepage: "https://github.com/nohn3043-arch/ai-draw-cue-word-project"
---

# AI Drawing Composition Template (ai-draw-cue-word-project)

A quality-control workbench for generating character prompts that stay consistent
across models and across a series of images. The setting layer (anchors, composition,
validation) is model-agnostic; the syntax layer is adapted per model family.

## When to use

Use this skill when the user needs to generate or refine an AI image prompt for a
character — especially when consistency across multiple images or across different
models matters (illustrations, storyboards, character cards, series).

## Workflow (run through once per generation)

1. **Character anchors** — read `references/CharacterAnchors.csv`. Pick or create an
   image version row: identity anchor (≥1.6), temperament tag (≥1.3), palette,
   signature props, negative anchoring.
2. **Composition & shots** — read `references/CompositionAndShots.csv`. Fill the
   Section A config (aspect ratio, composition type, camera angle, shot scale, focal
   length, lighting, layers, occlusion). Choose composition type from the
   Composition Type Reference table in `references/NOTES.md` (Section B).
   Look up posture by temperament in the Posture-Emotion Mapping table
   (`references/NOTES.md` Section D) — never free-hand it.
3. **Model & reference strategy** — read `references/ReferenceImageCapabilityMatrix.csv`
   to pick the model's consistency method (`--cref`, LoRA, native reference, or
   verbatim anchor reuse for DALL-E 3). For series work, follow the
   **reference-first workflow** in `references/ReferenceFirstWorkflow.md` (P0).
4. **Assemble the prompt** — read `references/NaturalLanguagePromptTemplate.csv` for
   the syntax of the target family (see the five rows below).
5. **Validate** — run the P0/P1/P2 checks in `references/Checklist.csv`. Any P0
   failure (identity anchor, core features, anchor-description reuse, negative
   coverage) means regenerate.
6. **Batch production** — for series / production runs, follow the pipeline in
   `references/ProductionPipeline.md` (P0): 12-image pre-flight, drift labels,
   retry rules, versioned reference pack.

## Five syntax families

| Family | Key rules |
|---|---|
| Natural language (Flux / DALL-E 3 / SD3) | Full English paragraph: scene+shot → anchors → posture → lighting → background. No weight brackets, no plus signs. Anchor sentences first, verbatim across images. |
| Conversational (GPT-4o / Gemini 2.5 Flash Image) | Complete description in round 1, then single-point fixes in conversation. Never change anchor sentences. First image acts as the native reference. |
| MJ / Niji | Core anchors in the first 20 tokens; CLI params appended at the end (`--ar`, `--cref`, `--cw`, `--s`, `--niji`). `--no` filters only 4-6 highest-risk words. |
| Stable Diffusion 1.5 / XL / SD3 | Comma-separated tags: identity anchors (1.5+) → core features (1.3-1.5) → posture/composition → lighting (0.7-0.9). Use `(tag:weight)`. Separate Negative Prompt box. |
| Domestic API (Jimeng / Kling / Doubao / Tongyi Wanxiang) | Chinese natural-language paragraph + API params (aspect_ratio / size). Negative-word and reference-image support vary per vendor — follow official docs. |

## Weight semantics (SD/MJ numeric baseline)

| Weight | Meaning |
|---|---|
| 1.6-2.0 | Hard anchor — absolutely immutable, force-kept in every scene |
| 1.3-1.5 | Core feature — kept in all scenes, validated as P0 |
| 1.0-1.2 | Baseline — default strength, fluctuate ≤0.2 |
| 0.7-0.9 | Atmosphere — adjustable per scene |
| <0.7 | Weak prompt — atmosphere only, never carries key info |

## v2.6 multi-format outputs (image / storyboard / comic panel / video / 3D)

Beyond single-image generation, v2.6 adds sheets for serialized and cross-modal work:

| Output | Key sheet | Rules |
|---|---|---|
| Multi-character scenes | `references/MultiCharacterSpatialRelations.csv` | Subject size hierarchy, occlusion, gaze direction, relative positioning anchors |
| Comic panels / pages | `references/PanelLayoutRules.csv`, `references/SpeechBubblePositioning.csv` | Panel grid baselines, gutter rules, bubble placement by speech type |
| Storyboard sequences | `references/StoryboardSkeletonTemplate.csv`, `references/TemporalConsistencyChecklist.csv` | Shot-to-shot continuity: anchor reuse, lighting/wardrobe lock, jump-cut avoidance |
| Conversational iterative editing (GPT-4o / Gemini) | `references/ConversationalEditChain.csv` | Single-point edits only, anchor sentences frozen, edit log structure |
| LoRA management | `references/LoRAManagement.csv` | Trigger tokens, weight baselines, version pins, conflict detection |
| Video generation | `references/VideoGenerationPromptTemplate.csv` | Motion verbs, camera trajectory, duration baselines per model family |
| 3D generation | `references/ThreeDGenerationMatrix.csv` | Model-specific syntax for 3D asset outputs (Turntable / orthographic / mesh) |

## Cross-model red lines

- `(word:1.3)` works only on SD; MJ uses token position; natural-language models
  forbid bracket weights.
- MJ `--no` ≤ 4-6 short words; SD has a Negative Prompt box; natural-language and
  domestic API models rely on affirmative writing first, negation as fallback.
- Anchor sentences must be reused verbatim — synonym rewriting breaks consistency.
- **DALL-E 3 is deprecated (v2.5)**: no reference-image support; for series or
  consistency-critical scenes, route to a conversational model (GPT-4o / Gemini)
  instead of compensating with description only.
- **Reference-first (v2.5)**: for any multi-image series, prepare a reference pack
  and follow `references/ReferenceFirstWorkflow.md`; text anchors are the second
  layer of defense, never the first.

## Files

- `references/*.csv` — the 21 workbench sheets (flat tables):
  - Core (v2.5 baseline): `CharacterAnchors`, `CompositionAndShots`, `AspectRatioBaselines`, `FeatureDetails`, `ModelsAndReferences`, `ReferenceImageCapabilityMatrix`, `NaturalLanguagePromptTemplate`, `NegativeWordBank`, `Checklist` (P0/P1/P2), `Usage`, `ChangeLog`, `GenerationIterationLog`
  - Multi-format (v2.6): `ConversationalEditChain`, `LoRAManagement`, `MultiCharacterSpatialRelations`, `PanelLayoutRules`, `SpeechBubblePositioning`, `StoryboardSkeletonTemplate`, `TemporalConsistencyChecklist`, `ThreeDGenerationMatrix`, `VideoGenerationPromptTemplate`
- `references/NOTES.md` — supplementary tables & rules (composition types B,
  two-character interaction C, posture-emotion mapping D, weight semantics,
  narrative-intensity mapping, parameter interaction rules, strength ranking)
- `references/ReferenceFirstWorkflow.md` — P0 reference-first workflow (v2.5):
  decision rule, reference-pack quality gates, per-model methods, two-layer defense
- `references/ProductionPipeline.md` — P0 production pipeline (v2.5): 12-image
  pre-flight, drift labels, retry rules, versioned reference pack
- `examples/nanwang_spring_garden_prompt.md` — finished prompts in four syntax
  flows for the example character Nanwang

## Source

Version-controlled at github.com/nohn3043-arch/ai-draw-cue-word-project (also
SourceForge `p/ai-draw-cue-word-project` and Gitee `nohn-ecosystem/aidraw`).
Apache-2.0. Copyright (c) 2026 NOHN AI TECHNOLOGY PTE LTD.
