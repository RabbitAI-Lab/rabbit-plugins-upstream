## Description:

Grok 视频生成应用，支持快速视频生成和标准视频生成，并通过用户提供的 api.a7w.cn API Key 创建和查询视频任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agent users use this skill to submit Grok video generation jobs, query task status, and retrieve generated video results through the a7w API using their own API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled a7w client can use the configured API key to list available apps, view recent task data, and invoke services beyond the Grok video helper.

Mitigation: Install only if that client scope is acceptable, use the least-privileged a7w key available, and review commands before execution.

Risk: The API key is stored locally or read from the environment, and host overrides can direct authenticated requests away from the default api.a7w.cn endpoint.

Mitigation: Keep keys out of repositories, use the default host unless a destination is fully trusted, and rotate the key if exposure is suspected.

Risk: Video generation calls consume the user's own a7w account points, and repeated submissions can create unexpected cost.

Mitigation: Confirm request parameters and account balance before submitting tasks, avoid duplicate submissions, and use task queries for follow-up status checks.

## Reference(s):

- [Getting Started](references/getting-started.md)
- [Grok Video Submit API](references/api-submit.md)
- [Grok Video Query API](references/api-query.md)
- [ClawHub Skill Page](https://clawhub.ai/2253128/skills/sanjianke-grok-video)
- [a7w Compute Market](https://api.a7w.cn/)
- [a7w AI Plugin Market](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided A7W_API_KEY or local ~/.a7w/config.json; asynchronous video tasks may be polled until completion.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
