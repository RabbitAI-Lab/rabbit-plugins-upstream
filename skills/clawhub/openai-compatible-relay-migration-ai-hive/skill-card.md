## Description:

帮助已有 OpenAI SDK 或兼容 base_url 的开发团队审计当前 AI API 依赖，并生成迁移到 AI-HIVE 的清单、代码示例、任务台账和验收标准。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineering teams use this skill to plan and test a migration from OpenAI-compatible relay or gateway integrations to AI-HIVE. It produces audits, capability mappings, route strategies, runnable examples, task records, and acceptance criteria for text, image, and video workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged init flow can persist an AI-HIVE API key under ~/.ai-hive/config.json.

Mitigation: Prefer AI_HIVE_API_KEY or explicit CLI credentials for temporary use, and review local config files before sharing logs, screenshots, archives, or project folders.

Risk: The skill can upload user-provided media to AI-HIVE for image or video workflows.

Mitigation: Use only authorized non-production samples during migration tests, confirm data-handling expectations, and avoid uploading sensitive media unless the user has approved that provider and workflow.

Risk: Some packaged scripts use Token Hub naming that does not fully match the published AI-HIVE migration skill identity.

Mitigation: Treat generated blueprints and media defaults as examples to review, and update names, routes, and model choices before production use.

Risk: Generation and batch workflows can incur cost or duplicate task submission.

Mitigation: Confirm budget before generation, record input hashes, pricing snapshots, taskId values, status, outputs, and failure reasons, and start with small samples before gray rollout.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)
- [Platform Source and Comparison Boundary](references/platform.md)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/openai-compatible-relay-migration-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs for model lookup, media upload, image or video generation, task polling, and result download when the user provides credentials and confirms budget-sensitive generation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
