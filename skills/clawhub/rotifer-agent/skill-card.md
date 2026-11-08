## Description:

Helps users build a Rotifer Agent by decomposing intent into capability units, selecting Genes, composing a Genome, and testing the Agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill to plan a Rotifer agent, choose and validate Genes, create a Genome, and test the resulting Agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted CLI packages or Genes could introduce unwanted behavior.

Mitigation: Review and approve CLI packages and Genes before use; test new Genes with non-sensitive inputs.

Risk: Genes may use external APIs when handling user material.

Mitigation: Review external API use before supplying private material.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xiaoba-dev/skills/rotifer-agent)
- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with capability tables, inline shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the selected Genes and the user's Rotifer setup.]

## Skill Version(s):

1.2.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
