## Description:

Creates and edits Walmart Marketplace product images, variant galleries, package-content views, dimension bases, and omnichannel retail visuals using AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers, ecommerce operators, and retail creative teams use this skill to generate and edit Walmart listing imagery while preserving approved item, package, variant, dimension, and claim facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected product/reference images and prompts to AI Hive.

Mitigation: Use it only for material approved for AI Hive processing and avoid confidential or restricted product data unless that transfer is permitted.

Risk: The AI Hive API key is a real credential that may be stored locally.

Mitigation: Keep the key revocable, prefer environment-based secret handling where practical, and rotate or revoke it if exposed.

Risk: Generated retail imagery can misstate product facts, quantities, dimensions, claims, or marketplace availability.

Mitigation: Review outputs against Walmart Marketplace requirements and merchant-approved item records before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/walmart-ecommerce-image-generation-editing)
- [AI Hive API console](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files or task JSON from the AI Hive command-line workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, accepts product/reference images and prompts, and writes downloaded outputs to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
