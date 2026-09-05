## Description:

A professional product image generation skill purpose-built for Amazon product detail pages, including main images, secondary product images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and creative teams use this skill to plan and generate Amazon-ready product image sets, including compliant main images, secondary infographics or lifestyle images, and A+ page modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product media are sent to dLazy-hosted services for generation.

Mitigation: Use only approved product media, avoid uploading sensitive local files, and review generated image URLs before sharing or publishing.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for temporary sessions when a saved key is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact contains a minor documentation mismatch around CLI versions.

Mitigation: Review the documented install command and package version before installation or pin the CLI version explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown instructions with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides staged image generation through the dLazy CLI and returns progress status, image checklists, consistency checks, and next-step confirmations.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
