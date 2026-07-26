# Three-View Source Workflow

Use this reference when the user submits a base three-view image and asks for a complete IP asset package. The submitted three-view is the source of truth, not a loose inspiration image.

## Core Principle

Do not redesign the character. Extract the character bible from the provided front/side/back views, then expand the same character into new image assets.

## Step 1: Diagnose The Source Image

Identify:

- Whether the image contains front, side, and back views.
- Whether the views are aligned and consistent.
- Whether colors, limbs, accessories, and proportions match across views.
- Whether any hidden back-view details must be preserved.
- Whether any details are unclear and need either assumption or user confirmation.

Ask at most 2 questions only if missing details would block production. Otherwise make assumptions and label them.

## Step 2: Extract View-Specific Anchors

### Front View Anchors

Capture:

- Head/body ratio
- Face layout
- Eye shape and eye position
- Mouth, beak, nose, or muzzle shape
- Front silhouette
- Main color zones
- Front-facing accessories
- Arm, wing, hand, or paw placement
- Leg and foot structure

### Side View Anchors

Capture:

- Body depth
- Forehead, nose, beak, mouth, or muzzle projection
- Belly contour
- Back contour
- Arm, wing, or accessory side placement
- Leg angle and foot length
- Tail or rear detail visibility

### Back View Anchors

Capture:

- Rear silhouette
- Back color zones
- Tail, leaf, hood, strap, shell, or other rear elements
- Rear accessory placement
- Back-of-head or back-of-body structure
- Any detail that must appear in toy renders and packaging turns

## Step 3: Convert Into A Locked Character Bible

Write a short character bible:

- Temporary IP name
- Prototype/species/object hybrid
- Personality inferred from shape language
- Target use cases
- Locked silhouette
- Locked face structure
- Locked color distribution
- Locked limb structure
- Locked back-view details
- Allowed optimization variables

If the user provides no personality or commercial direction, infer it from the visual language and mark it as an assumption.

## Step 4: Generate Image-To-Image Prompt Modules

Every prompt should assume the base three-view image is attached as a visual reference.

Use this source-reference module:

```text
based on the provided front-side-back three-view reference image, preserve the exact character identity, silhouette, proportions, face structure, color zones, limb structure, side-view depth, and back-view details
```

Use this Chinese source-reference module:

```text
基于用户提供的正面、侧面、背面三视图参考图，严格保留原角色身份、轮廓比例、五官结构、颜色分区、肢体结构、侧面厚度关系和背面细节
```

## Step 5: Asset Expansion Logic

For three-view input, the asset sequence changes slightly:

1. **Source audit and anchor extraction**: describe what must remain.
2. **Cleaned standard reference prompt**: improve clarity without redesign.
3. **Line-art three-view prompt**: trace and simplify the existing design.
4. **Character specification sheet prompt**: convert extracted anchors into a production board.
5. **Expression grid prompt**: change only expression, not structure.
6. **Pose sheet prompt**: change only pose, preserve proportions.
7. **Daily scene prompt**: put the same character into life context.
8. **Commercial scene prompt**: put the same character into brand/project context.
9. **Toy figure render prompt**: translate the same design into 3D collectible material.
10. **Packaging render prompt**: use the same character and source palette.
11. **Merchandise mockup prompt**: apply the same character art to products.
12. **Social key visual prompt**: create launch visual without redesign.

## Three-View Source Prompt Additions

Add these lines to asset prompts when a reference image is attached:

```text
use the attached three-view image as the primary visual reference
do not invent a new character
do not change the body shape, face, color layout, limbs, or back-view details
only change the requested asset type, expression, pose, scene, material, or layout
```

Chinese version:

```text
以用户上传的三视图图片作为最高优先级视觉参考
不要重新设计角色
不要改变身体形状、五官、颜色分区、肢体结构或背面细节
只改变当前资产所要求的表情、动作、场景、材质或版式
```

## Reference Strength Guidance

When the image-generation tool supports reference strength:

- **Cleaned reference, line art, specification sheet**: use high or medium-high reference strength.
- **Expression grid and pose sheet**: use medium-high reference strength.
- **Toy figure render**: use medium reference strength with strong textual identity anchors.
- **Scene, packaging, merchandise, social visual**: use medium reference strength so layout can change while identity stays locked.

## Three-View Output Format

Use this output structure:

1. Three-view source diagnosis
2. Front-view anchors
3. Side-view anchors
4. Back-view anchors
5. Locked character bible
6. Allowed optimization variables
7. Global style and consistency rules
8. Image asset matrix
9. Image-to-image prompt set
10. Negative prompt rules
11. Consistency checklist against the original three-view
12. Suggested generation order
