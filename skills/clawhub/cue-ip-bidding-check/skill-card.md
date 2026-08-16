## Description:

用 Cue 整合企业专利、软著、商标、资质许可、招投标与融资记录，帮助判断公开可见的技术能力与商业落地证据，并产出可复核的硬实力证据底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, procurement teams, and agents use this skill to run Cue-based due diligence on a target company before bidding, supplier onboarding, technical diligence, or commercial-readiness review. It focuses on public evidence for intellectual property, certifications, bidding records, financing history, and source-linked conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The target company name, due-diligence query, and API-key-authenticated requests are sent to Cue's external service.

Mitigation: Use the skill only for approved targets and avoid confidential or regulated investigation subjects unless the organization has approved sending that information to cuecue.cn.

Risk: Generated reports may depend on Cue service availability and the freshness or reachability of external public data sources.

Mitigation: Run the documented health checks before use, retry interrupted jobs with the same query, and review source links in the generated report before relying on conclusions.

Risk: The local runner is referenced as a setup dependency.

Mitigation: Review the referenced runner repository before first setup and keep API keys in the documented Cue configuration or environment variable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-ip-bidding-check)
- [Cue service](https://cuecue.cn)
- [Cue sample report](https://cuecue.cn/share/buddy-template-063fa4f79b2c)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown due-diligence report with source links, plus setup and run commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report quality and freshness depend on Cue service availability and external public data sources.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
