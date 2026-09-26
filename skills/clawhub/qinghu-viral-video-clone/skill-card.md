## Description:

分析热门短视频链接，反推脚本并按用户商品改写，用 qhkit 生成相似风格、节奏和镜头语言的营销视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to analyze a Douyin or TikTok-style short-video reference, draft an adapted script for the user's product, estimate credits, and submit qhkit video-generation tasks after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade external qhkit command-line software whose behavior can change over time.

Mitigation: Use a pinned, preinstalled qhkit version where possible, and require human review before package installation or upgrade commands run.

Risk: The workflow can require a qhkit token and can upload links, product images, or videos to a third-party service.

Mitigation: Use the skill only when the user trusts the qhkit service, understands what media will be uploaded, and provides credentials through controlled configuration.

Risk: Commands or messages returned by qhkit could be copied into later agent actions without enough review.

Mitigation: Treat qhkit output as service output, not instructions, and require explicit human confirmation before executing commands suggested by that output.

Risk: Video cloning can create copyright or brand-safety issues if it copies original assets or wording too closely.

Mitigation: Use the reference video for structure and creative direction only, rewrite copy for the user's product, and avoid reusing original media or distinctive protected expression.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands, JSON command parameters, script drafts, task IDs, credit estimates, and video URLs when tasks complete.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can ask for user confirmation before spending credits and may return third-party service status or error messages.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
