# Image-First Mode Reference (image-with-comfyui)

The SKILL.md core says "image-first: route remembered image + new text to
`i2i`/`wan2.2`". This file holds the full detection logic and worked examples.
Open it when a user sends an image and then a short edit request.

## Detection

1. The user sends **only an image** (no other text that turn).
2. Within **2 minutes**, the user sends a **text** message that looks like an
   edit or video request. The agent matches whichever language the user wrote —
   CN or EN keywords, e.g. `修一下/fix`, `换背景/change background`,
   `加特效/add an effect`, `变动画/turn into a video`, `改颜色/change color`.
3. The text intent is **I2I** (edit the image) or **I2V** (animate the image).

## Action

- Route the **remembered latest image** + the **new text** to
  `image_with_comfyui.py i2i` or `wan2.2`.
- `--image <path>` = the latest image received. `--prompt` = the new text.
- If unsure whether it's I2I or I2V, **default to I2I** unless the text clearly
  says video/animation.
- Do **NOT** ask the user for the image again — you already have it from the
  previous turn.
- **Scope:** only the immediately preceding image from the **same user, same
  session**, within the 2-minute window. Never reuse images from other users,
  other sessions, or older than 2 minutes.

## Context tracking

- Store the latest image media path (or URL) when no text is received.
- Clear the stored image after it's used, or after 2 minutes of no new text.

## Examples

- `[image: a photo of a dog]` → (wait)
- `[text: change the background to a beach]` → `i2i --image <path> --prompt "change the background to a beach"`
- `[image: a cat sitting on a chair]` → (wait)
- `[text: make it stand up and walk]` → `wan2.2 --image <path> --prompt "the cat stands up and walks"`

## Multi-image reference (up to 16)

With 2+ reference images the model sees them in **slot order**
(`image_1`, `image_2`, …). Reference each by index in the prompt:

```
Put the garment from <image2> onto the person in <image1>, keep <image1>'s pose and lighting.
```

`--image` accepts multiple paths in slot order: `--image /base.jpg /ref.jpg`
= `<image1>` `/base.jpg`, `<image2>` `/ref.jpg`.
