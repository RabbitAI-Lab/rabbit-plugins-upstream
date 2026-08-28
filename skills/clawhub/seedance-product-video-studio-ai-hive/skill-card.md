## Description:

This skill helps e-commerce and marketing teams turn Seedance product-video requests into production briefs, storyboard scripts, video-generation prompts, AI-HIVE task commands, and platform-ready review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce merchants, marketers, and content operators use this skill to plan product-focused short videos for platforms such as Taobao, JD, Douyin, Xiaohongshu, and cross-border commerce. The skill emphasizes factual product claims, authorized media, budget-aware AI-HIVE routing, and reviewable deliverables before any paid generation task is submitted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation commands may consume paid AI-HIVE credits.

Mitigation: Review prompts, routing choice, model configuration, and price snapshot before submitting any task, especially for batch work.

Risk: Uploading unauthorized media or unsupported product claims can create rights, privacy, or misleading-advertising issues.

Mitigation: Use only media the user is authorized to upload and verify product facts, prices, claims, and platform constraints before generation.

Risk: The init workflow stores an AI-HIVE API key locally.

Mitigation: Use placeholders in examples, keep the local config private, and avoid committing keys, logs, screenshots, or generated records that expose credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-product-video-studio-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce reviewable production briefs, storyboard prompts, local configuration guidance, API task records, and ffmpeg command workflows.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
