## Description:

Helps short-drama teams, comic-drama studios, brand content teams, and independent creators turn Seedance short-drama requests into production plans, character and scene boards, shot prompts, generation tasks, and continuity checks using AI-HIVE workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, and developers use this skill to plan and execute AI-HIVE short-drama content workflows, including scripts, prompts, runnable commands, media generation tasks, and acceptance checks. It is intended for authorized commercial content production where human review confirms facts, rights, cost, and platform constraints before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, video, or audio selected by the user may be uploaded to AI-HIVE for generation.

Mitigation: Use only authorized media, confirm rights and privacy constraints before upload, and avoid sending sensitive assets unless the user accepts AI-HIVE processing.

Risk: Image and video generation calls may incur costs through the AI-HIVE API.

Mitigation: Show final prompts, models, routing mode, and price snapshot before submitting generation tasks; start with a small sample for batch work.

Risk: API keys can be provided through environment variables or stored by the init command in a local config file.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable for temporary use, keep config files permission-restricted, and never include real keys in skill output, logs, screenshots, or commits.

Risk: Short-drama and marketing outputs can become misleading through unauthorized copying, unsupported product claims, fake testimonials, or implied brand endorsement.

Mitigation: Require human review of facts, rights, trademarks, testimonials, and platform rules; when source rights are unclear, use only abstract structure and create original scenes, dialogue, and visual style.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-short-drama-studio-ai-hive)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, JSON task records, and local media file outputs when generation or editing scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected media to AI-HIVE, create or read an AI-HIVE API key configuration, poll asynchronous generation tasks, and download generated image or video files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
