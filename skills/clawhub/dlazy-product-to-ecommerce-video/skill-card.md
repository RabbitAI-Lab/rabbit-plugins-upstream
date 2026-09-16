## Description:

Turns a product spec, manual, catalog, or Amazon, Shopify, eBay, or Temu listing into a conversion-focused ecommerce video with multi-language voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, ecommerce operators, and developers use this skill to create product advertising and cross-border selling videos from product documents, images, or marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party CLI and hosted dLazy API, so prompts, options, and attached files are sent to dLazy services.

Mitigation: Install only if you trust dLazy and attach only files you intend to upload to dLazy.

Risk: The dLazy API key is saved locally or supplied through an environment variable.

Mitigation: Treat the API key as sensitive, avoid sudo or privileged installs, and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A global npm install persists a third-party binary on the user's machine.

Mitigation: Prefer on-demand npx or a non-privileged local install when a persistent global CLI is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference hosted video generation results, project IDs, uploaded file URLs, or follow-up instructions returned by the dLazy service.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
