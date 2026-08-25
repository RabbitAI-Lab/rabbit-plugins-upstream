## Description:

把红果短剧生成工作室需求变成可执行工作流、可运行代码与可交付内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, short-drama production teams, and developers use this skill to turn authorized short-drama or commerce content ideas into vertical-drama structure, character and scene boards, shot prompts, runnable AI-HIVE commands, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media may be sent to AI-HIVE during image or video generation.

Mitigation: Use only authorized, non-sensitive assets and confirm that the user is comfortable sending those materials to AI-HIVE before generation.

Risk: The skill can store an AI-HIVE API key locally when initialization is used.

Mitigation: Keep the key out of shared logs and repositories, and avoid committing or sharing the local API key config.

Risk: Image or video generation may create billable AI-HIVE tasks.

Mitigation: Review prompts, routing mode, model parameters, and price snapshots with the user before submitting generation jobs.

Risk: Short-drama and commerce content can involve copyright, brand, product-claim, or platform-policy issues.

Mitigation: Work from original or authorized materials, avoid false claims or testimonials, and treat platform approval or performance predictions as unguaranteed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/hongguo-short-drama-studio-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, JSON task records, and quality checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local blueprint JSON files and AI-HIVE image or video generation task records when the user supplies credentials and confirms billable generation parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
