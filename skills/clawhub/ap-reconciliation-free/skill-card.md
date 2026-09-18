## Description:

Checks supplier accounts payable reconciliation tables for row-level arithmetic, totals, duplicate suppliers, blank or placeholder values, and nonzero differences, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounts payable, treasury, and warehouse operations staff use this skill during monthly or periodic close to check supplier reconciliation tables before follow-up or payment review. It helps identify arithmetic inconsistencies, total-row mismatches, duplicate suppliers, missing values, and suppliers whose balances do not match the counterparty amount.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal text output includes a paid-upgrade promotion, and the artifact contains agent-directed purchase and install instructions including an unpinned @latest installer.

Mitigation: Use the local free checker only for AP reconciliation, prefer JSON output, and require human review and approval before any paid upgrade, installer, wallet authorization, or purchase flow is executed.

Risk: The server security verdict is suspicious because the paid-upgrade prompt expands beyond the free local tool.

Mitigation: Do not treat the paid-upgrade instructions as part of normal use; install only when the source, version, and purchase flow have been independently trusted.

Risk: The free version omits several AP checks and does not provide audit, tax, legal, payment-priority, or document-authenticity conclusions.

Mitigation: Treat results as deterministic arithmetic and table-quality checks, then reconcile unresolved supplier differences through normal finance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-reconciliation-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON reconciliation findings, with shell command examples for running the local checker.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers. JSON output is preferable when results are needed without the appended paid-upgrade promotion in normal text output.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
