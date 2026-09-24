## Description:

三剪客 · 智能剪辑 helps agents call the api.a7w.cn smart_clip APIs for template lookup and video mixcut workflows, including real-person broadcast, material mixcut, and news-style videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to discover smart_clip templates, inspect request parameters, configure an a7w API key, and submit video-editing jobs through the bundled zero-dependency client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client uses an a7w API key that may access the wider a7w marketplace, not only smart_clip.

Mitigation: Use a separate low-balance or restricted API key where possible, and avoid reusing broad production credentials.

Risk: A user-configured host can receive the bearer API key.

Mitigation: Do not set --host or A7W_HOST unless the destination is fully trusted; prefer the documented api.a7w.cn endpoint.

Risk: Submitted media URLs and callback endpoints may disclose sensitive workflow data to the service.

Mitigation: Submit only media URLs and callback endpoints that are intended for the video-editing workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-smart-clip)
- [a7w compute marketplace](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)
- [Getting started](references/getting-started.md)
- [General smart_clip notes](references/通用说明.md)
- [Template API reference](references/api-template.md)
- [Template detail API reference](references/api-template_detail.md)
- [Real-person broadcast API reference](references/api-realman_broadcast.md)
- [Material mixcut API reference](references/api-broadcast_mixcut.md)
- [News-style mixcut API reference](references/api-news_mixcut.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided api.a7w.cn API key; asynchronous video jobs may return task IDs and later result payloads.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
