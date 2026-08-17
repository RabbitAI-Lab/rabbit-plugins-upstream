## Description:

Generate and edit video with InfiniteTalk through RunAPI. Use when the user asks an agent to create, edit, or transform video with InfiniteTalk. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, or transform video with InfiniteTalk through RunAPI. It supports one-off generation through the RunAPI CLI and SDK-based integration for applications, backends, workers, and webhook pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files included in a request may be uploaded to RunAPI for processing.

Mitigation: Confirm the exact files before submission and use only files the user intends to send to RunAPI.

Risk: Video generation may use paid RunAPI capacity once a request is submitted.

Mitigation: Review the request before submission, use the intended API key or CLI login, and do not submit replacement paid tasks without user authorization.

## Reference(s):

- [RunAPI InfiniteTalk model documentation](https://runapi.ai/models/infinitetalk.md)
- [RunAPI InfiniteTalk homepage](https://runapi.ai/models/infinitetalk)
- [RunAPI Meigen AI provider overview](https://runapi.ai/providers/meigen-ai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [InfiniteTalk SDK integration](https://github.com/runapi-ai/infinitetalk-sdk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request JSON, task/result JSON handling guidance, SDK integration code, and media download verification steps.]

## Skill Version(s):

0.2.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
