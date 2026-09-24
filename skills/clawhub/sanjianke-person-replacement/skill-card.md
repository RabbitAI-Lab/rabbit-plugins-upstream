## Description:

人物替换，基于参考图片和输入视频生成替换后的视频结果，支持提交任务和查询任务，需要使用者自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit person-replacement video jobs to the a7w API, poll task status, and retrieve generated MP4 output URLs. It is intended for workflows where the user supplies their own API key, input media URLs, and account balance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key may be sent to a user-selected or environment-selected host if host overrides are used.

Mitigation: Use the default api.a7w.cn endpoint unless the alternate endpoint is fully trusted; avoid saved custom hosts and rotate the API key if it may have been exposed.

Risk: The bundled client can call more a7w endpoints than the person replacement submit and query endpoints.

Mitigation: Review commands before execution and use a scoped or low-balance API key for this skill.

Risk: Person images and videos can involve privacy, rights, and consent concerns.

Mitigation: Use only media that the user has rights and consent to process, and prefer short-lived private object-storage links for inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-person-replacement)
- [Getting started](references/getting-started.md)
- [Submit task API](references/api-submit.md)
- [Query task API](references/api-query.md)
- [General usage notes](references/通用说明.md)
- [a7w API service](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous submit calls return task IDs; query and polling commands return task status, usage data, and generated video URLs when available.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
