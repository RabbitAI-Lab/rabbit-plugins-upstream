## Description:

Use this skill to operate Plisio through an OOMOL-connected account for reading, creating, and updating Plisio data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Plisio invoices, balances, and operations through the oo CLI with an OOMOL-connected Plisio account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts in a shell.

Mitigation: Install the oo CLI through a pinned, signed, or package-manager-based method, or independently verify the installer before running it.

Risk: The create_invoice action changes Plisio state by creating hosted invoices for merchant orders.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [Plisio homepage](https://plisio.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
