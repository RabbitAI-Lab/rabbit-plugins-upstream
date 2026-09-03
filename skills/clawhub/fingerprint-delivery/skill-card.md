## Description:

Fingerprint Delivery helps agents add timestamped SHA-256 fingerprints and verification files to delivery artifacts so users can check content integrity and tamper evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, documentation owners, and delivery teams use this skill to prepare HTML reports or similar deliverables with timestamped SHA-256 fingerprints and a .sha256 verification file before external handoff or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can overwrite the selected HTML file when run without --no-inject.

Mitigation: Run it only on intended deliverables and keep a backup if preserving the original file matters.

Risk: Broad multilingual trigger wording may activate the skill outside narrow document-fingerprinting requests.

Mitigation: Limit use to requests about timestamps, fingerprints, SHA-256 checksums, tamper evidence, content integrity, or delivery locking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/fingerprint-delivery)
- [SKILL.md](artifact/SKILL.md)
- [manifest.json](artifact/manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional generated verification files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SHA-256 fingerprint text and a .sha256 verification file when the helper is run.]

## Skill Version(s):

1.0.1 (source: server release metadata and target metadata; artifact frontmatter and manifest list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
