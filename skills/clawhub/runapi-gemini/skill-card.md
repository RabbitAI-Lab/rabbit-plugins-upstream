## Description:

Call the Gemini API through RunAPI using OpenAI-compatible clients or Gemini contents clients for chat, streaming completions, multimodal vision input, Google Search grounding, structured output, and reasoning-effort workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure Gemini requests through RunAPI, including OpenAI-compatible chat completions and native Gemini contents routes. It is intended for building or adapting applications that need Gemini text, streaming, multimodal, grounding, structured-output, or reasoning examples through a RunAPI key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, request payloads, and API credentials may be sent to RunAPI and Gemini when following this skill.

Mitigation: Use the skill only with an approved provider path, keep RUNAPI_TOKEN secret, and avoid secrets, personal data, or regulated content unless organizational policy permits that use.

Risk: The skill provides integration guidance and examples, so generated calls or model choices may need review before use in an application.

Mitigation: Review generated code and shell commands before execution, and verify current model availability, pricing, quotas, and rate limits against the linked RunAPI documentation.

## Reference(s):

- [RunAPI Gemini model page](https://runapi.ai/models/gemini)
- [RunAPI Gemini documentation](https://runapi.ai/models/gemini.md)
- [RunAPI Google provider page](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, JSON examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RunAPI API key supplied through RUNAPI_TOKEN; optional Gemini-compatible environment aliases are GOOGLE_API_KEY and GOOGLE_GENAI_BASE_URL.]

## Skill Version(s):

0.2.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
