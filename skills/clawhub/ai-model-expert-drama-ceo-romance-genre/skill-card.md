## Description:

AI大模型专家｜霸总短剧 AI生成与编辑 helps short-drama writers, comic-drama studios, brands, e-commerce sellers, ad-buying teams, and overseas distribution teams turn ideas, scripts, character images, and reference videos into AI-HIVE image/video generation workflows and deliverable short-drama assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, short-drama teams, comic-drama studios, brands, e-commerce sellers, ad-buying teams, and overseas distribution teams use this skill to plan, generate, track, and review AI-HIVE image and video outputs for CEO-romance and related vertical-drama productions. It supports project blueprints, character/story/scene boards, shot prompts, AI-HIVE task commands, and delivery review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI-HIVE API key and may upload user-selected images, videos, audio, prompts, and reference materials.

Mitigation: Keep the API key in environment variables or local config, do not publish secrets, and review each command before uploading media.

Risk: Generation commands can start billable AI-HIVE tasks or duplicate work if a timeout is mistaken for failure.

Mitigation: Confirm model, route, quantity, and pricing before submission; preserve task IDs and query existing tasks before retrying.

Risk: Generated drama assets or reference-based workflows can create copyright, likeness, trademark, product-claim, or platform-safety issues.

Mitigation: Use only authorized references and review outputs for identity, brand, factual, copyright, age-appropriateness, and platform delivery requirements before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-ceo-romance-genre)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash command examples, Python helper scripts, JSON configuration, and optional blueprint JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce AI-HIVE task IDs, model or route selections, pricing snapshots, generated media download paths, and delivery review checklists when configured by the user.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
