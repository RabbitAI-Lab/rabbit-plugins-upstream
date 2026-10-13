## Description:

帮助电商商家、设计师和独立站运营使用青虎AI，根据商品图片和卖点生成 Vidu Q3 电商短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商商家、设计师和独立站运营使用商品图片和卖点，生成用于商品展示和广告的短视频。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Use a protected secret mechanism or environment variable rather than pasting the key into ordinary chat.

Risk: Installing or upgrading packages at runtime can introduce unreviewed code.

Mitigation: Prefer pinned or preinstalled qhkit and image-processing tools; review package sources before installation.

Risk: Video generation uploads product media and consumes account credits.

Mitigation: Review the media and estimated credits, then obtain explicit user approval before submitting a generation task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-vidu-q3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Video links]

**Output Format:** [Markdown with commands and generated video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires product media and account credits; returns generated video links after task completion.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
