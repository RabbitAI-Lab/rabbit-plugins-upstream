## Description:

Calls Gemini 2.5 and 3 series models through RunAPI using Gemini contents clients for chat, streaming, multimodal input, grounding, structured output, reasoning, or conditional compatibility-client guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Gemini requests through RunAPI, choose supported Gemini models, and apply request verification, retry, streaming, grounding, structured output, and compatibility-client guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gemini requests and submitted content are routed through RunAPI.

Mitigation: Confirm RunAPI account, billing, and data handling expectations before sending sensitive prompts or files.

Risk: The skill requires API key environment variables for use.

Mitigation: Set only the disclosed environment variables and manage API keys with standard secret-handling practices.

## Reference(s):

- [Gemini Compatibility Protocol](references/compatibility-protocols.md)
- [RunAPI Gemini Documentation](https://runapi.ai/models/gemini.md)
- [RunAPI Google Provider](https://runapi.ai/providers/google.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [RunAPI Gemini Homepage](https://runapi.ai/models/gemini)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes environment variable requirements, protocol boundaries, response verification expectations, and retry limits.]

## Skill Version(s):

0.2.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
