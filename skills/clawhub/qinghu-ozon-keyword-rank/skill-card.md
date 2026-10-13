## Description:

查询 Ozon 热搜关键词的搜索、转化、曝光、供需和订单等指标，并按类目、周期和指标筛选排序。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and market analysts use this skill to identify promising search terms and compare keyword demand, competition and order performance across categories and reporting periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading Node and qhkit can make persistent changes and run an unpinned package.

Mitigation: Review changes and get approval before installation or upgrade; preinstall a pinned qhkit version where possible.

Risk: Configuring the paid-service API token may expose a credential if handled carelessly.

Mitigation: Use an environment variable or secret store for the token rather than passing it in visible commands.

Risk: Keyword-data requests may incur usage charges.

Mitigation: Estimate charges and get explicit approval before each paid qhkit call.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown findings with an optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports platform, reporting period, sample size and credits spent when applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
