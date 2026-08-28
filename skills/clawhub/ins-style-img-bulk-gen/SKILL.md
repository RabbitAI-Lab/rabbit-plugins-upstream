---
name: ins-style-img-bulk-gen
description: Generate batches of Instagram-aesthetic photos (INS-style / Xiaohongshu / lifestyle flat-lay) by randomly composing prompts from an 80+ element library, then dispatching them in parallel to image generation skills and archiving to ~/Download/ins-image-{timestamp}/. Use when the user wants bulk INS-style images, lifestyle flat-lays, Xiaohongshu or WeChat cover art, or scene-based marketing visuals — even if they don't say 'Instagram' explicitly.
allowed-tools: Read, Bash
---

## Task

1. Read `./references/ins-style-elements.md` to understand the available element library
2. Compose prompts. Default to **5 prompts** if the user doesn't specify a count. Each prompt randomly draws **12 elements** (1-2 per category, no duplicates within a prompt)
3. Iterate the prompt queue and dispatch them **in parallel** to whichever image generation skill is available (recommended: `wanx-img` or `huny-img`)
4. Save all generated images to `~/Download/ins-image-{timestamp}/`

## Prompt Skeleton

Fill each prompt using the following template:

```
[Subject scene, 3-4 sentences, incorporating elements 1-12]. Unified Morandi / cream / wood-tone palette. 3:4 aspect ratio. Relaxed INS aesthetic.
```

## Gotchas

- **Must return to this flow** ⚠️: The image generation skill is only a sub-step. After generation completes, return to this skill and execute step 4 (archiving). Do not leave control inside the sub-skill.
- **Avoid duplicate elements**: Don't repeat the same element within one prompt (e.g. "vintage book stack" + "open book").
- **Sub-skill failures**: Skip the failed prompt and continue with the remaining queue. Don't abort the entire batch.