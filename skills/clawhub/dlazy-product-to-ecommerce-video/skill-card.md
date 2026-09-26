## Description:

Turns a product spec, manual, catalog, or marketplace listing into a conversion-focused ecommerce video with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce marketers, and developers use this skill to run dLazy's product-to-ecommerce-video workflow for product ads and cross-border shopping videos from product inputs or marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy SaaS endpoints.

Mitigation: Use the skill only with data approved for upload to dLazy, and attach only files intended for transfer.

Risk: A dLazy API key may be saved in local CLI configuration.

Mitigation: Protect the local user account, rotate or revoke keys from the dLazy dashboard when needed, or provide the key per invocation with DLAZY_API_KEY.

Risk: Project context may persist across follow-up turns.

Mitigation: Use separate projects for distinct work and clear sessions when continuing context is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or terminal text with dLazy CLI command output and links to generated assets when provided by the service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; optional local file attachments may be uploaded through the dLazy CLI.]

## Skill Version(s):

1.3.18 (source: release evidence; artifact frontmatter declares 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
