## Description:

Turns product specs, manuals, catalogs, or Amazon / Shopify / eBay / Temu listings into conversion-focused shopping videos with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce teams, and marketing developers use this skill to start or continue a dLazy project that turns product information, listing URLs, and attached media into ecommerce advertising videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and attached files are sent to the third-party dLazy hosted service.

Mitigation: Review content before submission and avoid attaching confidential files unless approved for use with dLazy.

Risk: A dLazy API key may be saved locally for future CLI use.

Mitigation: Use per-invocation credentials or rotate and revoke the key from dLazy when access is no longer needed.

Risk: Global installation persists the dLazy CLI on the local system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated ecommerce video projects managed by the dLazy hosted service.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
