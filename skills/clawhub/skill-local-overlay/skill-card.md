## Description:

Preserves local changes to marketplace, connector, and built-in skills with snapshots, an append-only patch ledger, and replay guidance after upgrades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill before modifying marketplace, connector, or built-in skills and after upgrades that may overwrite local edits. It guides them to snapshot originals, record minimal changes in an append-only ledger, and review patch replay after upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patches change installed skill behavior and may introduce incorrect guidance.

Mitigation: Review and test each patch and its replay before relying on the changed skill.

Risk: Snapshots and change history remain on the machine until removed.

Mitigation: Protect the overlay files from unintended access and review their contents before retaining them.

Risk: The published frontmatter version field is malformed and may interfere with parsing or installation.

Mitigation: Have the publisher correct and validate the version field before installation.

## Reference(s):

- [Skill Local Overlay on ClawHub](https://clawhub.ai/haiyangchenbj/skills/skill-local-overlay)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with file paths and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include snapshot instructions, append-only ledger entries, patch summaries, and replay status.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
