## Description:

Audits user-supplied cosmetic offers with evidence-graded price, gift, bundle, and history comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to compare two or more user-supplied cosmetic offers under the same product, region, currency, and fulfillment assumptions. It helps audit cash landed price, bundle allocation, gift net value, evidence quality, historical offers, and purchase-readiness limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a bounded comparison as real-time full-market price discovery.

Mitigation: State that conclusions apply only to the current provided sample and require fresh checkout-page confirmation before purchase.

Risk: Users may provide private account, payment, address, order, or login-state information while collecting offer evidence.

Mitigation: Use only public or user-supplied offer evidence and avoid collecting or retaining private purchasing data.

Risk: Incomplete discounts, mandatory costs, bundle components, or gift details can make rankings misleading.

Mitigation: Keep unknown values null or unresolved, exclude ineligible offers from rankings, and record evidence downgrade reasons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/beauty-offer-auditor)
- [Offer Snapshot v2](references/offer-snapshot-v2.md)
- [Beauty offer audit output template](references/output-template.md)
- [Generic example case](examples/generic-case.json)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, guidance]

**Output Format:** [Markdown report with structured offer snapshot fields and evidence-linked tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follows the user's selected language and region; unknown values remain null or explicitly unresolved.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
