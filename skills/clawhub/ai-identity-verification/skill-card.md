## Description:

Provides a Three-Anchor-One-Vote framework for checking AI agent identity and provenance using account, behavior, and memory evidence, then producing a Level 1-4 confidence report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, auditors, and teams evaluating AI agents use this skill to structure identity checks, provenance reviews, and evidence-chain reports. It is especially suited to comparing AI sessions or agents, auditing agent identity claims, and documenting when stronger cryptographic or institutional evidence is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat an identity rating as definitive proof.

Mitigation: Present conclusions as advisory confidence levels and require independent expert or cryptographic verification for legal, medical, financial, or other high-impact decisions.

Risk: Users may provide unnecessary sensitive personal, medical, legal, or account information while gathering identity evidence.

Mitigation: Collect only the minimum user-provided evidence needed for the check and avoid unnecessary sensitive data.

Risk: Weak behavioral or memory evidence can be mistaken for verified account or cryptographic proof.

Mitigation: Separate account, behavior, and memory evidence in the report, cap confidence when signatures or verifiable credentials are missing, and document contradictions explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-identity-verification)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text report with Level 1-4 confidence rating, anchor-by-anchor evidence, contradictions, and recommended next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-based advisory output; does not produce an absolute identity guarantee]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
