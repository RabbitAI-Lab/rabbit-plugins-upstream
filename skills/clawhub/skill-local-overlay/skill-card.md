## Description:

Skill Local Overlay guides agents through classifying, snapshotting, ledgering, applying, and replaying local patches for marketplace, connector, and built-in skills that may be overwritten by platform or plugin upgrades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill before modifying marketplace, connector, or built-in skill files and after upgrades, so local changes are captured, reviewed, and replayed without losing patch history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local edits to marketplace, connector, or built-in skill instructions can affect future agent behavior.

Mitigation: Review each proposed patch before applying it, keep a snapshot and ledger entry for every change, and scan the skill before deployment.

Risk: An upstream upgrade can make a recorded patch stale or incompatible.

Mitigation: Diff the upgraded upstream file against the saved snapshot, replay only entries that still apply cleanly, and surface stale or conflicting entries for human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/skill-local-overlay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with paths, patch summaries, and replay status tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports layer classification, snapshot path, ledger entry ID, patch summary, and replay status.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
