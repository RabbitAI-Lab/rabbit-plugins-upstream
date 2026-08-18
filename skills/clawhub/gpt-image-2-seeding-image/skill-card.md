## Description:

使用 GPT Image 2 制作基于真实商品事实和使用过程的种草图片，包括开箱、使用步骤、细节证据、生活场景、图文卡片和社媒封面。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, merchants, and content teams use this skill to generate product seeding visuals, unboxing sets, usage-step images, detail evidence cards, lifestyle scenes, and social cover/carousel assets from verifiable product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are uploaded to AI Hive for generation.

Mitigation: Do not provide private, sensitive, confidential, or rights-uncleared reference files, and review prompts for sensitive content before execution.

Risk: The helper can store an AI Hive API key in ~/.ai-hive/config.json.

Mitigation: Use environment variables or CLI keys when possible, keep the config file permissions restricted, and remove ~/.ai-hive/config.json when the key should no longer remain on the machine.

Risk: Generated seeding images may imply unverified product claims if prompts include unsupported performance, review, or test language.

Mitigation: Limit prompts and captions to documented product facts, disclose AI generation and commercial relationships under platform rules, and require qualified review for medical, beauty efficacy, food nutrition, child-focused, or financial products.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-seeding-image)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with runnable shell commands and generated image files saved locally by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper sends prompts and optional reference images to AI Hive, polls generation tasks, and downloads generated images to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
