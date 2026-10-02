## Description:

Plans and generates Amazon product listing images and A+ content with a consistent visual style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and designers use this skill to plan and generate Amazon main images, secondary product images, and A+ page visuals using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected media are sent to the dLazy cloud service.

Mitigation: Upload only content approved for the service and review its data handling before use.

Risk: Signing in can save an API key on the local device.

Mitigation: Use DLAZY_API_KEY when persistent local credential storage is not desired.

Risk: The skill text contains conflicting dLazy CLI version references.

Mitigation: Verify the intended @dlazy/cli version and review the package before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with image plans, prompts, progress checklists, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are generated one at a time after user confirmation.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
