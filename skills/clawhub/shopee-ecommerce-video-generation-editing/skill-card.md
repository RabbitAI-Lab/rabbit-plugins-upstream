## Description:

Creates and edits Shopee product videos, localized demos, short-form ads, and seller campaign assets for Southeast Asian ecommerce markets using AI Hive video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and creative teams use this skill to generate, adapt, and review Shopee-oriented product videos for localized marketplace campaigns while preserving approved product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an AI Hive API key when initialized.

Mitigation: Review ~/.ai-hive/config.json after initialization, keep the file private, and rotate the key if it may have been exposed.

Risk: Selected product images, videos, or audio are uploaded to AI Hive for generation workflows.

Mitigation: Use only media approved for upload to AI Hive, and avoid sending confidential, restricted, or rights-uncleared assets.

Risk: Generated output may be downloaded automatically to the local filesystem.

Mitigation: Use --no-download to inspect task responses first or --output-dir to control where generated files are saved.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/shopee-ecommerce-video-generation-editing)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown guidance with bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can submit AI Hive video tasks, poll task status, upload media, and optionally download generated video files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
