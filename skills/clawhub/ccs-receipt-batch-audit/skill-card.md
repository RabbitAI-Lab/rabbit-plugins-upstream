## Description:

Batch Ed25519 signature verification for up to 200 AI-agent audit receipts, fully offline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dshcorrectover](https://clawhub.ai/user/dshcorrectover)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and auditors use this skill to batch-check CCS AI-agent audit receipts for valid Ed25519 signatures, JCS/SHA-256 integrity, tampering indicators, and optional receipt-chain linkage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional online audit mode can send receipts and credential-like environment values to hosted or user-configured endpoints.

Mitigation: Use local mode for sensitive receipts, avoid setting CCS_API_TOKEN or payment-proof variables unless intentionally using hosted mode, and only pass --endpoint for destinations you fully trust.

Risk: JCS number handling may reject some standards-compliant receipts that contain floating-point values.

Mitigation: Test representative receipt batches before relying on automated results and manually review rejected receipts that contain floating-point values.

Risk: Automated verification identifies cryptographic and structural issues but does not decide business impact, compliance status, or audit conclusions.

Mitigation: Route tampered or invalid receipt findings to qualified human review before making security, compliance, or operational decisions.

## Reference(s):

- [Correctover Homepage](https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_batch)
- [ClawHub Skill Page](https://clawhub.ai/dshcorrectover/skills/ccs-receipt-batch-audit)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text audit report or machine-readable JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports aggregate valid/invalid counts, pass rate, failure distribution, tampered indexes, per-receipt details, and optional hash-chain status for batches of up to 200 receipts.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
