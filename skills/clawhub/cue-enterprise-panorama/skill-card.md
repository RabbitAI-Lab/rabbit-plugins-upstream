## Description:

用 Cue 一键穿透企业的工商、股权、财务与经营全维基本面，评估业务模式与合作适配性，挖掘供应链金融与产业债机会，并产出可用于内部决策的尽调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external business, credit, and supply-chain finance reviewers use this skill to request a Cue-generated enterprise panorama for a target company. It supports pre-diligence, customer onboarding, peer comparison, and opportunity discovery from public-source company, ownership, financial, legal, and operating signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target company queries and generated diligence reports may be processed by Cue and stored locally.

Mitigation: Avoid confidential transaction strategy, private customer data, or non-public financial details unless organizational approval covers Cue use and the selected storage path.

Risk: Generated diligence conclusions depend on Cue service availability and public external data sources.

Mitigation: Review the report's cited sources, evidence gaps, and any source-unavailable markers before using the report for internal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-enterprise-panorama)
- [Cue report example](https://cuecue.cn/share/Phkgv0o_)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown due-diligence report with source links, plus shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Cue template template_BWILbV, requires a Cue API key, and writes generated reports to a local path selected by the user.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
