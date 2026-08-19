## Description:

Nano Banana 2 图生图 helps agents turn selected reference images such as sketches, photos, product shots, and existing designs into controlled image-to-image variants through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to guide Nano Banana 2 image-to-image edits with an explicit change budget, preserving selected subjects, layouts, products, or scene structure while changing approved attributes such as color, weather, style, setting, completion level, or aspect ratio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images and prompts are uploaded to AI Hive for image generation.

Mitigation: Use only images and prompts that are appropriate to send to AI Hive; avoid sensitive or private content unless that matches the intended use.

Risk: The AI Hive API key can be stored locally for repeated use.

Mitigation: Keep the key private and review ~/.ai-hive/config.json after initialization; the helper stores the file with 0600 permissions.

Risk: Generated edits can be mistaken for factual product, space, or person evidence.

Mitigation: Label substantial edits as synthetic or concept versions and compare outputs against the approved change budget before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-image-to-image)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; the helper script can return JSON task details and download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one user-selected reference image for generation; supports batch size, routing mode, model parameters, task lookup, uploads, and output directory selection.]

## Skill Version(s):

1.0.1 (source: release evidence and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
