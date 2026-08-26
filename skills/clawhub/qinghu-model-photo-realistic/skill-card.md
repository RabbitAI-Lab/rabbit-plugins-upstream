## Description:

青虎AI 模特图去 AI 感超写实：上传模特图一键去除 AI 感，提亮肤色、修复细节、还原真实皮肤质感并做高清超分，专为电商模特图优化设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce image operators use this skill to submit a single model or portrait image to the Qinghu workflow for more realistic skin texture, brighter tone, detail repair, and high-resolution enhancement. It is intended for authorized model or portrait images, especially e-commerce model photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow processes model or portrait imagery and may be inappropriate for unauthorized or rights-restricted images.

Mitigation: Use only images the user owns or is authorized to process, and remind users about commercial-use rights when needed.

Risk: Generation is a paid workflow and can consume Qinghu credits.

Mitigation: Run an estimate first, present expected credit use and key parameters, and wait for explicit user approval before submitting generation.

Risk: The skill asks for Qinghu API-token configuration and includes broad installation steps.

Mitigation: Prefer local environment variables or secure credential storage for tokens, avoid pasting secrets into chat, and review installs before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-photo-realistic)
- [Publisher profile: autoagc](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu website](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent through qhkit setup, estimate, user approval, generation, status polling, and delivery of resulting image URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
