---
name: ip-character-image-system
description: Use this skill when the user has an IP idea, sketch, reference image, base three-view image, character concept, mascot brief, toy figure concept, brand/project need, or story setting and wants to automatically break it into a complete image asset production plan with stable, reusable, iterable prompts for each image type. Use for IP character design, character visual systems, base three-view image extraction, three-view-to-asset expansion, line-art turnarounds, expression packs, pose sheets, collectible toy renders, packaging/merchandise mockups, social launch visuals, and full prompt systems. Do not use for unrelated general poster, logo, UI, presentation, layout, or non-character image editing tasks.
---

# IP Character Image System

## Core Goal

When a user has an IP idea, sketch, base three-view image, or character concept, automatically break it into a complete image asset production plan and generate stable, reusable, iterable prompts for each image type.

Transform a rough IP idea, text concept, sketch, base three-view image, reference image, or brand need into a complete character image asset system that is repeatable, iterable, and deliverable.

Act like an IP image development director, prompt engineer, and visual producer. Prioritize a structured production pipeline over a single impressive prompt.

## Operating Principle

Always prioritize character consistency over visual novelty. For an IP system, the same identity must survive across master image, three-view sheet, line art, expressions, poses, scenes, toy renders, packaging, merchandise, and social visuals.

When the user works in Chinese, output Chinese by default. Add English prompt variants only when useful for image-generation models or when requested.

## 7-Step Workflow

### Step 1: Identify the Input Type

Classify the user's input:

1. **Pure idea**: a short concept without visual references, such as "I want to make a watermelon IP".
2. **Text setting**: a written personality, story, or role, such as "a socially anxious but warm-hearted city monster".
3. **Sketch or reference image**: an existing visual basis that must be preserved.
4. **Base three-view image**: an existing front/side/back character sheet that should become the locked source of truth for all later assets.
5. **Brand or commercial project**: a project that needs a mascot/IP figure for communication, product, space, or campaign use.

Then decide whether the task has an existing visual basis or needs to be inferred from zero.

If a sketch/reference image exists, preserve defining details unless the user explicitly asks for redesign. If a base three-view image exists, treat it as the highest-priority source of truth for silhouette, proportions, structure, color zones, face, limbs, and back-view details. If no visual basis exists, infer a coherent character direction and label important assumptions.

### Step 2: Extract the Character Core

Summarize the character using:

- IP name or temporary codename
- Species, object prototype, or hybrid logic
- Core personality
- Target audience
- Emotional value
- Commercial use cases
- Visual memory points
- Must-keep design elements
- Elements that can be optimized or varied

If information is missing, make reasonable assumptions and mark them clearly.

### Step 3: Build the Visual Anchor System

Define the non-negotiable elements that keep the IP recognizable:

- Silhouette
- Head/body ratio
- Eyes
- Mouth, beak, nose, or other face structure
- Limbs
- Body texture
- Color zones
- Signature accessories or symbols
- Front/side/back structural consistency
- Material style
- Emotional expression range

For reference-image-based work, list exact features that must remain unchanged. Example visual anchors for a scallion-duck character: white scallion body, green scallion leaves on top, yellow duck beak, round eyes, small wings, thin long legs, yellow webbed feet, small back tail, and consistent front/side/back structure.

For base-three-view work, extract anchors from each view:

- **Front view**: face layout, body width, symmetry, main color blocks, front accessories.
- **Side view**: depth, beak/nose/mouth projection, belly/back contour, arm/wing placement, leg angle.
- **Back view**: back silhouette, tail/back accessory, rear color blocks, hidden structural details.

When generating new assets from a base three-view image, do not create a new master design first. Instead, lock the design from the submitted three-view sheet, then expand it into expressions, poses, scenes, toy renders, packaging, merchandise, and social visuals.

### Step 4: Choose the Image Asset Matrix

Unless the user asks for a smaller scope, generate a 12-part asset matrix:

1. Main character render
2. Character three-view sheet
3. Clean line-art three-view sheet
4. Character design specification sheet
5. Nine-expression sticker/emote grid
6. Common action pose sheet
7. Daily life scene illustration
8. Brand/commercial application scene
9. Collectible toy figure render
10. Blind-box or packaging box render
11. Merchandise mockup
12. Social media key visual/poster

For each asset, define purpose, composition, required consistency anchors, and expected output.

### Step 5: Define Global Style Rules

Create a shared style guide that applies to every prompt:

- Image style
- Rendering style
- Color palette
- Lighting
- Background
- Camera angle
- Texture
- Material
- Mood
- Quality level
- Forbidden changes

Use consistency phrases across prompts:

- Keep the exact same character identity
- Preserve all signature features
- Same body proportion
- Same facial structure
- Same color distribution
- Same silhouette
- No extra accessories unless requested
- Clean white background for design sheets

When the user names a living brand, platform, toy company, artist, or copyrighted property as a style reference, translate it into descriptive visual traits instead of instructing direct imitation.

### Step 6: Generate Modular Prompts

For each image asset, output a separate prompt. Do not provide only one large all-purpose prompt.

For each asset, include:

- Purpose
- Chinese prompt
- Optional English prompt when useful
- Key consistency notes
- Negative prompt / avoid list

Build every prompt from these modules:

1. **Character identity module**: what the role is.
2. **Visual feature module**: must-keep shapes, colors, proportions, facial features, limbs, and textures.
3. **Style module**: 2D, 3D, toy figure, picture book, line art, designer toy, mascot, or another chosen direction.
4. **Composition module**: single character, three-view sheet, nine-grid, specification page, packaging render, merchandise display, or scene.
5. **Material module**: soft vinyl, flocked toy, plush, ceramic, paper craft, illustration line art, or another material system.
6. **Lighting module**: soft studio light, natural light, no harsh shadow, bright clean light, or asset-specific lighting.
7. **Background module**: pure white, light gradient, scene space, shelf display, studio tabletop, or social poster background.
8. **Consistency module**: keep the same character identity, proportion, silhouette, facial structure, and color distribution.
9. **Negative constraint module**: do not redesign the character, do not add complex accessories, do not make it realistic animal anatomy unless requested.

Use this assembled prompt structure:

```text
[character identity module], [visual feature module], [style module], [composition module], [material module], [lighting module], [background module], [consistency module], [negative constraint module]
```

Write concrete visual descriptions. Avoid vague phrases such as "beautiful", "interesting", "high quality only", or "make it better". Prefer phrases such as "soft vinyl toy material", "rounded simplified limbs", "front, side, and back views aligned horizontally", "pure white studio background", "clean black line art", "no shading", "consistent silhouette", and "same character proportions".

### Step 7: Output the Quality Control Checklist

End with a checklist that helps the user judge whether generated images have drifted:

- Is the silhouette consistent?
- Are the eyes consistent?
- Is the mouth/beak/nose shape consistent?
- Are color zones unchanged?
- Are limbs and proportions unchanged?
- Does the side view match the front view?
- Does the back view preserve hidden details?
- Is the style consistent across all images?
- Is each image useful for IP production?
- Are optional variants clearly separated from locked identity traits?

## Output Format

Use this structure for a full IP image-system request:

1. IP concept summary
2. Input type judgment
3. Character core
4. Must-keep visual anchors
5. Global style rules
6. Full image asset matrix
7. Prompt set for each asset
8. Negative prompt rules
9. Consistency checklist
10. Suggested next iteration

For a submitted base three-view image, use this structure:

1. Three-view source diagnosis
2. Extracted front/side/back visual anchors
3. Locked identity traits
4. Optional optimization suggestions
5. Global style rules
6. Full image asset matrix based on the submitted three-view
7. Image-to-image prompt set for each asset
8. Negative prompt rules
9. Consistency checklist against the original three-view
10. Suggested generation order

For smaller requests, keep the same logic but output only the relevant sections.

## Handling Existing Sketches Or Images

When the user provides an image:

- Do not invent a new character unless asked.
- Preserve body shape, facial features, limbs, colors, distinctive details, and front/side/back logic.
- Translate the character into the requested style without changing its identity.
- For line art, remove color and shading while preserving outlines and structural details.
- For toy figure renders, translate texture into soft 3D vinyl form while preserving character identity.
- If improving the design, separate "locked features" from "optimization suggestions".

When the user provides a base three-view image:

- Treat the three-view image as the character bible.
- Extract front, side, and back details separately before writing prompts.
- Preserve the front-facing face and color zones across expressions and poses.
- Preserve side-view depth and limb placement when creating pose sheets or toy renders.
- Preserve back-view details for packaging turns, figure renders, and specification sheets.
- Use image-reference wording such as "based on the provided three-view reference image" and "preserve the exact character structure from the reference".
- Output prompts that expect the submitted image to be attached as the visual reference in the image-generation tool.
- If a model supports image strength/reference strength, recommend medium-high reference strength for identity assets and medium reference strength for scenes/merchandise.

## Default Style Presets

When the user says "Pop Mart style", "blind box toy style", or similar, describe the style as:

- 3D cartoon character
- Collectible designer toy
- Soft vinyl material
- Rounded simplified shape
- Cute proportions
- Clean modern look
- Soft studio lighting
- Bright clean color tone
- Pure white or studio background
- High-resolution product render

When the user says "line art", describe the style as:

- Clean black-and-white line drawing
- No color
- No complex shading
- Clear contour lines
- Minimal construction details
- Front, side, and back views when relevant
- Character design sheet layout
- Pure white background

## Reference Files

Read [prompt-blueprints.md](references/prompt-blueprints.md) when generating the full 12-part prompt suite or a specific asset prompt.

Read [three-view-source-workflow.md](references/three-view-source-workflow.md) when the user submits a base front/side/back character image and wants to expand it into a complete IP asset package.

Read [production-checklist.md](references/production-checklist.md) when reviewing generated results, preparing client-facing deliverables, or planning the next iteration.
