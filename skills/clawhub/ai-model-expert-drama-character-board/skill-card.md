## Description:

AI大模型专家｜短剧人物版人物板 helps short-drama, comic-drama, brand, ecommerce, advertising, and internationalization teams turn character, scene, plot, and brand requirements into reusable visual planning assets and optional AI-HIVE image or video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, brand operators, ecommerce merchants, advertising teams, and developers use this skill to plan short-drama character boards, storyboards, scene boards, prompts, acceptance checks, and AI-HIVE generation commands. It supports character consistency, reference-material handling, task polling, cost-aware model routing, and downloadable image or video outputs when configured with an AI-HIVE API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload selected reference images, video, or audio to AI-HIVE for remote generation.

Mitigation: Use only files the user is comfortable sending to AI-HIVE, remove unnecessary sensitive content before upload, and confirm rights for portraits, brands, products, and source media.

Risk: The helper scripts require a local AI-HIVE API key and may store it in a local configuration file.

Mitigation: Store credentials outside public skill files, keep local config permissions restricted, rotate or revoke keys when access changes, and avoid sharing screenshots or logs that include secrets.

Risk: The image helper is inconsistently branded as a generic GPT Image 2 workflow rather than a strictly character-board-only wrapper.

Mitigation: Review the selected model and generated prompt path before relying on the image helper for a narrow character-board production workflow.

Risk: Generated short-drama assets may contain inaccurate facts, inconsistent characters, or unauthorized likeness, trademark, music, image, video, or brand use.

Mitigation: Verify factual claims, character consistency, platform safety zones, and rights clearances before publication or commercial delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-character-board)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline bash commands plus JSON, image, or video file outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create a local production blueprint JSON, initialize local AI-HIVE configuration, submit remote image/video generation jobs, poll task status, and download generated media when credentials are configured.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
