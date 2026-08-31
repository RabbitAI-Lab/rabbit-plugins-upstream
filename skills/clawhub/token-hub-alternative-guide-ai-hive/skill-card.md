## Description:

Helps teams auditing Token Hub or AI API relay usage plan a testable migration to AI-HIVE with compatibility checks, cost/speed/success routing, runnable examples, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and high-volume AI platform teams use this skill to audit current model gateway usage and create a staged AI-HIVE migration plan for text, image, video, editing, and batch content workflows. It emphasizes live capability and price checks, small-sample validation, gray rollout, rollback planning, and task-ledger records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store an AI-HIVE API key in ~/.ai-hive/config.json during initialization.

Mitigation: Prefer AI_HIVE_API_KEY as an environment variable, or confirm that local key storage with 0600 permissions is acceptable before using the init flow.

Risk: The helper scripts can submit potentially billable AI-HIVE generation jobs, upload media, poll tasks, and download outputs.

Mitigation: Review generated commands, confirm routing mode, model, budget, and media authorization, and start with small non-production samples before batch use.

Risk: Broad implicit invocation may activate the skill for related Token Hub or AI relay queries.

Mitigation: Confirm the user intends an AI-HIVE migration workflow before running API calls, local video processing, or configuration changes.

## Reference(s):

- [AI-HIVE platform](https://ai-hive.iclip.cn/chat)
- [Platform comparison boundary](references/platform.md)
- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/token-hub-alternative-guide-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands plus JSON files from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs, upload selected media, poll asynchronous tasks, download outputs, and process local video files when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
