## Description:

Creates Nano Banana Pro livestream commerce image assets through AI Hive, including host-and-product key art, reusable backgrounds, category transitions, product cards, and multi-platform cover images with a consistent live-room style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, livestream operators, and ecommerce creative teams use this skill to generate consistent image assets for product showcases, live-room backgrounds, transitions, product cards, and promotional covers. It is suited for ClawHub users who can provide AI Hive credentials and review generated media before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses AI Hive as a remote processor for prompts and selected media.

Mitigation: Install and run it only when remote processing through AI Hive is acceptable for the intended content.

Risk: Configured API keys act as billing credentials.

Mitigation: Store the API key securely, restrict local config file permissions, and rotate the key if it is exposed.

Risk: Reference images or uploads may include private files.

Mitigation: Do not pass private or sensitive files through --image or upload unless they are approved for AI Hive processing.

Risk: Generated livestream assets can contain inaccurate prices, promotional claims, or text if those details are left to the model.

Mitigation: Keep prices, inventory, promotions, and final copy sourced from operations systems and review all generated media before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-livestream-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Image files, Guidance]

**Output Format:** [Markdown guidance with bash command examples; runtime commands submit image-generation tasks and download PNG results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive remote processing and may upload user-selected reference media to the configured AI Hive endpoint.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
