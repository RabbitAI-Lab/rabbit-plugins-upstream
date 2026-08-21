## Description:

Create and edit TikTok Shop UGC sales videos, product demos, unboxings, Spark Ads and GMV Max creative variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and creative teams use this skill to create TikTok Shop-style product demo, unboxing, localization, Spark Ads, and GMV Max video workflows from merchant-provided product facts and media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper requires an AI Hive API key and can upload product photos, videos, or audio selected by the user.

Mitigation: Use only approved media and an intended AI Hive account; keep the API key in the supported environment variable or local config file with restricted permissions.

Risk: Generated sales videos may contain unsupported commercial claims if prompts or review steps are incomplete.

Mitigation: Review generated scripts and videos against merchant-provided product facts, approved offers, usage rights, and current TikTok Shop or advertising rules before publishing.

Risk: Generated outputs are downloaded locally by default.

Mitigation: Set an appropriate output directory or use no-download mode when local storage of generated media is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/tiktok-shop-viral-sales-video-generation)
- [ClawHub Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API Base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API Key Setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples, JSON task responses, and downloaded media files from the helper CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can upload user-selected product media, submit AI Hive video tasks, poll task status, and download generated videos or images locally.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
