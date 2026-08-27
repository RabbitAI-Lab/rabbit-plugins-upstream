# Image consistency

## Build the visual bible

Create one reference image containing:

- neutral full-body front, side, and back views;
- face closeups with neutral and high-value expressions;
- signature clothes and accessories;
- palette and material details;
- a small environment/world inset.

Use distinct silhouette and color cues. Avoid two leads with nearly identical hair, coat, or face shape.

## Reference hierarchy

For every shot:

1. Use the visual bible as the identity reference.
2. Use an approved environment frame when location continuity matters.
3. Use the previous shot only as a pose/composition reference.

Never rely only on the immediately previous generated frame. Small deviations compound across a chain.

Label input roles in the image prompt:

```text
Input images:
- Image 1: identity and wardrobe source of truth.
- Image 2: environment and lighting reference only.
- Image 3: pose continuity reference only.
```

## Prompt skeleton

```text
Use case: illustration-story
Asset type: vertical 9:16 motion-comic keyframe
Primary request: <single story moment>
Input images: <labeled roles>
Subject: <named characters with locked visual traits>
Scene/backdrop: <location and continuity details>
Style/medium: <series art direction>
Composition/framing: <shot size, focal subject, caption-safe area>
Lighting/mood: <series palette plus local change>
Constraints: preserve exact identities, wardrobe, proportions, and signature props
Avoid: text, captions, speech bubbles, logos, watermarks, duplicate people, extra fingers
```

## Review

Inspect at full size. Reject or correct:

- changed hairstyle, age, facial proportions, or clothing;
- missing signature accessory;
- duplicate or fused people;
- wrong hand count;
- changed bottle, weapon, photo, or other story-critical prop;
- accidental letters;
- focal face placed beneath planned captions.

When a shot fails, return to the visual bible and correct one issue at a time.

