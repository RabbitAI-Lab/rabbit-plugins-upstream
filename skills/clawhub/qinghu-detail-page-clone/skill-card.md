## Description:

智能分析优秀商品详情页设计，用你的商品快速生成同类型布局及视觉风格的详情图，提高详情页制作效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and design agents use this skill to reproduce the layout and visual style of a reference product-detail page for a user's own product assets. It supports competitor-detail-page matching workflows while preserving the constraint to avoid copying the original product, brand name, or logo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade an unpinned global third-party qhkit CLI.

Mitigation: Install only when the qhkit npm package and registry source are trusted; prefer a pinned, user-local, or platform-managed install.

Risk: Persistent API token setup can expose account credentials if handled broadly.

Mitigation: Use a scoped API token and run generation with access only to the images needed for the task.

Risk: Reference-page cloning can copy protected brand elements if the prompt constraint is removed.

Mitigation: Keep the documented constraint to avoid the original product, brand name, or logo, and review outputs before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-detail-page-clone)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Image URLs]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage from qhkit after the image generation command completes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
