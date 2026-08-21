## Description:

服饰图生成（模特/服装类）。支持单张或套图：白底图（隐形模特）、模特图、种草图、卖点图、A+图、尺码图。单张单类型直接出图；多张多类型自动编排规划。用户上传模特图或服饰图（上装/下装/连衣裙/外套/鞋帽等）并说"做套图""做模特图""做种草图""做卖点图""做A+图""做尺码图""做服饰白底图"时触发。纯图片编辑操作走 linkfox-aigc-imagegen。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and creative teams use this skill to generate apparel product images from clothing or model references, including white-background, model, social-scene, selling-point, A+ content, and size-chart images. It supports both one-off image requests and planned multi-image sets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles apparel images, prompts, API credentials, and account or billing actions through LinkFox workflows.

Mitigation: Install and use it only where LinkFox is a trusted service provider, and require explicit user consent before login, API-key, payment, upload, or child-model generation flows.

Risk: Upload flows can make local files publicly accessible.

Mitigation: Confirm that any file is safe to publish before invoking upload behavior, and do not upload sensitive or private content.

Risk: Job or state files that contain arbitrary script paths could expand execution beyond the intended packaged workflow.

Mitigation: Use only the packaged scripts and validated state files; do not accept or inject arbitrary script paths from untrusted job data.

Risk: Endpoint environment variables could redirect prompts, images, credentials, or account actions away from trusted LinkFox hosts.

Mitigation: Keep LINKFOX_* endpoint variables pointed only at trusted LinkFox hosts and review environment configuration before deployment.

Risk: Generated ecommerce imagery may reflect biased model-generation rules or inaccurate apparel, model, scene, and size-chart assumptions.

Mitigation: Review generated outputs for product accuracy, representation, rights-sensitive text, and platform compliance before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-imagegen-cloth)
- [Skill Definition](artifact/SKILL.md)
- [Runtime Workflow Index](artifact/references/runtime/00-index.md)
- [Delivery Protocol](artifact/references/runtime/03-deliver.md)
- [White Background Image Type](artifact/references/types/white-bg.md)
- [Model Image Type](artifact/references/types/model-image.md)
- [Scene Image Type](artifact/references/types/scene.md)
- [Selling Point Image Type](artifact/references/types/selling-point.md)
- [A+ Image Type](artifact/references/types/aplus.md)
- [Size Image Type](artifact/references/types/size.md)
- [LinkFox Image Generation API Reference](artifact/skills/linkfox-aigc-imagegen/references/api.md)
- [LinkFox Text Generation API Reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [LinkFox File Upload API Reference](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown responses with inline image references, JSON parameter files, and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local data and media files while coordinating LinkFox text generation, image generation, and optional upload flows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
