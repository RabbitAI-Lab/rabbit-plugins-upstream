## Description:

Uses Seedream 5.0 Lite through AI Hive to retouch authorized product photos by removing reversible photographic defects while preserving product structure, materials, labels, and commercial facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to prepare ecommerce product images by cleaning dust, scratches, wrinkles, reflections, edges, and background defects while keeping factual product details intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retouching may remove real damage or alter labels, quantity, materials, color, or other commercial facts.

Mitigation: Compare original and output at 100% and 200%, keep locked facts unchanged, and reject outputs that misrepresent the product.

Risk: Selected product images and prompts are sent to AI Hive, and an API key may be stored locally when init is used.

Mitigation: Use only images approved for upload, protect the API key, and keep the local configuration file private.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-product-retouch)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one user-selected product image and an AI Hive API key; generated images download to the configured output directory.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
