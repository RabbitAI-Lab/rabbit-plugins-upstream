## Description:

Reviews buyer-side software and hardware purchase contracts, identifies unfavorable delivery, acceptance, payment, invoice, warranty, intellectual property, data compliance, and liability terms, and prepares a graded issue list with negotiable revisions and a redlined DOCX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longtel-skill](https://clawhub.ai/user/longtel-skill)

### License/Terms of Use:

MIT

## Use Case:

Procurement, legal operations, and business teams use this skill to review Chinese-language buyer-side software, hardware, SaaS, implementation, maintenance, framework, order, and SLA contracts before signing. It helps surface buyer protection issues, summarize negotiation points, and prepare contract revisions while preserving the boundary that high-stakes or regulated matters require qualified counsel.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill is legal-adjacent and may process confidential contract terms.

Mitigation: Use appropriate document-sharing controls, avoid unnecessary sensitive disclosure, and route high-stakes or regulated matters to qualified counsel.

Risk: Contract scans or images can reduce clause extraction and citation accuracy.

Mitigation: Prefer searchable source documents and manually review extracted clauses before relying on the issue list or revisions.

Risk: Redlined DOCX output can vary by editing environment.

Mitigation: Check the delivered DOCX to confirm additions, deletions, and replacements are visibly distinguishable before circulation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/longtel-skill/skills/buyer-side-contract-review)
- [Skill instructions](artifact/SKILL.md)
- [Test cases](artifact/test-cases.md)
- [Test report](artifact/test-report.md)
- [Maintainer contact](artifact/CONTACT.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Code, Shell commands, Guidance]

**Output Format:** [Markdown report plus redlined DOCX file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DOCX contract revisions should retain visible change tracking or equivalent redline markings when contract edits are requested.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
