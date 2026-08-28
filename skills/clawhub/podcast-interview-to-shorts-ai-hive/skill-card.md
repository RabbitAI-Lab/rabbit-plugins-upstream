## Description:

This Chinese-language skill helps podcast hosts, interview shows, knowledge creators, and content teams turn authorized podcast or interview material into reviewable short-video plans, titles, timestamps, supplemental-shot prompts, runnable AI-HIVE commands, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content teams, and developers use this skill to convert authorized podcast or interview assets into short-form video production briefs, editing decisions, AI-HIVE generation tasks, local ffmpeg processing commands, and acceptance checklists. It is intended for commercial content workflows where facts, platform constraints, budget, and media rights must be reviewed before generation or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized media and API credentials may be uploaded to AI-HIVE for potentially billable generation.

Mitigation: Use only media the user has rights to process, confirm final prompts, routing, and cost-sensitive parameters before submitting generation tasks, and keep API keys out of chats, logs, screenshots, and repositories.

Risk: Generated clips can misrepresent interview context, product claims, or endorsements if facts and permissions are not reviewed.

Mitigation: Preserve the complete argument and necessary context for each clip, mark uncertain facts for verification, and require human review for likeness, voice, trademark, copyright, platform, medical, financial, or child-related content.

Risk: Local ffmpeg edits and downloads can overwrite or misplace media files if paths are chosen carelessly.

Mitigation: Back up originals, inspect commands before execution, use explicit output paths, and keep task records that include inputs, hashes, model settings, task IDs, status, and download locations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/podcast-interview-to-shorts-ai-hive)
- [AI-HIVE Chat and API Access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline bash commands and optional JSON or media files produced by helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize reviewable plans before billable generation, task records with route/model/pricing/task IDs, and acceptance checks for rights, facts, encoding, and API-key handling.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
