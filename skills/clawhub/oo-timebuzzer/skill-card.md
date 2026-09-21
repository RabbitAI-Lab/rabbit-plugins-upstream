## Description:

timeBuzzer (timebuzzer.com). Use this skill for ANY timeBuzzer request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected timeBuzzer account through OOMOL, including reading account, tile, layer, and activity data and managing activities when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, update, and delete actions can change or remove timeBuzzer activity data.

Mitigation: Confirm the exact payload, target activity, and intended effect with the user before running write or destructive actions.

Risk: The optional oo CLI installer command runs code fetched from the network.

Mitigation: Use the installer only when the CLI is missing and the user intends to connect OOMOL, and treat the install command as a trusted setup step requiring care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-timebuzzer)
- [timeBuzzer homepage](https://timebuzzer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL timeBuzzer connection settings](https://console.oomol.com/app-connections?provider=timebuzzer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas before constructing JSON payloads and to request approval before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
