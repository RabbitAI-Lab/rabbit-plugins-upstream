# DeepEvidence Public API Reference

This reference follows the public DeepEvidence Open Platform docs at:

<https://deepevid.medsci.cn/platform/docs>

Use this file for public skill packaging, public platform uploads, developer examples, and customer-facing integration guidance. For public marketplace listings, describe the skill as a DeepEvidence API access skill for physicians' evidence-based clinical decision support. Content is generated from retrieved literature and guidelines for clinical reference; specific diagnosis and treatment decisions remain the physician's responsibility.

## Base URL

```text
https://deepevid.medsci.cn/api/v1
```

When using the OpenAI SDK, set `base_url` to the full value above.

## Authentication

Pass the API key in the request header:

```http
Authorization: Bearer <api_key>
```

Do not log, print, commit, screenshot, or package API keys.

## Chat Completions

### POST /chat/completions

Full URL:

```text
https://deepevid.medsci.cn/api/v1/chat/completions
```

DeepEvidence is compatible with the OpenAI Chat Completions request shape. The public model is `DeepEvidence-V1`.

### Request Parameters

| Parameter | Type | Required | Public-doc description |
|---|---|---:|---|
| `model` | `string` | Yes | Model name. Current public model: `DeepEvidence-V1`. Enterprise custom models may be available when authorized. |
| `messages` | `array` | Yes | Message list. Supports `system`, `developer`, `user`, and `assistant` roles. User message `content` can be a string or an array of `text` / `image_url` parts. |
| `stream` | `boolean` | No | Whether to stream output. Default is `true`. |
| `stream_options` | `object` | No | When `{ "include_usage": true }`, usage is returned before the stream ends. |
| `user` | `string` | No | End-user identifier for multi-tenant scenarios. Prefer stable opaque non-PII IDs. |

### Text Request Example

```bash
curl https://deepevid.medsci.cn/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPEVIDENCE_API_KEY" \
  -d '{
    "model": "DeepEvidence-V1",
    "messages": [
      {"role": "user", "content": "阿司匹林的适应症有哪些？"}
    ],
    "stream": true
  }'
```

### Image Input

`messages[].content` supports OpenAI standard content parts with `text` and `image_url`.

`image_url` accepts:

- HTTPS image URLs
- base64 data URLs, such as `data:image/jpeg;base64,...`

Example:

```json
{
  "model": "DeepEvidence-V1",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "请分析这张医学图片的关键信息。" },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/medical-image.jpg",
            "detail": "auto"
          }
        }
      ]
    }
  ],
  "stream": true
}
```

### Non-Streaming Calls

The public docs show streaming examples and state that `stream` defaults to `true`. For SDK or script usage where a standard JSON response is easier to handle, set:

```json
{ "stream": false }
```

### Streaming Usage

To request usage in streaming mode:

```json
{
  "stream": true,
  "stream_options": {
    "include_usage": true
  }
}
```

## OpenAI SDK Examples

### Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPEVIDENCE_API_KEY"],
    base_url="https://deepevid.medsci.cn/api/v1",
)

resp = client.chat.completions.create(
    model="DeepEvidence-V1",
    messages=[
        {"role": "user", "content": "阿司匹林的适应症有哪些？"}
    ],
    stream=False,
)

print(resp.choices[0].message.content)
```

### Node.js

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.DEEPEVIDENCE_API_KEY,
  baseURL: "https://deepevid.medsci.cn/api/v1",
});

const resp = await client.chat.completions.create({
  model: "DeepEvidence-V1",
  messages: [
    { role: "user", content: "阿司匹林的适应症有哪些？" },
  ],
  stream: false,
});

console.log(resp.choices[0].message.content);
```

## Error Codes

| Status | Description |
|---:|---|
| `200` | Request succeeded. |
| `400` | Request parameter error. |
| `401` | Authentication failed; API Key is invalid or expired. |
| `403` | Forbidden, for example the project does not belong to the current tenant. |
| `429` | Daily quota exhausted. |
| `500` | Internal server error. |

## Public vs Internal Extensions

The current server code includes additional OpenAI-compatible or platform extension endpoints and fields, such as conversations, project attachments, QA records, feedback, `metadata`, `store`, and code-level model aliases. These are not shown in the public platform docs above.

For public distribution, marketplace uploads, public demos, and general developer documentation:

- Document only `POST /chat/completions` unless another endpoint is published in the public docs.
- Use `https://deepevid.medsci.cn/api/v1` as the base URL.
- Use `DeepEvidence-V1` as the public model name.
- Treat any project, conversation, QA, feedback, `metadata`, `store`, or private/custom model behavior as an internal or explicitly authorized extension.

For internal validation against source code, verify behavior directly in the server repository before documenting an extension publicly.

## Safety and Privacy Notes

- DeepEvidence output is generated from retrieved literature and guidelines for clinical reference.
- Specific diagnosis and treatment decisions must be made by physicians based on the individual patient or pediatric patient context.
- Clinicians should verify original literature and the latest guideline versions before applying outputs to clinical work.
- Do not use the API as an emergency triage or first-aid substitute.
- Avoid sending patient-identifiable data unless the integration, contract, consent, and compliance controls explicitly allow it.
- Log minimal operational metadata only: status, latency, token usage, model, and redacted error codes.
