## Description:

智能分析热门短视频：一键反推爆款脚本并复刻同款营销视频，同时支持提取视频中的音频内容，帮助卖家快速打造爆款内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and marketing operators use this skill to analyze a short-form video link, derive a script and direct video URL, generate a related marketing video with qhkit, or extract audio with ffmpeg.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update third-party tooling and modify PATH before running qhkit workflows.

Mitigation: Prefer a local pinned qhkit installation and require explicit user approval for package installs, PATH changes, and upgrades.

Risk: The workflow requires service access and may handle API tokens.

Mitigation: Avoid passing API tokens directly on the command line; prefer environment variables or reviewed configuration storage.

Risk: Video remixing and audio extraction can involve third-party content rights.

Mitigation: Confirm the user's rights before processing third-party videos or audio, especially for commercial use.

Risk: Paid generation steps can consume service credits.

Mitigation: Run estimates where supported and obtain user approval before paid generation or uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-toolkit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, generated media URLs, extracted audio file paths, credit estimates, and setup guidance.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
