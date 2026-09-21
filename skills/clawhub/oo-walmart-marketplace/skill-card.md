## Description:

Walmart Marketplace (marketplace.walmart.com). Use this skill for ANY Walmart Marketplace request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketplace operators use this skill to let an agent inspect Walmart Marketplace seller catalog, order, and inventory data through an OOMOL-connected account, and to update inventory only after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Walmart Marketplace catalog, order, and inventory data through the connected OOMOL account.

Mitigation: Install only when OOMOL is trusted and the account owner wants this agent-mediated access.

Risk: The update_inventory action can replace inventory for a seller SKU.

Mitigation: Require explicit approval of the target SKU, payload, and expected effect before running the action.

Risk: First-time setup may involve a remote CLI installer.

Mitigation: Review official installation guidance before running the installer and avoid running setup commands unless an action fails for that reason.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-walmart-marketplace)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Walmart Marketplace homepage](https://marketplace.walmart.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
