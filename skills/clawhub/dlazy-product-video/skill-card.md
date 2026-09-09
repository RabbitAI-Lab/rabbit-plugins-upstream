## Description:

Turns product photos, links, specifications, manuals, or catalogs into polished product demo, showcase, or advertising videos for ecommerce and cross-border selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce teams use this skill to run a dLazy product-video workflow that converts product inputs such as photos, listings, specifications, manuals, or catalogs into product demo, showcase, or advertising videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party npm execution can install or run code from the dLazy CLI package.

Mitigation: Review the dLazy CLI source before installation, or use the pinned npx command for on-demand execution instead of a persistent global install.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use OS-user-restricted configuration or the DLAZY_API_KEY environment variable as appropriate, and rotate or revoke organization keys from the dLazy dashboard if needed.

Risk: Messages and user-selected files are sent to dLazy services for processing.

Mitigation: Only attach files and submit product information that the user is comfortable uploading to dLazy-hosted services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with CLI command examples and streamed hosted-agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated product-video workflow outputs and uploaded file URLs returned through the dLazy CLI.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
