## Description:

Helps Pinduoduo merchants preview and apply SKU price changes through a logged-in Chrome session, with price-change guardrails, audit logging, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[claw-school](https://clawhub.ai/user/claw-school)

### License/Terms of Use:

MIT-0

## Use Case:

Pinduoduo merchants and their authorized agents use this skill to preview proposed SKU price changes and, after explicit confirmation, apply or revert them in an already logged-in shop session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect price change could affect a live shop listing.

Mitigation: Review the dry-run plan with the merchant before using --execute; do not bypass the change guardrail with --force without explicit authorization.

Risk: Price updates may not take effect immediately, and a successful submission does not guarantee the displayed price changed.

Mitigation: Check the verification result and recheck the price if verification is pending; use the audit log and confirmed rollback when needed.

Risk: The audit log contains merchant pricing history.

Mitigation: Keep PDD_AUDIT_PATH unset or point it to a dedicated audit-log file under your own data directory.

## Reference(s):

- [PDD Price Update on ClawHub](https://clawhub.ai/claw-school/skills/pdd-update-price)
- [Claw School homepage](https://claw-school.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown instructions and single-line JSON results from the price-change script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview is the default; execution and rollback require explicit confirmation. Results report status and verification of the price change.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
