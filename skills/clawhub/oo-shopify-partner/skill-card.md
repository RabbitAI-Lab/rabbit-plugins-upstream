## Description:

Shopify Partner helps agents read, create, and update Shopify Partner data through the OOMOL shopify_partner connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Shopify Partner operators use this skill to inspect apps, app events, partner organization events, transactions, and GraphQL operations for a connected Shopify Partner organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad Shopify Partner account authority through an external connector and raw GraphQL mutations.

Mitigation: Fetch the live action schema before building payloads and require explicit user review of every GraphQL mutation payload and expected effect before execution.

Risk: The skill may expose sensitive Shopify Partner app, event, or earnings data.

Mitigation: Use only trusted OOMOL-connected accounts, limit access to authorized operators, and avoid sharing raw partner data outside the intended workflow.

Risk: The first-time setup path recommends a pipe-to-shell installer.

Mitigation: Verify the oo CLI installer through official OOMOL channels before running it, or install the CLI through an approved internal software distribution process.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shopify-partner)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Shopify Partner Homepage](https://www.shopify.com/partners)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Shopify Partner Connection](https://console.oomol.com/app-connections?provider=shopify_partner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands and JSON request or response snippets for Shopify Partner connector actions.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
