## Description:

Creates a coherent scroll-based visual narrative for product detail pages with Nano Banana Pro, using AI Hive to generate consistent opening, problem, reveal, material-proof, usage, and closing image modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce teams, brand marketers, designers, and agent operators use this skill to plan and generate consistent product detail page visuals for channels such as Taobao, Tmall, Amazon A+, Shopify PDPs, long-form detail images, brand stories, product scenes, and launch pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are uploaded to AI Hive during generation.

Mitigation: Use only media that is approved for AI Hive processing, and avoid unreleased or confidential product assets unless AI Hive handling and retention terms are acceptable.

Risk: The workflow stores an AI Hive API key locally when initialized.

Mitigation: Keep the local config file private, prefer environment variables where appropriate, do not commit credentials, and rotate exposed keys.

Risk: Generated product-detail visuals can drift from approved product structure, material, logo, color, pricing, or claim requirements.

Mitigation: Review generated modules against source product media and approved copy before publication, especially for claims, prices, sizes, and marketplace policy compliance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-product-detail-page)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; the bundled CLI returns task JSON and can download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts, reference images, batch size, aspect-ratio parameters, AI Hive API credentials, task polling, and an output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
