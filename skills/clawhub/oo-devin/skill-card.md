## Description:

Devin (devin.ai). Use this skill for ANY Devin request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Devin sessions through an OOMOL-connected account, including creating sessions, inspecting session state, listing sessions, sending messages, and terminating sessions with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to run remote installer scripts in a shell.

Mitigation: Review the installer path first, prefer a verified or pinned installer, and require explicit user approval before setup commands.

Risk: Write actions and session termination can change or end Devin sessions.

Mitigation: Confirm the exact payload, target session, and effect with the user before write or destructive actions.

## Reference(s):

- [Devin homepage](https://devin.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-devin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release metadata, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
