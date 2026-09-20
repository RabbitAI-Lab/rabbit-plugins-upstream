## Description:

Turns product specs, manuals, catalogs, or Amazon, Shopify, eBay, and Temu listings into conversion-focused shopping videos with multilingual voiceover and an optional virtual host for ecommerce ads and cross-border selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, marketers, and agent developers use this skill to create product advertising videos and cross-border shopping videos from product descriptions, catalogs, listings, and attached reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts, listings, and attached files may be sent to dLazy services.

Mitigation: Submit only content intended for upload and review service terms and data handling expectations before use.

Risk: The dLazy API key is required for use and may be stored in the local CLI configuration.

Mitigation: Use the documented login or auth flow, keep local config access limited to the OS user, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists a third-party executable on the user's system.

Mitigation: Use the pinned npx invocation when a non-global install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and streamed CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload attached product files to dLazy storage and stream hosted agent replies through the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
