## Description:

公众号创作者对标账号匹配工具，基于3层加权匹配体系推荐同阶对标账号和高阶标杆账号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

WeChat Official Account creators, content operators, MCN teams, and brand marketing users use this skill to find comparable accounts, review recent article and readership signals, and identify peer or aspirational benchmarks for content planning and advertising decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and may encourage persistent shell-profile configuration.

Mitigation: Use a temporary key or a dedicated secret manager, avoid hard-coding secrets, and confirm the key can be rotated or revoked.

Risk: WeChat account query inputs are sent to RedFox for benchmarking.

Mitigation: Avoid submitting confidential account plans or sensitive campaign details unless RedFox handling is acceptable for the use case.

Risk: The skill appends subscription and enterprise sales prompts to results.

Mitigation: Review generated output before sharing it externally and remove promotional sections when they are not appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-similar-account)
- [RedFox data platform](https://redfox.hk/)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [Core workflow](references/core_workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown-style text with tables, account links, command examples, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends WeChat account query inputs to the RedFox API.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
