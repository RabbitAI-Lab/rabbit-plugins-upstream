## Description:

自动生成完整视频分镜方案，包含镜头设计、运镜建议、文案脚本及分镜图，提升视频制作效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn product or campaign inputs into storyboard scripts and generated storyboard images for video planning. It can also provide setup and command guidance for the qhkit workflow when the required CLI or token is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or upgrade mutable third-party qhkit tooling, including upgrade commands surfaced by CLI output.

Mitigation: Review the package, registry, version, and exact install or upgrade command before execution; do not run copied upgrade commands without independent verification.

Risk: Using the workflow can require a QHKIT_TOKEN and selected media uploads to the LinkPix/qhkit service.

Mitigation: Use only approved media, protect the token, and confirm the user is comfortable sharing the selected inputs with that service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown response with storyboard script text, qhkit command guidance, JSON status details, and generated image links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require polling for storyboard image generation and may report credit estimates or consumed credits from the service response.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
