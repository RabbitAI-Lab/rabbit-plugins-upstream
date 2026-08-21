## Description:

用 AI Hive Nano Banana Pro 将已授权成年模特图与已授权服装 SKU 图组合成可审核的虚拟试穿商品图，锁定人物身份与身体比例、服装版型与纹理、层叠遮挡和电商构图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion sellers and brand teams use this skill to generate authorized adult virtual try-on product images for apparel listings and visual review. Outputs are visual previews and are not sizing, fit, material-performance, or purchase guarantees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected model, garment, and optional background images to AI Hive.

Mitigation: Use only authorized adult person, garment, and background assets, and install only when that external upload is acceptable.

Risk: The tool can store an AI Hive API key locally.

Mitigation: Prefer environment or command-line credentials when appropriate, restrict stored key permissions, and remove ~/.ai-hive/config.json when local storage is no longer wanted.

Risk: Virtual try-on images may be mistaken for real sizing or fit guarantees.

Mitigation: Review outputs as visual previews only and avoid using them as claims about sizing, fit, material performance, or purchase commitments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/virtual-try-on-product-image-generation)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash command examples and Python CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are submitted through AI Hive, may be downloaded locally, and require authorized adult person and garment references.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
