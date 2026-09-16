## Description:

Operate Respond.io through the OOMOL oo CLI connector for reading, creating, updating, and deleting contact and conversation data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Respond.io contacts, tags, workspace users, channels, and conversation workflows from an agent through OOMOL-connected account access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup guidance could execute changing code on the user's machine.

Mitigation: Install the oo CLI through a verified package, or separately download, inspect, and verify the installer before execution.

Risk: Write and destructive Respond.io actions can modify or remove CRM contact, tag, and conversation data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Respond.io Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-respond-io)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Respond.io Homepage](https://respond.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Respond.io connector action results are returned as JSON when commands are executed.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
