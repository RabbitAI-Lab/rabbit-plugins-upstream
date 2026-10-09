## Description:

帮助电商商家和设计师使用商品图片与卖点，通过青虎 AI 的 Vidu Q2 工作流制作商品展示和带货短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商商家、设计师和独立站运营可用商品图和卖点生成带声音的商品展示或广告短视频，并获取任务状态及成片链接。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks users to share an API key in chat.

Mitigation: Do not paste API keys into chat; configure QHKIT_TOKEN or a secure local secret instead.

Risk: The workflow can install or update qhkit and upload product media to its service.

Mitigation: Review the package before installation, prefer a pinned version or preinstalled binary, and upload only media approved for sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-vidu-q2-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎 AI API key instructions](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status, generated video URLs, and credit usage.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
