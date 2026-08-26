## Description:

AI大模型专家｜企业AI网关与成本路由 helps AI platforms, enterprise engineering teams, content studios, and ecommerce technical teams organize authorized model APIs into a unified AI-HIVE gateway for key management, routing, quotas, audit, asynchronous image and video tasks, cost snapshots, polling, and downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, platform operators, and enterprise teams use this skill to design and test an AI-HIVE model gateway workflow with authorized keys, routing policies, quotas, audit records, asynchronous task tracking, and cost snapshots. It also provides runnable command examples for blueprint generation, image/video task submission, task lookup, and local result handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI-HIVE API key and can store configuration locally.

Mitigation: Use only team-owned or explicitly authorized keys, keep keys out of public artifacts and logs, restrict local file permissions, and rotate or revoke credentials when access changes.

Risk: Generated commands may upload selected local media and submit billable model tasks.

Mitigation: Review prompts, file paths, routing settings, and download options before execution; confirm media rights and budget approval before submitting tasks.

Risk: Implicit invocation is enabled for the skill interface.

Mitigation: Review whether implicit invocation is acceptable for the workspace and require explicit confirmation in sensitive or cost-bearing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-enterprise-ai-gateway)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with inline shell commands, Python script invocations, and JSON configuration or output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save AI-HIVE API configuration locally, create gateway blueprint JSON, submit image or video tasks, poll task status, and optionally download generated media.]

## Skill Version(s):

1.0.0 (source: evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
