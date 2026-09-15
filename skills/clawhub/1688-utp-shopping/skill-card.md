## Description:

1688-utp-shopping helps agents guide users through 1688 product search, supplier comparison, cart management, checkout, and payment confirmation using UTP MCP or CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External shoppers, procurement teams, and agent operators use this skill to search real 1688 products, compare supplier candidates, manage a shopping cart, and proceed through checkout with user confirmation for order and payment steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may download and run unpinned npm packages.

Mitigation: Review the install scripts and package sources before installing, and install only in an environment where npm package execution is acceptable.

Risk: Installation may alter agent MCP configuration, overwrite an existing utp command, and persist a new MCP server across sessions.

Mitigation: Back up agent configuration first, review the MCP server entry after installation, and disable or remove the server if it is not the intended shopping path.

Risk: The skill can initiate a 1688 checkout and payment workflow.

Mitigation: Require explicit user confirmation for checkout and payment steps, and review order details in the supported confirmation UI before proceeding.

Risk: Using reset behavior can remove local UTP or host configuration.

Mitigation: Avoid reset options unless local configuration removal is intended, and back up relevant local configuration before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/1688aiinfra/skills/1688-utp-shopping)
- [README](README.md)
- [Install Guide](references/install-guide.md)
- [Cloud Mode Guide](references/cloud-mode.md)
- [Checkout Guide](references/checkout-guide.md)
- [Error Guide](references/error-guide.md)
- [Update Guide](references/update-guide.md)
- [Commercial Host Registry](references/registry.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with MCP or CLI command patterns and interactive shopping card handoffs where supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shopping, login, order review, and payment confirmation flows that require explicit user action.]

## Skill Version(s):

2.4.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
