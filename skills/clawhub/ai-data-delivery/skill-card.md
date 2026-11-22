## Description:

Build and edit source-linked ontologies from DDL or selected database metadata, then export semantic graphs for local agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

MIT

## Use Case:

Data teams and agent developers use this skill to turn SQL DDL or selected database structure into an evidence-linked semantic model, review business meanings, and hand the resulting package to a local agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exported semantic packages can contain confidential business definitions and quoted source excerpts.

Mitigation: Review the selected export scope and source excerpts before sharing, and store packages where their contents are access-controlled.

Risk: Database catalog access and local file writes rely on permissions supplied by the host; the scanner does not establish the runtime's actual permissions.

Mitigation: Use a dedicated least-privilege account for explicitly selected tables, limit host permissions to the authorized project and export paths, and verify remote database TLS settings.

Risk: The benign scan verdict has medium confidence, with partial component inspection and unresolved references.

Mitigation: Review the reported capability declarations and YAML-loading pattern, and inspect any relevant files that were not fully covered before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-data-delivery)
- [ClawHub security audit](https://clawhub.ai/franklinxkk/skills/ai-data-delivery/security-audit)
- [Read-only metadata catalogs](references/readonly-metadata.md)
- [Semantic package reader](references/semantic-package.md)
- [Architecture](references/architecture.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [Source-linked semantic graph packages (ZIP or directory), with structured JSON receipts and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Packages may preserve draft status, unresolved gaps and cited source excerpts; optional database input is limited to selected schema metadata.]

## Skill Version(s):

0.3.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
