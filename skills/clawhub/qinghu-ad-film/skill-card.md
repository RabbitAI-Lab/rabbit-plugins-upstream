## Description:

帮助用户用商品参考图和场景提示词制作电影感商品广告与品牌宣传视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Brand and marketing teams use this skill to turn product images and creative direction into short cinematic advertisements, check estimated credits, and retrieve finished video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade external tools and change the local environment without an explicit consent checkpoint.

Mitigation: Require user confirmation before installing Node or qhkit, changing PATH, or upgrading tools.

Risk: Product images and an API token may be sent to the Qinghu service.

Mitigation: Confirm image uploads and token configuration with the user before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ad-film)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Text with CLI examples, task status, and video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task ID and credit usage when available.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
