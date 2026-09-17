## Description:

Operate Cursor through an OOMOL-connected oo CLI connector for reading, creating, updating, and deleting Cursor data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Cursor cloud-agent sessions, inspect live action schemas, run connector actions, and retrieve usage, spending, model, team, and audit-log data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that were not verified by the security evidence.

Mitigation: Review installer contents before execution and prefer official signed or otherwise verifiable installation steps.

Risk: Write and destructive Cursor actions can change, archive, cancel, or permanently delete cloud-agent sessions.

Mitigation: Require confirmation of the exact target, payload, and expected effect before running write or destructive actions.

Risk: Cursor operations depend on OOMOL acting as an intermediary for connector execution and credential handling.

Mitigation: Install only when the user accepts OOMOL as an intermediary and understands the connected-account trust boundary.

## Reference(s):

- [ClawHub Cursor skill page](https://clawhub.ai/oomol/skills/oo-cursor)
- [Cursor homepage](https://cursor.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON responses from Cursor connector actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
