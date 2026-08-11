## Description:

Generate and edit images with Ideogram V3 through RunAPI. Use when the user asks an agent to create, edit, or transform images with Ideogram V3. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, remix, and reframe images with Ideogram V3 through RunAPI. It supports one-off CLI tasks and SDK-based application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or source images may be sent to RunAPI's Ideogram V3 service.

Mitigation: Review RunAPI pricing, data handling, and auth setup before use, and avoid sending private images or prompts unless that is acceptable for the workflow.

Risk: Generated file URLs are temporary and should not be treated as durable storage.

Mitigation: Download and store generated assets in durable storage within the retention window described by the skill.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the SDK integration path for apps, backends, workers, libraries, services, and production workflows.

## Reference(s):

- [RunAPI Ideogram V3 model page](https://runapi.ai/models/ideogram-v3)
- [Ideogram V3 model documentation](https://runapi.ai/models/ideogram-v3.md)
- [Ideogram provider comparison](https://runapi.ai/providers/ideogram.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-ideogram-v3)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and SDK integration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce image-generation request files, RunAPI CLI commands, SDK usage, and follow-up download steps for generated assets.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
