# Production Checklist

Use this checklist to review an IP image system before delivery, image generation, or iteration.

## Locked Identity Traits

Define and preserve:

- Name or codename
- Species/object/hybrid prototype
- Core silhouette
- Head-body proportion
- Face layout
- Eye style
- Mouth/beak/nose shape
- Limb structure
- Main color zones
- Signature accessory or symbol
- Material/texture direction
- Personality keywords
- Commercial use cases

## Allowed Iteration Variables

Vary deliberately:

- Expression
- Pose
- Scene
- Prop
- Outfit variant
- Seasonal theme
- Packaging composition
- Merchandise category
- Rendering medium, if the asset type requires it

Do not vary these unless the user explicitly wants redesign exploration:

- Species/object base
- Signature silhouette
- Face layout
- Main color distribution
- Main accessory
- Overall proportion system
- Front/side/back structure

## 12-Asset Delivery Checklist

For a complete image package, deliver:

- Main character render prompt
- Character three-view prompt
- Clean line-art three-view prompt
- Character design specification sheet prompt
- Nine-expression sticker/emote grid prompt
- Common action pose sheet prompt
- Daily life scene illustration prompt
- Brand/commercial application scene prompt
- Collectible toy figure render prompt
- Blind-box or packaging box render prompt
- Merchandise mockup prompt
- Social media key visual/poster prompt

## Quality Review Questions

Check every prompt and generated output:

- Is the silhouette consistent?
- Are the eyes consistent?
- Is the mouth, beak, or nose shape consistent?
- Are color zones unchanged?
- Are limbs and proportions unchanged?
- Does the side view match the front view?
- Does the back view preserve hidden details?
- Is the style consistent across all images?
- Is the asset useful for real IP production?
- Are optional variants clearly separated from locked identity traits?
- Does the toy/merch version preserve the character instead of redesigning it?
- Does the prompt avoid copying a protected character or brand style directly?

For a submitted base three-view image, also check:

- Did the output preserve the submitted front-view face?
- Did the output preserve the submitted side-view depth and contour?
- Did the output preserve the submitted back-view details?
- Did the output avoid creating a new character identity?
- Did the output only change the requested asset type, expression, pose, scene, material, or layout?
- Would a viewer recognize the generated image as the same character from the source three-view?

## Suggested Generation Order

1. Generate 3-6 main character render candidates.
2. Select one candidate and lock identity traits.
3. Generate the character three-view sheet.
4. Generate clean line-art three-view sheet.
5. Generate character design specification sheet.
6. Generate expression grid and pose sheet.
7. Generate daily life and commercial application scenes.
8. Generate collectible figure, packaging, merchandise, and social media visuals.
9. Review drift and regenerate weak assets using stricter locked traits.

## Suggested Generation Order From A Base Three-View Image

1. Audit the submitted three-view and extract front/side/back anchors.
2. Create a cleaned standard reference image if the source needs polish.
3. Generate line-art three-view from the source.
4. Generate character design specification sheet.
5. Generate expression grid and pose sheet with medium-high reference strength.
6. Generate toy figure render with medium reference strength plus strong text anchors.
7. Generate scene, packaging, merchandise, and social visuals.
8. Compare every output against the original three-view and tighten prompts where drift appears.

## Client-Facing Delivery Language

Use concise production wording:

```text
This IP image system is organized around a locked character identity, a reusable visual anchor system, and a staged image asset matrix. The first stage establishes the master character image; the second stage creates technical consistency references; the third stage expands into expressions, poses, scenes, collectible figure renders, packaging, merchandise, and social launch visuals.
```
