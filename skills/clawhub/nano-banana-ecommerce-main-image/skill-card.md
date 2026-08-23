## Description:

Creates reviewable ecommerce main-image briefs and AI Hive Nano Banana 2 render jobs from authorized SKU reference images while keeping product facts, required visual elements, permitted changes, platform use, and safe zones explicit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and creative teams use this skill to prepare SKU-controlled main-image briefs and submit AI Hive Nano Banana 2 render jobs from authorized product reference images for marketplace hero, white-background, lifestyle, feature, and localized storefront assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product reference images and prompt details are sent to AI Hive during render and upload operations.

Mitigation: Run render or upload only when the selected assets can be shared with AI Hive; use the brief command to inspect the generated prompt without upload or cost.

Risk: Saved AI Hive credentials may persist on the local machine.

Mitigation: Use AI_HIVE_API_KEY or --api-key for temporary use, or review ~/.ai-hive/config.json permissions after using the auth command.

Risk: Generated product imagery can drift from actual SKU facts or current marketplace rules.

Mitigation: Compare outputs against authorized reference images and manually review size, crop, text, claims, safe zones, and restricted-category requirements before publication.

Risk: Required text in generated images may be incorrect.

Mitigation: Manually check required text character by character before using the asset.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-ecommerce-main-image)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash command examples and CLI-generated prompt text; render and status commands can produce downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-selected product reference images and an AI Hive API key for render, upload, and status commands; the brief command only emits prompt text.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
