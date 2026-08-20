## Description:

This skill helps agents turn product photos, product links, specs, manuals, or catalogs into conversion-focused ecommerce ad videos using dLazy's hosted ecommerce video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and agents use this skill to create shopping ad videos from product images, store listings, product specs, manuals, or catalogs. It is suited for storefront, TikTok Shop, Amazon, Shopify, eBay, Temu, and cross-border selling workflows that need multilingual voiceover or an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product links, and selected product files may be sent to dLazy's hosted service when the skill is invoked.

Mitigation: Use the skill only for ecommerce video generation tasks and attach only files or links intended for dLazy processing.

Risk: The dLazy CLI stores an API key in the user's local configuration or accepts one through DLAZY_API_KEY.

Mitigation: Use standard secret handling for the API key and rotate or revoke it from the dLazy dashboard if it may have been exposed.

Risk: The skill depends on the pinned @dlazy/cli package to perform service calls and optional file uploads.

Mitigation: Install only when the user intends to use dLazy's hosted service and review the pinned CLI package before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli package and may upload user-selected product files when the agent passes --files.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
