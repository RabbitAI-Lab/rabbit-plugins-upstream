## Description:

青虎AI 图片高清写实去 AI 感：极速出图，增强画面细节、去除 AI 生成图片的油腻失真感、提升画面统一度并减少图像偏移，快速得到写实高清图像。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit a Qinghu AI qhkit workflow that makes AI-generated non-portrait images look more realistic, sharper, and more visually consistent. It is intended for image enhancement tasks such as product and scene images where the user wants to reduce obvious AI-generated texture or distortion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade local qhkit tooling before running the workflow.

Mitigation: Prefer a preinstalled, reviewed qhkit package and confirm package installation or upgrade behavior before deployment.

Risk: The workflow uploads selected images to Qinghu AI and may process user-provided media through that service.

Mitigation: Use only images the user owns or is authorized to process, and confirm the user accepts Qinghu AI processing before submission.

Risk: The workflow can consume Qinghu credits when generate is submitted.

Mitigation: Run estimate first, present the selected workflow, field values, source files, and expected credit cost, and submit only after explicit user approval.

Risk: The skill requires a Qinghu API token or platform-managed credential.

Mitigation: Use managed secrets or a preconfigured qhkit environment where possible; avoid asking users to paste long-lived API keys into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-deai-hd)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu AI API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs an agent to use qhkit workflow commands, report generated image URLs, and disclose actual Qinghu credit consumption after successful completion.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
