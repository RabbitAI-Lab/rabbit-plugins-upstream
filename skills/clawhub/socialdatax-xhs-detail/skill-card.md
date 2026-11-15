## Description:

用于小红书数据分析、小红书笔记详情、笔记数据、互动指标、内容调研和内容分析。覆盖 Xiaohongshu / XHS / RedNote note details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve Xiaohongshu note details and engagement metrics for content research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unpinned latest-version CLI can change without review and may access credentials before installation.

Mitigation: Use a reviewed fixed CLI version where possible, and make credentials available only through the documented private local store or supported secret injection.

Risk: The security analysis is incomplete because two local references could not be resolved.

Mitigation: Review the unresolved references and reassess the skill before relying on the automated security verdict.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-detail)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Shell commands, Configuration instructions]

**Output Format:** [JSON note details with optional Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Factual note fields such as title, content, author, publish time, interaction counts and media details when available.]

## Skill Version(s):

0.1.19 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
