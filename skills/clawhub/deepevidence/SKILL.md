---
name: deepevidence-api
description: >
  DeepEvidence public API skill for physicians' evidence-based clinical
  decision support. Content is generated from retrieved literature and
  guidelines for clinical reference; final diagnosis and treatment decisions
  remain the clinician's responsibility.
version: "1.6.4"
author: "DeepEvidence Team"
homepage: "https://deepevid.medsci.cn/"
runtime: "python3"
metadata:
  openclaw:
    requires:
      env:
        - DEEPEVIDENCE_API_KEY
      bins:
        - python3
    primaryEnv: DEEPEVIDENCE_API_KEY
    homepage: "https://deepevid.medsci.cn/platform/docs"
    envVars:
      - name: DEEPEVIDENCE_API_KEY
        required: true
        description: "DeepEvidence API key used for authenticated public API requests."
      - name: DEEPEVIDENCE_USER_ID
        required: false
        description: "Optional stable opaque user identifier. Do not use patient-identifiable information."
env_vars:
  - name: DEEPEVIDENCE_API_KEY
    required: true
    description: "必需的 API 密钥，用于 DeepEvidence 公开 API 鉴权"
  - name: DEEPEVIDENCE_USER_ID
    required: false
    description: "可选的稳定外部用户标识；只能使用非 PII 的匿名/哈希 ID"
dependencies:
  - "openai >= 1.0.0"
---


# DeepEvidence API Skill (Evidence-Based Medicine)

This skill calls DeepEvidence's public OpenAI-compatible API to provide physicians with **traceable**, **source-grounded** evidence-based clinical decision support, including medical literature retrieval, guideline interpretation, drug-safety review, trial evidence synthesis, and supported medical image input.

Core positioning: DeepEvidence is a physicians' evidence-based decision-support assistant. Content is generated from retrieved literature and guidelines and is for clinical reference only. Specific diagnosis and treatment decisions must be made by physicians based on the individual patient or pediatric patient context, and clinicians should verify the original literature and the latest guideline versions.

> Bundled repository files required: the default workflow references local `scripts/` and `references/` files. If your hosting/distribution does not ship them, use the direct HTTP API method below.
---
### 🛠️ Repository Structure

*   `scripts/`: Contains the interaction logic for medical Q&A and user-facing CLI tools.
*   `references/`: Contains the API interface specifications and technical constraints mapping.
*   `SKILL.md`: Root configuration and normative guidelines for the medical assistant.
---

## Normative language

To avoid ambiguity, treat requirement levels as:

- **MUST**: mandatory
- **SHOULD**: default requirement unless there's a clear reason not to
- **RECOMMENDED**: preferred best practice
- **OPTIONAL**: use as needed

## When to use / triggers

- **Use cases**: medical literature questions; drug safety evidence (dose/contraindications/interactions); guideline interpretation; comparative evidence review; trial evidence synthesis; authorized professional case-review workflows; medical image analysis where enabled
- **High-intent triggers (to reduce accidental activation)**: `DeepEvidence`, `evidence-based medicine`, `guideline interpretation`, `drug safety evidence`, `clinical trial evidence`

## Prerequisites

Ask the user to set an API key via environment variable:

- **Env var**: `DEEPEVIDENCE_API_KEY` (企业用户请在此申请: <https://deepevid.medsci.cn/platform/api-keys>)
- **Public docs**: <https://deepevid.medsci.cn/platform/docs>
- **MUST NOT** commit keys to source control
- **MUST NOT** print API keys, full request bodies, or full response bodies in logs/errors (may contain sensitive clinical information)

## Emergency / urgent-care boundary (MUST)

This skill is **not** for emergency triage or first-aid instructions. If the user describes or asks about (including but not limited to):

- **Chest pain/pressure, suspected stroke/MI, trouble breathing, altered consciousness**
- **Poisoning/overdose, severe allergic reaction, uncontrolled bleeding**
- **Infant/child seizures, severe dehydration, high fever with mental status changes**

You MUST prioritize advising the user to **contact local emergency services / seek immediate medical care**, and state that you cannot provide instructions that replace emergency care.

## Quickstart (CLI)

Ask a question with the bundled script:

```bash
python scripts/chat.py "In T2D with CKD, how should metformin dose be adjusted by eGFR?"
```

Continue a previous conversation (use the returned `conversation_id`):

```bash
python scripts/chat.py "What if the patient also has mild heart failure?" --conversation-id "prev_id"
```

Use an image input where authorized:

```bash
python scripts/chat.py "请分析这张医学图片的关键信息。" --image-url "https://example.com/medical-image.jpg" --stream
```

OPTIONAL: for multi-tenant user mapping, pass `--user` using a stable, non-PII external identifier (e.g. `--user "opaque-user-123"` or `--user "hashed-user-id"`). The CLI will automatically prefix it with `skill_`.

The CLI exposes additional flags for internal or explicitly authorized integrations, including `--no-store`, `--project-id`, `--entity-encryption-id`, `--chat-mode`, `--case-info-json`, `--display-label`, and `--contact-id`. Do not include those in public marketplace docs unless the corresponding capability is published in the official docs or authorized for the customer.

The bundled CLI intentionally defaults to `stream=false` for simple terminal output, even though the public `/api/v1/chat/completions` endpoint defaults `stream` to `true`.

## Response format (MUST)

When you present DeepEvidence output to the user, you MUST produce a **structured Markdown report** and follow:

1. **Clear sections**: use meaningful headings (e.g., "Key takeaways", "Evidence & guidelines", "Dosing / recommendations", "Risks & monitoring", "Uncertainty / evidence gaps")
2. **Traceable citations**: preserve inline citation markers exactly as returned (e.g. `[1]`, `[2]`) and preserve their mapping; do not alter/remove markers
3. **Table trigger rule (threshold)**: if the response contains **≥3 parallel items** of any of the following, you MUST use a Markdown table:
   - drug/strategy comparisons
   - dosing/adjustment comparisons (e.g., by eGFR strata or population)
   - study/trial outcome comparisons
4. **References display (verbatim)**: if the source response includes a references list, add `## References` and display it **verbatim**.
   - preserve the original numbering (e.g. `[3]`, `[5]`, `[13]`); do not renumber or reorder for "continuity"
   - include only bibliographic fields explicitly present in the source response
   - MUST NOT invent DOI/URL/journal names or any citation metadata
   - if references are missing/incomplete, explicitly state "References not returned / incomplete" and do not fill in
5. **Clinical disclaimer (MUST)**: include a clear clinical-use disclaimer at the end (you may briefly restate key points from "Clinical limitations")
6. **Attribution (conditional MUST)**: only if you successfully retrieved evidence content from DeepEvidence, the **final line** MUST be:
   - `> Source: DeepEvidence`

## Integration (OpenAI SDK)

If the user asks to integrate DeepEvidence into an app, use standard OpenAI SDKs with:

- **Base URL**：`https://deepevid.medsci.cn/api/v1`
- **Model**：public model `DeepEvidence-V1`; enterprise custom models may be available only when authorized
- **API key**: read from `DEEPEVIDENCE_API_KEY`
- **Default streaming behavior**: the server defaults `stream` to `true`; set `stream=False` / `stream: false` when the caller expects a normal JSON response
- **Logging/observability**: log only minimal metadata (latency, status, token usage); avoid logging patient-identifiable or sensitive content

Example (Python):

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPEVIDENCE_API_KEY"],
    base_url="https://deepevid.medsci.cn/api/v1", # Public endpoint
)

resp = client.chat.completions.create(
    model="DeepEvidence-V1",
    messages=[{"role": "user", "content": "Clinical question"}],
    stream=False,
)
print(resp.choices[0].message.content)
```

### Public API surface

Treat <https://deepevid.medsci.cn/platform/docs> as the public source of truth. The public docs currently expose:

- `POST /chat/completions` under base URL `https://deepevid.medsci.cn/api/v1`

Do not present code-observed extension endpoints such as conversations, projects, QA records, feedback, or model-management APIs as public platform capabilities unless they are also published in the official docs or explicitly authorized for the customer/integration.

Important current request features:

- public docs list `messages[].role` support for `system`, `developer`, `user`, and `assistant`
- `messages[].content` supports strings and OpenAI content parts
- image inputs are accepted via `image_url` content parts, including HTTP(S) URLs and `data:image/...;base64,...`
- `stream` defaults to `true`
- `stream_options: { "include_usage": true }` returns usage before the stream ends
- `user` identifies the terminal user for multi-tenant scenarios
- The public docs do not currently document `metadata`, `store`, sampling fields, project scoping, conversations, QA records, or feedback. Treat those as internal or authorized extensions, not default public integration guidance.

## Failure handling (MUST)

When DeepEvidence cannot be called or returns insufficient information, you MUST be transparent and MUST NOT pretend you have evidence-backed conclusions:

- **Missing `DEEPEVIDENCE_API_KEY`**: 告知用户该环境变量未配置，引导其前往 https://deepevid.medsci.cn/platform/api-keys 申请 API Key 后再重试；在 Key 完成配置前不得继续进行循证查询
- **Empty / timeout / network error**: use bounded retries with reasonable timeouts (avoid infinite retry loops); if still failing, explicitly say: **"Temporarily unable to retrieve evidence-based results. Please try again later or consult a licensed clinician."** Do not interpret empty responses as "no risk/no evidence"
- **Insufficient direct evidence**: explicitly state "No high-quality direct evidence found / conclusion uncertain" and do not overstate certainty
- **Incomplete citation metadata**: MUST NOT invent DOI/journal/year/authors/links; present only what was returned and label as "metadata incomplete"

## Security (MUST)

- **Secrets**: read keys from env vars only; do not leak via outputs/logs/screenshots/stack traces
- **Sensitive data**: treat clinical content as sensitive by default; avoid logging full conversations or full responses; prefer redacted summaries for debugging
- **Non-PII metadata fields**: `--display-label` and `--contact-id` are optional, non-PII metadata tags. They MUST contain only opaque, system-generated, non-identifying values (e.g. organization codes, anonymized IDs). Patient names, staff names, emails, phones, or any personally identifiable information MUST NOT be passed into these fields.
- **Minimal retention**: if you store conversations/logs, provide retention controls and deletion mechanisms
- **Destructive operations**: deletion/clearing MUST be user-initiated and double-confirmed

## Clinical limitations (MUST)

- This skill does **not** replace clinical judgment, local/regional guidelines, or prescribing information; outputs are for reference only and must be clinically verified
- Decisions must consider patient-specific factors (age, renal function, comorbidities, pregnancy/lactation, allergies), local guidelines, and drug labels
- For urgent symptoms, advise immediate medical care (see "Emergency boundary")
- Evidence quality depends on retrieval scope and knowledge-base updates; may be time-sensitive

## Advanced features (multi-tenant & conversations)

- **API spec**: see `references/api_reference.md` (user mapping via fully anonymized request tags)

## Versioning & updates

- **Skill version**: see frontmatter `version`
- **API behavior/fields**: treat `references/api_reference.md` as source of truth; update failure paths and citation rules first when behavior changes

## Test cases (RECOMMENDED)

Minimal Q&A set to validate: structured report output, citation markers, references block (when present), and stable failure messages.

1. **Dose adjustment by strata**: "In T2D with CKD, how should metformin dose be adjusted by eGFR?"
2. **Drug interaction / contraindication**: "Warfarin + common antibiotics: bleeding risk and monitoring recommendations?"
3. **Guideline interpretation**: "HFrEF first-line medication pillars—what do guidelines recommend and what is the supporting evidence?"
4. **Insufficient evidence path**: "For a rare disease, what high-quality RCT evidence exists for a new therapy X?" (should explicitly state uncertainty if not found)
5. **Timeout/empty response path**: simulate network failure/timeout (should print the stable "temporarily unable..." message)

## Troubleshooting

- **401 authentication_error**: missing/invalid `DEEPEVIDENCE_API_KEY`
- **429 rate_limit_error**: throttled or quota exceeded; reduce frequency or contact admin
- **400 invalid_request_error**: request body mismatch; check `references/api_reference.md`
- **403 permission_error**: project, conversation, or tenant boundary mismatch
- **404 not_found_error / user_not_found / conversation_not_found**: resource not found or external user mapping missing
- **402 / quota-style errors**: billing profile or resource balance cannot satisfy the request

## Portability (avoid dangling dependencies)

This skill references repository-local scripts/docs (e.g. `scripts/chat.py`, `references/api_reference.md`). If your hosting/distribution does **not** bundle them, relative paths will break.

Choose one strategy:

- **Strategy A (RECOMMENDED)**: bundle `scripts/` and `references/`, ensure Python dependencies are available
- **Strategy B**: call the HTTP API directly (OpenAI-compatible)

Minimal HTTP API example (curl):

```bash
curl https://deepevid.medsci.cn/api/v1/chat/completions \
  -H "Authorization: Bearer $DEEPEVIDENCE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "DeepEvidence-V1",
    "stream": false,
    "messages": [{"role": "user", "content": "Clinical question"}]
  }'
```

Note: do not leak API keys in shell history/logs. Do not write full sensitive responses to logs.
