## Description:

Creates GPT Image 2 livestream commerce image assets, including warm-up posters, live covers, room backgrounds, product explainer cards, promotion transition graphics, and replay covers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, designers, and developers use this skill to generate base images for livestream campaigns while keeping dates, prices, inventory, promotions, and platform-specific claims in later review and layout steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-selected reference media to AI Hive for generation.

Mitigation: Use only media that is approved for upload, avoid private or sensitive reference files, and review each command's image paths before execution.

Risk: The skill stores or reads an AI Hive API key locally or from the AI_HIVE_API_KEY environment variable.

Mitigation: Keep local key files restricted, prefer scoped credentials where available, and rotate the key if it may have been exposed.

Risk: Generated commerce assets may contain incorrect product details, prices, discounts, inventory statements, or advertising claims.

Mitigation: Compare final assets against the live-session source of truth and current platform advertising rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-livestream-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; generated image files are downloaded as PNG files unless no-download is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional reference images, batch size, routing mode, output directory, and model parameters such as aspect ratio.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
