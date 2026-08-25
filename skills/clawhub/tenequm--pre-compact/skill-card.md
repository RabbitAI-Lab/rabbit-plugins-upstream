## Description:

Prepare the session for context compaction - write a handoff file a fresh session can continue from, propose updates to the project's durable docs, apply them on approval or with `auto`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill before context compaction or context clearing to create a durable handoff note and identify stale project or agent instructions that should be updated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write durable session handoff files that may accidentally preserve sensitive details.

Mitigation: Review the generated handoff before relying on it and record secret locations, such as environment variable names or vault items, instead of secret values.

Risk: In auto mode, the skill may update persistent project or global agent instruction files without a separate confirmation.

Mitigation: Avoid auto mode unless the proposed scope has already been reviewed, especially when global files such as `~/.claude/CLAUDE.md` or `AGENTS.md` could change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/pre-compact)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/pre-compact)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown handoff file plus concise text instructions and optional documentation updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a durable handoff file and, with approval or auto mode, update project or agent instruction files.]

## Skill Version(s):

0.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
