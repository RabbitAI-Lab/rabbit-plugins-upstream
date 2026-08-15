## Description:

Call Gemini 2.5 and 3 series models through RunAPI using Gemini contents clients for chat, streaming, multimodal input, grounding, structured output, reasoning, and compatible clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Gemini contents clients against RunAPI, send synchronous or streaming requests, verify terminal responses, and use OpenAI-compatible chat completions only when an existing client requires that protocol.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gemini requests and submitted content are routed through RunAPI.

Mitigation: Install and use the skill only when this routing is acceptable for the intended data and workflow.

Risk: Incorrect environment variable use could expose credentials or route requests to an unintended endpoint.

Mitigation: Set only the documented API-key and base-URL environment variables for this purpose.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gemini)
- [RunAPI Gemini model documentation](https://runapi.ai/models/gemini.md)
- [RunAPI Google provider documentation](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Gemini compatibility protocol](references/compatibility-protocols.md)
- [RunAPI Gemini homepage](https://runapi.ai/models/gemini)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline bash commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GEMINI_API_KEY and GEMINI_BASE_URL for Gemini contents clients; compatibility mode may use OPENAI_API_KEY for existing OpenAI-compatible clients.]

## Skill Version(s):

0.2.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
