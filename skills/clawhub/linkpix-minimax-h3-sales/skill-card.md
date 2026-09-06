## Description:

MiniMax H3 电商带货视频 | LinkPix helps e-commerce operators, short-video teams, and ad buyers use qhkit/Qinghu AI to generate MiniMax H3 product and social ad videos from product images, selling points, and selected video options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, short-video teams, and advertising teams use this skill to prepare product images, selling points, model choices, and qhkit video commands for MiniMax H3-style product promotion videos. It supports social commerce, marketplace ads, product showcase clips, and related short-form sales video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product media, prompts, and generated-video requests may be sent to qhkit/Qinghu services.

Mitigation: Use only approved product assets and avoid confidential media unless the organization permits that service path.

Risk: API keys could be exposed if users paste raw credentials into chat or shared logs.

Mitigation: Configure credentials through QHKIT_TOKEN or a platform secret mechanism, and avoid entering raw API keys in prompts.

Risk: The skill includes broad host setup steps such as installing or upgrading Node and qhkit tooling.

Mitigation: Prefer preinstalled, pinned qhkit tooling and review install or upgrade commands before execution.

Risk: Video generation can consume paid credits and submitted tasks may not be cancelable.

Mitigation: Run an estimate when supported and get explicit approval for model, duration, orientation, assets, and expected credits before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, status guidance, credit estimates, and generated video URLs after user-confirmed paid generation.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
