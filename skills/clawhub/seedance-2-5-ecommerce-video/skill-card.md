## Description:

Generates traceable Seedance 2.5 ecommerce Listing, PDP, and detail-page short clips where each slot answers one buying question, such as included items, dimensions, compatibility, setup steps, material details, SKU variants, or feature evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators and content production teams use this skill to create fact-bound product video modules from approved SKU records, product media, platform policy guards, and post-production text maps. It is intended for Listing, PDP, and detail-page clips that each answer a single shopper question.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The clip command uploads selected product images or videos to AI Hive.

Mitigation: Use --preview before generation and upload only approved product media that is appropriate for the AI Hive service.

Risk: Generated clips may be saved under ~/Downloads/AiHive by default.

Mitigation: Use --output-dir for a controlled destination or --no-download when local persistence is not desired.

Risk: The API key can be stored in ~/.ai-hive/config.json.

Mitigation: Prefer AI_HIVE_API_KEY when avoiding a stored key, and keep any config file permissions restricted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-ecommerce-video)
- [AI Hive OpenAPI root](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples, JSON previews, and configuration instructions; clip runs may create MP4 files through AI Hive.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses approved product media and factual constraints to build prompts; supports preview mode before upload or billing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
