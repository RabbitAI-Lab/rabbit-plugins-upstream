## Description:

自动识别并修改图片中的文字内容，无需重新设计图片，快速替换标题、价格、卖点及促销信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to edit text embedded in ecommerce images, including prices, titles, selling points, and promotional copy, through the Qinghu qhkit image workflow. It is suited to targeted text replacement where the edited image must still be visually checked for spelling, numbers, logo fidelity, and product detail changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the qhkit npm CLI globally without pinning a reviewed package version.

Mitigation: Use a pinned, reviewed qhkit version in an isolated environment and avoid automatic @latest upgrades.

Risk: Using the skill can upload target images and prompts to Qinghu's service with a user-provided token.

Mitigation: Use a scoped and revocable API token, and avoid submitting images or prompts that should not be shared with that service.

Risk: Generated image edits can alter product details or produce incorrect text, numbers, prices, or logo details.

Mitigation: Visually inspect each result before delivery or publication, with extra attention to spelling, prices, logos, and product structure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-text-edit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands and concise user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or relay image URLs and credit estimates returned by the qhkit CLI.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
