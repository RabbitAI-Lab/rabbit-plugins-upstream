## Description:

Capture ideas, reference notes and tasks with searchable text and tags, then complete or archive them. Use for 随手记与待办.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users can capture ideas, reference notes, and actionable tasks, then search, complete, or archive records in their active agent workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notes and operation history are stored as unencrypted workspace files, which may expose sensitive information through workspace access or backups.

Mitigation: Avoid saving secrets or highly sensitive information, and protect workspace access and backups.

Risk: Due dates do not create reminders, and archiving retains records.

Mitigation: Use a scheduling tool when reminders are needed, and do not treat archiving as deletion.

## Reference(s):

- [Input contract](references/input.md)
- [MochiLab homepage](https://mochilab.bz)
- [ClawHub release](https://clawhub.ai/hznetnewpower/skills/mochi-quick-notes)
- [Publisher profile](https://clawhub.ai/user/hznetnewpower)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Concise text responses and structured JSON operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns record IDs and operation results; records remain in the current agent workspace. Due dates do not trigger reminders.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
