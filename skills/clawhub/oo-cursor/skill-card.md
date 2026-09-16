## Description:

Operate Cursor through OOMOL's oo CLI to read, create, update, and delete Cursor cloud-agent data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cursor cloud-agent sessions, runs, team usage, spend, models, team members, and audit logs through an authenticated OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes shell execution of remote installer scripts for the oo CLI.

Mitigation: Review or replace the installer flow with a verified installation method before installing.

Risk: Write and destructive Cursor actions can change, archive, cancel, or permanently delete cloud session data.

Mitigation: Confirm exact payloads and targets before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Cursor skill page](https://clawhub.ai/oomol/skills/oo-cursor)
- [Cursor homepage](https://cursor.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data and execution metadata when run.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
