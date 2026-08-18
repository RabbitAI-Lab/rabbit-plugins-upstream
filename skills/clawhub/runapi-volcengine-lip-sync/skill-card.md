## Description:

Generate lip-sync video with Volcengine Lip Sync through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to synchronize mouth movement in a source video to a supplied audio track through RunAPI's Volcengine Lip Sync service. It supports one-off CLI generation and SDK-oriented integration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-selected video and audio inputs to RunAPI for lip-sync generation.

Mitigation: Use only media the user is authorized to process and confirm RunAPI/Volcengine is the intended service before execution.

Risk: RunAPI requests may be paid or metered depending on the configured account.

Mitigation: Submit a task only after authentication and contract checks pass, and do not resubmit after a task is created without user authorization.

Risk: The skill saves generated videos and JSON evidence files locally.

Mitigation: Use a dedicated output directory and verify downloaded deliverables are non-empty videos from the expected service response.

## Reference(s):

- [RunAPI Volcengine Lip Sync homepage](https://runapi.ai/models/volcengine-lip-sync)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/volcengine-lip-sync.md)
- [Provider overview](https://runapi.ai/providers/bytedance.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/volcengine-lip-sync-sdk)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-volcengine-lip-sync)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files, Code]

**Output Format:** [Markdown guidance with shell command examples, JSON request and response artifacts, local media files, and SDK integration code when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save request.json, task.json, result.json, downloaded video files, and conformance notes; expects RunAPI authentication and the runapi CLI for one-off generation.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
