## Description:

Analyzes user-provided SaaS revenue metrics to identify churn, pricing, dunning, onboarding, and upsell leaks and produce a prioritized recovery plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

SaaS founders, operators, and revenue teams use this skill to analyze provided billing, churn, pricing, onboarding, and expansion metrics and turn identified revenue leaks into a prioritized 90-day recovery plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business, pricing, dunning, or churn recommendations may be incomplete or unsuitable for a specific company if inputs are partial or inaccurate.

Mitigation: Review calculations, assumptions, and proposed customer-facing changes with the appropriate finance, legal, and operations stakeholders before implementation.

Risk: The skill works from user-provided business and customer metrics that may be sensitive.

Mitigation: Provide only the billing, customer, and SaaS metrics that are necessary for the analysis and that the user is comfortable sharing.

Risk: The skill can resemble financial advisory support even though it is a business-analysis prompt skill.

Mitigation: Treat outputs as planning guidance rather than CPA, legal, tax, or financial advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/saas-revenue-leak-detector)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown analysis with formulas, tables, prioritized recommendations, and a 90-day plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided SaaS billing and customer metrics; does not access accounts directly.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
