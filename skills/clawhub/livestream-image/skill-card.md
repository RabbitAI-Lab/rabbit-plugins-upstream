## Description:

Creates mobile-readable livestream shopping visual assets with Nano Banana 2 through AI Hive, including room backgrounds, product explanation cards, benefit panels, countdown placeholders, and emergency static screens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to generate livestream shopping visual layouts and image-generation commands while preserving mobile safe areas and leaving live prices, inventory, discounts, timers, and QR codes for real-time overlays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional reference images are sent to AI Hive or its upload storage.

Mitigation: Use only images and prompts that the user is permitted to share with AI Hive, and avoid confidential or sensitive product materials unless policy allows that transfer.

Risk: The AI Hive API key may be stored locally in ~/.ai-hive/config.json.

Mitigation: Prefer environment variables for temporary use or keep the config file restricted to the current user, and rotate the key if it may have been exposed.

Risk: Generated livestream visuals can imply incorrect product details, prices, inventory, offers, or countdown timing if live data is embedded directly.

Mitigation: Review generated assets before use and keep prices, stock, discounts, timers, QR codes, and other live commercial information as real-time overlays controlled by the livestream operator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/livestream-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples; command execution may return JSON task details and download generated PNG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key supplied by command line, environment variable, or ~/.ai-hive/config.json; optional user-provided reference images may be uploaded to AI Hive.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
