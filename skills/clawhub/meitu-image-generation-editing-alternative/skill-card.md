## Description:

This skill helps agents migrate Meitu-style image generation and editing tasks into reproducible AI Hive workflows for product retouching, portrait lighting, poster backgrounds, multi-SKU shoots, and social-media crops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Commercial creative operators and developers use this skill to convert Meitu-like image generation and editing requests into repeatable AI Hive prompts and CLI commands for approved product, portrait, poster, SKU, and social-media image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images provided with --image are uploaded to AI Hive for generation or editing.

Mitigation: Use only images the user is authorized to process, avoid sensitive inputs unless permitted, and confirm that AI Hive handling matches the intended data policy.

Risk: The API key may be stored at ~/.ai-hive/config.json.

Mitigation: Prefer environment variables for transient use or keep the config file permission-restricted, rotate exposed keys, and remove stored credentials when no longer needed.

Risk: Generated results are downloaded locally and may contain altered product, identity, label, price, or claim details.

Mitigation: Review each output against the approved source assets and add critical Chinese text, pricing, and legal statements in a controlled post-production step.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/meitu-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash examples, CLI status text, JSON task responses, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed AI Hive image model, accepts optional reference images, can batch requests, and can download generated image results locally.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
