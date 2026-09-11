---
name: deepseek
description: Call the DeepSeek API (deepseek-v4-pro, deepseek-v4-flash, and deepseek-v4-flash-vision-exp) through RunAPI using OpenAI-compatible Chat Completions and Responses. Use for DeepSeek text, image input, streaming, the verified Flash function path, or an existing compatibility client that needs the conditional reference.
documentation: https://runapi.ai/models/deepseek.md
provider_page: https://runapi.ai/providers/deepseek.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/deepseek
    primaryEnv: OPENAI_API_KEY
    requires:
      env: [OPENAI_API_KEY, OPENAI_BASE_URL]
    envVars:
    - {name: OPENAI_API_KEY, required: true, description: RunAPI API key used by OpenAI-compatible DeepSeek clients.}
    - {name: OPENAI_BASE_URL, required: true, description: Set to https://runapi.ai/v1 for DeepSeek on RunAPI.}
---

# DeepSeek on RunAPI

Use OpenAI-compatible endpoints at `https://runapi.ai/v1` as the primary protocol.

## Primary protocol recipe

### Authenticate

Set `OPENAI_API_KEY` to a RunAPI API key and `OPENAI_BASE_URL` to `https://runapi.ai/v1`.

### Send request

```python
from openai import OpenAI
client = OpenAI(api_key="YOUR_RUNAPI_TOKEN", base_url="https://runapi.ai/v1")
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Explain this decision."}],
)
print(response.choices[0].message.content)
print(response.usage)
```

For long output, set `stream=True` and
`stream_options={"include_usage": True}`; consume through `[DONE]`.
`deepseek-v4-flash` additionally supports one custom function on Responses;
keep automatic tool selection and one serial call/result lifecycle.

For image input, use `deepseek-v4-flash-vision-exp` with a Chat Completions
message content array containing a text part and an `image_url` part. The image
URL must be publicly reachable and use JPEG, PNG, GIF, or WebP.

### Verify result

For Chat, require final assistant content, `finish_reason`, and `usage`. For
Responses, require final output, one usage-bearing `response.completed`, and
`[DONE]` when streaming.

### Stop boundaries

Correct a rejected shape once using the structured error. Retry transport once
only before any response or Usage and when replay is safe. Record a terminal
error and stop without changing model or protocol. Add tools, reasoning,
storage, cache controls, documents, or multimodal input only when the current
RunAPI contract verifies the exact model/protocol shape.

## Compatibility protocols

Load [compatibility protocols](references/compatibility-protocols.md) only when an existing client requires Anthropic Messages or Gemini contents.

## Supported models

| Model ID | Use when |
|---|---|
| `deepseek-v4-flash-vision-exp` | Image input and vision tasks |
| `deepseek-v4-pro` | Higher-quality verified text workloads |
| `deepseek-v4-flash` | Fast text and one verified custom-function lifecycle |

## References

- <https://runapi.ai/models/deepseek.md>
- <https://runapi.ai/providers/deepseek.md>
- <https://runapi.ai/models.md>
