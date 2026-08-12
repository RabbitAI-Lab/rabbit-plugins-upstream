## Description:

Helps an agent operate MX through an OOMOL-connected account via the oo CLI for user create, read, update, list, and delete operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations teams use this skill to manage MX Platform API users through OOMOL's connector. It is intended for agent-assisted MX account operations that require live schema inspection before each connector action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update MX Platform API users.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The destructive delete action can permanently remove an MX Platform API user.

Mitigation: Confirm the target identifier and get explicit user approval before running delete_user.

Risk: First-time setup can install the oo CLI or connect an OOMOL account.

Mitigation: Run setup only after an auth, connection, or missing-command failure, and only when the user trusts OOMOL and needs the connector configured.

Risk: Connector payloads can become stale if they are built from assumptions instead of the live action contract.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub MX skill page](https://clawhub.ai/oomol/skills/oo-mx)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [MX homepage](https://www.mx.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with bash, PowerShell, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
