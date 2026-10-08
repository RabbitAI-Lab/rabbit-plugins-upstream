## Description:

根据热门短视频链接分析脚本与镜头节奏，结合用户商品改写内容并生成同类营销视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商商家和营销团队可提供抖音或 TikTok 视频链接，借鉴其脚本结构和节奏，结合自有商品制作新的营销视频。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrades of command-line tools may change the local environment.

Mitigation: Use a sandbox and preinstalled, pinned dependencies; seek approval before any installation or upgrade.

Risk: Local media and an access token may be sent to the video provider.

Mitigation: Confirm permission before uploading media, and keep the token private.

Risk: Video generation and reference media may incur service-credit charges.

Mitigation: Estimate credits, show the revised script, and request approval before paid generation.

Risk: Close imitation of a source video may infringe rights in its content.

Mitigation: Create original wording and assets; borrow only general structure and pacing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Video links]

**Output Format:** [Markdown with script comparison, CLI commands, and a generated video URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports generation status and service-credit estimates or charges.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
