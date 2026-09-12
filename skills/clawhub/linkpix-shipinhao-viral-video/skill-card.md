## Description:

帮助微信视频号电商运营和直播带货团队通过青虎 AI / LinkPix 生成适配私域流量转化的竖屏带货、种草、知识口播和直播引流视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, private-traffic operators, and e-commerce teams use this skill to prepare WeChat Channels product videos, social recommendation stories, knowledge-talk tracks, and livestream traffic clips through qhkit-powered LinkPix workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the unpinned @iqinghu/qhkit package before use.

Mitigation: Install in an isolated environment when possible and pin or review the qhkit package version before running generation workflows.

Risk: The workflow requires a Qinghu/LinkPix API key and may expose account access if secrets are pasted into chat or logs.

Mitigation: Configure credentials through local secret handling such as QHKIT_TOKEN or qhkit config, and avoid sharing API keys in conversation.

Risk: Generation jobs can upload media and consume credits once submitted.

Mitigation: Confirm model, duration, reference media, orientation, language, and estimated credits with the user before running any generate command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-shipinhao-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides model selection, estimate checks, task submission, polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
