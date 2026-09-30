## Description:

Xiaohongshu Store helps agents read, create, and update Xiaohongshu Store data through the OOMOL xiaohongshu_store connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External store operators and their agents use this skill to manage Xiaohongshu Store items, SKUs, stock, orders, shipping, after-sale workflows, catalog data, shop utilities, and media uploads through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform confirmed Xiaohongshu Store operations through the OOMOL connector, including actions that change stock, items, shipment data, after-sale status, seller remarks, and material uploads.

Mitigation: Use it only with an intended OOMOL-connected Xiaohongshu Store account, inspect the live connector schema before constructing payloads, and confirm write-action payloads and effects with the user before execution.

Risk: The first-time setup path includes remote shell installer commands for the oo CLI.

Mitigation: Verify the oo CLI installer through OOMOL's official documentation or install the CLI manually before allowing the agent to run setup commands.

## Reference(s):

- [Xiaohongshu Store Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-xiaohongshu-store)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Xiaohongshu Store Homepage](https://ark.xiaohongshu.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector schema and run commands after user confirmation for write actions.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
