## Description:

自动生成适用于电商推广及广告投放的图文营销素材：广告图片、促销图，以及从视频反推的图文种草内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce operators use this skill to generate LinkPix advertising images, promotional images, and social commerce post copy from product images or product videos. Agents can use it to prepare qhkit commands, confirm paid generation parameters with the user, poll results, and return generated media links plus written content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run the qhkit package and may require additional local tooling.

Mitigation: Install only after reviewing and trusting the qhkit package and the Qinghu/LinkPix service; surface installation failures and permission issues to the user.

Risk: Local media may be uploaded to Qinghu/LinkPix during image or video workflows.

Mitigation: Confirm the user is comfortable uploading the selected files or URLs, and avoid sending sensitive media unless the service is approved for that data.

Risk: API keys may be requested when qhkit is not configured.

Mitigation: Do not ask users to paste API keys into chat when avoidable; prefer a secure secret store, environment variable, or out-of-band qhkit configuration.

Risk: Generate actions may consume paid credits and cannot be cancelled after submission.

Mitigation: Run estimates where supported, restate key parameters and expected credits, and wait for explicit user approval before submitting paid generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [@iqinghu/qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service](https://www.iqinghu.com)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads; generated results are returned as media URLs and long-form text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, Qinghu/LinkPix credentials, explicit user confirmation before credit-consuming generate actions, and visual review of generated image text.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
