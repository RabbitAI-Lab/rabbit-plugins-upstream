## Description:

Guides ecommerce teams in creating Kling 3.0 product-promotion videos through Qinghu AI using product images and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, short-video teams, and brand content teams use this skill to plan and request product showcase and advertising videos from product images and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup directions ask users to share an API key in chat.

Mitigation: Never paste the key into chat; configure it locally or through a secure secret mechanism.

Risk: Tool installation or upgrades can persistently change the local environment using an unpinned npm package.

Mitigation: Review the package, version, and installation commands before allowing installation or upgrade.

Risk: Product media is uploaded to an external service and video-generation jobs consume paid credits.

Mitigation: Review uploaded media, generation settings, and estimated credits; explicitly approve each paid submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-kling-3-sales)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Markdown with shell commands and video result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes generation parameters, estimated or actual credits, and task status when available.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
