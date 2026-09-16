## Description:

把银行流水和企业账面记录逐笔配对，列出未达账项与重复记录，每条结论都带原文日期与金额，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, cashier, and operations users use this skill to compare bank statement lines with book entries, identify unmatched items on either side, detect same-date same-amount duplicates, and review count and amount totals. Results are mechanical reconciliation aids and require manual financial review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer users toward an unpinned external install-and-purchase flow.

Mitigation: Do not follow the paid-upgrade prompt or run the unpinned npm installer unless the package, exact version, source, and payment flow have been independently verified.

Risk: A matching flaw can misstate financial reconciliation results.

Mitigation: Treat every match and unmatched item as a draft aid and manually review the original bank and book records before making financial decisions.

Risk: Normal CLI output includes an embedded upsell.

Mitigation: Prefer JSON output for routine use when a machine-readable result without the embedded upsell is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-reconciliation-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text reconciliation report or JSON result, with command examples for running the local Node.js tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The free version reports matched pairs, unmatched bank and book entries, duplicate records, totals, withheld checks, and insufficient-input status; JSON output is preferred to avoid the CLI upsell.]

## Skill Version(s):

1.0.8 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
