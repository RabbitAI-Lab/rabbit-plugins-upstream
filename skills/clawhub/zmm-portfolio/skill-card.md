## Description:

詹明明·该投哪条线 helps operators running multiple business or product lines decide where to invest, where to hold, and what to cut by identifying the binding resource constraint across the portfolio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External business owners and operators use this agent skill to run a portfolio checkup across active lines, comparing revenue contribution, bottleneck-resource consumption, maintenance cost, marginal response, and cut conditions before reallocating time, cash, capacity, store space, or inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive product-line revenue, resource constraints, and related business context may be shared during the portfolio checkup.

Mitigation: Use the skill only in trusted agent environments and use pseudonyms, ratios, or coarse ranges when business details are sensitive.

Risk: The skill may save summarized business-decision notes to the configured local memory path.

Mitigation: Review and prune stored memory, and avoid providing customer names, domains, account IDs, or other direct identifiers.

Risk: Broad conversational triggers may activate the skill around product-focus or line-cutting questions.

Mitigation: Use explicit triggers and confirm the user wants a portfolio-level checkup before collecting business data.

## Reference(s):

- [理论底座](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-portfolio)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown conversation and portfolio checkup report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask staged questions and may save summarized business-decision notes to the configured local memory path.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
