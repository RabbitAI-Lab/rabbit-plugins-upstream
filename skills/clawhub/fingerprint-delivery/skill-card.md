## Description:

Helps users fingerprint HTML deliverables with SHA-256 checksums and an optional timestamp so recipients can check file integrity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theoretical text)

## Use Case:

Developers and document publishers use this skill to add a content fingerprint and optional local timestamp to an HTML deliverable and generate a separate checksum file for integrity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper modifies the selected HTML deliverable in place.

Mitigation: Keep a backup and review the selected path before running it.

Risk: A local timestamp alone does not independently prove authorship or creation time.

Mitigation: Use a trusted timestamp or external notarization if independent proof is needed.

## Reference(s):

- [ClawHub fingerprint-delivery release](https://clawhub.ai/zhaoxinghua09-cell/skills/fingerprint-delivery)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When run on a selected HTML file, the helper updates that file and writes a .sha256 checksum file.]

## Skill Version(s):

1.0.3 (source: server-resolved release; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
