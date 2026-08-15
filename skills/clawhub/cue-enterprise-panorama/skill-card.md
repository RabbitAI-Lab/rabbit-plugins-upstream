## Description:

用 Cue 一键穿透企业的工商、股权、财务与经营全维基本面，评估业务模式与合作适配性，挖掘供应链金融与产业债机会，产出可用于内部决策的尽调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business, credit, finance, and risk teams use this skill to generate public-source enterprise due-diligence drafts for borrower review, customer onboarding, supply-chain finance exploration, peer comparison, and risk triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, query text, and the Cue API credential are used with cuecue.cn.

Mitigation: Avoid entering confidential or non-public diligence details unless the organization's data-sharing rules allow it.

Risk: The generated report depends on Cue service availability and external public data sources, which may be incomplete, delayed, or temporarily unavailable.

Mitigation: Preserve source links, review cited evidence, and verify important conclusions before using the report for decisions.

Risk: The report is a public-source pre-diligence draft rather than a substitute for formal due diligence.

Mitigation: Validate findings with internal records, contracts, financial statements, and qualified reviewers where required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-enterprise-panorama)
- [Cue service](https://cuecue.cn)
- [Cue runner source repository declared by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror declared by artifact](https://gitee.com/sensedeal/cue-skills)
- [Cue sample report](https://cuecue.cn/share/Phkgv0o_)
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn)
- [CNINFO](https://www.cninfo.com.cn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown due-diligence draft with source links and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; report quality and freshness depend on Cue service availability and public data sources.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
