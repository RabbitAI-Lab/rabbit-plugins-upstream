## Description:

Guides agents in calling Gemini 2.5 and 3 series models through RunAPI for chat, streaming, multimodal input, grounding, structured output, and reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure RunAPI credentials and Gemini clients, send requests, and check responses. An optional reference supports existing OpenAI-compatible Chat Completions clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and submitted content are sent to RunAPI's Gemini endpoint.

Mitigation: Send only data authorized for that provider.

Risk: A RunAPI API key is required for requests.

Mitigation: Store GEMINI_API_KEY as a secret and do not include it in shared output.

## Reference(s):

- [RunAPI Gemini documentation](https://runapi.ai/models/gemini.md)
- [RunAPI Gemini model page](https://runapi.ai/models/gemini)
- [RunAPI Google provider documentation](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Compatibility protocols](references/compatibility-protocols.md)
- [ClawHub skill listing](https://clawhub.ai/runapi-ai/skills/runapi-gemini)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes request and response-check guidance for streaming and compatibility clients.]

## Skill Version(s):

0.2.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
