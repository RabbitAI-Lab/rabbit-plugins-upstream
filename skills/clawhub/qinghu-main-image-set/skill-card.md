## Description:

智能识别商品主体，根据一张产品图一键生成不同类型、不同电商平台风格的主图+轮播图套图，无需写提示词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to turn one product image and optional marketing copy into platform-specific product main images and carousel image sets through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade an unpinned third-party qhkit CLI from npm.

Mitigation: Confirm user approval before installing or upgrading qhkit, and prefer an explicit package version or reviewed package metadata before use.

Risk: The qhkit workflow uploads selected product images and marketing copy to Qinghu.

Mitigation: Confirm that the selected files and text are intended for upload before running generation or estimate commands.

Risk: The workflow stores or uses a QHKIT token.

Mitigation: Ask the user before token setup, avoid exposing the token in logs or replies, and rely on environment variables or the CLI's masked configuration output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-main-image-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return qhkit result JSON containing generated image URLs and actual credit usage.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
