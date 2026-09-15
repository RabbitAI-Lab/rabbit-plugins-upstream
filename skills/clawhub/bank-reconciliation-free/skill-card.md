## Description:

A free, local bank reconciliation skill that matches bank statement lines against book entries by amount and date, lists outstanding items and duplicates, and reports totals without requiring payment, registration, API keys, or network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance staff, bookkeepers, and agents use this skill to compare bank statement lines with enterprise book entries, identify unmatched records and same-date same-amount duplicates, and produce a local reconciliation summary. It supports monthly reconciliation review but does not make accounting, audit, tax, or legal judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports suspicious paid-upgrade automation instructions that ask an agent to install a mutable payment package and buy or install a separate paid skill.

Mitigation: Do not let an agent run the payment installer or purchase another skill unless the package, source, price, merchant, and permissions have been independently verified and the user personally confirms any payment.

Risk: Reconciliation findings can be incomplete or misleading when records have missing, malformed, or out-of-scope data.

Mitigation: Treat the output as an aid, review source records manually, and avoid using it as accounting, audit, tax, legal, or banking-system authority.

Risk: The free version only matches exact amounts within a fixed date window and omits checks such as near-amount matches, cross-period candidates, reconciliation identity validation as a product feature, and custom tolerances.

Mitigation: Review withheld checks before relying on the result and perform separate analysis when fee, exchange-rate, typo, cross-period, or tolerance-sensitive cases matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-reconciliation-free)
- [Sample reconciliation input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or JSON reconciliation report, often summarized in Markdown with local Node.js commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided bank and book records; reports executed and withheld checks.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
