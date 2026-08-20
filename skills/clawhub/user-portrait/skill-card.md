## Description:

Openclaw keeps a local user portrait so an agent can adapt replies to the user's language, expertise level, knowledge gaps, and communication preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zbc0315](https://clawhub.ai/user/zbc0315)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to make an agent communicate in language and detail calibrated to the user. It also lets the user show, correct, pause, resume, or reset the local portrait.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists a local profile of the user's language, expertise level, knowledge gaps, and communication preferences across sessions.

Mitigation: Review ~/.claude/user-portrait/profile.md periodically and use the pause or reset controls when ongoing learning is not wanted.

Risk: Profile details may influence replies in later conversations because the portrait is shared globally across sessions.

Mitigation: Use the show and correct controls to inspect and edit stored facts, and keep the portrait limited to durable person-level communication facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/user-portrait)
- [Related user-portrait Claude Code plugin](https://github.com/zbc0315/user-portrait)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with local profile-file updates and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains a local portrait file under ~/.claude/user-portrait/ and supports pause, resume, show, correct, and reset controls.]

## Skill Version(s):

0.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
