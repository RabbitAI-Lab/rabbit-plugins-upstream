# Prompt Formatting Reference (image-with-comfyui)

Per-model guidance for writing prompts. This is reference material — the SKILL.md
procedure just says "format your prompt; see below". Prompt keywords are kept
bilingual where they originally appeared bilingual (e.g. `blurry 模糊`).

## Z-Image (T2I)

Z-Image works best with **structured natural language prompts**, not keyword spam.

**6-part formula:**
```
Subject + Scene + Composition + Lighting + Style + Constraints
```

**Rules:**
- ✅ Use natural language sentences (not comma-separated tags)
- ✅ Be specific about subject, camera, lighting, style
- ❌ **NO negative prompts** — Z-Image Turbo ignores them completely
- ❌ No weighted tags like `(word:1.2)`

**Example:**
```
A young woman with long wavy blonde hair sits at a wooden café table,
steam rising from a ceramic cup. Shot from a 3/4 angle, close-up framing.
Soft morning light filters through sheer curtains, casting warm golden tones.
Cinematic photography, shallow depth of field, Kodak Portra 400 aesthetic.
No text, no logos, photorealistic skin texture.
```

**Aspect ratios:** `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, `2:3`
Should be ommited (defaults to 1:1) unless specified by user or as an extracted requirement from user's requests.
In I2I situation, it should match the original image which the user asks to modify.

---

## SD3.5 Medium (T2I)

SD3.5 Medium uses **natural language prompts** with optional negative prompts.

**Prompt formula:**
```
[Composition/Angle] + [Subject] + [Scene/Environment] + [Lighting/Color] + [Style/Texture] + [Details]
```

**Rules:**
- ✅ **Complete natural language sentences** — describe telling a human what to see
- ✅ Subject first (model prioritizes early text)
- ✅ Be specific about colors, materials, mood, atmosphere
- ✅ Mixed CN/EN is fine (Chinese works better for Chinese scenes)
- ✅ Use `--negative` for elements to exclude
- ✅ Default 1:1 (1024×1024), use `--aspect` to change
- ✅ Default 20 steps, CFG 4.01 (higher = stronger control)
- ✅ Seed defaults to random; specify `--seed` for reproducibility
- ❌ No comma-separated keyword spam (`beautiful, amazing, 4k`)
- ❌ No weighted tags `(word:1.2)` — SD3.5 doesn't recognize them

**Parameter recommendations:**
- **CFG**: 4-7 (4.01 = softer, 5-7 = stronger control)
- **Steps**: 20-25 (below 20 may lack detail)
- **Negative prompt**: Highly effective in SD3.5

**Common negative prompt words (mixed CN/EN — either or both work):**
```
blurry 模糊, low quality 低质量, pixelated 像素化, grainy 颗粒感,
overexposed 过曝, underexposed 欠曝, flat lighting 平光,
text 文字, watermark 水印, logo 商标, signature 署名, caption 字幕,
poorly drawn face 画坏的脸, deformed 变形, mutated 畸变, disfigured 毁容, extra limbs 多余肢体,
cartoonish 卡通风(写实时用)
```

**Mixed CN/EN example — both work; for Chinese scenes the prompt may be written in Chinese:**
```
上海魔都春日花海 — 黄浦江畔，大片郁金香、樱花、油菜花盛开，繁花似锦；
春日和煦阳光，远景陆家嘴三件套天际线；湿润的滨江步道倒映花影；
低饱和胶片色调，文艺清新，广角视野。
```

**English example:**
```
Cinematic photography, wide-angle shot of a bustling Tokyo street at night,
neon signs reflecting on wet pavement, people with transparent umbrellas,
moody atmospheric lighting, deep blues and vibrant reds, street photography,
shallow depth of field with bokeh background
```

---

## Qwen-Image 2.1 (T2I default & I2I default)

- T2I: same 6-part natural-language formula as Z-Image. **Optional `--negative`** (kept short, e.g. `text, watermark, blurry`). **CFG locked to 1.0** (distilled) — never pass `--cfg`.
- I2I: concise prompts, user's original language; **optional `--negative`** allowed (concise, positive-only edits still work best). Multi-image: up to 16 refs, `--image` order = slot order, referenced as `<image1>`, `<image2>`, ...; with the reference switch ON the output follows the first reference's aspect ratio.

## Qwen Image Edit (I2I) — Concise Prompts

I2I prompts must be **concise and direct**. Keep the user's original language.

**Rules:**
- ✅ **Positive prompt only** — no negative prompts
- ✅ Use user's exact words (don't translate or expand)
- ✅ Concise (either language): 换红外套/put on a red jacket, 把背景换成蓝天白云/change the background to a blue sky with clouds, 把女孩换成男孩/turn the girl into a boy
- ❌ Don't translate between languages
- ❌ Don't over-explain or add details

**Prompt routing fix (2026-04-22):**
- The Qwen workflow has TWO `TextEncodeQwenImageEditPlus` nodes:
  - `115:110` — empty negative prompt node
  - `115:111` — positive prompt node (contains default text like "the girl")
- Script must route prompts to **node 111 (positive)**, not node 110
- The `prepare_i2i_workflow()` function auto-detects by scanning for existing default text

---

## Wan2.2 I2V (Image → Video)

Wan2.2 generates short videos (~5 seconds) from a static image + motion description.

**Rules:**
- ✅ Prompt describes **actions/movement** (not scene description)
- ✅ English motion descriptions tend to give the best results; the user's own language is acceptable — do not force a translation the user didn't ask for
- ✅ Focus on "who does what" and "how the camera moves"
- ❌ Don't describe static scene elements in motion prompt

- Default: 81 frames (~5s @ 16fps), 4 steps, CFG 4.5
- Base resolution: **560×720** (3:4, fast and OK quality)
- Auto-detect input image aspect ratio and select reference resolution:

### Resolution Reference

| Aspect | Fast & OK | User Fav | WAN 2.2 Native |
|--------|-----------|----------|----------------|
| 3:4 | 560×720 | 720×912 | 848×1088 |
| 2:3 | 528×768 | 656×960 | 784×1136 |
| 9:16 | 480×848 | 608×1072 | 720×1264 |

Other available resolutions:
- **3:4**: 416×544, 672×864, 784×1008
- **2:3**: 384×576, 624×912, 736×1072
- **9:16**: 368×624, 576×1008, 672×1184

**Examples:**
```
prompt: "the cat walks forward and looks at the camera, tail wagging"
prompt: "the girl smiles and turns her head, wind blowing her hair"
prompt: "the person stands in a busy street, camera pans left and slowly zooms in, cars driving, red flag fluttering"
```
