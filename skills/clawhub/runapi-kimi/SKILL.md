---
name: kimi
description: Call the Kimi API (kimi-k3, kimi-k2.7-code, kimi-k2.6, kimi-k2.5) through RunAPI using the official OpenAI SDK or compatible clients. Use when the user asks for Kimi chat, streaming completions, Anthropic or Gemini protocol compatibility, or when they want to point an existing OpenAI SDK setup at RunAPI as the base URL.
documentation: https://runapi.ai/models/kimi.md
provider_page: https://runapi.ai/providers/moonshot-ai.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/kimi
    primaryEnv: OPENAI_API_KEY
    requires:
      env:
      - OPENAI_API_KEY
      - OPENAI_BASE_URL
    envVars:
    - name: OPENAI_API_KEY
      required: true
      description: RunAPI API key used by OpenAI-compatible Kimi clients.
    - name: OPENAI_BASE_URL
      required: true
      description: Set to https://runapi.ai/v1 for Kimi on RunAPI.
---

# Kimi on RunAPI

Use the official **OpenAI SDK** or any OpenAI-compatible HTTP client and switch
the base URL to `https://runapi.ai/v1`. The primary endpoint is Chat
Completions (`POST /v1/chat/completions`).

## Setup

```dotenv
OPENAI_API_KEY=YOUR_RUNAPI_TOKEN
OPENAI_BASE_URL=https://runapi.ai/v1
```

Get a RunAPI API Key at <https://runapi.ai/api_keys>.

## Core recipe - Chat Completions

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_RUNAPI_TOKEN",
    base_url="https://runapi.ai/v1",
)

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[{"role": "user", "content": "Explain this code review finding."}],
)
print(response.choices[0].message.content)
print(response.usage)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_RUNAPI_TOKEN",
  baseURL: "https://runapi.ai/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k3",
  messages: [{ role: "user", content: "Explain this code review finding." }],
});
```

## Streaming

```python
stream = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{"role": "user", "content": "Write a compact changelog."}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

Streaming runs through a regional edge proxy so the request does not hold a
Rails/Puma thread. Long generations should always stream.

## Protocol compatibility

Kimi models are also available through RunAPI's Anthropic-compatible and Gemini
`contents` client surfaces. RunAPI bridges those request and response shapes to
the OpenAI-compatible chat request format, so use these protocol paths only when an
existing tool expects those formats:

```bash
curl -X POST "https://runapi.ai/v1/messages" \
  -H "x-api-key: YOUR_RUNAPI_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k3",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Draft a concise answer."}]
  }'
```

```bash
curl -X POST \
  "https://runapi.ai/v1beta/models/kimi-k3:streamGenerateContent" \
  -H "x-goog-api-key: YOUR_RUNAPI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"role":"user","parts":[{"text":"Hello!"}]}]}'
```

For new app code, prefer the OpenAI-compatible setup.

## List models

```bash
curl https://runapi.ai/v1/models \
  -H "Authorization: Bearer YOUR_RUNAPI_TOKEN"
```

## Supported models

| Model ID | Use when |
|---|---|
| `kimi-k3` | Current flagship for text requests with always-on reasoning |
| `kimi-k2.7-code` | Dedicated coding model with always-on thinking |
| `kimi-k2.6` | Latest Kimi K2 chat workloads |
| `kimi-k2.5` | Kimi K2.5 compatibility |

## K3 and K2.7 Code capability boundary

Across Chat Completions, Responses, Messages, and Gemini native, RunAPI supports
basic text, final answers, canonical reasoning/cache Usage, and automatic cache
handling for `kimi-k3` and `kimi-k2.7-code`. Raw `reasoning_content` is not
returned.

Do not send explicit reasoning controls, tools or tool history, multimodal
content, structured-output fields, cache IDs/TTL controls, opaque continuation
state, or signed thought blocks. These shapes fail before a task is created.
`kimi-k3` reasoning effort and both models' tools/multimodal features are
`native-only`; `kimi-k2.7-code` reasoning effort, explicit cache expiry,
opaque continuation, and protocol-signed thoughts are `cull`.

Omit sampling controls, or use `temperature=1.0`, `top_p=0.95`, `n=1`,
`presence_penalty=0`, and `frequency_penalty=0`. Keep requested output at or
below 131072 tokens for `kimi-k3` and 32768 tokens for `kimi-k2.7-code`. For
Chat Completions, send either `max_tokens` or `max_completion_tokens`, never
both.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/kimi.md
- Provider comparison: https://runapi.ai/providers/moonshot-ai.md
- Catalog: https://runapi.ai/models.md

## Agent rules

- Keep API keys in `OPENAI_API_KEY`, `RUNAPI_TOKEN`, or a secret manager; never
  inline them in commits or shell history.
- Default new integrations to the OpenAI-compatible client at
  `https://runapi.ai/v1`.
- For `kimi-k3` and `kimi-k2.7-code`, send basic text only and consume the final
  answer plus Usage; do not depend on raw reasoning or stateful continuation.
- Use streaming for responses longer than a few hundred tokens.
- For pricing, rate-limit, and commercial-usage answers, link to
  https://runapi.ai/models/kimi.md rather than copying values.
