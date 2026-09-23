## Description:

数字人对口型（Lipsync），任务由平台弹性部署调度，支持提交和查询任务，使用时需要用户自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to configure an a7w API key, submit digital human lipsync jobs, poll task status, and retrieve JSON results such as task IDs, status, generated video URLs, dimensions, duration, and point usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can invoke marketplace apps beyond the lipsync endpoints and may consume the user's paid API points.

Mitigation: Use a limited a7w API key where possible, inspect app and API arguments before execution, and monitor account point usage.

Risk: API keys can be stored locally and sent to a configured host, including an overridden host.

Mitigation: Avoid --host or A7W_HOST unless the destination is trusted, prefer tightly scoped keys, and revoke or rotate keys after suspected exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-lipsync)
- [Getting started](references/getting-started.md)
- [Submit task API](references/api-submit.md)
- [Query task API](references/api-query.md)
- [a7w API platform](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The client can store an API key locally, call a7w marketplace endpoints, poll asynchronous jobs, and emit machine-readable JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
