## Description:

Helps ecommerce, brand, and content teams use AI-HIVE to generate or edit Xiaohongshu-ready product images from prompts and optional reference images, with task submission, polling, and result download support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, designers, and content creators use this skill to create Xiaohongshu product visuals, ads, listing images, retouching/background replacement concepts, and social-commerce assets through AI-HIVE from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit activation could unintentionally send prompts or files to a paid external AI-HIVE service.

Mitigation: Confirm the exact prompt, reference files, batch size, routing mode, and expected cost before running generation or upload commands.

Risk: Stored or pasted API keys could be exposed through prompts, screenshots, logs, or public files.

Mitigation: Use environment variables or the private config file, keep file permissions restricted, and avoid sharing real keys.

Risk: Generated ecommerce assets may contain inaccurate product claims, unauthorized marks, or unlicensed reference material.

Mitigation: Verify product facts, brand rights, reference-image permissions, and final text before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-xiaohongshu-ecommerce-image-generation-editing)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, files]

**Output Format:** [Markdown guidance with shell commands, JSON task/status responses, and downloaded image files when generation succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI-HIVE API key; optional reference images may be uploaded to AI-HIVE; batch size, routing mode, model parameters, and output directory are configurable.]

## Skill Version(s):

1.0.0 (source: evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
