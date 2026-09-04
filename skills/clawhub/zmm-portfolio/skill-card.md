## Description:

Helps operators running multiple business or product lines compare revenue, binding resource use, marginal return, and exit conditions to decide where to invest, maintain, shrink, or stop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External business owners and operators use this skill to run a portfolio checkup across active product or business lines, identify the binding resource, and produce a focused allocation or exit plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive business information such as revenue proportions, cash constraints, product-line names, and resource allocation decisions.

Mitigation: Use pseudonym privacy mode and avoid real product, customer, domain, or account identifiers in outputs or memory when confidentiality matters.

Risk: The skill can produce business advice that influences investment, shrink, or stop decisions across product lines.

Mitigation: Treat the output as decision support, review source data and calculations before acting, and keep execution decisions outside the agent.

Risk: Configured memory may persist portfolio context and business decisions.

Mitigation: Use the configured memory path intentionally, check what will be stored, and prefer pseudonyms for sensitive lines or customers.

## Reference(s):

- [理论底座](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-portfolio)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with tables and concise decision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include resource-allocation tables, bottleneck-resource accounting, numbered next steps, and memory notes when configured.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
