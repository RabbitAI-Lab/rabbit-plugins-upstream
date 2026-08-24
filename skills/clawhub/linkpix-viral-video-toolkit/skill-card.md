## Description:

智能分析热门短视频：一键反推爆款脚本并复刻同款营销视频，同时支持提取视频中的音频内容，帮助卖家快速打造爆款内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and content agents use this skill to analyze Douyin or TikTok-style short-video links, extract a reusable script and video URL, adapt the script to the user's product, generate a similar marketing video, or extract audio from the resolved video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may change the local toolchain by installing Node, qhkit, Pillow, sharp-cli, or related command-line dependencies.

Mitigation: Run it in a sandboxed environment or preinstall and vet required dependencies before use.

Risk: The workflow can request or reuse qhkit API credentials.

Mitigation: Provide tokens through an environment variable or secret store and avoid pasting long-lived credentials into chat.

Risk: Generated marketing videos and extracted audio can raise copyright or rights-clearance concerns if source material is copied too closely.

Mitigation: Adapt scripts to the user's own product and verify rights for music, audio, and any reused source material before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-toolkit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters; downstream tool results may include generated video URLs, extracted audio files, or status JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit commands for video analysis and generation, and ffmpeg for audio extraction when a video URL is available.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
