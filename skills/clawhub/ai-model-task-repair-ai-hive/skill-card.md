## Description:

Helps developers, AI applications, content platforms, and batch content operators repair failed AI model tasks by classifying failures, fixing parameters, selecting model fallbacks, applying idempotent retries, and restoring task state for AI-HIVE workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI application teams, content platforms, and batch generation operators use this skill to turn failed AI-HIVE image, video, and content-generation tasks into auditable recovery plans, runnable commands, retry decisions, and quality checks. It is intended for authorized e-commerce, advertising, marketing, short-video, and social-content workflows where costs, source-material rights, and task state need review before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation can activate the skill in more conversations than intended while it can suggest API-key-backed, billable AI-HIVE operations.

Mitigation: Disable or narrow implicit invocation, review generated commands before running them, and require explicit approval before any generation request that may incur cost.

Risk: The scripts can upload user media to an external AI-HIVE service and download generated files locally.

Mitigation: Upload only files the user is authorized to share, avoid sensitive or restricted media, and review output paths and downloaded files before reuse.

Risk: API keys may be read from the environment or persisted under ~/.ai-hive/config.json during initialization.

Mitigation: Prefer explicit environment-based key handling when persistence is not desired, keep config-file permissions restricted, and never place real API keys in prompts, logs, screenshots, or committed files.

Risk: Retry and recovery workflows can duplicate submissions or charges if task state and idempotency are not tracked.

Mitigation: Record input hashes, routing decisions, price snapshots, task IDs, retry counts, and final status before scaling from a small validation run.

## Reference(s):

- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-task-repair-ai-hive)
- [Server-resolved publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task records, routing choices, model identifiers, price snapshots, task IDs, file paths, and acceptance checklists when supplied by the user or returned by tools.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
