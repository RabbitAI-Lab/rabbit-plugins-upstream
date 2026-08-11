## Description:

Generate and edit video with Luma through RunAPI. Use when the user asks an agent to create, edit, or transform video with Luma. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, or transform video with Luma through RunAPI. It guides one-off CLI use as well as SDK-based integration for applications and services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users must trust RunAPI and configure either the runapi CLI or RUNAPI_API_KEY before use.

Mitigation: Confirm the publisher and service are acceptable before installation, then prefer environment authentication or saved CLI configuration for agent runs.

Risk: Generated media URLs are temporary and may not remain available for long-term access.

Mitigation: Download and store generated media in durable storage within 7 days.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the language SDK integration path for apps, services, workers, and production workflows.

## Reference(s):

- [RunAPI Luma model overview](https://runapi.ai/models/luma)
- [RunAPI Luma documentation](https://runapi.ai/models/luma.md)
- [RunAPI Luma provider comparison](https://runapi.ai/providers/luma.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-luma)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include CLI authentication steps, SDK package choices, request-field inspection, and storage reminders for temporary generated media URLs.]

## Skill Version(s):

0.2.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
