## Description:

Plans and generates Amazon product listing images, including a main image, secondary images, and A+ page modules, using dLazy's cloud image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and designers use this skill to plan and generate coordinated product listing images and A+ page visuals, reviewing each image before proceeding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy services for generation.

Mitigation: Review prompts and media for sensitive content before submission.

Risk: Installing the CLI or logging in can leave a global package or locally stored API key.

Mitigation: Review the package before installation; consider on-demand npx use and DLAZY_API_KEY instead of persistent login.

Risk: The release, skill frontmatter, and documented CLI versions differ.

Mitigation: Confirm the intended versions before use; the publisher should correct the mismatch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Image URLs, Markdown guidance]

**Output Format:** [Hosted image URLs with Markdown progress and review prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a main image, optional secondary images, and optional A+ modules in user-confirmed stages.]

## Skill Version(s):

1.3.33 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
