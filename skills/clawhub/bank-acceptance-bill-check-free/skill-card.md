## Description:

This skill checks Chinese bank acceptance bill ledgers for maturity-date, receivable-balance, duplicate bill-number, missing-status, non-positive amount or term, and redeemed-but-still-booked issues, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, treasury, and accounting users use this skill to reconcile bank acceptance bill ledgers against stated maturity dates and receivable balances. It helps surface line-cited issues in copied or JSON-formatted ledger data while leaving authenticity, ECDS verification, and legal conclusions outside scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mixes local financial validation with a paid-install flow that asks users to run an unpinned package installer.

Mitigation: Do not run the optional paid-install command or complete any payment flow unless the installer path and source are independently reviewed and the user personally confirms payment.

Risk: Free and paid scope claims may make it unclear which checks actually ran.

Mitigation: Verify the output's executed and withheld check lists, treat the free checker results as local-only, and manually review any financial decisions that depend on omitted checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-acceptance-bill-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable ledger check report or JSON result, with shell command examples for local execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines when checks run; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
