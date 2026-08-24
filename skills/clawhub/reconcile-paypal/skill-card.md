## Description:

Read-only PayPal transaction reconciliation for OpenClaw that finds a transaction by approximate date, amount, and currency, identifies the downstream merchant, and captures accounting evidence with minimal browser round-trips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[calibhden](https://clawhub.ai/user/calibhden)

### License/Terms of Use:

MIT-0

## Use Case:

External users and finance or accounting operators use this skill to reconcile PayPal-backed credit card charges, identify the downstream merchant, and capture receipt or transaction evidence from PayPal in a read-only browser workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill views sensitive PayPal transaction history and may save receipts or reports containing financial details.

Mitigation: Use it only for intended reconciliation work, capture the minimum relevant evidence, and protect any downloaded PDF or report files.

Risk: The workflow depends on an already authenticated PayPal browser profile.

Mitigation: Do not enter passwords, OTPs, recovery codes, or security answers through the agent; stop with PAYPAL_LOGIN_REQUIRED when manual authentication is needed.

Risk: PayPal pages can expose account-changing actions such as payments, refunds, disputes, or settings changes.

Mitigation: Keep the workflow read-only and stop before any action that could move money or modify account state.

Risk: A transaction match can be uncertain when multiple candidates share similar dates or amounts.

Mitigation: Report AMBIGUOUS or NOT_FOUND rather than guessing, and include confidence and notes for human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/calibhden/skills/reconcile-paypal)
- [Publisher profile](https://clawhub.ai/user/calibhden)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Structured text or Markdown status report with optional PayPal receipt or evidence PDF file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns one reconciliation status such as MATCHED, AMBIGUOUS, NOT_FOUND, PAYPAL_LOGIN_REQUIRED, or BROWSER_TOOL_UNAVAILABLE.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter, README, and CHANGELOG report 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
