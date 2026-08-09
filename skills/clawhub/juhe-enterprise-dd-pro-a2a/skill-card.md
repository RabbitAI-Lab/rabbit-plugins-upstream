## Description:

A paid enterprise due-diligence Skill that queries Juhe for company registration details and public risk signals, then renders a concise Markdown report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this Skill for pre-cooperation company due diligence, supplier or customer risk screening, and checks for public records such as abnormal operations, enforcement, dishonesty, and consumption restrictions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The paid lookup sends the queried company name, registration number, or unified social credit code to Juhe and uses an Alipay payment flow.

Mitigation: Obtain explicit user confirmation before payment and query submission, and send only the single required enterprise identifier.

Risk: Reports may contain public but sensitive identifiers, including legal representative names, shareholder names, registered addresses, credit codes, case information, and possible identity-number-like fields.

Mitigation: Show and retain only the fields needed for the report, avoid logging full report data, and mask values determined to be personal ID numbers.

Risk: Risk modules return only the most recent page and the rendered report applies display caps, so the output is not a complete legal or credit record.

Mitigation: State that listed records are partial recent records, direct users to official sources for complete checks, and avoid legal, credit, or cooperation recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-dd-pro-a2a)
- [Skill Instructions](artifact/SKILL.md)
- [Output Format](artifact/OUT_FORMAT.md)
- [Product Scope](artifact/PRODUCT.md)
- [Return Data Reference](artifact/README.md)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown report with tables, summary signals, payment-flow guidance, and bounded command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid lookup accepts one enterprise name, registration number, or unified social credit code. Risk modules are limited to the most recent page, with report display caps for enforcement, dishonesty, consumption restriction, and change records.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
