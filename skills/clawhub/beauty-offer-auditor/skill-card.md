## Description:

Compare and audit two or more beauty or cosmetic offers: cash landed price, bundle split, gift net value, and evidence grade. Use for sale-season, live-stream, or duty-free price checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External shoppers and shopping assistants use this skill to compare beauty and cosmetic offers on a consistent cash-price, bundle, gift-value, and evidence-quality basis before deciding whether more verification is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide private account, order, address, phone, payment, or login/session details.

Mitigation: Use public offer details or redacted evidence only; do not collect or retain private shopping or account data.

Risk: Offer comparisons may be mistaken for real-time lowest-price guarantees or purchase execution.

Mitigation: State the time boundary, evidence grade, and current-sample scope; do not claim all-market coverage or place orders.

Risk: The README's local validation path requires cloning a repository and running Python test discovery.

Mitigation: Pin and inspect the repository revision or run validation in a disposable sandbox before executing tests.

## Reference(s):

- [Offer Snapshot v2](references/offer-snapshot-v2.md)
- [Beauty Offer Audit Output Template](references/output-template.md)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/beauty-offer-auditor)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with structured offer-snapshot fields and comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses evidence grades and conservative formulas; unknown values remain null and historical offers are excluded from current rankings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
