## Description:

Operates Google Calendar through the OOMOL oo CLI so agents can read, create, update, and delete calendars, events, settings, ACLs, attendees, free/busy data, and recurring instances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Google Calendar through an OOMOL-connected account while inspecting live action schemas and confirming write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can ask an agent to run remote OOMOL CLI installer scripts without independent verification.

Mitigation: Review the installer source or use a verified installation method before allowing setup commands to run.

Risk: Write and destructive actions can create, update, delete, clear, move, or overwrite Google Calendar data.

Mitigation: Require explicit user approval after showing the exact target, payload, and expected effect before any write or destructive action.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Calendar](https://workspace.google.com/products/calendar/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-googlecalendar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.5 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
