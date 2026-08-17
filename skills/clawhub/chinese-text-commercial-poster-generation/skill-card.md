## Description:

This skill helps brand marketing, advertising, design, and social media teams generate or edit commercial images with precise Chinese text using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, designers, and ecommerce operators use this skill to create Chinese-text commercial posters, product images, detail-page visuals, social media creatives, and reference-guided image edits through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key for API calls.

Mitigation: Use a dedicated key, store it only through the documented environment variable or 0600 config file path, and rotate it if it is exposed.

Risk: Reference images explicitly passed to the skill are uploaded to AI Hive for generation or editing.

Mitigation: Pass only files intended for upload and avoid private, unrelated, or sensitive local files.

Risk: Batch generation and repeated task submission can create avoidable cost.

Mitigation: Review the runtime pricing snapshot and batch size before submission, then reuse the returned task ID for status checks instead of resubmitting the same job.

Risk: Generated Chinese text or commercial claims may be inaccurate or unsuitable for publication.

Mitigation: Review generated images before use, including exact Chinese characters, product facts, brand claims, platform fit, and visual consistency.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/chinese-text-commercial-poster-generation)
- [AI Hive chat and API key portal](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompt text, optional reference images, batch size, model parameters, routing mode, and output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
