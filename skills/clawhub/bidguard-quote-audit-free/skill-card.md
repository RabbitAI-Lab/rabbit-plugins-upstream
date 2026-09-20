## Description:

Free local bid-quotation checker that audits line-item arithmetic and flags missing quantity, unit-price, or amount fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, estimating, and bid teams use this skill to self-check a single quotation for mechanical line-item errors and missing pricing fields before submission. It supports review preparation, not formal bid evaluation or award decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may assume the free version checks totals, tender caps, or written-figure consistency because one description is broader than the runtime behavior.

Mitigation: Treat the runtime checks_given and checks_withheld fields as authoritative; verify totals, tender caps, written figures, bid-bond ratios, and unbalanced pricing through separate review.

Risk: Users may treat the audit output as a formal bid evaluation decision.

Mitigation: Use the output as a mechanical arithmetic self-check only; final determinations remain with qualified reviewers or the evaluation committee.

Risk: Incomplete or ambiguous quotation input can prevent reliable checking.

Mitigation: Provide complete tabular quotation text or structured items with quantity, unit price, and amount fields; when input is insufficient, the skill returns no conclusion.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/bidguard-quote-audit-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON audit result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checks performed, checks withheld, arithmetic differences, missing fields, and insufficient-input status without fabricating conclusions.]

## Skill Version(s):

1.0.53 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
