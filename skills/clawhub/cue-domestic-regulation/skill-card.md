## Description:

检索中国法律法规与行政令，梳理立法背景和合规要点，并生成附来源链接的中文调研报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

企业法务、合规人员和个人可查询中国现行法规、核对法律条文出处，并研究监管要求或日常法律问题；报告不构成法律意见。

### Deployment Geography for Use:

China (legal research scope)

## Known Risks and Mitigations:

Risk: An external runner is installed and automatically updated before use.

Mitigation: Review the runner before executing it or accepting updates.

Risk: Legal research queries are sent to Cue and a stored Cue API key is used.

Mitigation: Avoid submitting sensitive case details; use a limited key if possible and protect ~/.cue/config.json.

Risk: Legal sources or conclusions may be incomplete or outdated.

Mitigation: Check cited provisions and their current validity against official sources before relying on the report.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-domestic-regulation)
- [Cue playbook](https://cuecue.cn/playbook)
- [Cue runner (external dependency, not verified release provenance)](https://github.com/sensedeal/cue-skills)
- [National Database of Laws and Regulations](https://flk.npc.gov.cn)

## Skill Output:

**Output Type(s):** [Legal research guidance, Markdown reports]

**Output Format:** [Chinese Markdown report with cited legal provisions and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides the Cue report link and a local Markdown copy when a report is available.]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
