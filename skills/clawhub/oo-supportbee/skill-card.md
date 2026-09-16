## Description:

SupportBee (supportbee.com). Use this skill for ANY SupportBee request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, support operators, and developers use this skill to inspect SupportBee action schemas and operate tickets, replies, comments, users, teams, labels, and search through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code from OOMOL-controlled URLs on the user's machine.

Mitigation: Review setup instructions before installing, prefer a verified release or package manager, and run the pipe-to-shell or iex commands only when the installer source is trusted.

Risk: Write and destructive SupportBee actions can create, update, or remove SupportBee records.

Mitigation: Inspect the live action schema before building a payload, confirm the exact payload and effect with the user for write actions, and require explicit approval for destructive actions.

## Reference(s):

- [SupportBee Homepage](https://supportbee.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SupportBee Skill Page](https://clawhub.ai/oomol/skills/oo-supportbee)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SupportBee Icon](https://static.oomol.com/logo/third-party/supportbee.png)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect action schemas before execution and return JSON responses when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
