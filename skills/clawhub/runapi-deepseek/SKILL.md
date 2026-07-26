---
name: deepseek
description: Call the DeepSeek API (deepseek-v4-pro, deepseek-v4-flash) through RunAPI using the official OpenAI SDK, Anthropic SDK, or compatible clients. Use when the user asks for DeepSeek chat, Responses, streaming completions, a single custom function on Flash, Anthropic Messages compatibility, Gemini contents compatibility, or when they want to point an existing LLM SDK setup at RunAPI as the base URL.
documentation: https://runapi.ai/models/deepseek.md
provider_page: https://runapi.ai/providers/deepseek.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/deepseek
    primaryEnv: OPENAI_API_KEY
    requires:
      env:
      - OPENAI_API_KEY
      - OPENAI_BASE_URL
    envVars:
    - name: OPENAI_API_KEY
      required: true
      description: RunAPI API key used by OpenAI-compatible DeepSeek clients.
    - name: OPENAI_BASE_URL
      required: true
      description: Set to https://runapi.ai/v1 for DeepSeek on RunAPI.
    - name: ANTHROPIC_API_KEY
      required: false
      description: Optional RunAPI API key alias when using Anthropic Messages examples.
    - name: ANTHROPIC_BASE_URL
      required: false
      description: Optional base URL for Anthropic-compatible DeepSeek requests.
---

# DeepSeek on RunAPI

DeepSeek on RunAPI exposes **OpenAI-compatible Chat Completions and Responses**
plus **Anthropic-compatible Messages**. Use the OpenAI SDK for most
integrations, or point Anthropic-compatible clients at `https://runapi.ai` when
the existing application already speaks `/v1/messages`.

## Setup

```dotenv
OPENAI_API_KEY=YOUR_RUNAPI_TOKEN
OPENAI_BASE_URL=https://runapi.ai/v1
```

Get a RunAPI API Key at <https://runapi.ai/api_keys>.

## OpenAI-compatible setup

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_RUNAPI_TOKEN",
    base_url="https://runapi.ai/v1",
)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_RUNAPI_TOKEN",
  baseURL: "https://runapi.ai/v1",
});
```

## Core recipe - Chat Completions

```python
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Explain vector databases simply."}],
)
print(response.choices[0].message.content)
print(response.usage)
```

```typescript
const response = await client.chat.completions.create({
  model: "deepseek-v4-pro",
  messages: [{ role: "user", content: "Explain vector databases simply." }],
});
```

## Responses API - one Flash function

`deepseek-v4-flash` supports one custom function with automatic selection. Do
not send `tool_choice`.

```python
tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Get weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
            },
        },
        "required": ["city"],
    },
}

response = client.responses.create(
    model="deepseek-v4-flash",
    input="What is the weather in Shanghai?",
    tools=[tool],
)

call = next(item for item in response.output if item.type == "function_call")
followup = client.responses.create(
    model="deepseek-v4-flash",
    input=[
        {
            "type": "function_call",
            "call_id": call.call_id,
            "name": call.name,
            "arguments": call.arguments,
        },
        {
            "type": "function_call_output",
            "call_id": call.call_id,
            "output": {"temperature_c": 28, "conditions": ["sunny"]},
        },
    ],
    tools=[tool],
)
print(followup.output_text)
```

The same lifecycle is available as one OpenAI `tool_calls` / tool result pair
or one Anthropic `tool_use` / `tool_result` pair.

```bash
curl -X POST "https://runapi.ai/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_RUNAPI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [{"role": "user", "content": "Hello, DeepSeek!"}]
  }'
```

## Streaming

```python
stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Write a concise release note."}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

Streaming returns incremental output without holding an application request
open for the full generation. Long generations should always stream.

## Anthropic Messages compatibility

```python
import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_RUNAPI_TOKEN",
    base_url="https://runapi.ai",
)

message = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Draft a migration checklist."}],
)
print(message.content[0].text)
```

```bash
curl -X POST "https://runapi.ai/v1/messages" \
  -H "x-api-key: YOUR_RUNAPI_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Summarize this incident."}]
  }'
```

`max_tokens` is required for Anthropic-compatible requests.

## Gemini contents compatibility

```bash
curl -X POST \
  "https://runapi.ai/v1beta/models/deepseek-v4-flash:streamGenerateContent" \
  -H "x-goog-api-key: YOUR_RUNAPI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      { "role": "user", "parts": [{ "text": "Write a short product FAQ." }] }
    ]
  }'
```

Use this path only when the caller already expects Gemini `contents` streaming.
RunAPI accepts this client shape for DeepSeek streaming.
For new app code, prefer the OpenAI-compatible setup.

## List models

```bash
curl https://runapi.ai/v1/models \
  -H "Authorization: Bearer YOUR_RUNAPI_TOKEN"
```

## Supported models

| Model ID | Use when |
|---|---|
| `deepseek-v4-pro` | Higher-quality DeepSeek text and reasoning tasks |
| `deepseek-v4-flash` | Fast text and one custom-function lifecycle |

## Consistent cross-protocol subset

- Both models support text input, sync responses, SSE terminal events,
  canonical token Usage, and protocol-specific public errors on Chat,
  Responses, and Messages.
- Flash supports one custom function and one serial call/result lifecycle.
  Omit `tool_choice`; automatic selection is supported.
- Do not send tools to Pro when consistent behavior is required. Multiple or
  parallel calls, explicit tool selection, hosted/MCP/non-function tools,
  Responses state or storage, reasoning references or controls, prompt-cache
  controls, signed thinking, citations, documents, and multimodal content are
  outside this subset.
- Requests outside the subset may return a 4xx response before Usage reservation.
  RunAPI does not silently drop these fields.
- A Responses stream is complete after one usage-bearing
  `response.completed` and `[DONE]`; a Messages stream ends with terminal
  `message_delta` Usage and `message_stop`.
- Terminal Usage is preserved as returned; RunAPI does not synthesize cache
  fields.

## References

- Model overview, pricing, and rate limits: https://runapi.ai/models/deepseek.md
- Provider comparison: https://runapi.ai/providers/deepseek.md
- Catalog: https://runapi.ai/models.md

## Agent rules

- Keep API keys in `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `RUNAPI_TOKEN`, or a
  secret manager; never inline them in commits or shell history.
- Default new integrations to the OpenAI-compatible client at
  `https://runapi.ai/v1`.
- Use streaming for responses longer than a few hundred tokens.
- For pricing, rate-limit, and commercial-usage answers, link to
  https://runapi.ai/models/deepseek.md rather than copying values.
