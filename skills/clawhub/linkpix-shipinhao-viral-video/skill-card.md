## Description:

帮助微信视频号商家和运营团队用青虎 AI 生成适合带货、种草和私域推广的短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

微信私域运营人员、直播带货团队和商家用它选择视频模型、编写视频号风格提示词，并生成带货、知识口播或直播引流短视频。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating qhkit and other local packages exposes the environment to mutable package supply chains.

Mitigation: Use a trusted, pinned package version in a sandboxed or preprovisioned environment and review changes before installation.

Risk: The workflow handles an API token and may persist credentials locally; sharing a raw token in chat can expose it.

Mitigation: Store the token in a platform secret store instead of chat and limit access to local configuration.

Risk: Local media files may be uploaded to the video service during generation.

Mitigation: Check that users are authorized to upload each media file and avoid sensitive or private assets without consent.

Risk: Video generation consumes credits and submitted tasks cannot be canceled.

Mitigation: Show the selected settings and estimated credits, then obtain explicit user approval before submitting a generation task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-shipinhao-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎 API 密钥获取指南](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video links]

**Output Format:** [Markdown with inline shell commands and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation returns a task ID before a completed video link; estimates and actual credit usage are reported where available.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
