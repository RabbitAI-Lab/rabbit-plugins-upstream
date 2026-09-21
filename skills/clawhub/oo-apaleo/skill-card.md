## Description:

The apaleo skill lets an agent read, create, update, and delete apaleo data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to manage apaleo properties, units, unit groups, and unit attributes through an OOMOL-connected account. The skill supports read actions as well as write and destructive account operations when the user confirms the intended payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a connected apaleo account and includes write and destructive actions.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: First-time setup may ask users to install the oo CLI using fetched installer scripts.

Mitigation: Prefer verified OOMOL installation documentation before running installer commands.

Risk: The agent depends on live connector schemas to construct valid action payloads.

Mitigation: Run the schema inspection command before building payloads for connector actions.

## Reference(s):

- [apaleo homepage](https://apaleo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
