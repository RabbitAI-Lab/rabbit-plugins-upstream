## Description:

Creates accurate, reusable ecommerce main images for multiple channels with Nano Banana 2, using SKU truth tables to generate white-background, scene, specification, variant, and promotional-layout versions through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, listing operators, and creative teams use this skill to prepare channel-specific product main images from approved SKU photos and explicit SKU attributes. It helps produce consistent listing assets while preserving product identity, quantity, variants, accessories, layout, and platform-safe composition requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to AI Hive for image generation.

Mitigation: Use only product images and prompts approved for that service, and confirm data-sharing acceptability before generation.

Risk: Generated images may misrepresent SKU details or fail a marketplace's current main-image rules.

Mitigation: Manually review SKU identity, quantity, structure, color, logo, accessories, packaging, text-safe areas, and target platform policy compliance before commercial use.

Risk: The AI Hive API key is a credential that may be supplied through the environment, CLI, or local config file.

Mitigation: Treat the key as sensitive, keep the local config permission-restricted, avoid sharing command histories containing keys, and rotate the key if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-main-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline bash commands; the bundled script emits JSON task responses and downloads generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI_HIVE_API_KEY or a local AI Hive config file and writes generated outputs to a configurable download directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
