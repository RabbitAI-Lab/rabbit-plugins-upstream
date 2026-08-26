## Description:

智能分析热门短视频：一键反推爆款脚本并复刻同款营销视频，同时支持提取视频中的音频内容，帮助卖家快速打造爆款内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content operators use this skill to analyze short-video links, extract scripts and direct video links, generate adapted marketing videos from product images, or extract audio for downstream editing. The workflow is intended for normal ClawHub agent use with confirmation before credit-consuming generation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the user to provide a billable third-party API key for qhkit configuration.

Mitigation: Configure tokens through a secure local environment variable or secret mechanism when available, avoid pasting API keys directly into chat, and confirm credit-consuming generation actions before submission.

Risk: Generated video workflows can consume paid credits and may not be cancelable after submission.

Mitigation: Run estimate where supported, restate the selected model, inputs, duration, quality, and expected credits, then wait for explicit user approval before running generate.

Risk: Video replication and audio extraction can raise content ownership, likeness, or music copyright concerns.

Mitigation: Adapt scripts to the user's own product and selling points, avoid copying original assets or dialogue verbatim, and remind users to confirm rights before commercial use of extracted audio.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, status JSON, generated media URLs, extracted audio files, and concise user-facing setup or failure guidance.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
