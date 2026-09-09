## Description:

Turns product specs, manuals, catalogs, or Amazon, Shopify, eBay, and Temu listings into conversion-oriented ecommerce videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce marketers, and agents use this skill to create product advertising and cross-border selling videos from product documents or ecommerce listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attached files are sent to dLazy hosted endpoints for processing.

Mitigation: Use the skill only for data that may be processed by dLazy's hosted service, and avoid attaching sensitive files unless that use is approved.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Protect the saved key, use environment-scoped credentials when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The skill relies on a pinned npm CLI package.

Mitigation: Prefer the on-demand npx path for temporary use and review or audit the pinned CLI before deployment in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and streamed terminal text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted video-generation results returned by the dLazy service.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
