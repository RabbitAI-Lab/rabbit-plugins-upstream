## Description:

Generate and edit video with Hailuo through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform video with Hailuo through RunAPI. It supports one-off CLI video generation and points developers to SDKs for application or backend integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video prompts or source media may be sent to RunAPI/Hailuo.

Mitigation: Confirm the user is comfortable with external processing before submitting sensitive prompts or media.

Risk: RunAPI authentication uses an API key or CLI login.

Mitigation: Prefer environment-based or saved CLI authentication and avoid exposing the API key in command output, logs, or committed files.

Risk: Generated file URLs are temporary.

Mitigation: Download needed generated assets into durable storage within the documented retention window.

## Reference(s):

- [RunAPI Hailuo model page](https://runapi.ai/models/hailuo)
- [RunAPI Hailuo documentation](https://runapi.ai/models/hailuo.md)
- [RunAPI Minimax provider comparison](https://runapi.ai/providers/minimax.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill reference](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to generate video files through RunAPI; returned file URLs are temporary and should be downloaded for durable storage.]

## Skill Version(s):

0.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
