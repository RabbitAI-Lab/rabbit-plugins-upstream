## Description:

Operate Walmart Marketplace through an OOMOL-connected account to read catalog, inventory, and order data and update inventory with confirmation safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators and agents use this skill to inspect live action schemas and run OOMOL-connected Walmart Marketplace actions for seller catalog, inventory, and order workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer commands.

Mitigation: Review the installer path before use and prefer a pinned, verified release or trusted package manager.

Risk: The skill can perform write-capable Walmart Marketplace operations.

Mitigation: Use only the intended Walmart Marketplace account and require explicit user confirmation of the payload and effect before inventory or other state-changing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-walmart-marketplace)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Walmart Marketplace](https://marketplace.walmart.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands that call Walmart Marketplace connector actions and may require user confirmation for write-capable operations.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
