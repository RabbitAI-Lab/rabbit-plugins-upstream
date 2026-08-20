## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）上传商品素材自动生成带货短视频，支持 AI 脚本、配音、字幕及转场，适用于 TikTok、抖音等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to turn product images and selling points into short promotional videos with generated scripts, voiceover, subtitles, and transitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade global Node/npm tooling before use.

Mitigation: Review installation commands before execution and prefer a contained environment or explicit approval for dependency installation and upgrades.

Risk: The skill uploads local product images or videos for generation.

Mitigation: Use only non-sensitive media and confirm token configuration before submitting assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent instructions for submitting, polling, and delivering video-generation tasks through qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
