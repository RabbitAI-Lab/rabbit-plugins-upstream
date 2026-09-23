## Description:

Turns product specifications, manuals, catalogs, or Amazon, Shopify, eBay, and Temu listings into conversion-focused ecommerce shopping videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and developers use this skill to launch or continue dLazy product-video projects from product details, listings, and optional reference files. It is intended for product ads, cross-border selling videos, TikTok Shop content, and Amazon or Shopify listing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product details, and attached files may be sent to the dLazy hosted service.

Mitigation: Do not include private or regulated data unless the user intends to share it with dLazy; review attached files before invocation.

Risk: Authentication stores a dLazy API key in local CLI configuration or uses the DLAZY_API_KEY environment variable.

Mitigation: Protect the local config and environment, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A global npm install persists the dLazy CLI on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and streamed CLI text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated ecommerce video work performed by the hosted dLazy service; attached local files are uploaded before use.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
