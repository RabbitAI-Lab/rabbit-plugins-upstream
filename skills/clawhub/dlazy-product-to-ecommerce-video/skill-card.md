## Description:

Turns product specs, manuals, catalogs, or Amazon, Shopify, eBay, and Temu listings into conversion-focused ecommerce videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agents helping sellers use this skill to prepare product ads and cross-border shopping videos from product assets or marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files may be sent to dLazy's hosted service.

Mitigation: Use the skill only with product materials intended for that service, and avoid attaching confidential files unless approved.

Risk: The dLazy CLI needs an API key that can be stored locally.

Mitigation: Use local account protections, prefer per-invocation environment variables when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Installing an npm CLI globally introduces ordinary package supply-chain and persistence risk.

Mitigation: Prefer the pinned npx invocation or a non-global install when a persistent command is not needed, and review the linked package or source before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown-style text with inline dLazy CLI commands and generated task guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy API authentication; files attached through the CLI may be uploaded to dLazy-hosted storage.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
