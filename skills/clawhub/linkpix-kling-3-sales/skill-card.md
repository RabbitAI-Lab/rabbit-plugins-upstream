## Description:

Helps e-commerce and brand teams plan and generate product-promotion videos through Qinghu AI's Kling video workflow using product images and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, short-video teams, and brand content teams use this skill to turn product images and selling points into short promotional videos for online listings, social commerce, and ads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing qhkit or its dependencies may introduce software supply-chain risk.

Mitigation: Review npm installs before running them and prefer pinned package versions where possible.

Risk: API credentials and product media are used with the Qinghu AI service.

Mitigation: Use the service only if comfortable providing an API key and uploading the selected product media.

Risk: Video generation consumes credits, and submitted tasks cannot be cancelled.

Mitigation: Confirm generation parameters and estimated credits with the user before submitting a task.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-kling-3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Markdown text with commands and generated-video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a video prompt and prepared command if media, credentials, or generation are unavailable; reports estimated and actual credits when available.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
