## Description:

Generate and edit images and videos with Grok Imagine through RunAPI. Use when the user asks an agent to create, edit, animate, or transform media with Grok Imagine. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents that generate, edit, animate, or transform images and videos with Grok Imagine through RunAPI. It supports one-off CLI media generation and SDK-oriented application integration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts or media to external RunAPI and Grok Imagine services.

Mitigation: Confirm the user is comfortable with external processing and avoid sensitive prompts or media unless appropriate.

Risk: The skill depends on the RunAPI CLI or SDK authentication, including optional RUNAPI_API_KEY use.

Mitigation: Use environment auth or saved CLI configuration deliberately, check authentication status before use, and avoid interactive browser login unless the user requests it.

Risk: RunAPI-generated file URLs are temporary.

Mitigation: Download generated media and store it in durable storage within 7 days when the output must be retained.

Risk: Using CLI commands as a production integration layer can create fragile application behavior.

Mitigation: Use the documented SDK integration path for app, backend, worker, or production workflow integration.

## Reference(s):

- [Grok Imagine model overview](https://runapi.ai/models/grok-imagine.md)
- [RunAPI Grok Imagine homepage](https://runapi.ai/models/grok-imagine)
- [xAI provider page](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok-imagine)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, SDK package names, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of external RunAPI services; generated media URLs should be downloaded to durable storage within 7 days.]

## Skill Version(s):

0.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
