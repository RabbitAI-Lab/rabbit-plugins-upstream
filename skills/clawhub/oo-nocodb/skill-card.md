## Description:

NocoDB connector skill for reading, creating, updating, and deleting NocoDB data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect NocoDB action schemas and run read, write, and delete connector actions through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path recommends running remote installer scripts directly in a shell.

Mitigation: Install the oo CLI from a pinned, verifiable release or trusted package manager, and avoid the remote shell installer unless the installer delivery chain is trusted.

Risk: Write and destructive actions can modify or remove NocoDB data accessible to the connected account.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval for destructive actions such as deleting records or tables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nocodb)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [NocoDB homepage](https://nocodb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON action responses from the oo CLI, including data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
