## Description:

Guides ecommerce teams through creating Kling 3.0 product-promotion videos from product images using Qinghu AI, including model selection, cost estimates, and delivery of video links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, short-video teams, and brand content teams use this skill to plan and request product-promotion videos with reference images, then receive generated video links for review or distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A request for an API key in chat could expose the credential.

Mitigation: Do not share keys in chat; configure QHKIT_TOKEN or set the token locally through a secure secret path.

Risk: Installing or upgrading unpinned tools can run unreviewed code.

Mitigation: Pin package versions or review qhkit and image-processing tools before installing or upgrading them.

Risk: Uploaded product images and other media are sent to qhkit for video generation.

Mitigation: Upload media only when its use with qhkit is acceptable to the user and their organization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-kling-3-sales)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video URLs]

**Output Format:** [Markdown with command examples and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires product reference images for Kling 3.0; generation consumes credits after user confirmation.]

## Skill Version(s):

0.1.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
