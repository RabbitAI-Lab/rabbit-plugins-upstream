## Description:

Generates and edits Tmall flagship-store ecommerce visuals, including product hero images, detail-page key visuals, storefront banners, launch graphics, campaign backgrounds, member marketing images, SKU sets, and brand-consistent reference-image outputs through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Brand ecommerce operators, designers, and developers use this skill to generate Tmall-ready product and campaign visuals while preserving product, packaging, Logo, SKU, and brand-system references. Final prices, promotion mechanics, legal text, complex Chinese copy, and current Tmall category or campaign requirements should be reviewed and added by human operations or design staff before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and can store it locally under ~/.ai-hive/config.json.

Mitigation: Use a scoped key where possible, protect the local config file, rotate keys if exposed, and remove the file when the skill is no longer needed.

Risk: Selected product and brand reference files are uploaded to AI Hive during generation.

Mitigation: Only upload assets approved for the intended service, and avoid confidential, embargoed, or rights-restricted materials unless sharing with AI Hive is permitted.

Risk: Changing --base-url sends the API key and uploaded media to the configured service.

Mitigation: Use the default endpoint unless an alternate endpoint is trusted and approved for the data being processed.

Risk: Generated ecommerce visuals may contain incorrect claims, campaign details, platform marks, or copy that is not publication-ready.

Mitigation: Have operations, legal, and design reviewers add and verify pricing, promotion mechanics, complex Chinese text, certifications, platform marks, and current Tmall requirements before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/tmall-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides API-key setup, media upload, task polling, and image-download workflows for AI Hive image generation.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
