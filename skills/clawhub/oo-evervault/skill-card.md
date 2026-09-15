## Description:

Evervault helps agents use an OOMOL-connected Evervault account to encrypt and decrypt JSON-compatible values and inspect encrypted token metadata through the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Evervault encryption, decryption, and token-inspection workflows from an agent while relying on OOMOL-managed connection credentials. It is intended for explicit Evervault tasks where the agent first checks the live connector schema and then runs the requested action with a matching JSON payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI from a verified, versioned source and review installer contents before execution.

Risk: The trigger scope is broader than the listed Evervault actions.

Mitigation: Use the skill only for explicit Evervault encryption, decryption, or token-inspection tasks and check the live connector schema before each action.

Risk: Connector payloads are handled through OOMOL infrastructure.

Mitigation: Send sensitive values only when the user intends Evervault processing through the connected OOMOL account.

## Reference(s):

- [ClawHub Evervault Skill](https://clawhub.ai/oomol/skills/oo-evervault)
- [Evervault Homepage](https://evervault.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples; connector executions return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
