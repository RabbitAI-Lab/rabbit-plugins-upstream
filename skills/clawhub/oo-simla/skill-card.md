## Description:

Simla.com lets an agent read, create, and update Simla.com customer and order data through the OOMOL simla connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Simla.com customer and order workflows from an agent through OOMOL-connected actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or edit Simla.com customers and orders.

Mitigation: Confirm each write payload and intended business effect with the user before running the connector action.

Risk: The setup path references a remote CLI installer.

Mitigation: Install the CLI manually from a trusted source and verify setup steps before allowing the agent to proceed.

Risk: The skill gives mediated access to customer and order data.

Mitigation: Install only when that level of Simla.com data access through OOMOL is acceptable for the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simla)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Simla.com homepage](https://www.simla.com/en)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON payloads, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses as JSON.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
