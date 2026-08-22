## Description:

Generate and edit video with Kling through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate, edit, or transform video with Kling through RunAPI, using the CLI for one-off work and SDK references for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, request metadata, and selected local media may be sent to RunAPI/Kling for processing.

Mitigation: Use API credentials intentionally and avoid submitting sensitive source media unless upload is intended.

Risk: Generated media download URLs may need review before files are saved locally.

Mitigation: Inspect returned URLs and verify downloaded files are non-empty and match the expected media type.

## Reference(s):

- [RunAPI Kling homepage](https://runapi.ai/models/kling)
- [Kling model documentation](https://runapi.ai/models/kling.md)
- [Kuaishou provider overview](https://runapi.ai/providers/kuaishou.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Kling SDK integration](https://github.com/runapi-ai/kling-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell command examples and JSON request handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create request, task, result, and downloaded media files during agent execution.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
