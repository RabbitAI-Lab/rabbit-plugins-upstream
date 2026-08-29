## Description:

AI大模型专家｜Claude API中转 helps AI platform teams, relay operators, enterprise developers, and content studios organize authorized model APIs through AI-HIVE for key isolation, routing, quotas, auditing, and asynchronous image/video task testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI gateway operators, and content production teams use this skill to plan and test authorized Claude/API relay workflows on AI-HIVE, including model catalogs, key isolation, routing, quotas, task tracking, and audit records. It can also produce local setup guidance and executable commands for image, video, upload, task polling, and blueprint workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores credentials locally and uses external AI-HIVE APIs, which can create exposure or misuse risk if users provide shared, unauthorized, or poorly protected API keys.

Mitigation: Install only for AI-HIVE workflows using an authorized key; keep credentials in local protected configuration or environment variables, avoid exposing keys in logs or screenshots, and rotate or revoke keys when needed.

Risk: Broad implicit invocation may cause the skill to appear for drama, editing, SEO, model-provider, or relay queries outside the user's intended Claude API relay workflow.

Mitigation: Review the skill invocation before execution and limit use to the intended AI-HIVE API relay, routing, audit, and task-testing workflows.

Risk: Image, video, upload, and async task commands may incur API costs, process user media, or download generated files.

Mitigation: Check model, routing, and pricing snapshots before submitting tasks; retain task IDs for status checks; use no-download modes when appropriate; and confirm rights to any submitted media.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-claude-api-relay)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs, store a local API key configuration, print task metadata, and optionally download generated image or video files.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
