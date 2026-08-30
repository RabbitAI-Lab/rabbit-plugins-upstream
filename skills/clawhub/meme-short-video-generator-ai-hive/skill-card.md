## Description:

Helps social media, ecommerce, advertising, marketing, short-drama, manhua, and brand teams turn meme or reference ideas into Chinese production workflows, rewritten original concepts, prompts, scripts, AI-HIVE generation commands, task records, and delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social media operators, brand marketers, ecommerce teams, game teams, and internet product teams use this skill to convert meme or trend references into original short-video concepts, storyboards, prompts, runnable AI-HIVE commands, and reviewable delivery records. It is intended for authorized media and truthful brand/product claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can store or pass an AI_HIVE_API_KEY.

Mitigation: Use environment variables or the local config path intentionally, do not paste real keys into chat logs or repositories, and rotate any key that may have been exposed.

Risk: The workflow can upload user-provided media to AI-HIVE for generation.

Mitigation: Upload only media the user has rights to use, and require authorization review before using reference images, videos, logos, likenesses, or third-party creative work.

Risk: Generation commands may create billable AI-HIVE tasks.

Mitigation: Review prompts, model, routing mode, pricing snapshot, and task parameters before submission; use small test runs before batch generation.

Risk: Meme adaptation can produce misleading claims or content that copies protected expression too closely.

Mitigation: Keep only abstract meme mechanics, rewrite scenes and wording into original brand-safe content, and verify product, pricing, performance, and endorsement claims before publishing.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/meme-short-video-generator-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with runnable command examples, JSON task records, and generated media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use an AI-HIVE API key, upload authorized reference media, poll asynchronous generation tasks, and download generated image or video assets.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
