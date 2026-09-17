## Description:

SupportBee (supportbee.com). Use this skill for SupportBee requests such as reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operations teams use this skill to operate SupportBee tickets, replies, comments, users, teams, and labels through the OOMOL oo CLI. It supports read workflows and guarded write or destructive actions that require confirming the target payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer scripts for the oo CLI.

Mitigation: Review the installation path before installing and prefer a verified, pinned, or package-manager flow when available.

Risk: Write and destructive SupportBee actions can change or remove account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-supportbee)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SupportBee Homepage](https://supportbee.com)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before constructing payloads and should return JSON responses from the oo CLI when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
