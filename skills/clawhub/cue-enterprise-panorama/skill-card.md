## Description:

Uses Cue to generate an enterprise due-diligence draft covering company registration, ownership, financials, operations, compliance, risks, and supply-chain finance opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business, credit, and partnership review teams use this skill to request company panorama reports from Cue and receive a structured Markdown due-diligence draft with source links. It is suited to pre-credit review, customer onboarding, supply-chain finance screening, peer comparison, and early risk triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends company names, due-diligence prompts, and generated reports to Cue/cuecue.cn.

Mitigation: Use it only when Cue's data handling is approved for the organization, and avoid confidential targets or internal investigation context.

Risk: The skill depends on an external runner and Cue service behavior outside the artifact itself.

Mitigation: Review, pin, or verify the runner source before use, and run the documented health checks before requesting reports.

Risk: Referral, payment, and share-link behavior may include vendor messaging.

Mitigation: Treat credit, referral, payment, and share-link guidance as vendor-specific instructions rather than neutral agent advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-enterprise-panorama)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner source referenced by the skill](https://github.com/sensedeal/cue-skills)
- [Gitee mirror referenced by the skill](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source links and Cue share URL, plus setup, health-check, and conversion commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; report quality and freshness depend on Cue service availability and public data source coverage.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
