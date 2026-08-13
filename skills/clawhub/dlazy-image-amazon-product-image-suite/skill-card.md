## Description:

A professional product image generation skill purpose-built for Amazon product detail pages, including main images, secondary images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, brand teams, and e-commerce designers use this skill to plan and generate Amazon product-detail image sets, including compliant main images, secondary infographics, lifestyle/detail shots, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded product or source media are sent to dLazy-hosted services.

Mitigation: Avoid sensitive or unreleased assets unless approved, and rotate or remove the dLazy API key when the skill is no longer in use.

Risk: A global CLI install and local API-key configuration can persist on the machine.

Mitigation: Use npx for one-off runs when persistence is not desired, and remove local credentials after use.

Risk: Generated product imagery or embedded copy may require review before Amazon publication.

Mitigation: Check generated assets against Amazon image requirements and product-claim accuracy before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown status updates with prompt drafts, image checklists, and dLazy CLI commands; generated image results are returned as hosted URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; user-provided media may be uploaded to dLazy services for generation.]

## Skill Version(s):

1.3.8 (source: release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
