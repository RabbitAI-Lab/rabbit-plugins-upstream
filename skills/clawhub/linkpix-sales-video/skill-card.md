## Description:

上传商品素材自动生成带货短视频，支持 AI 脚本、配音、字幕及转场，适用于 TikTok、抖音等平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to create ecommerce product short videos from product images, selling points, optional reference media, and selected LinkPix/qhkit video models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install qhkit or supporting image tools before use.

Mitigation: Install from the disclosed package source, prefer official registries where available, and follow the artifact's checksum verification step for Node binary installation.

Risk: The workflow may request a qhkit API key and upload selected product media to the provider.

Mitigation: Use an account-scoped API key, share only media intended for product video generation, and confirm provider use before submission.

Risk: Video generation can consume account credits.

Mitigation: Run estimates when supported and require explicit user confirmation of model, media, duration, orientation, language, and expected credits before billable generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit setup steps, model-selection guidance, credit estimates, polling instructions, and generated video URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
