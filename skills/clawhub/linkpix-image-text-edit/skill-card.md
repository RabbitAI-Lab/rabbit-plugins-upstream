## Description:

自动识别并修改图片中的文字内容，无需重新设计图片，快速替换标题、价格、卖点及促销信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to guide an agent through LinkPix/qhkit image text edits, such as replacing prices, titles, promotional copy, and selling points while preserving the rest of the image as much as possible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and upgrades a third-party CLI package that can affect the local agent environment.

Mitigation: Review the skill before installation, trust the qhkit package before use, and prefer a pinned or local install where possible.

Risk: API tokens and uploaded image files may be exposed to the LinkPix service.

Mitigation: Treat QHKIT_TOKEN and configured API tokens as sensitive, and avoid using images that should not be uploaded to the service.

Risk: Generated image edits can alter product details, prices, logos, or text accuracy.

Mitigation: Manually inspect each output image, especially prices and brand-critical details, before delivery or publication.

Risk: Image generation may consume credits or fail when account balance is insufficient.

Mitigation: Use qhkit estimate before quoting credit use, and tell users when the tool reports insufficient balance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [npm package: @iqinghu/qhkit](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and qhkit JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image generation URLs and credit-use guidance through the qhkit CLI; generated images require manual visual inspection.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
