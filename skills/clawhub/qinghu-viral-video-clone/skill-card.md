## Description:

智能分析热门短视频内容，反推脚本并一键复刻视频风格、节奏及镜头语言，用你的商品快速打造同类型营销视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to analyze a Douyin or TikTok-style short video link, draft a comparable script, adapt it to the user's product, and generate a new marketing video through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or upgrade unpinned third-party command-line software globally.

Mitigation: Prefer a pinned local qhkit install and review package provenance before running install or upgrade commands.

Risk: The workflow may send prompts, media, and product assets to the qhkit service.

Mitigation: Use only media and prompts approved for that service, and avoid submitting sensitive or confidential assets.

Risk: The workflow requires a QHKIT token and references token setup commands.

Mitigation: Store tokens in environment variables or a secure secret store, and avoid pasting credentials into chat or shell history.

Risk: The security summary warns against blindly following upgrade commands copied from tool output.

Mitigation: Validate any upgrade instruction against trusted package metadata before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and qhkit JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce rewritten scripts, task IDs, status summaries, credit estimates, and generated video URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
