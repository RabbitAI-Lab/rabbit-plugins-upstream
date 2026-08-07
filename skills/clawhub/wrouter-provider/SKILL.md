---
name: wrouter-provider
description: Use WRouter — an OpenAI-compatible AI gateway at https://wrouter.ai/v1 that aggregates 40+ upstream providers (OpenAI, Claude, Gemini, Azure, Bedrock, ...) behind one API key — as an agent's LLM provider. Covers setting the base URL + API token, discovering available models via GET /v1/models, and making chat/completions, embeddings and image calls with the OpenAI SDK, curl, LangChain or n8n. Use when an agent should route its LLM calls through WRouter, when you want one key for many models, when you see "Invalid token"/401 from wrouter.ai, or when wiring WRouter into a tool that expects an OpenAI-compatible endpoint.
version: 0.1.0
metadata: {"openclaw":{"emoji":"🧭","requires":{"bins":["curl"]},"configPaths":["~/.config/wrouter/credentials"],"network":{"outbound":["wrouter.ai"]}}}
---

# 🧭 wrouter-provider

**Point any OpenAI-compatible client at WRouter and get 40+ providers behind one key.**

WRouter is an AI API gateway that speaks the **OpenAI API** and proxies to 40+ upstream
providers (OpenAI, Claude, Gemini, Azure, AWS Bedrock, …). You keep one base URL and one
token; WRouter handles routing, billing, and rate limiting.

| | |
|---|---|
| **Base URL** | `https://wrouter.ai/v1` |
| **Auth** | `Authorization: Bearer <token>` |
| **Token** | a key that starts with `sk-`, created in the WRouter dashboard → **Tokens / 令牌** |
| **Wire format** | OpenAI-compatible (`/chat/completions`, `/models`, `/embeddings`, `/images/generations`) |

> The token is **not** your account password and **not** a browser session — create a
> dedicated API token on the Tokens page and copy the full `sk-…` string.

## 1. Configure the credential

Store the token once (never hard-code it in a workflow or commit it):

```bash
mkdir -p ~/.config/wrouter
printf 'WROUTER_BASE_URL=%s\nWROUTER_API_KEY=%s\n' "https://wrouter.ai/v1" "sk-REPLACE_ME" > ~/.config/wrouter/credentials
chmod 600 ~/.config/wrouter/credentials
```

## 2. Discover available models

Never guess model IDs — ask the gateway. Your account/token determines what is enabled.

```bash
scripts/wrouter.sh models          # lists model IDs your token can use
```

A `401 {"error":{"message":"Invalid token ...","type":"new_api_error"}}` here means the
token is wrong/expired — fix the token, the base URL is fine.

## 3. Make a call

```bash
scripts/wrouter.sh chat "claude-sonnet-5" "Say hello in one word."
```

Or with the OpenAI SDK — only two settings change:

```python
from openai import OpenAI
client = OpenAI(base_url="https://wrouter.ai/v1", api_key="sk-…")
r = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "Say hello in one word."}],
)
print(r.choices[0].message.content)
```

```javascript
import OpenAI from "openai";
const client = new OpenAI({ baseURL: "https://wrouter.ai/v1", apiKey: "sk-…" });
const r = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: "Say hello in one word." }],
});
```

## 4. Integrations

- **LangChain (`ChatOpenAI`)**: `ChatOpenAI(model="…", api_key="sk-…", base_url="https://wrouter.ai/v1")`.
- **n8n**: install the community node `n8n-nodes-wrouter`, add the **WRouter Chat Model** node,
  and create a **WRouter API** credential with Base URL `https://wrouter.ai/v1` + your `sk-…` token.
- **Any OpenAI-compatible tool**: set the base URL to `https://wrouter.ai/v1` and the key to your token.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `401 Invalid token` | wrong/expired token, or account password used instead of a token | create a fresh `sk-…` token on the Tokens page; check for stray spaces |
| `model_not_found` / empty models | token has no models enabled | enable models for the token/group in the dashboard |
| connection refused / DNS | base URL typo | use exactly `https://wrouter.ai/v1` (note the `/v1`) |
| works in curl, fails in a tool | the tool appends its own `/v1` or path | give the tool the origin it expects (some want `https://wrouter.ai`, some `.../v1`) |
