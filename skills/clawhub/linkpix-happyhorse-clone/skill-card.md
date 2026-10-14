## Description:

帮助短视频创作者和电商团队分析热门短视频的镜头结构，改写商品脚本，并通过青虎 AI 生成 HappyHorse 1.1 视频素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

短视频创作者和电商运营团队用它分析参考视频、改写商品脚本，并生成用于社交平台投放的短视频。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing an API key in chat can expose account credentials.

Mitigation: Configure credentials privately through a secure local or platform secret mechanism; never paste API keys into chat.

Risk: Installing or updating packages and changing the local environment can introduce untrusted software.

Mitigation: Review each command and trust its package source before approving installation, upgrades, or environment changes.

Risk: Submitting a video generation task can spend account credits.

Mitigation: Confirm the exact generation parameters and estimated cost with the user before submitting a task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video links]

**Output Format:** [Markdown with script comparisons, command examples, and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires explicit approval of the parameters and estimated credit cost.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
