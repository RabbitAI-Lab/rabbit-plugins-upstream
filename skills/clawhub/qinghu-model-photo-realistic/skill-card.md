## Description:

青虎AI 模特图去 AI 感超写实：上传模特图一键去除 AI 感，提亮肤色、修复细节、还原真实皮肤质感并做高清超分，专为电商模特图优化设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to process ecommerce model or portrait images with Qinghu AI so the agent can estimate cost, confirm paid generation, submit a one-image workflow, poll for completion, and return the generated image result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected model images to Qinghu's external service.

Mitigation: Use only images the user owns or is authorized to process, and disclose that the selected image will be uploaded before generation.

Risk: The skill uses a Qinghu API token and can persist credentials through qhkit configuration.

Mitigation: Prefer pre-provisioned credentials or environment-scoped tokens, avoid exposing token values in chat, and confirm configuration failures without retrying with guessed credentials.

Risk: The skill may spend Qinghu credits when generation is submitted.

Mitigation: Run estimate first, report the expected charge and key parameters, and wait for explicit user approval before any generate action.

Risk: The skill can install or upgrade Node, qhkit, or supporting image tooling.

Mitigation: Require approval before package installation, runtime upgrades, or fallback compression tooling, and report installation failures clearly.

Risk: Broad photo-editing trigger phrases may invoke the skill outside its intended model-photo use case.

Mitigation: Confirm the input is a model or portrait image and redirect product, scene, outfit-change, face-swap, or background-change requests to more appropriate workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-model-photo-realistic)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI website](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, API calls]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may return generated image URLs and a final credit-consumption line after workflow completion.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
