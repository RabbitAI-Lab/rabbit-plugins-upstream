## Description:

Uses Seedream 5.0 Lite through AI Hive to generate and edit marketing images for campaign key visuals, ads, social media, banners, email, and landing pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, ecommerce, and creative teams use this skill to turn a campaign brief, product references, and brand assets into Seedream 5.0 Lite marketing visuals and channel variants. It supports campaign key visuals, ad concepts, social posts, banners, activity backdrops, email hero images, and landing page hero images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a user-provided AI Hive API key.

Mitigation: Use a dedicated key, store it only through the documented environment variable or local config path, keep local file permissions restricted, and rotate the key when access is no longer needed.

Risk: Selected reference files can be uploaded to AI Hive or its object storage.

Mitigation: Do not pass sensitive, confidential, or legally restricted assets to the upload or image options; use approved product and brand references only.

Risk: The bundled helper includes broader generic AI Hive client code than the advertised image-only workflow.

Mitigation: Review the helper before deployment in strict image-only environments and limit agent use to the documented generate, task, upload, and init paths.

Risk: Generated marketing visuals may imply unsupported claims, prices, promotions, logos, awards, or legal text.

Mitigation: Keep copy, pricing, promotion mechanics, legal statements, and final brand approvals in a separate human review and layout step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-marketing-image)
- [AI Hive OpenAPI base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files are saved locally by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided AI Hive API key, can upload selected reference images, supports batch generation, and can submit tasks without downloading results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
