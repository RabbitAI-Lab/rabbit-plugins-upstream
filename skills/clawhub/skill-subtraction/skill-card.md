## Description:

Skill Subtraction audits installed AI skills and generates keep, archive, or uninstall recommendations using domain classification, weighted scoring, deduplication, and batch-install detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inventory installed skills, classify their value, and decide which skills to keep, archive, or uninstall. It is intended for periodic skill-set cleanup across supported agent platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skill inventory can expose installed skill names, paths, and related local metadata.

Mitigation: Install only if this inventory is acceptable; use the default scan scope unless a broader --all or custom workspace scan is intended.

Risk: Cleanup recommendations could lead to archiving or uninstalling useful skills if approved without review.

Mitigation: Use report-only review first and approve archive or uninstall actions only after checking each proposed change.

## Reference(s):

- [Evaluation Framework](references/evaluation_framework.md)
- [Example Audit Reports](examples/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown audit report with structured tables, optional JSON scan output, and cleanup command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports English and Chinese report output; cleanup actions require explicit user confirmation.]

## Skill Version(s):

1.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
