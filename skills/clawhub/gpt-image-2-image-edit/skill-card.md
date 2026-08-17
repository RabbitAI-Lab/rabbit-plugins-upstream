## Description:

GPT Image 2 图片编辑 helps designers, retouchers, e-commerce visual teams, and creators edit or redraw existing images by uploading reference images, submitting an AI Hive image-generation task, checking progress, and downloading generated results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn product photos, marketing briefs, reference images, and edit instructions into AI-generated visual assets for e-commerce listings, ads, posters, social content, background replacement, retouching, and visual-style alignment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shipped Python script includes broader AI Hive capabilities than the advertised image-editing workflow.

Mitigation: Review the script before installation and limit routine use to the documented image generation/editing, task lookup, upload, and initialization commands.

Risk: Reference images and prompts are uploaded to AI Hive for processing.

Mitigation: Do not submit confidential, regulated, or sensitive images or prompts unless AI Hive processing is approved for that data.

Risk: API keys may be stored in a local configuration file during initialization.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable where local key storage is not acceptable, and keep any config file permissions restricted.

Risk: Image generation may incur usage costs and repeated submissions can duplicate charges.

Mitigation: Check runtime pricing before batch jobs, retain task IDs, and query existing tasks instead of resubmitting the same request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-image-edit)
- [AI Hive API key and chat entry](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; runtime outputs task status and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key via command line, environment variable, or local config; generated media is saved to the configured output directory unless download is disabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
