## Description:

Helps Chinese LLM users, developers, and enterprise evaluators verify Niulai/GLM model identity, compare AI-HIVE runtime model availability and pricing, and produce reusable task templates, routing plans, and result comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and enterprise evaluators use this skill to turn Niulai, GLM-5.3, AI-HIVE, and related model-selection searches into verifiable workflows. It guides identity checks, capability tests, current model and pricing review, task planning, route selection, and result comparison before paid or externally visible actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may contact AI-HIVE using a user API key and may write local plan or task-record JSON files.

Mitigation: Keep the API key only in environment variables or credential storage, review local JSON outputs before sharing, and avoid committing secrets or task records.

Risk: Broad implicit invocation could run workflow planning or model queries when the user did not intend to use AI-HIVE.

Mitigation: Review the agent activation settings and require explicit confirmation before paid, batch, publishing, deletion, or permission-changing actions.

Risk: Model names, hotspot nicknames, availability, prices, and platform capabilities can change after the skill release.

Mitigation: Verify current official or runtime information before execution, preserve the pricing snapshot and task ID, show fallback model differences, and do not silently substitute unavailable target models.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Zhipu GLM-5.3-Flash](https://www.zhipuai.cn/zh/research/163)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-hot-niulai-workbench)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash examples and JSON execution-plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plan-only mode is available before paid AI-HIVE work; generated task records may include model, routing, pricing snapshot, input hash, task ID, status, and output paths.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
