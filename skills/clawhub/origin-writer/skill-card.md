## Description:

OriginWriter helps agents write long-form fiction as transactional chapter commits with persisted world state, declared state changes, and gated consistency checks for characters, items, foreshadowing, and timelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agent developers use this skill to continue long-form fiction while preserving world state across sessions. It guides chapter submission as prose plus state changes, then checks consistency against forbidden zones, foreshadowing state, assertions, and prose-vs-state details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact promotes an unrelated U-King executable installer without verification guidance.

Mitigation: Do not run the installer unless its source and integrity are independently trusted and verified.

Risk: The documented init and submit commands can create or modify local story package files.

Mitigation: Use a dedicated workspace and review generated transaction files before committing them.

Risk: Long-form writing state may become misleading if chapter text and declared state changes are not reviewed.

Mitigation: Review gate failures, assertions, and prose-vs-state checks before relying on the persisted story state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/origin-writer)
- [English skill artifact](artifact/SKILL.en.md)
- [Chinese skill artifact](artifact/SKILL.md)
- [2origin repository mentioned by the skill](https://github.com/dongsheng123132/2origin.git)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce chapter text, transaction JSON, state-change declarations, and local CLI commands for a story workspace.]

## Skill Version(s):

1.1.0 (source: server release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
