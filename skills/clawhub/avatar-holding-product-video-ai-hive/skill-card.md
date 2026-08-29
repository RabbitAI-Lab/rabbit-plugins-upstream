## Description:

This skill turns authorized avatar and product references into a Chinese AI-HIVE workflow for product-holding avatar videos, including production briefs, prompts, runnable commands, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, brands, and advertising teams use this skill to convert product-holding avatar video requests into reviewable briefs, shot plans, prompts, AI-HIVE generation commands, and delivery checks. It is aimed at teams that have rights to the source media and need a repeatable Chinese workflow for product videos without live filming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media files can be uploaded to AI-HIVE during upload or generation commands.

Mitigation: Use only media the operator is authorized to process, and confirm asset rights before running commands that upload images, videos, or audio.

Risk: Generation commands may create billable AI-HIVE tasks.

Mitigation: Review the final prompt, model mode, routing preference, price snapshot, and budget before submitting generation work; use small samples before batch jobs.

Risk: AI-HIVE credentials can be exposed through environment variables, configuration files, logs, or screenshots.

Mitigation: Store the API key only in AI_HIVE_API_KEY or ~/.ai-hive/config.json with restricted permissions, and avoid pasting real keys into prompts, logs, or version control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/avatar-holding-product-video-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON records, Python command examples, shell commands, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit asynchronous AI-HIVE image or video generation tasks, upload user-selected media, poll task status, and download generated files when the user runs the provided commands.]

## Skill Version(s):

1.0.0 (source: release.version in evidence.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
