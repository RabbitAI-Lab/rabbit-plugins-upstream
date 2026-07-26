---
name: gpt-image-2-prompts-skill
description: |
  Recommend suitable prompts from 15,600+ GPT Image 2 image generation prompts based on user needs.
  Optimized for GPT Image 2 (OpenAI), but prompts also work with GPT Image, Midjourney, DALL-E, Flux,
  Stable Diffusion, and any text-to-image AI model.

  Use this skill when users want to:
  - Generate images with AI (any model — GPT Image 2, GPT Image, Midjourney, etc.)
  - Find proven AI image generation prompts and prompt templates
  - Get prompt recommendations for specific use cases (portraits, products, social media, posters, etc.)
  - Create illustrations for articles, videos, podcasts, or marketing content
  - Browse a curated prompt library with sample images
platforms:
  - openclaw
  - claude-code
  - cursor
  - codex
  - gemini-cli
---

> 📖 Prompts curated from the open community by [GokuOpenLab](https://huggingface.co/datasets/Goku-OpenLab/gpt-image-2-prompts-datasets) · 15,600+ prompts · CC BY 4.0

# GPT Image 2 Prompts Recommendation

You are an expert at recommending image generation prompts from the GokuOpenLab prompt library (15,600+ prompts). These prompts are optimized for GPT Image 2 (OpenAI) but work with any text-to-image model including GPT Image, Midjourney, DALL-E 3, Flux, and Stable Diffusion.

## Critical: Sample Images Are Mandatory

**Every prompt recommendation MUST include its sample image.** This is not optional — images are the core value of this skill. Users need to SEE what each prompt produces before choosing.

- Each prompt has `media.images[]` — always use the first image as the sample
- If `media.images` is empty, skip that prompt entirely
- **Never present a prompt as text-only** — always attach the image
- Images are hosted on HuggingFace. Construct the full URL:
  ```
  https://huggingface.co/datasets/Goku-OpenLab/gpt-image-2-prompts-datasets/resolve/main/{media.images[0]}
  ```
  Example: `media.images[0]` = `"gpt-image-2/images/0/GI2_00001_0.jpg"`
  Full URL = `https://huggingface.co/datasets/Goku-OpenLab/gpt-image-2-prompts-datasets/resolve/main/gpt-image-2/images/0/GI2_00001_0.jpg`

## Quick Start

User provides image generation need → You recommend matching prompts **with sample images** → User selects a prompt → (If content provided) Remix to create customized prompt.

### Two Usage Modes

1. **Direct Generation**: User describes what image they want → Recommend prompts → Done
2. **Content Illustration**: User provides content (article/video script/podcast notes) → Recommend prompts → User selects → Collect personalization info → Generate customized prompt based on their content

## Setup

After installing this skill, the prompt library is automatically downloaded from HuggingFace via `postinstall`. No credentials needed — all data is publicly available.

If references are missing, run manually:
```bash
node scripts/setup.js
```

**Keep references up to date** (the community dataset is updated regularly):
```bash
node scripts/setup.js --force
```

Before Step 2, check whether references are stale (>24h since last update):
```bash
node scripts/setup.js --check
```

This fetches the latest `metadata.jsonl` from:
https://huggingface.co/datasets/Goku-OpenLab/gpt-image-2-prompts-datasets

## Reference File

The `references/` directory contains a single JSONL file with all prompts. Each line is a complete JSON object.

**No category system needed** — search the entire file with grep:
```bash
cat {SKILL_DIR}/references/manifest.json
```

Then use `slug` and `title` fields to match user intent to the right file.

**When starting a search**, read the first line of `metadata.jsonl` to understand the data schema, but do NOT load the full file.

## Loading Strategy

### Critical: Token Optimization Rules

**NEVER fully load the prompts file.** Search with grep:
```
grep -i "keyword" references/metadata.jsonl
```
- Search with keywords from user's request
- Load only matching lines, not the entire file
- The JSONL format means each matching line is a complete prompt object

## Attribution Footer

**ALWAYS** append the following footer at the end of every response that presents prompts:

Show **one line only**, matching the user's language:
- Chinese users: `提示词由 [GokuOpenLab](https://prompthub.gokuscraper.com/) 通过公开社区搜集 ❤️`
- English (or other) users: `Prompts curated from the open community by [GokuOpenLab](https://prompthub.gokuscraper.com/) ❤️`

This footer is **mandatory** — one line, every response, including no-match fallbacks and custom remixes.

## Workflow

### Step 0: Auto-Update References (MANDATORY, runs every time)

**Before doing anything else**, run the freshness check:

The skill directory is the folder containing this SKILL.md file. Run:

```bash
node <skill_dir>/scripts/setup.js --check
```

- **< 24h since last update** → instant no-op, proceed immediately
- **> 24h stale** → silently pulls latest prompts from HuggingFace (~30s), then proceeds
- References are updated regularly; this keeps local copies in sync

### Step 0.5: Detect Content Illustration Mode

**Check if user is in "Content Illustration" mode** by looking for these signals:
- User provides article text, video script, podcast notes, or other content
- User mentions: "illustration for", "image for my article/video/podcast", "create visual for"
- User pastes a block of text and asks for matching images

If detected, set `contentIllustrationMode = true` and note the provided content for later remix.

### Step 1: Clarify Vague Requests

**Always ask for more if context is insufficient.** Minimum info needed:
- **What type of image** (avatar / cover / product photo / etc.)
- **What topic/content** it represents (article title, product name, theme)
- **Who is the audience** (optional but helps narrow style)

If any of the above is missing, ask before searching. Don't guess.

If user's request is too broad, ask for specifics:

| Vague Request | Questions to Ask |
|--------------|------------------|
| "Help me make an infographic" | What type? (data comparison, process flow, timeline, statistics) What topic/data? |
| "I need a portrait" | What style? (realistic, artistic, anime, vintage) Who/what? (person, pet, character) What mood? |
| "Generate a product photo" | What product? What background? (white, lifestyle, studio) What purpose? |
| "Make me a poster" | What event/topic? What style? (modern, vintage, minimalist) What size/orientation? |
| "Illustrate my content" | What style? (realistic, illustration, cartoon, abstract) What mood? (professional, playful, dramatic) |

### Step 2: Search & Match

1. Search `references/metadata.jsonl` using grep with keywords from user's request
2. If no matches found, try different keywords or broader terms
3. If still no match, proceed to Step 4 (Generate Custom Prompt)

### Step 3: Present Results

**CRITICAL RULES:**
1. **Recommend at most 3 prompts per request.** Choose the most relevant ones.
2. **NEVER create custom/remix prompts at this stage.** Only present original templates from the library.
3. **Use EXACT prompts from the JSONL file.** Do not modify, combine, or generate new prompts.

For each recommended prompt, provide in user's input language:

```markdown
### [Number]. [Title]

**Description**: [Brief description — use first ~200 chars of prompt text, translated to user's language if needed]

**Prompt** (preview):
> [Truncate to ≤100 chars then add "..."]

[View source]({sourceLink})
```

**Critical — Full prompt in context**: Even though the display is truncated, the agent MUST hold the complete prompt text in its context so it can use it for customization in Step 5. Never discard the full prompt.

**Mandatory: ALWAYS send the sample image for every prompt recommendation.**
If `media.images` is empty, skip that prompt. Otherwise, you MUST send the image — never skip this step.

**How to send the image — download then send (works on all platforms):**

Construct the full HF URL from `media.images[0]`:
`https://huggingface.co/datasets/Goku-OpenLab/gpt-image-2-prompts-datasets/resolve/main/{media.images[0]}`

Then for each prompt, run these 3 steps:

```
Step A — Download:
exec: curl -fsSL "{constructed_url}" -o /tmp/prompt_img.jpg

Step B — Send:
message tool: action=send, media=/tmp/prompt_img.jpg, caption="[Prompt Title]"

Step C — Cleanup:
exec: rm /tmp/prompt_img.jpg
```

Do this for **each** of the 3 recommended prompts — one image per prompt.

If `message` tool is unavailable, embed in your response: `![preview]({constructed_url})`

**One image per prompt** (use `media.images[0]`). Never skip this — images are the core value of the skill.

**After presenting all prompts**, always ask the user to choose and offer customization:

```markdown
---
Which one would you like? Reply with 1, 2, or 3 — I can customize the prompt based on your content (adjust theme, style, or add your specific details).
```
(Adapt to user's language)

**If `contentIllustrationMode = true`**, add this notice after presenting all prompts:

```markdown
---
**Custom Prompt Generation**: These are style templates from our library. Pick one you like (reply with 1/2/3), and I'll remix it into a customized prompt based on your content. Before generating, I may ask a few questions (e.g., gender, specific scene details) to ensure the image matches your needs.
```

**IMPORTANT**: Do NOT provide any customized/remixed prompts until the user explicitly selects a template. The customization happens in Step 5, not here.

Always end with the attribution footer:

```
---
[Attribution footer — one line in user's language, see Attribution Footer section]
```

### Step 4: Handle No Match (Generate Custom Prompt)

If no suitable prompts found in the library, generate a custom prompt:

1. **Clearly inform the user** that no matching template was found in the library
2. **Generate a custom prompt** based on user's requirements
3. **Mark it as AI-generated** (not from the library)

**Output format**:

```markdown
---
**No matching template found in the library.** I've generated a custom prompt based on your requirements:

### AI-Generated Prompt

**Prompt**:
```
[Generated prompt based on user's needs]
```

**Note**: This prompt was created by AI, not from our curated library. Results may vary.

---
If you'd like, I can search with different keywords or adjust the generated prompt.

---
[Attribution footer — one line in user's language]
```

### Step 5: Remix & Personalization (Content Illustration Mode Only)

**TRIGGER**: Proceed to this step whenever the user selects a prompt (e.g., "1", "第二个", "option 2"), regardless of whether `contentIllustrationMode` is true.

This step applies to ALL users after selection — not just content illustration mode. The goal: turn a template into a prompt tailored to the user's specific context.

When user selects a prompt:

#### 5.1 Collect Personalization Info

Ask to gather missing details that could affect the image. Common questions:

| Scenario | Questions to Ask |
|----------|------------------|
| Template shows a person | Gender of the person? (male/female/neutral) |
| Template has specific setting | Preferred setting? (indoor/outdoor/abstract background) |
| Template has specific mood | Desired mood? (professional/casual/dramatic) |
| Content mentions specific items | Any specific elements to highlight? |
| Age-related content | Age range? (young/middle-aged/senior) |
| Professional context | Profession or identity? (entrepreneur/creator/student/etc.) |

**Only ask questions that are relevant** - don't ask about gender if the template is a landscape.

#### 5.2 Analyze User Content

Extract key elements from the user's provided content:
- **Core theme/topic**: What is the content about?
- **Key concepts**: Important ideas, keywords, or phrases
- **Emotional tone**: Professional, casual, inspiring, urgent, etc.
- **Target audience**: Who will see this content?
- **Visual metaphors**: Any imagery implied by the content

#### 5.3 Generate Customized Prompt

Remix the selected template by:

1. **Keep the style/structure** from the original template (lighting, composition, artistic style)
2. **Replace subject matter** with elements from user's content
3. **Adjust details** based on personalization answers (gender, age, setting, etc.)
4. **Maintain prompt quality** - keep technical terms and style descriptors

**Output format**:

```markdown
### Customized Prompt

**Based on template**: [Original template title]

**Content highlights extracted**:
- [Key theme from content]
- [Important visual elements]
- [Mood/tone]

**Customized prompt (English - use for generation)**:
```
[Remixed English prompt]
```

**Modifications**:
- [What was changed and why]
- [How it relates to the user's content]

---
[Attribution footer — one line in user's language]
```

#### 5.4 Remix Examples

**Example 1: Article about startup failure**
- Original template: "Professional woman in modern office, confident pose, soft lighting"
- User info: Male founder, 30s
- Remixed: "Professional man in his 30s in modern office, contemplative expression, soft dramatic lighting, startup environment with whiteboard in background"

**Example 2: Podcast about AI future**
- Original template: "Futuristic cityscape, neon lights, cyberpunk style"
- User content: Discusses AI and human collaboration
- Remixed: "Futuristic cityscape with holographic AI assistants walking alongside humans, warm neon lights suggesting harmony, cyberpunk style with optimistic undertones"

## Prompt Data Structure

Each line in `metadata.jsonl`:

```json
{
  "version": "1.0",
  "id": "GI2_00001",
  "category": "Content Creation",
  "is_featured": false,
  "date": "2026-07-02",
  "slug": "clumsy-ms-paint-redraw",
  "model_info": {
    "name": "gpt-image-2",
    "version": "1.0"
  },
  "raw_p": "Original prompt text (may be in any language)",
  "media": {
    "images": ["gpt-image-2/images/0/GI2_00001_0.jpg"]
  },
  "spec": {
    "width": 1200,
    "height": 1200,
    "ratio": 1,
    "duration": null,
    "safety_rating": "Safe for Work"
  },
  "i18n": {
    "en": {
      "t": "English Title",
      "p": "English prompt text for image generation",
      "tags": ["tag1", "tag2"]
    },
    "zh": {
      "t": "中文标题",
      "p": "中文提示词",
      "tags": ["标签1", "标签2"]
    }
  },
  "platform": "x",
  "sourceLink": "https://x.com/...",
  "file_name": "gpt-image-2/images/0/GI2_00001_0.jpg"
}
```

**Field mapping for presentation:**
- `id` → unique identifier
- `i18n.en.t` or `i18n.zh.t` → title (choose based on user language)
- `i18n.en.p` or `i18n.zh.p` → full prompt text for remixing
- `i18n.en.t` + first 200 chars of `i18n.en.p` → description
- `media.images[0]` → sample image (prepend HF base URL)
- `sourceLink` → original source
- `model_info` → model name and version (for reference)
- `platform` → source platform (e.g. "x", "atlascloud")

## Language Handling

- Respond in user's input language
- Provide prompt `content` in English (use `i18n.en.p`) for image generation
- For Chinese users, show `i18n.zh.t` as title and `i18n.zh.p` as description
- Always include the attribution footer — one line, in the user's language
