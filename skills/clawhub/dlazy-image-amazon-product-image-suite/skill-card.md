## Description:

Helps create a coordinated set of Amazon product listing images, including a main image, secondary images, and A+ content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, marketers, and designers use this skill to plan and create consistent Amazon listing imagery, from the main product image to secondary images and A+ modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and referenced local media are sent to dLazy-hosted services.

Mitigation: Share only content you are comfortable sending to dLazy; check media for sensitive information before use.

Risk: Using the third-party CLI installs or runs external software.

Mitigation: Review the CLI source and package before use; prefer on-demand npx execution if a global installation is unnecessary.

Risk: The CLI stores an API key under the user's profile.

Mitigation: Protect the user profile and rotate or revoke the key when it is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (tool reference, not skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Markdown guidance, Shell commands]

**Output Format:** [Image URLs with Markdown progress updates and generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Main product image, optional secondary images, and optional A+ modules; generated one at a time after user confirmation.]

## Skill Version(s):

1.3.28 (source: server release metadata; bundled skill frontmatter: 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
