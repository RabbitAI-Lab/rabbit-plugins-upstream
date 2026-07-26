# Prompt Blueprints

Use these blueprints as production-ready starting points. Replace bracketed fields with concrete character details and keep locked identity traits consistent across every asset prompt.

## Prompt Module System

Every prompt must be assembled from these modules. Keep the module order stable so prompts are easy to compare and iterate.

### 1. Character Identity Module

Answer: what is this role?

```text
[Character name/codename], a [species/object/hybrid prototype] IP character for [target audience/use case], personality of [3-5 traits], designed for [commercial applications]
```

### 2. Visual Feature Module

Answer: what shapes, colors, proportions, features, limbs, and textures must remain?

```text
must preserve [signature silhouette], [head-body proportion], [face structure], [eye style], [mouth/beak/nose shape], [limb structure], [fixed color zones], [signature accessory/symbol], [body texture]
```

### 3. Style Module

Answer: what visual language is being used?

```text
[2D illustration / 3D cartoon / collectible designer toy / picture book / clean line art / mascot branding / social sticker style]
```

### 4. Composition Module

Answer: what kind of image is this?

```text
[single character render / front-side-back three-view sheet / 3x3 expression grid / character specification page / action pose sheet / packaging render / merchandise display / scene illustration / social poster]
```

### 5. Material Module

Answer: what is the surface or medium?

```text
[soft vinyl / flocked toy / plush / ceramic / paper craft / smooth 3D render / flat vector-like illustration / black-and-white line art]
```

### 6. Lighting Module

Answer: how is the image lit?

```text
[soft studio lighting / bright clean lighting / natural daylight / no harsh shadow / even product photography lighting]
```

### 7. Background Module

Answer: where does the image sit?

```text
[pure white background / light gradient background / simple scene space / studio tabletop / toy shelf display / social poster background]
```

### 8. Consistency Module

Answer: what must remain unchanged across the asset system?

```text
keep the exact same character identity, preserve all signature features, same body proportion, same facial structure, same color distribution, same silhouette
```

### 9. Negative Constraint Module

Answer: what should the model avoid?

```text
do not redesign the character, do not add complex accessories, do not change color zones, do not change proportions, do not make it realistic animal anatomy unless requested, no watermark, no unreadable text
```

## Shared Prompt Blocks

### Identity Anchor

Use the character identity module plus the visual feature module.

### Global Consistency Block

Use the consistency module.

### Negative Constraint Bank

Use only relevant constraints:

Use the negative constraint module and add asset-specific constraints when needed:

```text
avoid inconsistent proportions, avoid changing the face structure, avoid changing color zones, avoid extra limbs, avoid extra accessories, avoid busy background, avoid logo imitation, avoid copied copyrighted character, avoid multiple characters unless requested, avoid over-detailed texture that breaks toy manufacturability
```

### Three-View Source Reference Block

Use when the user attaches a base front/side/back character image:

```text
based on the provided front-side-back three-view reference image, preserve the exact character identity, silhouette, proportions, face structure, color zones, limb structure, side-view depth, and back-view details, use the attached three-view image as the primary visual reference
```

Chinese version:

```text
基于用户提供的正面、侧面、背面三视图参考图，严格保留原角色身份、轮廓比例、五官结构、颜色分区、肢体结构、侧面厚度关系和背面细节，以用户上传的三视图图片作为最高优先级视觉参考
```

## 1. Main Character Render

Purpose: establish the standard IP identity.

```text
[Character identity module], [Visual feature module], [Style module], full-body front-facing main character render, neutral standing pose, clear readable silhouette, visible facial features and signature details, [Material module], [Lighting module], clean studio background, commercial IP character design, polished but simple enough for merchandise and stickers, [Consistency module], [Negative constraint module].
```

For a base three-view image, use:

```text
[Three-view source reference block], create a cleaned standard front-facing main character render from the submitted design, neutral standing pose, clear readable silhouette, preserve the original face, body shape, color zones, limbs, and signature details, [Style module], [Material module], [Lighting module], clean studio background, polished commercial IP character image, do not redesign the character, do not add new accessories, no text, no watermark.
```

## 2. Character Three-View Sheet

Purpose: lock front/side/back structure.

```text
[Character identity module], [Visual feature module], [Style module], character three-view turnaround sheet, front view, side view, and back view aligned horizontally, same scale and same proportions across all views, neutral standing pose, clear body structure, visible accessory placement, [Material module], even clean lighting, pure white background, production-ready character reference sheet, [Consistency module], [Negative constraint module].
```

## 3. Clean Line-Art Three-View Sheet

Purpose: create a controllable outline reference.

```text
[Character identity module], [Visual feature module], clean black-and-white line-art style, clean line-art three-view turnaround sheet, front view, side view, and back view aligned horizontally, consistent proportions, clear contour lines, simplified structural details, no color fill, no complex shading, pure white background, suitable for coloring and production reference, [Consistency module], [Negative constraint module].
```

For a base three-view image, use:

```text
[Three-view source reference block], convert the submitted three-view character design into a clean black-and-white line-art three-view sheet, front view, side view, and back view aligned horizontally, preserve all original outlines and structural details, remove color and shading, keep clear contour lines, pure white background, no redesign, no new details, no text, no watermark.
```

## 4. Character Design Specification Sheet

Purpose: show the design system in one reference image.

```text
[Character identity module], [Visual feature module], [Style module], character design specification sheet, includes main full-body view, close-up face detail, signature accessory detail, color palette swatches, material texture sample, clean grid layout, [Material module], [Lighting module], white studio background, production design board style, small note areas without readable text, [Consistency module], [Negative constraint module].
```

## 5. Nine-Expression Sticker/Emote Grid

Purpose: test expression scalability and sticker potential.

```text
[Character identity module], [Visual feature module], cute commercial sticker style, nine-expression sticker sheet in a 3x3 grid, same character design and same proportions in every cell, expressions include happy, surprised, shy, angry, sleepy, crying, excited, confused, proud, clean cutout shapes, flat illustration or soft 3D sticker look as requested, even bright lighting, plain light background or transparent-background look, [Consistency module], [Negative constraint module].
```

For a base three-view image, use:

```text
[Three-view source reference block], create a 3x3 nine-expression sticker sheet using the exact same character from the submitted three-view image, only change facial expressions and small gesture energy, expressions include happy, surprised, shy, angry, sleepy, crying, excited, confused, proud, preserve body shape, face layout, color zones, limbs, and signature details in every cell, cute commercial sticker style, clean cutout shapes, plain light background, no redesign, no new accessories, no text unless requested, no watermark.
```

## 6. Common Action Pose Sheet

Purpose: explore daily reusable motion language.

```text
[Character identity module], [Visual feature module], [Style module], action pose sheet with 6 to 8 full-body poses, same character proportions and design details, poses include waving, running, jumping, holding [prop], sitting, cheering, thinking, sleeping, [Material module], bright even lighting, clean white background, dynamic but readable silhouette, production-ready pose exploration sheet, [Consistency module], [Negative constraint module].
```

For a base three-view image, use:

```text
[Three-view source reference block], create a 6 to 8 pose sheet using the exact same character from the submitted three-view image, poses include waving, running, jumping, holding [prop], sitting, cheering, thinking, sleeping, preserve the original proportions, silhouette, face structure, color zones, limbs, and signature details in every pose, dynamic but readable silhouette, clean white background, no redesign, no new accessories unless requested, no text, no watermark.
```

## 7. Daily Life Scene Illustration

Purpose: place the IP into relatable life scenarios.

```text
[Character identity module], [Visual feature module], [Style module], daily life scene illustration, character [specific everyday action] in [specific environment], warm narrative moment, [Material module or illustration medium], coherent soft lighting, background supports the story without hiding the silhouette, character remains the clear focal point, commercial IP illustration, [Consistency module], [Negative constraint module].
```

## 8. Brand/Commercial Application Scene

Purpose: show how the IP communicates for a project or business.

```text
[Character identity module], [Visual feature module], [Style module], brand/commercial application scene for [brand/project/category], character interacting with [product/space/service touchpoint], friendly communication pose, clear commercial context, [Material module or illustration medium], polished promotional lighting, clean composition, brand-safe colors, [Consistency module], no fake logo, no unreadable text, no watermark, do not redesign the character.
```

## 9. Collectible Toy Figure Render

Purpose: translate the character into a toy/figure object.

```text
[Character identity module], [Visual feature module], collectible designer toy style, collectible toy figure render, front three-quarter view, soft vinyl material, rounded simplified forms, compact toy proportions, polished surface, product photography lighting, clean studio background, optional display base if appropriate, high-end blind-box collectible presentation, [Consistency module], [Negative constraint module].
```

For a base three-view image, use:

```text
[Three-view source reference block], translate the exact submitted three-view character into a collectible designer toy figure render, front three-quarter view, preserve the original silhouette, face, color zones, limbs, side-view depth, and back-view details, soft vinyl material, rounded simplified forms, polished surface, product photography lighting, clean studio background, do not redesign the character, no extra accessories unless requested, no text, no watermark.
```

## 10. Blind-Box Or Packaging Box Render

Purpose: show retail packaging potential.

```text
[Character identity module], [Visual feature module], collectible designer toy packaging style, blind-box packaging render for the character, box standing next to the collectible figure, soft vinyl figure material, cohesive color palette based on the character, character illustration used as main packaging visual, clean modern toy packaging design, studio product photography lighting, studio tabletop background, [Consistency module], no readable brand claims unless provided, no watermark, do not change the character design.
```

## 11. Merchandise Mockup

Purpose: test whether the IP works across products.

```text
[Character identity module], [Visual feature module], mascot merchandise presentation style, merchandise mockup display, includes sticker sheet, acrylic keychain, postcard, tote bag, mug or phone case as appropriate, consistent character artwork across all items, mixed materials matching each product, clean studio tabletop lighting, clean studio tabletop background, cohesive palette, commercial product presentation, [Consistency module], no unreadable text, no watermark, do not redesign the character.
```

## 12. Social Media Key Visual/Poster

Purpose: create a launch-ready promotional image.

```text
[Character identity module], [Visual feature module], social media IP launch visual style, social media key visual poster for IP launch, character-first composition, includes avatar-style main visual, sticker preview or product teaser elements, platform-ready square or vertical layout, polished illustration or 3D render as requested, bright clean lighting, bold but clean background, cohesive visual system, [Consistency module], no unreadable text, no watermark, do not redesign the character.
```

## Style Anchor Presets

### Designer Toy / Blind Box

```text
3D cartoon character, collectible designer toy aesthetic, soft vinyl material, oversized head, compact body, rounded simplified shape, cute proportions, clean modern look, soft studio lighting, bright clean color tone, high-resolution product render
```

### Sticker / Emote

```text
clean sticker illustration, simplified outline, readable facial expression, high contrast, clear cutout edge, small-screen clarity, cute and expressive commercial sticker style
```

### Mascot Branding

```text
brand mascot design, clear silhouette, memorable symbol, limited color palette, scalable details, friendly communication posture, high recognition at small sizes
```

### Children's Illustration

```text
warm children's illustration, soft texture, friendly proportions, gentle lighting, narrative expression, approachable color palette
```

### Line Art

```text
clean black-and-white line drawing, no color, no complex shading, clear contour lines, minimal construction details, pure white background
```
