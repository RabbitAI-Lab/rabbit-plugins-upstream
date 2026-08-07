---
name: mimo
description: Call the MiMo API (mimo-v2.5-pro and mimo-v2.5) through RunAPI using OpenAI-compatible Chat Completions or Responses clients, or Anthropic-compatible Messages clients. Use when the user asks for MiMo text generation, supported image understanding, streaming, or wants to point an existing LLM client at RunAPI.
documentation: https://runapi.ai/models/mimo.md
provider_page: https://runapi.ai/providers/xiaomi.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/mimo
    primaryEnv: OPENAI_API_KEY
    requires:
      env:
      - OPENAI_API_KEY
      - OPENAI_BASE_URL
    envVars:
    - name: OPENAI_API_KEY
      required: true
      description: RunAPI API key used by OpenAI-compatible MiMo clients.
    - name: OPENAI_BASE_URL
      required: true
      description: Set to https://runapi.ai/v1 for MiMo on RunAPI.
    - name: ANTHROPIC_API_KEY
      required: false
      description: Optional RunAPI API key alias for Anthropic-compatible Messages.
    - name: ANTHROPIC_BASE_URL
      required: false
      description: Optional base URL for Anthropic-compatible MiMo requests.
---

# MiMo on RunAPI

MiMo on RunAPI supports basic text requests through OpenAI-compatible Chat
Completions and Responses, plus Anthropic-compatible Messages. `mimo-v2.5`
also supports synchronous Chat Completions with HTTP(S) image URLs. Use the
OpenAI SDK for new integrations.

## Setup

```dotenv
OPENAI_API_KEY=YOUR_RUNAPI_TOKEN
OPENAI_BASE_URL=https://runapi.ai/v1
```

Get a RunAPI API Key at <https://runapi.ai/api_keys>.

## Chat Completions

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_RUNAPI_TOKEN",
    base_url="https://runapi.ai/v1",
)

response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[{"role": "user", "content": "Summarize this design decision."}],
)
print(response.choices[0].message.content)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_RUNAPI_TOKEN",
  baseURL: "https://runapi.ai/v1",
});

const response = await client.chat.completions.create({
  model: "mimo-v2.5",
  messages: [{ role: "user", content: "Draft a concise release note." }],
});
```

### Image input

Use `mimo-v2.5` with a synchronous Chat Completions request. Image parts accept
an HTTP(S) URL and may be combined with text parts.

```python
response = client.chat.completions.create(
    model="mimo-v2.5",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe this image."},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://cdn.runapi.ai/public/samples/image.jpg"
                },
            },
        ],
    }],
    stream=False,
)
print(response.choices[0].message.content)
```

## Responses

```python
response = client.responses.create(
    model="mimo-v2.5-pro",
    input="Explain this incident in three bullets.",
)
print(response.output_text)
```

## Streaming

```python
stream = client.chat.completions.create(
    model="mimo-v2.5",
    messages=[{"role": "user", "content": "Write a short status update."}],
    stream=True,
    stream_options={"include_usage": True},
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Anthropic Messages

```python
import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_RUNAPI_TOKEN",
    base_url="https://runapi.ai",
)

message = client.messages.create(
    model="mimo-v2.5-pro",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Draft a migration checklist."}],
)
print(message.content[0].text)
```

## Supported subset

- Basic text supports sync and SSE on Chat Completions, Responses, and Messages.
- `mimo-v2.5` additionally accepts `text` and HTTP(S) `image_url` content parts
  on synchronous Chat Completions requests.
- Tools, reasoning controls, continuation state, hosted capabilities,
  documents, audio, video, data URL images, streaming image requests, and image
  input on `mimo-v2.5-pro`, Responses, or Messages are outside the verified
  subset and are rejected before usage is reserved.
- Image parts accept only `type` and `image_url.url`; omit extensions such as
  `detail` and `cache_control`.
- Keep the requested model ID unchanged. The response uses the same canonical
  identity.

## Supported models

| Model ID | Use when |
|---|---|
| `mimo-v2.5-pro` | Higher-quality MiMo text generation |
| `mimo-v2.5` | Efficient MiMo text generation |

## References

- Model overview and pricing: <https://runapi.ai/models/mimo.md>
- Provider page: <https://runapi.ai/providers/xiaomi.md>
- Catalog: <https://runapi.ai/models.md>

## Agent rules

- Keep API keys in environment variables or a secret manager.
- Prefer the OpenAI-compatible client at `https://runapi.ai/v1` for new code.
- Use streaming for long responses.
- Keep image requests within the exact synchronous `mimo-v2.5` Chat Completions subset.
- Omit `detail`, `cache_control`, and other unverified image fields.
- Do not add advanced or multimodal fields that are outside the supported subset.
- Link to <https://runapi.ai/models/mimo.md> for pricing instead of copying values.
