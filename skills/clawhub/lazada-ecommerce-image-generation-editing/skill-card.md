## Description:

Create and edit Lazada product catalog images, SKU galleries, specification graphics, campaign tiles and localized storefront visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and developers use this skill to generate Lazada-ready product images, SKU galleries, campaign tile bases, localization backgrounds, and variant matrices while preserving product details and leaving claims for approved copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images and prompts are uploaded to AI Hive.

Mitigation: Use only approved product assets, avoid unrelated private files, and confirm that the upload is acceptable before running generation commands.

Risk: The workflow stores or reads an AI Hive API key locally.

Mitigation: Use a dedicated key, keep the config file private, prefer environment variables where appropriate, and rotate the key if it may have been exposed.

Risk: Batch generation can create API usage costs.

Mitigation: Check AI Hive live configuration and pricing before multi-market or high-volume batch runs.

Risk: Generated ecommerce imagery may accidentally imply unapproved prices, ratings, seller badges, warranties, specifications, or platform claims.

Mitigation: Keep offers and claims out of generated pixels, add approved copy after generation, and validate Lazada marketplace rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/lazada-ecommerce-image-generation-editing)
- [AI Hive API base endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task responses from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, optional reference images, routing modes, batch size, model parameters, task polling, and optional local downloads.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
