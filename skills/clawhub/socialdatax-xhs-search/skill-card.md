## Description:

用于小红书数据分析、小红书笔记搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Xiaohongshu / XHS / RedNote note search，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容研究者和市场分析人员，用关键词检索小红书笔记，并整理主题发现、竞品观察和趋势研究结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be exposed.

Mitigation: Keep SOCIALDATAX_API_KEY private and avoid including it in prompts, logs, or shared output.

Risk: The external package and hosted service have not been fully audited through the skill documentation.

Mitigation: Prefer a reviewed, pinned package version instead of @latest.

Risk: Searches may use confidential terms or consume API credits.

Mitigation: Use intended XHS research terms, avoid confidential search terms, and monitor API credits.

## Reference(s):

- [SocialDataX API access and key management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown summaries and research findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are based on the fetched search pages; they may not represent complete platform coverage.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
