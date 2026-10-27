## Description:

依据官网页面清单、简介或有限发现结果生成中文llms.txt与链接校验报告，分组产品、文档和FAQ，保留可用页面并列出私有、缺资料及失败项。支持离线生成与现有索引检查；可让Agent把已读页面用于免费aimeGeo的内容与引用复测，不把索引当自动导入、部署或引擎采用证明。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

网站所有者和内容团队可用此技能，将提供的页面资料或有限的公开页面发现结果整理为分组的中文 llms.txt 索引和链接校验报告。Agent 也可检查现有索引，并在报告中明确保留缺资料、排除和请求失败状态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Choosing an existing output file can replace it.

Mitigation: Choose a new output path or preserve a copy of any file that must be kept.

Risk: A successful local validation does not establish that links are publicly reachable.

Mitigation: Check the report's evidence and online-check status; run an online check when live availability matters.

Risk: An index can expose information from pages that were not intended to be public.

Mitigation: Confirm the public status of the supplied pages before including them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xxjrq/skills/aimegeo-llms-txt)
- [Skill repository](https://github.com/xxjrq/aimegeo-llms-txt)
- [aimeGeo documentation](https://geo.aimmme.com/docs/)
- [Design reference: GEOly AI geo-llms-txt](https://clawhub.ai/geoly-geo/geo-llms-txt)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Chinese llms.txt Markdown file and a JSON link validation report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [UTF-8 files; reports distinguish local checks from online checks and record excluded, unresolved, and failed links.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata, artifact/manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
