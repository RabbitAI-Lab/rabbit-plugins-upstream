## Description:

批量把商品图处理成干净的纯白底图：自动识别商品主体、去除杂乱背景，适配平台白底图规范。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agents use this skill to convert product photos into clean white-background images in batches with Qinghu AI's qhkit CLI. It is suited for marketplace main-image preparation where users need background removal or white-background product presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade qhkit and Node tooling without pinned package versions.

Mitigation: Require user confirmation before installs or upgrades, prefer an isolated environment, and review package source and version before execution.

Risk: The workflow requires Qinghu AI token configuration and may upload product images for processing.

Mitigation: Use environment-scoped credentials or a local token store, avoid sensitive product images, and disclose external image processing before generation.

Risk: The output is generative image editing, so product details such as text, logos, or structure may change.

Mitigation: Have the user review generated images for key product details before marketplace use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-white-background)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON command parameters, status messages, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit CLI estimates, generated image links, and actual credit consumption when generation completes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
