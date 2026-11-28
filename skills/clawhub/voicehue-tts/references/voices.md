# VoiceHue Voices & Allowance Reference

## Live Catalog Endpoint

```bash
GET https://voicehue.com/v1/voices
# Optional query parameters: ?language=en&tier=standard
```

- **Authentication**: None required.
- **Scale**: 600+ voices across 40+ languages (17 `standard` voices + 590+ `premium` voices).
- **Audio previews**: Browse and audition voices at `https://voicehue.com/voices`.

### Response Shape

```json
{
  "object": "list",
  "data": [
    {
      "id": "vh-zhixia",
      "object": "voice",
      "name": "映夏",
      "language": "zh",
      "gender": "female",
      "tier": "standard",
      "tags": ["energetic", "narration"],
      "description": "Bright and friendly for explainers and everyday narration.",
      "description_zh": "明亮亲切，适合轻松讲解和日常旁白。"
    },
    {
      "id": "vh-en-thalia",
      "object": "voice",
      "name": "Thalia",
      "language": "en-US",
      "gender": "female",
      "tier": "standard",
      "daily_char_limit": 2000
    },
    {
      "id": "vh-en-06933c708bda",
      "object": "voice",
      "name": "Theo",
      "language": "en-US",
      "gender": "male",
      "tier": "premium",
      "char_rate": 1
    }
  ]
}
```

- Always pass the exact `id` field as `voice` in synthesis requests.
- Never invent a voice ID from memory; query `GET /v1/voices` or run `node <SKILL_DIR>/scripts/voicehue.mjs voices` (supports `--tag <tag>` and `--query <text>` matching name, tags, and descriptions).
- `tags`, `description`, `description_zh`, and `daily_char_limit` are synchronized live from the website voice library (5-minute cache) and are present whenever configured on a voice.

## Standard Free Voices (Illustrative Snapshot — Always Query Live API)

These 17 standard voices work on the free API plan (shared account quota: 10,000 characters/month, 2,000 characters/day, 10 requests/minute):

| Voice ID | Name | Language | Gender | Best for |
|---|---|---|---|---|
| `vh-mia` | Mia | `en` | female | General narration, demos, courses (no per-voice cap) |
| `vh-clara` | Clara | `en` | female | Clear explainers, tutorials (no per-voice cap) |
| `vh-ethan` | Ethan | `en` | male | Podcasts, long articles, narration (no per-voice cap) |
| `vh-leo` | Leo | `en` | male | Product videos, presentations (no per-voice cap) |
| `vh-en-thalia` | Thalia | `en-US` | female | Short voiceovers & promos (2,000/day per-voice cap) |
| `vh-en-aurora` | Aurora | `en-US` | female | Short narration & clips (2,000/day per-voice cap) |
| `vh-en-apollo` | Apollo | `en-US` | male | Short announcements & clips (2,000/day per-voice cap) |
| `vh-en-orion` | Orion | `en-US` | male | Short commentary & clips (2,000/day per-voice cap) |
| `vh-qinghe` | 清禾 | `zh` | female | Chinese narration, courses, long articles (no per-voice cap) |
| `vh-zhixia` | 映夏 | `zh` | female | Chinese videos, storytelling (no per-voice cap) |
| `vh-warm-design` | 暖声 | `zh` | female | Warm conversational Chinese voiceovers (no per-voice cap) |
| `vh-baichuan` | 柏川 | `zh` | male | Chinese podcasts, explainers, long texts (no per-voice cap) |
| `vh-yangye` | 阳野 | `zh` | male | Energetic Chinese demos & commentary (no per-voice cap) |
| `vh-es-estrella` | Estrella | `es-MX` | female | Spanish (Mexico) short voiceovers (2,000/day per-voice cap) |
| `vh-es-celeste` | Celeste | `es-CO` | female | Spanish (Colombia) short voiceovers (2,000/day per-voice cap) |
| `vh-es-alvaro` | Alvaro | `es-ES` | male | Spanish (Spain) short voiceovers (2,000/day per-voice cap) |
| `vh-es-javier` | Javier | `es-MX` | male | Spanish (Mexico) short voiceovers (2,000/day per-voice cap) |

## Language Matching Tip

When searching with regional codes like `en-US` or `zh-CN`:
- A strict prefix filter (`"zh".startsWith("zh-cn")`) misses base-language voices (`vh-qinghe`, `vh-baichuan`, `vh-mia`, `vh-ethan`).
- Use `node <SKILL_DIR>/scripts/voicehue.mjs voices --language zh-CN` (which matches base `zh` voices too) or pass the two-letter base code (`?language=zh`, `?language=en`) when calling `GET /v1/voices` directly.

## Free vs. Premium Quota Summary

- **Standard voices (`tier: "standard"`)**: Draw from the API key's plan allowance.
  - Free API plan: **10,000 characters/month**, **2,000 characters/day**, **10 requests/minute**, up to 2 keys per account (quota shared across keys). Resets daily at 00:00 UTC and monthly on the 1st.
- **Premium voices (`tier: "premium"`)**: 590+ voices across 40+ languages (including Japanese, Korean, French, German, Portuguese, Italian, Arabic, Hindi, etc.).
  - Draw from the account's daily free premium trial (**500 characters/day**, up to **200 characters per request** without credits) and then account premium character balance (`char_rate` per character, at most 1).
- **Higher limits & paid options**: Do not hardcode prices; direct users to `https://voicehue.com/developers` and `https://voicehue.com/pricing`.
