## Description:

Lingxing lets agents read, create, and update Lingxing ERP data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Lingxing ERP workflows from an agent, including product, listing, seller, inventory, shipment, advertising, and profit reporting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a connected Lingxing ERP account through OOMOL CLI actions.

Mitigation: Install and use it only when the agent is intended to access that Lingxing account.

Risk: Actions tagged as write can change Lingxing state, and list_order_profit has inconsistent write-tag documentation.

Mitigation: Confirm the exact payload and expected effect before approving write or destructive actions, with special review for list_order_profit.

Risk: First-time setup may install the oo CLI, authenticate an OOMOL account, or connect Lingxing access.

Mitigation: Run setup only after a command fails with an installation, authentication, or connection error.

## Reference(s):

- [ClawHub Lingxing skill page](https://clawhub.ai/oomol/skills/oo-lingxing)
- [Lingxing homepage](https://www.lingxing.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; action results are returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
