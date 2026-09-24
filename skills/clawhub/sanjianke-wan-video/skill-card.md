## Description:

Wan 模型族视频生成应用，用于通过 api.a7w.cn 创建和查询文生视频、角色参考生视频和视频编辑任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and content automation teams use this skill to submit Wan video generation jobs, poll task status, and retrieve generated video results through a command-line client and local API references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can send the user's API key to a non-default host if configured with --host or A7W_HOST.

Mitigation: Use only the default api.a7w.cn host, avoid setting --host or A7W_HOST, and revoke the API key if it may have been exposed.

Risk: Submitted media URLs and prompts are sent to a third-party video generation platform and may consume paid account points.

Mitigation: Do not submit sensitive or internal media URLs, review prompts and inputs before sending them, and check account balance and task costs before repeated submissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-wan-video)
- [Publisher profile](https://clawhub.ai/user/2253128)
- [a7w compute marketplace](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)
- [Getting started](references/getting-started.md)
- [General notes](references/通用说明.md)
- [Wan query API](references/api-query.md)
- [Wan create API](references/api-create.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON request examples, and Python CLI usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled client emits JSON responses to stdout and stores user-provided API credentials locally or reads them from environment variables.]

## Skill Version(s):

1.0.6 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
