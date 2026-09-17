## Description:

Operate Shopify Storefront through an OOMOL-connected account for storefront data lookup and cart workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Shopify Storefront through an OOMOL-connected account, including cart workflows and storefront catalog lookups. It supports reads directly and requires user confirmation before write actions such as creating carts or adding cart lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code.

Mitigation: Require explicit user approval and verify the installer path, package source, checksum, or signature before running any downloaded installer.

Risk: Write actions can change Shopify Storefront cart state.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running write-tagged actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shopify-storefront)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Shopify Storefront](https://www.shopify.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and can return JSON responses from Shopify Storefront connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
