## Description:

Create OmniHuman audio-to-video tasks and helper tasks for human identification and subject-mask detection through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create talking-head video from a source image and audio file, and to run OmniHuman helper tasks for human identification or subject-mask detection through RunAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and task data are sent to RunAPI and ByteDance-backed OmniHuman services.

Mitigation: Confirm the user's approval and data suitability before submitting image, audio, or task data to the service.

Risk: Authentication may be stored in RunAPI CLI configuration when token import or interactive login is used.

Mitigation: Prefer environment-based authentication for headless agent runs and avoid exposing API keys in logs, prompts, or shell history.

Risk: Generated file URLs returned by RunAPI are temporary.

Mitigation: Download generated videos, masks, and related outputs promptly and store required results in durable storage.

Risk: Using the CLI as a production runtime integration layer can create brittle application behavior.

Mitigation: Use the RunAPI SDK integration path for apps, backends, workers, and production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-omnihuman)
- [RunAPI OmniHuman model homepage](https://runapi.ai/models/omnihuman)
- [OmniHuman model overview, pricing, and rate limits](https://runapi.ai/models/omnihuman.md)
- [OmniHuman audio-to-video variant](https://runapi.ai/models/omnihuman/1.5.md)
- [OmniHuman human-identification variant](https://runapi.ai/models/omnihuman/1.5-human-identification.md)
- [OmniHuman subject-detection variant](https://runapi.ai/models/omnihuman/1.5-subject-detection.md)
- [ByteDance provider comparison](https://runapi.ai/providers/bytedance.md)
- [RunAPI model catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RunAPI CLI or SDK instructions and notes about temporary generated file URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
