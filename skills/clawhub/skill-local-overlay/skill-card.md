## Description:

Skill Local Overlay helps agents preserve local edits to marketplace, connector, and built-in skills by using snapshots, a patch ledger, and replay after upgrades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill before modifying marketplace, connector, or built-in skill files, and after upgrades, to preserve and replay local changes with an auditable snapshot and ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide changes to installed marketplace, connector, or built-in skills, which may affect future agent behavior.

Mitigation: Review each proposed patch before applying it and keep the snapshot and ledger so changes remain auditable and reversible.

Risk: Local patches may become stale when upstream skill files are restructured during an upgrade.

Mitigation: Replay patches only after comparing the new upstream file with the recorded snapshot, and mark entries for human review when they no longer apply cleanly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/skill-local-overlay)
- [ClawHub publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status report with paths, ledger entry details, patch summaries, and replay status tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
