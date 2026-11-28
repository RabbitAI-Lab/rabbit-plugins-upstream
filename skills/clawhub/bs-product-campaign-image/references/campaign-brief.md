# Campaign image brief

Complete this brief before writing the generation prompt.

## Campaign decision

- Placement and exact dimensions:
- Audience and viewing context:
- Single conversion action:
- Single message or approved claim:
- Exact on-image copy, or `none`:

## Product identity lock

- Reference image roles:
- Silhouette and proportions:
- Materials and finish:
- Color and label boundary:
- Controls, cap, seams, and distinctive details:
- Details that are hidden or uncertain:
- Elements that must remain pixel-accurate:

## Art direction

- Scene and props:
- Camera angle and lens feel:
- Lighting and mood:
- Palette and contrast:
- Product box in normalized coordinates:
- Copy-safe box in normalized coordinates:
- CTA-safe box in normalized coordinates:
- Crop-safe core for alternate ratios:

## Prompt pattern

Write the final prompt in this order:

1. State the intended campaign asset and the real product shown in reference image 1.
2. Lock product geometry, material, label boundary, color, and all identity-critical details.
3. Describe the environment, action, props, camera, lighting, and surface behavior.
4. Describe product placement and the exact copy-safe and crop-safe regions.
5. Quote approved text only when it must be rendered in the image.
6. End with explicit exclusions: no unapproved marks, no extra products, no changed controls, no watermark, and no invented claims.

For an edit request, include: "Change only the environment and requested campaign treatment. Preserve the product silhouette, proportions, material, color, cap, controls, label geometry, and visible product details from reference image 1."

