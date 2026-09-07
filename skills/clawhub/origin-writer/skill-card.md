## Description:

OriginWriter helps agents write and continue long-form fiction by committing each chapter as a transaction with prose, declared state changes, and consistency gates for world state, foreshadowing, and timelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, developers, and agents use this skill to produce or continue long-form fiction while preserving story state, character knowledge, item ownership, foreshadowing, and timelines across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create or update local story package files.

Mitigation: Run it in a version-controlled project or disposable copy and review file diffs before accepting changes.

Risk: Installation guidance points to an external repository, and no server-resolved import provenance is available for this release.

Mitigation: Review the repository before installation and pin a known commit when supply-chain control is required.

Risk: Story-state gates can reduce consistency errors but do not replace author review.

Mitigation: Review generated prose, declared state changes, and gate failures before committing chapter transactions.

## Reference(s):

- [OriginWriter ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/origin-writer)
- [2origin engine repository mentioned by the skill artifact](https://github.com/dongsheng123132/2origin.git)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON transaction examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local story-package workflow guidance; generated or updated story files should be reviewed before commit.]

## Skill Version(s):

1.1.1 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
