## Description:

Turn a product spec, manual, catalog, or Amazon / Shopify / eBay / Temu listing into a conversion-focused ecommerce video with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, ecommerce sellers, and developers use this skill to invoke the dLazy hosted product-to-video workflow for product ads, TikTok Shop clips, Amazon listing videos, and cross-border selling content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product assets are sent to dLazy services, and attached files may be uploaded to dLazy storage.

Mitigation: Use only product assets appropriate for dLazy processing, avoid submitting sensitive material unless approved, and review dLazy terms before use.

Risk: The dLazy API key can be stored in the local CLI configuration.

Mitigation: Restrict local config file access, prefer environment-scoped credentials when appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing the CLI globally persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a persistent global CLI is not desired and review the package/source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or continue dLazy project sessions and may reference uploaded product assets or generated ecommerce video outputs.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
