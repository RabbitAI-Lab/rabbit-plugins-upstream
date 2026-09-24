## Description:

Happy Horse（HappyHorse-1.1 系列）面向文生/图生高质量短视频，采用统一多模态建模，可一阶段生成声画、支持多语言对白与多镜头场景衔接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External creators, developers, and agents use this skill to submit Happy Horse text-to-video or image-to-video jobs, create tasks, and query generated video results through api.a7w.cn. It is useful when an agent needs documented parameters, command examples, and a zero-dependency Python client for Happy Horse video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use the user's a7w API key across the marketplace, not only the Happy Horse app.

Mitigation: Use a dedicated low-balance or scoped key where possible, and review any generated command before it calls a non-happy_horse app.

Risk: Submitting or repeating asynchronous generation jobs can consume account points or freeze balance.

Mitigation: Check the intended model, duration, resolution, and media before submission; avoid repeated submissions and use task queries to follow existing jobs.

Risk: Prompts and media URLs are sent to the third-party a7w service for processing.

Mitigation: Avoid private prompts, confidential media URLs, or sensitive source material unless the user has approved sending them to api.a7w.cn.

## Reference(s):

- [Getting started](references/getting-started.md)
- [General notes](references/通用说明.md)
- [Submit API](references/api-submit.md)
- [Create API](references/api-create.md)
- [Query API](references/api-query.md)
- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-happy-horse-video)
- [a7w API platform](https://api.a7w.cn/)
- [AI plugin market](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with command examples and JSON API responses from the bundled client]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided api.a7w.cn API key; asynchronous video jobs return task identifiers and can be polled for JSON results.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
