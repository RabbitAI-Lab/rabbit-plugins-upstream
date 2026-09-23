## Description:

动作迁移，基于参考图片和输入视频生成动作迁移后的视频结果，支持提交任务和查询任务，并需要使用者自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit action-transfer jobs that generate a new video from a reference person image and an input motion video, then query the asynchronous task result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included client is broader than the advertised action-transfer workflow and can use the configured a7w API key to call other paid platform features.

Mitigation: Use a dedicated low-balance or restricted API key, monitor point usage, and run only commands needed for the action-transfer workflow.

Risk: The workflow submits face, image, and video content to a third-party remote service.

Mitigation: Do not submit sensitive or non-consensual face or video content; review content-rights and consent requirements before use.

Risk: Changing the API host can send the API key and media task requests to an untrusted endpoint.

Mitigation: Use the default api.a7w.cn host unless a trusted administrator has approved another host.

## Reference(s):

- [Getting started](references/getting-started.md)
- [Submit API](references/api-submit.md)
- [Query API](references/api-query.md)
- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-action-transfer)
- [a7w API marketplace](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, code]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included client emits JSON to stdout and may write local API-key configuration when the user runs login.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
