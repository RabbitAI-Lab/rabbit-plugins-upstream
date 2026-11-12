## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use the skill to maintain continuity by recording and recalling emotion-linked experiences, tracking self-state, and writing subjective journals in Notion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the skill suspicious with medium confidence, citing persistent core-context edits and Notion capabilities beyond the stated memory and journaling purpose.

Mitigation: Review and approve core-context changes, keep recoverable versions, limit Notion access to required databases, and check write targets.

Risk: Only 10 of 41 components were fully inspected, leaving behavior in many scripts uncertain; the scan guidance also calls out an unpinned installer.

Mitigation: Review the remaining scripts and inspect and pin the installer source before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Emotion scale and history migration](references/emotion-scale.md)
- [Experience recall](references/experience-recall.md)
- [Heartbeat sensing](references/heartbeat-sensing.md)
- [Memory transition](references/memory-transition.md)
- [Vent journal](references/vent-journal.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, JSON records and state snapshots, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create persistent Notion records and local workspace state; requires Node.js and configured Notion access for Notion operations.]

## Skill Version(s):

2.1.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
