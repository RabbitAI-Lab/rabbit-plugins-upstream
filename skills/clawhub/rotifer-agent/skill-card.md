## Description:

Build a Rotifer Agent by decomposing intent into capability units, selecting Genes, composing a Genome, and creating and testing the Agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers working with Rotifer use this skill to plan an Agent from Genes, choose and compose those Genes into a Genome, then create and test the Agent with the Rotifer CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install or execute the Rotifer CLI and selected Genes.

Mitigation: Review npm packages and selected Genes before approving installation or execution.

Risk: Registry or Arena requests may involve external services when private inputs are used.

Mitigation: Check the external API use before supplying private inputs.

Risk: Publishing an Agent or Gene may expose project content externally.

Mitigation: Keep publishing subject to explicit approval.

## Reference(s):

- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [ClawHub release page](https://clawhub.ai/xiaoba-dev/skills/rotifer-agent)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown plans with CLI command examples and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides recommendations and command examples for user review before installation, publishing, or overwriting actions.]

## Skill Version(s):

1.2.7 (source: server-resolved release metadata, clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
