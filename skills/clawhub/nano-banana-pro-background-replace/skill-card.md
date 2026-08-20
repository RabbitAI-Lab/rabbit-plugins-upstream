## Description:

Replaces, removes, and extends product or portrait image backgrounds with Nano Banana Pro through AI Hive while preserving subject identity, product facts, lighting, scale, shadows, and reflections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and run background replacement workflows for ecommerce product images, portraits, lifestyle scenes, studio backgrounds, and localized advertising variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and uploads the specific images selected by the user to AI Hive.

Mitigation: Install only when that credential use and image upload are acceptable; review prompts and file paths before running generate or upload.

Risk: Generated background replacements may save output files locally by default.

Mitigation: Use --no-download to submit without downloading, or set --output-dir to control where generated files are stored.

Risk: Image composites can unintentionally change subject identity, product facts, logos, colors, shadows, reflections, or platform compliance.

Mitigation: Use the skill's compositing checks, compare against the original image, follow the target platform's current policies, and keep audit records for source and generated images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-background-replace)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key portal](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with bash command examples and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI Hive image editing tasks, upload selected input images, and download generated image files unless --no-download is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
