---
name: clawf-selfie
description: Generate character selfies via aibotclaw.com and send to messaging channels via OpenClaw
allowed-tools: Bash(npm:*) Bash(npx:*) Bash(openclaw:*) Bash(curl:*) Read Write WebFetch
---

# Clawf Selfie

Generate selfies by editing the current character's reference image via aibotclaw.com.

## ⚠️ CRITICAL: Always Use The Script

**Never construct the API call inline. Always call the shell script.**
The script reads the reference image URL from `character.json` at runtime.
If you hardcode any image URL, you will use the wrong image.

```bash
bash /root/.openclaw/workspace/skills/clawf-selfie/scripts/clawf-selfie.sh \
  "<PROMPT>" \
  "<CHANNEL>" \
  ["<CAPTION>"] \
  ["<IMAGE_SIZE>"]
```

## When to Use

- User says "send a pic", "send me a pic", "send a photo", "send a selfie"
- User says "send a pic of you...", "send a selfie of you..."
- User asks "what are you doing?", "how are you doing?", "where are you?"
- User describes a context: "send a pic wearing...", "send a pic at..."

## How to Use

### Step 1: Select mode

**Auto-select by keywords:**

| Keywords in request | Mode |
|---------------------|------|
| outfit, wearing, clothes, dress, suit, fashion | mirror |
| cafe, restaurant, beach, park, city, portrait, face, smile | direct |
| full-body, mirror, reflection | mirror |
| what are you doing, how are you, where are you | direct (invent a fitting scene) |

### Step 2: Enrich the prompt

**Do NOT pass the user's words directly.** Expand into a vivid, detailed English description.

Use this checklist to enrich the `<USER_CONTEXT>` before inserting into the template:

| Dimension | What to add |
|-----------|-------------|
| **Outfit detail** | fabric, color, fit, layering (e.g. "a fitted off-shoulder white linen top tucked into high-waist caramel cargo pants") |
| **Accessories** | bag, hat, sunglasses, jewelry, shoes |
| **Styling** | hair style, makeup vibe (e.g. "hair in a loose low bun, soft dewy makeup") |
| **Lighting** | golden hour sunlight, soft studio light, warm fairy lights, neon glow, overcast daylight |
| **Mood / expression** | playful smile, soft gaze, confident smirk, relaxed candid look |
| **Background / setting** | (mirror mode) clean white wall, marble bathroom, aesthetic bedroom; (direct mode) specific location detail |

**Outfit style reference library** — choose the closest match and expand:

| Style | Example enriched description |
|-------|------------------------------|
| Casual everyday | loose cream oversized hoodie, light wash straight-leg jeans, white sneakers, messy bun |
| Cozy home | oversized soft knit cardigan in dusty rose, biker shorts, barefoot, hair down |
| Sporty / athleisure | black fitted crop sports bra, high-waist ribbed leggings, white sneakers, hair in high ponytail |
| Swimwear / beach | strappy triangle bikini top in sage green, low-rise bikini bottoms, sun-kissed glow, wet hair |
| Flirty / feminine | baby-doll mini dress with flutter sleeves, delicate lace hem, strappy heels |
| Elegant evening | sleek backless satin slip dress in deep burgundy, minimal gold jewelry, subtle smoky eye |
| Chic office | tailored white button-up shirt tucked into a fitted black pencil skirt, block heel pumps |
| Streetwear | cropped graphic tee, wide-leg cargo pants, chunky sneakers, snapback cap |
| Party / going out | sequin mini skirt, strappy metallic crop top, stilettos, glam makeup |
| Sexy / bold | form-fitting cut-out bodycon dress, plunging neckline, thigh-high boots, confident expression |
| Lingerie lounge | soft satin slip camisole and matching shorts set in champagne, relaxed pose, bedroom setting |

### Step 3: Assemble the final prompt

**Character consistency note (Nano Banana model):**
Nano Banana has built-in character consistency when a reference image is provided via `image_urls`. Do NOT use repetitive anchor phrases like "same face, same body" — they are redundant and may confuse the model. Instead, describe what **changes** (outfit, scene, lighting) and leave everything else implicit. The model will preserve the character's face, body proportions, and breast size from the reference image automatically.

If a specific body feature is drifting across generations, describe it explicitly once in natural language (e.g. "her full figure", "her curvy silhouette") — not as a repeated keyword.

**⚠️ MANDATORY consistency rules — apply to EVERY prompt without exception:**
1. **Human subject** — the output must depict a human character, not an animal, pet, or object.
2. **Strict face & body fidelity** — the face, facial features (eyes, nose, lips, jawline), and body proportions MUST match the reference image exactly. Do NOT invent, alter, or idealize any facial feature or body shape. Any divergence from the reference is a hard failure.

**Mirror mode** — full-body, outfit showcase:
```
a photo of this exact person, same face and facial features as the reference image, same body proportions, but <ENRICHED_CONTEXT>. the person is taking a mirror selfie, natural relaxed pose, soft indoor lighting
```

**Direct mode** — close-up, location/scene:
```
a close-up selfie of this exact person, same face and facial features as the reference image, same body proportions, taken by herself at <ENRICHED_CONTEXT>, direct eye contact with the camera, looking straight into the lens, eyes centered and clearly visible, not a mirror selfie, phone held at arm's length, face fully visible
```

### Step 4: Call the script

```bash
bash /root/.openclaw/workspace/skills/clawf-selfie/scripts/clawf-selfie.sh \
  "<FINAL_PROMPT>" \
  "<CHANNEL>"
```

The script will:
1. Read `reference_image_url` from `/root/.openclaw/workspace/character.json`
2. Call aibotclaw.com API with the correct reference image
3. Send the result to the target channel via OpenClaw

### Step 5: Send (handled by the script automatically)

The script calls `openclaw message send` internally. No extra step needed.

## Examples

```bash
# Mirror selfie — casual outfit (enriched)
bash /root/.openclaw/workspace/skills/clawf-selfie/scripts/clawf-selfie.sh \
  "a photo of this exact person, same face and facial features as the reference image, same body proportions, but wearing a loose dusty rose oversized knit sweater, light wash straight-leg jeans, white sneakers, hair in a casual messy bun, soft warm indoor lighting. the person is taking a mirror selfie, natural relaxed pose" \
  "telegram"

# Mirror selfie — sexy / going out
bash /root/.openclaw/workspace/skills/clawf-selfie/scripts/clawf-selfie.sh \
  "a photo of this exact person, same face and facial features as the reference image, same body proportions, but wearing a form-fitting black cut-out bodycon dress with a subtle plunging neckline, strappy heels, minimal gold jewelry, confident expression, soft studio lighting. the person is taking a mirror selfie, natural relaxed pose" \
  "telegram"

# Direct selfie — location scene
bash /root/.openclaw/workspace/skills/clawf-selfie/scripts/clawf-selfie.sh \
  "a close-up selfie of this exact person, same face and facial features as the reference image, same body proportions, taken by herself at a cozy Tokyo night market, warm amber street light, soft smile, slightly windswept hair, direct eye contact with the camera, looking straight into the lens, eyes centered and clearly visible, not a mirror selfie, phone held at arm's length, face fully visible" \
  "telegram"

# Direct selfie — beach swimwear
bash /root/.openclaw/workspace/skills/clawf-selfie/scripts/clawf-selfie.sh \
  "a close-up selfie of this exact person, same face and facial features as the reference image, same body proportions, taken by herself at a tropical beach, wearing a strappy sage green bikini, golden hour sunlight, sun-kissed glowing skin, relaxed candid smile, ocean waves blurred in background, direct eye contact with the camera, looking straight into the lens, not a mirror selfie, phone held at arm's length, face fully visible" \
  "telegram"
```

## Supported Platforms

| Platform | Channel Format | Example |
|----------|----------------|---------|
| Telegram | `telegram` or chat ID | `telegram`, `-100123456` |
| Discord  | `#channel-name` or ID | `#general`, `123456789` |
| WhatsApp | Phone number (JID) | `1234567890@s.whatsapp.net` |
| Slack    | `#channel-name` | `#random` |

## Error Handling

- **CRS_API_KEY_ID missing**: Set environment variable in openclaw.json
- **403 quota exhausted**: Purchase more tokens at aibotclaw.com
- **504 timeout**: Generation took >60s, retry is safe
- **Wrong image**: Never hardcode URLs — always call the script
