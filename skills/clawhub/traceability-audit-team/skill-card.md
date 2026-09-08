## Description:

可追溯审计团 is an audit workflow for tracing AI identities, digital humans, generated content, theories, or claimed identities through three-anchor verification, evidence-chain review, standards mapping, and report drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, auditors, compliance reviewers, and external users use this skill to structure traceability audits for AI subjects, digital identities, generated content, theories, or identity claims. It guides evidence collection, standards alignment, finding classification, and report drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package's shipped integrity metadata does not match the actual SKILL.md file.

Mitigation: Review the package before installing and verify file hashes against the server evidence for this release.

Risk: The artifact claims local-only operation while the workflow requires online checks for current standards and identity evidence.

Mitigation: Require explicit user approval before any external lookup or submission of identifiers to online services.

Risk: Traceability audits can involve sensitive identity, company, credential, or behavioral data.

Mitigation: Keep report redaction enabled by default and avoid exposing raw identifiers unless the user explicitly approves disclosure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/traceability-audit-team)
- [Evidence Chain Checklist](artifact/references/evidence-chain-checklist.md)
- [Audit Report Template](artifact/references/audit-report-template.md)
- [Standards Map](artifact/references/standards-map.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown audit reports, evidence-chain checklists, standards mappings, findings, and recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should separate verified facts from inferences, cite evidence for each conclusion, redact sensitive identifiers, and require user approval before external checks.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, artifact/manifest.json, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
