## Description:

Nano Banana 2 广告图片 helps agents turn audience, product evidence, approved claims, and one test variable into ad-image candidates for pre-launch review and A/B testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creative operators, and developers use this skill to generate ad-image candidates from approved product facts, claim boundaries, channel layout needs, and single-variable A/B test hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected reference images are sent to AI Hive for image generation.

Mitigation: Use the skill only when that transfer fits the applicable data policy, and avoid uploading confidential product images unless approved.

Risk: The AI Hive API key may be stored locally for repeated use.

Mitigation: Use a limited API key when available and protect or rotate the key according to local credential-handling practices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-ad-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_nano_banana_2 route, accepts optional user-selected reference images, and saves completed results locally.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
