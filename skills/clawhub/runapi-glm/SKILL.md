---
name: glm
description: Call the GLM API (GLM 5 and 4 series) through RunAPI using OpenAI-compatible Chat Completions. Use for GLM text chat, streaming, or an existing compatibility client that needs the conditional reference.
documentation: https://runapi.ai/models/glm.md
provider_page: https://runapi.ai/providers/z-ai.md
catalog: https://runapi.ai/models.md
metadata:
  openclaw:
    homepage: https://runapi.ai/models/glm
    primaryEnv: OPENAI_API_KEY
    requires:
      env: [OPENAI_API_KEY, OPENAI_BASE_URL]
    envVars:
    - {name: OPENAI_API_KEY, required: true, description: RunAPI API key used by OpenAI-compatible GLM clients.}
    - {name: OPENAI_BASE_URL, required: true, description: Set to https://runapi.ai/v1 for GLM on RunAPI.}
---

# GLM on RunAPI

Use OpenAI-compatible Chat Completions at `https://runapi.ai/v1` as the primary protocol.

## Primary protocol recipe

### Authenticate

Set `OPENAI_API_KEY` to a RunAPI API key and `OPENAI_BASE_URL` to `https://runapi.ai/v1`.

### Send request

```python
from openai import OpenAI
client = OpenAI(api_key="YOUR_RUNAPI_TOKEN", base_url="https://runapi.ai/v1")
response = client.chat.completions.create(
    model="glm-5.2",
    messages=[{"role": "user", "content": "Summarize this review."}],
)
print(response.choices[0].message.content)
print(response.usage)
```

For long output, call the same method with `stream=True` and
`stream_options={"include_usage": True}`; consume every chunk through `[DONE]`.

### Verify result

Require final assistant content, a terminal `finish_reason`, and authoritative
`usage`. A stream is complete only after its terminal usage chunk and `[DONE]`.

### Stop boundaries

Correct a rejected shape once using the structured error. Retry transport once
only before any response or Usage and when replay is safe. Record a terminal
error and stop without changing model or protocol. For `glm-5.2`, start with
text history; add tools, reasoning, structured output, or multimodal input only
when the current RunAPI contract explicitly verifies that capability.

## Compatibility protocols

Load [compatibility protocols](references/compatibility-protocols.md) only when an existing client requires Anthropic Messages or Gemini contents.

## Supported models

| Model ID | Use when |
|---|---|
| `glm-5.2` | Current flagship text workloads |
| `glm-5.1` | Recent GLM chat workloads |
| `glm-5-turbo` | Faster GLM chat |
| `glm-5` | General GLM 5 requests |
| `glm-4.7` | GLM 4.7 compatibility |
| `glm-4.6` | Stable GLM 4.6 requests |
| `glm-4.5` | GLM 4.5 compatibility |
| `glm-4.5-air` | Lightweight GLM 4.5 requests |

## References

- <https://runapi.ai/models/glm.md>
- <https://runapi.ai/providers/z-ai.md>
- <https://runapi.ai/models.md>
