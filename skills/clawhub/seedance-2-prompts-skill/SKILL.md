---
name: seedance-2-prompts-skill
description: |
  Recommend suitable prompts from 8,000+ Seedance 2 video generation prompts based on user needs.
  Optimized for Seedance 2 (ByteDance), but prompts also work with other video generation models.

  Use this skill when users want to:
  - Generate videos with AI (Seedance 2, etc.)
  - Find proven AI video generation prompts and prompt templates
  - Get prompt recommendations for specific use cases (commercials, short films, social media, etc.)
  - Create video assets for articles, marketing, or content
  - Browse a curated prompt library with cover images and video samples
platforms:
  - openclaw
  - claude-code
  - cursor
  - codex
  - gemini-cli
---

> 📖 Prompts curated from the open community by [GokuScraper](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets) · 8,000+ prompts · CC BY 4.0

# Seedance 2 Prompts Recommendation

You are an expert at recommending video generation prompts from the GokuScraper prompt library (8,000+ prompts). These prompts are optimized for Seedance 2 (ByteDance) but work with other video generation models.

## Critical: Cover Images + Video Links Are Mandatory

**Every prompt recommendation MUST include its cover image and video link.** This is not optional — users need to SEE the style before generating.

- Each prompt has `media.c` (cover image) and `media.v` (video file)
- Always show the cover image as a preview
- Always provide the video link for the full result
- If `media.c` or `media.v` is empty, skip that prompt entirely
- **Never present a prompt as text-only** — always attach the cover image
- Covers are hosted on HuggingFace. Construct the full URL:
  ```
  https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/{media.c}
  ```
  Example: `media.c` = `"seedance-2/covers/SD2_00001.jpg"`
  Full URL = `https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_00001.jpg`

## Quick Start

User provides video generation need → You recommend matching prompts **with cover images + video links** → User selects a prompt → (If content provided) Remix to create customized prompt.

### Two Usage Modes

1. **Direct Generation**: User describes what video they want → Recommend prompts → Done
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
https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets

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
- User mentions: "illustration for", "video for my article/video/podcast", "create visual for"
- User pastes a block of text and asks for matching videos

If detected, set `contentIllustrationMode = true` and note the provided content for later remix.

### Step 1: Clarify Vague Requests

**Always ask for more if context is insufficient.** Minimum info needed:
- **What type of video** (commercial / cinematic / social media / etc.)
- **What topic/content** it represents (article title, product name, theme)
- **Who is the audience** (optional but helps narrow style)

If any of the above is missing, ask before searching. Don't guess.

If user's request is too broad, ask for specifics:

| Vague Request | Questions to Ask |
|--------------|------------------|
| "Help me make a commercial" | What product/service? What style? (cinematic, product showcase, animated) What duration? |
| "I need a cinematic video" | What genre? (drama, sci-fi, fantasy, documentary) What mood? (epic, intimate, suspenseful) |
| "Generate a product video" | What product? What style? (360 spin, lifestyle, macro) What purpose? |
| "Make me a social media video" | What platform? (TikTok/Reels/Shorts) What style? What message? |
| "Illustrate my content" | What style? (realistic, animation, cinematic, abstract) What mood? (professional, playful, dramatic) |

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

**Duration**: [spec.duration seconds]

**Prompt** (preview):
> [Truncate to ≤100 chars then add "..."]

🎬 [Watch video]({video_url}) | [View source]({sourceLink})
```

**Critical — Full prompt in context**: Even though the display is truncated, the agent MUST hold the complete prompt text in its context so it can use it for customization in Step 5. Never discard the full prompt.

**Mandatory: ALWAYS send the cover image for every prompt recommendation.**
If `media.c` is empty, skip that prompt. Otherwise, you MUST send the cover — never skip this step.

**How to send the cover — download then send (works on all platforms):**

Construct the full HF URL from `media.c`:
`https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/{media.c}`

Then for each prompt, run these 3 steps:

```
Step A — Download cover:
exec: curl -fsSL "{constructed_url}" -o /tmp/prompt_cover.jpg

Step B — Send cover:
message tool: action=send, media=/tmp/prompt_cover.jpg, caption="[Prompt Title] — Duration: [spec.duration]s"

Step C — Cleanup:
exec: rm /tmp/prompt_cover.jpg
```

Do this for **each** of the 3 recommended prompts — one cover per prompt.

If `message` tool is unavailable, embed in your response: `![cover]({constructed_url})`

**One cover per prompt** (use `media.c`). Never skip this — cover images are the core value of the skill.

**Video links**: Construct the video URL the same way:
`https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/{media.v}`

Do NOT download the video — it's too large. Only provide the link for users to view.

**After presenting all prompts**, always ask the user to choose and offer customization:

```markdown
---
Which one would you like? Reply with 1, 2, or 3 — I can customize the prompt based on your content (adjust theme, style, or add your specific details).
```
(Adapt to user's language)

**If `contentIllustrationMode = true`**, add this notice after presenting all prompts:

```markdown
---
**Custom Prompt Generation**: These are style templates from our library. Pick one you like (reply with 1/2/3), and I'll remix it into a customized prompt based on your content. Before generating, I may ask a few questions (e.g., characters, setting, duration) to ensure the video matches your needs.
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

Ask to gather missing details that could affect the video. Common questions:

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
- Original template: "Professional man in modern office, confident pose, soft lighting, cinematic camera movement"
- User info: Male founder, 30s
- Remixed: "Professional man in his 30s in modern office, contemplative expression, soft dramatic lighting, slow camera pan across startup environment with whiteboard in background"

**Example 2: Podcast about AI future**
- Original template: "Futuristic cityscape, neon lights, cyberpunk style, aerial drone shot"
- User content: Discusses AI and human collaboration
- Remixed: "Futuristic cityscape with holographic AI assistants walking alongside humans, warm neon lights suggesting harmony, cyberpunk style with optimistic undertones, smooth tracking shot"

## Prompt Data Structure

Each line in `metadata.jsonl`:

```json
{
  "version": "1.0",
  "id": "SD2_00001",
  "category": "Content Creation",
  "is_featured": false,
  "date": "2026-07-02",
  "slug": "cinematic-drone-shot",
  "model_info": {
    "name": "seedance-2",
    "version": "1.0"
  },
  "raw_p": "Original prompt text (may be in any language)",
  "media": {
    "c": "seedance-2/covers/SD2_00001.jpg",
    "v": "seedance-2/videos/SD2_00001.mp4"
  },
  "spec": {
    "width": 1920,
    "height": 1080,
    "ratio": 1.778,
    "duration": 5,
    "safety_rating": "Safe for Work"
  },
  "i18n": {
    "en": {
      "t": "English Title",
      "p": "English prompt text for video generation",
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
  "file_name": "seedance-2/covers/SD2_00001.jpg"
}
```

**Field mapping for presentation:**
- `id` → unique identifier
- `i18n.en.t` or `i18n.zh.t` → title (choose based on user language)
- `i18n.en.p` or `i18n.zh.p` → full prompt text for remixing
- `i18n.en.t` + first 200 chars of `i18n.en.p` → description
- `media.c` → cover image (prepend HF base URL)
- `media.v` → video file (prepend HF base URL, provide as link — do NOT download)
- `spec.duration` → video duration in seconds (display prominently)
- `spec.width`, `spec.height` → video resolution
- `sourceLink` → original source
- `model_info` → model name and version (for reference)
- `platform` → source platform (e.g. "x", "atlascloud")

**Cover image URL construction:**
```
https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/{media.c}
```

**Video URL construction (link only, do NOT download):**
```
https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/{media.v}
```

## Language Handling

- Respond in user's input language
- Provide prompt `content` in English (use `i18n.en.p`) for video generation
- For Chinese users, show `i18n.zh.t` as title and `i18n.zh.p` as description
- Always include the attribution footer — one line, in the user's language
