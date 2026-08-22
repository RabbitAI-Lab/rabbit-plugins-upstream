## Description:

一键生成服装的不同颜色版本，保持版型、材质及光影一致，无需重新拍摄即可完成 SKU 色卡图制作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agents use this skill to generate alternate color versions of a clothing product image for SKU color cards while preserving garment shape, material texture, lighting, and key details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and the qhkit package on the host environment.

Mitigation: Review installation commands before execution and prefer an isolated environment or npx fallback when global installation is not appropriate.

Risk: The skill may upload local product images to a provider service.

Mitigation: Confirm that uploaded images are approved for third-party processing before running qhkit generation commands.

Risk: Generation requests can spend account credits and cannot be canceled after submission.

Mitigation: Use qhkit estimate when supported and require explicit user confirmation of model, image count, size, reference images, and estimated credits before generate calls.

Risk: The skill can reuse an existing local qhkit credential file.

Mitigation: Verify the intended account and environment before using stored credentials or setting QHKIT_TOKEN.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit qhkit image generation jobs that return image URLs and credit usage after user confirmation.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
