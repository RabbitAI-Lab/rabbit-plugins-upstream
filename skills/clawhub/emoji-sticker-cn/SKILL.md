---
name: emoji-sticker-cn
version: 3.1.3
description: Designs three emoji sticker concepts from a user-provided theme, phrase, or character. Invoke only when the user explicitly asks to design emoji stickers or a sticker pack.
---

# Emoji Sticker Concept Designer

## Purpose

Turn a theme, short phrase, or character supplied by the user into exactly three distinct emoji sticker concepts. Provide design-ready text descriptions and copyable generation prompts only.

The `-cn` suffix is a legacy identifier, not a locale restriction. Use the caption language explicitly selected in the current request; if no caption language is given, ask the user to choose before drafting.

## Trigger Policy

Invoke this skill only when all of the following are true:

1. The user explicitly asks to design, create concepts for, or plan an emoji sticker or sticker pack.
2. The request is based on a theme, short phrase, or character supplied by the user.
3. The requested result can be satisfied with written sticker concepts.

Do not infer sticker-design intent from a general mention of emojis, reactions, illustrations, characters, or chat messages.

## Positive Trigger Examples

- “Design an emoji sticker pack around my sleepy orange-cat character.”
- “Create sticker concepts for the phrase ‘On my way!’”
- “Based on my theme ‘Monday office survival,’ give me three emoji sticker designs.”
- “Turn this character description into an emoji sticker set: a shy green dinosaur with round glasses.”

## Non-Trigger Examples

- “What does this emoji mean?”
- “Add emojis to this announcement.”
- “Translate these sticker captions into English.”
- “Generate and export a PNG sticker pack.”
- “Publish these stickers to a messaging platform.”
- “Find popular sticker packs online.”
- “Create a mascot logo.”
- “Write dialogue for my comic character.”

## Required Output

Return exactly three sticker proposals. Each proposal must include:

1. **Caption** — the short text shown on or associated with the sticker.
2. **Expression and Pose** — facial expression, gesture, body language, and emotional intensity.
3. **Composition** — subject placement, crop, visual hierarchy, background treatment, and text placement.
4. **Color Palette** — principal colors and their intended balance or contrast.
5. **Outline** — border color, thickness, edge treatment, and any cutline-friendly guidance.
6. **Copyable Generation Prompt** — one self-contained prompt that restates the relevant user-provided subject and all essential visual directions.

Use this structure:

```text
## Sticker 1 — [Concept title]
- Caption:
- Expression and Pose:
- Composition:
- Color Palette:
- Outline:
- Copyable Generation Prompt:

## Sticker 2 — [Concept title]
- Caption:
- Expression and Pose:
- Composition:
- Color Palette:
- Outline:
- Copyable Generation Prompt:

## Sticker 3 — [Concept title]
- Caption:
- Expression and Pose:
- Composition:
- Color Palette:
- Outline:
- Copyable Generation Prompt:
```

## Design Rules

- Preserve the user's supplied theme, phrase, or character identity.
- Make the three proposals visibly different in emotion, pose, or composition.
- Keep captions brief and legible at sticker scale.
- Favor a clear silhouette, expressive face, compact composition, and strong foreground-background separation.
- Describe transparent or simple backgrounds when useful, without claiming that an asset has been generated.
- Do not introduce copyrighted characters, brand marks, or identifiable public figures unless the user supplied them; if supplied, describe the concept without claiming authorization.

## Scope

Return written sticker concepts based on the current request and ordinary design knowledge. State clearly that the generation prompts are drafts for later use.
