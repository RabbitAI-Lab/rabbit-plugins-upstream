## Description:

Seedream 5.0 Lite 广告图片 helps agents create AI Hive image-generation workflows that keep ad visuals aligned with landing-page claims, audience context, visual evidence, and channel-safe layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to prepare and run ad-image generation workflows for product landing pages, ecommerce ads, content-download ads, retargeting, and single-variable A/B image variants. The skill emphasizes matching generated visuals to approved landing-page claims and reviewable advertising evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive and its upload storage flow.

Mitigation: Use only prompts and assets that are approved for upload, and avoid sending sensitive, private, or unlicensed material.

Risk: The skill relies on an AI_HIVE_API_KEY or ~/.ai-hive/config.json credential.

Mitigation: Protect the API key, avoid committing local configuration, and keep the credential file restricted to the current user.

Risk: Generated images are saved locally, with a default output location under Downloads/AiHive.

Mitigation: Set --output-dir to an appropriate project or controlled storage location when the default path is not suitable.

Risk: Generated ad visuals could imply claims, prices, certifications, or platform suitability that the landing page does not support.

Mitigation: Review each generated image against the landing page, approved copy, product evidence, and current ad-platform policies before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-ad-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; CLI output can include JSON task data and downloaded PNG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_seedream_5_0_lite image model, supports optional reference images, and saves generated images locally unless download is disabled.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
