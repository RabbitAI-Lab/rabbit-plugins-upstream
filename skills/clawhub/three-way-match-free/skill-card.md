## Description:

Checks purchase orders, goods receipts, and invoices for document-level inconsistencies, duplicate invoice numbers, and leftover template placeholders with line-referenced findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, procurement, and accounts payable users can use this skill for a preliminary local three-way match before payment review. It compares supplied purchase order, goods receipt, and invoice text and reports supported issues with source line references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a clean preliminary match as approval to pay.

Mitigation: Present results as limited document-level evidence and require normal finance approval before payment.

Risk: The skill does not verify invoice authenticity, supplier legitimacy, tax math, date logic, or payment authorization.

Mitigation: Pair the output with invoice validation, supplier due diligence, tax review, date checks, and payment authorization controls where those decisions matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/three-way-match-free)
- [Free web version](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON with line-referenced findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns no conclusion when input evidence is insufficient; findings are limited to the implemented document-level checks.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
