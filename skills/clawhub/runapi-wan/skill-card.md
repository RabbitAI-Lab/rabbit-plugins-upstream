## Description:

Generate and edit video with Wan through RunAPI for agents that need to create, edit, or transform video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform Wan video outputs through RunAPI. For one-off tasks it guides CLI execution; for application work it directs SDK integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI task submission may incur cost.

Mitigation: Confirm the selected operation and request before submitting; submit once and preserve the task response.

Risk: Referenced local media may be uploaded to RunAPI.

Mitigation: Review file paths before execution and include only media the user intends to send.

Risk: Authentication depends on an API key or saved CLI credentials.

Mitigation: Check authentication before submitting and request a valid RUNAPI_API_KEY or saved CLI auth when needed.

Risk: Generated deliverables may be missing, empty, or the wrong media type.

Mitigation: Download every requested deliverable and verify non-empty files with the expected MIME type before reporting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-wan)
- [RunAPI Wan homepage](https://runapi.ai/models/wan)
- [RunAPI Wan model documentation](https://runapi.ai/models/wan.md)
- [Alibaba provider overview](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Wan SDK](https://github.com/runapi-ai/wan-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request JSON, task/result JSON, downloaded media files, and SDK integration guidance depending on the user's task.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
