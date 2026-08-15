## Description:

用 Cue 沿核心企业客户/供应商/招投标关系链，挖掘产业链上下游可拓展名单，给出每家切入点和可能的金融需求，助力对公客户经理精准拓客。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External business development and commercial banking users use this skill to start from a core company and produce upstream/downstream prospecting targets with relationship context, suggested entry points, financial needs, prioritization, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends business research queries to Cue's hosted service and may involve sensitive enterprise context.

Mitigation: Use a scoped Cue API key when available and avoid sending confidential enterprise information unless that external processing is acceptable.

Risk: Generated prospecting reports depend on Cue service behavior and external data sources, which may be incomplete, stale, or temporarily unavailable.

Mitigation: Review generated reports and source links before distribution or customer outreach.

Risk: The artifact instructs users to run an external Cue runner from sensedeal/cue-skills.

Mitigation: Verify the runner source before installation and keep local credentials in the documented Cue configuration or environment variable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-prospecting)
- [Cue shared example report](https://cuecue.cn/share/Ml8DOQg5)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source cited by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror cited by artifact](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with structured prospecting lists and inline shell commands for Cue execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be converted to Word or PDF with pandoc; outputs depend on Cue service availability and external data source status.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
