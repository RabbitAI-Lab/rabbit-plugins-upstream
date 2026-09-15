## Description:

Enables agents to operate Shopify Storefront through OOMOL's shopify_storefront connector, including catalog reads and cart workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to inspect Shopify Storefront schemas, read storefront catalog data, or perform cart workflows through an OOMOL-connected Shopify account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands without integrity checks.

Mitigation: Prefer verified, version-pinned, or signed oo CLI installation sources before use.

Risk: Cart actions can change Shopify Storefront state.

Mitigation: Confirm the exact payload and expected effect before running write actions such as create_cart or add_cart_lines.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shopify-storefront)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Shopify Storefront Homepage](https://www.shopify.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
