## Description:

Call the DeepSeek API (deepseek-v4-pro, deepseek-v4-flash) through RunAPI using the official OpenAI SDK, Anthropic SDK, or compatible clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure DeepSeek requests through RunAPI, including OpenAI-compatible chat and Responses calls, Anthropic Messages compatibility, Gemini contents streaming, and function-call examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and API requests to RunAPI using a RunAPI token.

Mitigation: Keep tokens in environment variables or a secret manager, and only configure the RunAPI base URL when requests are intended to go through RunAPI.

Risk: Compatible SDK configuration can route existing OpenAI, Anthropic, or Gemini-style clients to RunAPI.

Mitigation: Review OPENAI_BASE_URL, ANTHROPIC_BASE_URL, and related environment variables before running commands in shared or production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-deepseek)
- [RunAPI DeepSeek homepage](https://runapi.ai/models/deepseek)
- [RunAPI DeepSeek model overview](https://runapi.ai/models/deepseek.md)
- [RunAPI DeepSeek provider comparison](https://runapi.ai/providers/deepseek.md)
- [RunAPI model catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with dotenv, Python, TypeScript, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes environment variable requirements and cross-protocol client setup guidance.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
