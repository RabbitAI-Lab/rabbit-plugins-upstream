## Description:

A Chinese-language local helper that checks bid quote line arithmetic and missing quantity, unit price, or total fields without requiring payment, registration, an API key, or network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, estimating, and bid-preparation users can run this skill before submission to find mechanically provable quote-table issues such as line-total arithmetic mismatches and missing quote fields. It supports a quick local pre-check but does not replace legal, procurement, or bid committee review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical quote checks as a procurement, legal, or bid committee decision.

Mitigation: Present results as local arithmetic and missing-field findings only, and require qualified human review before using them in a procurement decision.

Risk: The free version intentionally omits broader bid checks such as subtotal, bid-ceiling, amount-in-words, bond-ratio, and unbalanced-bid checks.

Mitigation: List withheld checks with the result so users can route remaining bid-review work to other controls or reviewers.

Risk: Incomplete or malformed inputs could otherwise lead to false reassurance.

Mitigation: Return an insufficient-input outcome with missing fields and remediation guidance instead of producing a pass/fail conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bidguard-quote-audit-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable terminal output or JSON containing executed checks, withheld checks, findings, summary, note, and disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns insufficient-input status and missing-material guidance instead of a quote conclusion when the provided material cannot be checked.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
