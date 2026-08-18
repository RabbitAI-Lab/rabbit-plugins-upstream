## Description:

Create and edit Temu product submission images, variant sets, package-content graphics, feature galleries and multi-market campaign bases. Use this skill for Temu商品图、跨境商品主图、工厂批量SKU、白底图、规格图、套装清单、多国家本地化、商品精修和广告测图；supports reference-guided AI Hive production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, catalog teams, and developers use this skill to plan and run reference-guided AI Hive image generation and editing for Temu product masters, SKU variants, package-content images, feature galleries, and localized campaign bases while preserving verified product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference media and prompts may be sent to the AI Hive API.

Mitigation: Use only files and prompts intended for that external service, and avoid unrelated private or sensitive materials.

Risk: The skill stores or reads an AI Hive API key through local configuration or environment variables.

Mitigation: Keep API keys private, prefer environment variables or restricted config-file permissions, and rotate any key that may have been exposed.

Risk: Batch generation can create unexpected cost or volume before quality is confirmed.

Mitigation: Confirm one SKU and live cost before scaling to batch generation.

Risk: Generated ecommerce images can misstate product geometry, labels, included parts, claims, or market requirements.

Mitigation: Map each output to a verified product master and SKU row, manually review factual details, and recheck current Temu seller requirements for the target category and market.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/temu-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with bash command examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for image-generation workflows; executing the bundled CLI can upload references, create AI Hive tasks, poll task status, and download generated image files.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
