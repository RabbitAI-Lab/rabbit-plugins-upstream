## Description:

查询亚马逊关键词的搜索量、购买量、购买率及同比、环比和近三个月增长率，帮助判断需求趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and researchers use this skill to assess keyword demand and seasonality across supported marketplaces using search, purchase, and growth trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade qhkit and Node, or change the user's PATH or shell profile.

Mitigation: Review setup commands and PATH changes first; prefer a preinstalled, pinned qhkit version.

Risk: Configuring the required Qinghu API token and calling the paid tool may expose credentials or spend credits.

Mitigation: Handle the token securely, check estimated credits, and obtain the user's approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Concise trend analysis with supporting figures; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures identify marketplace and period; if data is unavailable, provides query parameters and an analysis framework without invented figures.]

## Skill Version(s):

0.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
