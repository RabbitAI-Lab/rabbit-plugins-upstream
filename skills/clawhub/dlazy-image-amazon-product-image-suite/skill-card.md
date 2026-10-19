## Description:

Helps create Amazon product listing images, including a main image, secondary images, and A+ content modules, using dLazy's image-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, marketers, and designers use this skill to plan and generate Amazon product detail-page imagery and A+ content, reviewing each image before proceeding to the next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected local media are sent to dLazy's cloud service.

Mitigation: Review prompts and files for sensitive information before generation or upload.

Risk: Authentication requires a dLazy API key, which may be stored in local CLI configuration.

Mitigation: Protect the key, use the per-invocation environment option when appropriate, and rotate or revoke exposed keys.

Risk: Installing or invoking the third-party npm CLI introduces supply-chain dependencies.

Mitigation: Review the CLI repository and package before use; consider the npx option to avoid a long-lived global installation.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Image URLs, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with image links, progress checklists, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Main-image consistency checks and per-image confirmation steps; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
