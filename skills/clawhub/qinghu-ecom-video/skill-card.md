## Description:

一键生成电商视频：商品展示视频、带货短视频、品牌宣传片、广告素材，支持 AI 脚本、分镜、多图一键成片，适配 TikTok、抖音、Amazon、Shopee 等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan, submit, price, monitor, and deliver ecommerce product, promotional, review, and short-form advertising video tasks through the qhkit CLI and Qinghu AI service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs the mutable @iqinghu/qhkit CLI globally.

Mitigation: Run in an isolated environment, pin or review the CLI version, and review install or upgrade commands before execution.

Risk: Prompts, product images, and videos may be sent to the Qinghu service.

Mitigation: Use only if the user trusts the Qinghu service with the supplied media and prompts.

Risk: Video generation can consume service credits.

Mitigation: Confirm expected credit charges or estimates before submitting generation tasks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ecom-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, status summaries, credit estimates, and video delivery URLs returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
