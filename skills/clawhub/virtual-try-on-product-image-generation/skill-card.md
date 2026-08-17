## Description:

Generates and edits e-commerce product and virtual try-on images from prompts and optional reference images through AI Hive, then tracks generation tasks and downloads outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, product photographers, brand teams, and livestream commerce teams use this skill to create product main images, detail-page visuals, ad creatives, posters, social commerce images, retouched product images, background replacements, and consistent-character visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive as a third-party image-generation service.

Mitigation: Use only authorized, non-sensitive assets and avoid uploading personal photos, confidential product assets, or copyrighted materials unless permission exists.

Risk: The skill may activate for broad shopping, platform, or tool-comparison queries that are not clearly image-generation requests.

Mitigation: Review the user intent before running the skill and execute it only when the user wants image generation or image editing.

Risk: The skill can store an AI Hive API key locally in the user's home directory.

Mitigation: Prefer environment variables or confirm the local config file remains restricted to the user; rotate the key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/virtual-try-on-product-image-generation)
- [AI Hive user onboarding](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files, JSON]

**Output Format:** [Markdown guidance with shell command examples; CLI output may include JSON task data and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; selected prompts and reference images are sent to AI Hive for generation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
