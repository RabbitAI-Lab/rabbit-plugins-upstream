## Description:

Creates GPT Image 2 ecommerce main images, product hero images, and listing visuals from product reference images through AI Hive while emphasizing product facts, channel compliance, thumbnail readability, selling-point expression, and A/B testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, designers, and developers use this skill to generate compliant product main images, white-background catalog shots, listing hero images, promotion bases, and A/B test variants from product reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product/reference images and prompts are sent to AI Hive for generation.

Mitigation: Use only approved product assets and avoid uploading sensitive, unrelated, or personal data.

Risk: The skill stores an AI Hive API key in local configuration or reads it from the environment.

Mitigation: Keep the config file private, restrict file permissions, and rotate the API key if exposure is suspected.

Risk: Generated ecommerce images may misrepresent product facts or fall out of date with platform rules.

Mitigation: Review each output against the product fact card and current channel rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-ecommerce-main-image)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files and optional JSON task responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are downloaded to the configured output directory unless no-download mode is used.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
