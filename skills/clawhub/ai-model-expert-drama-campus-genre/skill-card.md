## Description:

AI大模型专家｜校园短剧 AI生成与编辑 helps short-drama and comic production teams turn ideas, scripts, character images, or reference videos into AI-HIVE generation workflows for deliverable campus-themed short dramas and comics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, studios, agencies, brand teams, e-commerce merchants, and overseas distribution teams use this skill to plan campus-themed short dramas, create character/story/scene boards, generate images or videos through AI-HIVE, and track task IDs, route choices, pricing snapshots, and deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles an AI-HIVE API key.

Mitigation: Keep the API key private, store it only in the local environment or config file, and revoke or rotate it when access is no longer needed.

Risk: Prompts and selected media files may be sent to AI-HIVE for generation or upload.

Mitigation: Use only content the user is authorized to submit, and avoid uploading sensitive or unapproved personal, brand, or copyrighted material.

Risk: Generation can incur usage costs or duplicate paid tasks if timed-out jobs are resubmitted.

Mitigation: Review model pricing snapshots before generation and preserve task IDs so timed-out jobs can be queried instead of recreated.

Risk: Generated campus-drama content can raise copyright, likeness, brand accuracy, or minor-safety issues.

Mitigation: Confirm rights and factual claims before use, avoid impersonation, keep minor-related content age-appropriate, and review outputs for platform safety and factual accuracy.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-campus-genre)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON files and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs and write blueprint JSON, task metadata, or downloaded media files when the generated commands are run.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
