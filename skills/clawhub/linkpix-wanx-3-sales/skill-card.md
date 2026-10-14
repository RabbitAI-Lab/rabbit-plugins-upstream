## Description:

Guides merchants and ecommerce teams in creating short product-promotion videos with Wanx through Qinghu AI, using text or product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and ecommerce teams create short product showcases and promotional videos from product images and selling points for online listings and advertisements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing an API key in chat could expose account credentials.

Mitigation: Configure the token locally through a secure prompt or QHKIT_TOKEN; do not paste it into chat.

Risk: Selected media is uploaded to the provider, and video generation consumes account credits.

Mitigation: Review selected media, confirm the estimated cost and generation parameters, and obtain explicit approval before submission.

Risk: Unpinned package installations can introduce unreviewed dependencies or updates.

Mitigation: Pin or preinstall trusted versions of qhkit and image tools where possible.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-wanx-3-sales)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with CLI commands and video result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status and credit usage; completed videos are delivered by URL.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
