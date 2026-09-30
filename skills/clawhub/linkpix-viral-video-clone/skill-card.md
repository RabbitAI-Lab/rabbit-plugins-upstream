## Description:

智能分析热门短视频内容，反推脚本并一键复刻视频风格、节奏及镜头语言，用你的商品快速打造同类型营销视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill to analyze a Douyin or TikTok-style short-video link, adapt the inferred script to their own product, estimate credits, and generate a similarly structured promotional video through LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run unpinned external qhkit tooling from npm.

Mitigation: Use a reviewed, pinned qhkit version where possible and review the package before deployment.

Risk: The workflow may send video links, product images, reference videos, and qhkit tokens to LinkPix/iQingHu tooling.

Mitigation: Run the skill only when that data sharing is acceptable and avoid exposing unnecessary sensitive media or tokens.

Risk: Generation tasks can spend credits and cannot be cancelled after submission.

Mitigation: Run the estimate command and obtain user confirmation before submitting generation jobs.

Risk: Environment setup may add PATH changes to shell startup files if made persistent.

Mitigation: Prefer session-scoped PATH changes unless persistent shell configuration is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit asynchronous video generation tasks, return task IDs, poll status, and provide generated video URLs and credit usage.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
