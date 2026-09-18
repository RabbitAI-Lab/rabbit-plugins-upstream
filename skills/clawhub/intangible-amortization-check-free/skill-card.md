## Description:

A local deterministic checker for intangible asset amortization ledgers that recalculates current-period amortization, accumulated amortization, carrying value, totals, duplicate asset IDs, missing fields, negative amounts, and non-positive amortization months with source-line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close or annual audit preparation to check intangible asset amortization ledgers. It helps compare ledger rows against declared formulas and reports only grounded findings when the required table fields are present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release as suspicious because the free checker embeds paid upgrade/install instructions outside the core ledger-checking purpose.

Mitigation: Use the free checker only for local ledger review, and treat any paid upgrade, marketplace install, or purchase flow as a separate trust decision that requires independent verification.

Risk: The artifact writes a small temporary marker related to the upsell prompt.

Mitigation: Expect the marker as part of the prompt behavior, and review local side effects before deploying the skill in a managed environment.

Risk: The skill produces accounting ledger checks but does not provide accounting, tax, or audit opinions and withholds several advanced checks from the free release.

Mitigation: Use results as deterministic reconciliation output only, review unsupported checks separately, and require qualified review before relying on the output for financial reporting decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/intangible-amortization-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable terminal text or structured JSON with ledger check scope, findings, and source-line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library code; materials are not sent over the network according to the artifact and security evidence.]

## Skill Version(s):

1.0.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
