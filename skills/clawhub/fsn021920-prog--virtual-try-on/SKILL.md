---
name: virtual-try-on
description: Virtual try-on prompt workflow. Takes a person photo and a clothing photo and produces a realistic try-on image. Face stays the same (no face swap), clothes look worn rather than pasted on, edges blend. Covers three garment types: tops, pants, dresses. Use when the user says try on clothes, virtual try-on, see how this looks on me, or put this outfit on this person.
---

# Virtual Try-On

Prompt workflow for AI try-on images. The user supplies photos. The agent's existing image generator does the render. This skill covers the part people get wrong: face lock, garment fit, and edge blend.

This skill does not call a paid API by itself.

## Rights and AIGC (read before every run)

1. **Likeness.** Only use a person photo the user owns or has written permission to use. Do not try garments on a celebrity, influencer, or any third party without that person's consent.
2. **Garment photo.** Use product shots or photos the user has rights to. Do not scrape brand lookbooks.
3. **Output is synthetic.** Label the result as AI-generated. Do not present it as a real photo, a real photoshoot, or an endorsement by the person in the reference.
4. **No identity misuse.** Do not generate try-ons for impersonation, fake ads, or deepfake-style face swap.

If any of the above is missing, stop and ask. Do not generate.

## Backends

Works with whatever image tool the agent already has (ChatGPT, Qwen, Doubao, Jimeng, fal, Replicate, or an MCP image server). If there is no image tool, write the prompt and stop.

## Core rules

1. The face does not change: same features, skin tone, hair, expression.
2. Clothes are worn, not pasted: wrinkles follow the body, lighting matches the photo, fabric reads as real.
3. Edges blend: collar, cuffs, and hem have no cutout outline.
4. Face and fit first. Polish later.

## Workflow

### 1. Read both photos

Person photo: age range, presentation, hairstyle, hair color, skin tone, facial features, pose, arm position, body direction, light direction (hard/soft, warm/cool). Headshot → invent a normal healthy body. Half-body → extend naturally. Full-body → keep the original body. Default output is full-body unless the user asks otherwise.

Clothing photo: type (top / pants / dress), precise color, material, neckline, sleeve length, fit, pattern, flat-lay vs worn.

State what was understood before generating.

### 2. Generate

Universal prompt core:

```
Keep the person's face exactly as in the reference: same features, skin tone, hairstyle, and expression.
The garment must look worn: shoulders align, waist follows the body, sleeves track the arms.
Natural wrinkles and shadows consistent with the photo's lighting.
Fabric texture is visible; collar, cuffs, and hem blend softly into the body.
Photorealistic, high detail. AI-generated try-on, not a real photograph.
```

Category templates (this public skill covers only these three):

- **Tops:** shoulder and sleeve structure; hem at the right length; neckline sits on the collarbone.
- **Pants:** waistband follows the waist; legs drape; hem length matches intent; no warped knees.
- **Dresses:** bodice fits without pulling; skirt has fabric weight; straps and sleeves stay aligned.

Negative prompt: face swap, deformed face, sticker-like clothing, mismatched lighting, low quality, celebrity likeness, brand logo invention.

Generate one image, then check it.

### 3. Check

- Face: eyes, nose, mouth, face shape, skin tone, hair, expression match. No plastic skin.
- Fit: shoulders, waist, sleeves follow pose. Nothing floating.
- Edges: no hard seam at collar, cuffs, or hem.
- Lighting: shadows agree with the source photo.

### 4. Fix

Targeted regen only. Max 3 retries, then show the best frame and ask.

- Face → strengthen the face-lock sentence; keep everything else.
- Fit → name shoulder line, waist, sleeve path.
- Edges → "soft transition, no hard outline."
- Lighting → repeat source light direction and intensity.

## Out of scope

Outerwear, skirts, matching sets, costume / cultural dress, bridal, swimwear, lingerie, and accessories are not in this skill. Do not improvise extra category templates.

## License

CC BY-SA 4.0. Commercial use allowed. Credit the author and share derivatives under the same license.
