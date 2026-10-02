## Description:

上传商品素材自动生成带货短视频，支持 AI 脚本、配音、字幕和转场，适用于 TikTok、抖音等电商平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short ecommerce sales videos from product images, selling points, and optional reference media. The skill guides qhkit setup, cost estimation, video task submission, status polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update qhkit or Node tooling and change local npm or PATH state.

Mitigation: Preinstall and pin qhkit where possible, and require explicit approval before npm, npx, curl, PATH, or upgrade commands run.

Risk: The workflow can upload selected product images or videos to the qhkit service and consume account credits.

Mitigation: Confirm the media files, target service, estimated credits, and account token scope before generation.

Risk: The skill requires credential configuration for qhkit access.

Mitigation: Use environment variables or approved secret storage, avoid exposing tokens in chat or shell history, and review configuration output for redaction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with qhkit command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cost estimates, task IDs, polling status, consumed credits, error messages, and generated video URLs.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
