## Description:

汽车后市场渠道洞察专家，分析润滑油、轮胎、维修保养和汽服连锁的门店规模、省市分布、服务类型与品牌对比。适用于市场、渠道和战略团队判断强弱市场与覆盖空白。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Market, channel, and strategy teams use this skill to analyze automotive aftermarket brand networks, regional coverage, service mix, city rankings, store surroundings, and competitive gaps from the published DDT API data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends automotive brand queries and user-provided coordinates to the DDT external API.

Mitigation: Use the skill only when that external API use is acceptable for the request, and avoid sending sensitive locations or confidential business data unless approved.

Risk: API credentials could be exposed if copied into prompts, logs, skill files, or version control.

Mitigation: Keep DDT_API_KEY in the local or controlled runtime environment only, and do not include real keys in chat, logs, or repository files.

Risk: Coverage gaps, truncated previews, or API failures could lead to overconfident market conclusions.

Mitigation: Report coverage and truncation status, stop conclusions when the API indicates failure or insufficient coverage, and avoid treating missing values as zero.

## Reference(s):

- [DDT Open API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-auto-channel-expert)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise structured prose, metrics, coverage notes, and inline shell commands when setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-backed automotive aftermarket metrics and limited store or location details only when the user provides an explicit brand, public store ID, or valid coordinates.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
