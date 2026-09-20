## Description:

Checks membership-card sales and redemption ledgers for redemption math, ending liability roll-forward, over-redemption, duplicate sales, expiration amounts, and missing fields, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance teams, store accountants, and internal auditors use this skill before month-end close, store reconciliation, or membership-card audits to check per-card ledgers for internal consistency. It is intended as audit assistance for exported ledger text, not as accounting or legal advice.

### Deployment Geography for Use:

Global; intended for Chinese-language ledger materials.

## Known Risks and Mitigations:

Risk: Users may treat ledger findings as accounting or legal determinations.

Mitigation: Review the output as audit assistance and confirm accounting or legal judgments with qualified reviewers.

Risk: Chinese-language output and field expectations may not fit every workflow.

Mitigation: Install only when Chinese-language ledger checks and the documented input columns match the intended process.

Risk: The free edition omits cross-store, cross-card-type, attribution, ranking, and cross-period checks.

Mitigation: Treat a clean result as limited to the six documented checks and use additional review for withheld or out-of-scope reconciliations.

Risk: Financial ledger text may contain sensitive business data.

Mitigation: Run checks locally and avoid sharing source ledger material unnecessarily; server evidence states the current artifact does not send ledger contents over the network.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/membership-liability-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or JSON with line-cited findings, severity levels, categories, summary counts, and verdicts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Insufficient input returns missing-field guidance without producing a consistency conclusion.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
