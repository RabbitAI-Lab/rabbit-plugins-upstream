## Description:

Cursor lets an agent operate Cursor cloud sessions through the oo CLI, including session management, run tracking, model listing, and team usage reads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Cursor cloud sessions, runs, models, usage, spend, audit logs, and team members through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands.

Mitigation: Review the oo CLI installation path manually before allowing an agent to run installer commands.

Risk: The skill can access Cursor team usage, spending, audit logs, and member information.

Mitigation: Use an OOMOL/Cursor account scoped to data the agent is allowed to view.

Risk: Write and destructive actions can create, archive, cancel, unarchive, or delete Cursor sessions and runs.

Mitigation: Require explicit user confirmation of the target and payload before any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cursor)
- [Cursor Homepage](https://cursor.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read Cursor team data or perform write and destructive session actions through the oo CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
