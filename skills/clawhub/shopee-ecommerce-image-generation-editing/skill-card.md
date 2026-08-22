## Description:

Create and edit Shopee product listing images, variant galleries, package-content visuals, localized campaign bases and livestream product cards for Southeast Asian markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and ecommerce creative teams use this skill to generate or edit Shopee listing, gallery, livestream, localization, and campaign image bases while keeping market, SKU, package, and offer facts reviewable.

### Deployment Geography for Use:

Southeast Asia and Taiwan marketplaces: Indonesia, Thailand, Vietnam, Malaysia, the Philippines, Singapore, and Taiwan.

## Known Risks and Mitigations:

Risk: Prompts and selected reference images may be sent to AI Hive.

Mitigation: Use project-appropriate images and avoid uploading confidential product assets unless the AI Hive account and governing policies allow it.

Risk: The AI Hive API key may be stored locally for repeated use.

Mitigation: Prefer approved secret handling, keep the local config protected, and rotate the key if exposure is suspected.

Risk: Generated files may remain in the configured output directory.

Mitigation: Review and remove generated files from Downloads or the configured output path when they should not persist.

Risk: Generated marketplace images can accidentally imply incorrect offers, prices, ratings, badges, warranties, or localized claims.

Mitigation: Keep offer and platform UI elements outside the generated image, validate one marketplace before scaling, and use native reviewers for local copy and units.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/shopee-ecommerce-image-generation-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON API responses, and generated image files from the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, batch generation, live model parameters, routing options, submit-only mode, task polling, and downloads to a configured output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
