## Description:

Helps designers, retouchers, e-commerce visual designers, and creators generate or edit Amazon listing, A+ content, product detail, advertising, poster, social commerce, retouching, background replacement, and character-consistent images from text prompts and optional reference images through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, designers, e-commerce sellers, and marketing teams use this skill to produce or edit product listing images, Amazon A+ visuals, product detail images, ad creatives, posters, social commerce covers, and reference-guided image variants without writing API code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and optional reference media to AI Hive for image generation or editing.

Mitigation: Use it only when external AI Hive processing is acceptable, and avoid sensitive commercial or personal assets unless approved.

Risk: Batch generation, uploads, and task submission may consume API credits.

Mitigation: Confirm user intent before uploads or batch generation and review routing, batch size, and pricing before submitting tasks.

Risk: The security summary says the activation scope is broader than the core image-generation purpose.

Mitigation: Review activation behavior before installation and invoke the skill only for image generation/editing workflows that match the documented purpose.

Risk: The skill depends on API key configuration for a third-party service.

Mitigation: Store API keys only in approved secret stores or the documented config path with restricted permissions, and do not expose keys in prompts, logs, or shared files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/amazon-listing-image-generation-editing)
- [AI Hive chat and API key page](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; generated image files are downloaded as PNG/JPEG/WebP or other model-supported formats.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompt text, optional reference images, batch size, routing mode, model parameters, API key configuration, task polling, and output-directory settings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
