## Description:

Guides agents through planning and generating Amazon product main images, secondary images, and A+ content using dLazy image tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and creative teams use this skill to plan and produce coordinated Amazon listing images and A+ page visuals, reviewing each image before continuing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and supplied media may be sent to dLazy's cloud service.

Mitigation: Use only content you are comfortable sharing with dLazy; review media before submission.

Risk: The CLI may store an API key in the local user profile.

Mitigation: Use a per-run environment key when persistent storage is undesirable, and rotate or revoke keys if exposed.

Risk: Installing the third-party CLI introduces a package supply-chain dependency.

Mitigation: Review the package and source before installation if supply-chain assurance is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with image checklists, prompts, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise generation with user approval between images; main-image consistency checks.]

## Skill Version(s):

1.3.27 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
