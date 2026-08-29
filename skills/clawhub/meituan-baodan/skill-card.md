## Description:

美团爆单操盘手 helps local-service merchants design Meituan group-buying plans covering competitor research, SKU architecture, pricing, promotions, cold starts, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikogeyu-cell](https://clawhub.ai/user/mikogeyu-cell)

### License/Terms of Use:

MIT-0

## Use Case:

External local-service merchants and operators use this skill to create Meituan group-buying launch and optimization plans. It guides the agent through nearby competitor research, price-band analysis, tiered SKU design, promotion planning, cold-start actions, and pre-launch compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pricing, platform-rule, or compliance advice may be outdated or unsuitable for a specific merchant, category, city, or promotion period.

Mitigation: Verify current Meituan rules, activity thresholds, category restrictions, and local regulations before publishing or acting on the plan.

Risk: Competitor research based on web results can be incomplete or stale.

Mitigation: Use dated, source-labeled competitor data and refresh the research before finalizing prices or SKU positioning.

## Reference(s):

- [Meituan Marketing Tools Rulebook](artifact/references/marketing-tools.md)
- [Group-Buying Plan Compliance Checklist](artifact/references/compliance.md)
- [Competitor Research Template](artifact/assets/competitor-research-template.md)
- [HTML Report Skeleton](artifact/assets/html-report-skeleton.html)
- [ClawHub Skill Page](https://clawhub.ai/mikogeyu-cell/skills/meituan-baodan)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown guidance with HTML report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prompt the agent to search the web for current competitor and platform-rule data before producing merchant-facing recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
