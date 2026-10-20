## Description:

Turns product specifications, catalogs, or ecommerce listings into promotional shopping videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketing teams use this skill to create product ads and cross-border ecommerce videos from product materials or marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files may be sent to the third-party dLazy service.

Mitigation: Review sensitive product information before sending prompts and attach only files intended for upload.

Risk: The CLI may save an API key locally.

Mitigation: Protect local credentials and rotate or revoke the dLazy key if needed.

Risk: A global npm installation persists on the user's system.

Mitigation: Review the CLI package before installation or use the pinned on-demand npx alternative.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a hosted video-generation service; requires a dLazy account and API key.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; supplied skill frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
