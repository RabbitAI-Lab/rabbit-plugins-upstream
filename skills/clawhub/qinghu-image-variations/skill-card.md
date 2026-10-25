## Description:

Generates multiple marketing image variations from a product image using Qinghu AI, with options for different backgrounds, layouts, and styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to create multiple product-image variations for advertising and A/B tests from one source image. It uses the Qinghu CN service and requires a Qinghu token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs the agent to install or upgrade unpinned qhkit and Node tooling on the host without clear user confirmation.

Mitigation: Preinstall a reviewed, pinned qhkit version and require confirmation before global npm, npx, or Node bootstrap commands.

Risk: Generated redraws may alter product text, logos, or structural details.

Mitigation: Review generated images against the source product before publishing or using them in ads.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-image-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Image URLs and text; shell commands for setup and generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report estimated and actual credit usage; generated images require review for product details.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
