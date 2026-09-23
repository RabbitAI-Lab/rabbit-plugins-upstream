## Description:

帮助 agent 调用 a7w seedsvc 接口提交音色修改或 AI 翻唱任务并查询结果，使用者需要提供自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to configure an a7w API key, submit source and reference audio URLs for voice conversion or AI cover workflows, and poll asynchronous task results. It is intended for agent-assisted API calls rather than local audio processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can send the configured API key to a host selected with --host, A7W_HOST, or saved configuration.

Mitigation: Use the default https://api.a7w.cn endpoint unless you intentionally trust another endpoint, and review any host override before running agent-generated commands.

Risk: API calls consume the user's a7w account points and repeated asynchronous submissions may create avoidable charges.

Mitigation: Use a limited API key, monitor billing, and prefer --no-wait plus explicit task polling when an agent might otherwise retry submissions.

Risk: The bundled client exposes generic a7w commands beyond the advertised seedsvc submit and query workflow.

Mitigation: Restrict agent use to the documented seedsvc schema, submit, query, and task operations unless a human explicitly approves broader app listing, dumping, or unrelated calls.

Risk: Submitted audio URLs and generated outputs are processed by the third-party a7w service.

Mitigation: Avoid sensitive or unlicensed audio, and perform content and rights review before publishing generated voice-conversion or cover outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-seedsvc)
- [Getting started](references/getting-started.md)
- [Submit API reference](references/api-submit.md)
- [Query API reference](references/api-query.md)
- [General a7w plugin guidance](references/通用说明.md)
- [a7w API portal](https://api.a7w.cn/)
- [AI plugin market](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous submit calls may return a task id and require polling; optional --out usage can save returned JSON.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
