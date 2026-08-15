## Description:

多源研究助手整合网页搜索、学术平台、社交媒体和新闻聚合结果，帮助代理去重信息、按来源可信度分类，并生成结构化研究报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, analysts, and teams use this skill to collect information from multiple public and academic sources, remove duplicates, assess source credibility, and produce structured Chinese-language research outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request shell command execution and process local files without clearly defined operational limits.

Mitigation: Install only in low-risk workspaces, avoid exposing sensitive files or credentials, and review command or file-write actions before approval.

Risk: The skill handles external research sources whose availability, access rights, and freshness can vary.

Mitigation: Verify important claims against primary sources, record collection time when using time-sensitive sources, and keep access to paid or restricted academic content within applicable terms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/multi-source-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown research reports and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include de-duplicated findings, credibility tiers, source notes, status metadata, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
