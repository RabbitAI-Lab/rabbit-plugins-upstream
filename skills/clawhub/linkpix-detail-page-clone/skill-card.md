## Description:

帮助电商运营和设计人员基于优秀商品详情页截图与自有商品图，生成相似布局和视觉风格的商品详情页图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and designers use this skill to analyze a competitor or reference detail page and generate matching product detail images for their own products. The workflow requires replacing copy with the user's own messaging and avoiding source brands, logos, and products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update a third-party CLI globally.

Mitigation: Use an isolated environment, avoid privileged global installs where possible, and verify npm install or upgrade commands before running them.

Risk: API tokens may be exposed during qhkit setup.

Mitigation: Do not paste tokens into chat; use a dedicated token with limited exposure and prefer environment-based configuration when available.

Risk: Generated detail pages may resemble competitor assets too closely or include unwanted brand elements.

Mitigation: Require user-provided replacement copy, preserve the no-source-brand constraint, and review generated outputs before publication.

Risk: Layout replication is generative and may not match the reference at pixel-level precision.

Mitigation: Set expectations before generation and iterate screen by screen when a long reference page is used.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-detail-page-clone)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses with generated image URLs and credit usage.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
