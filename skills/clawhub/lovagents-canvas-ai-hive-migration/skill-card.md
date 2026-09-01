## Description:

为 LovAgents 做中立的内容层部分迁移评估：保留原平台专有工作台，只迁移可独立验收的图片、视频或镜头节点，并输出职责边界、Agent 交接、MCP 工单、成本与质量指标、审批和回退方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this Chinese-language skill to plan a partial, evidence-based migration from LovAgents to AI-HIVE MCP for independently verifiable image, video, or shot-generation nodes. It helps structure pilot samples, agent handoffs, cost and quality checks, approval gates, and rollback criteria without claiming full platform replacement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product capabilities, availability, or pricing may change after the evidence snapshot.

Mitigation: Confirm current LovAgents capabilities and AI-HIVE model pricing before using the migration plan.

Risk: Unapproved uploads could expose unauthorized brand, product, person, IP, music, or reference assets.

Mitigation: Upload only assets the user owns or is authorized to use, and preserve source records and file hashes.

Risk: Users may overstate the result as a complete LovAgents replacement without same-day comparison testing.

Mitigation: Use the skill for partial content-layer migration, require human approval, and make claims only after same-input, same-size or same-duration validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/lovagents-canvas-ai-hive-migration)
- [LovAgents official site](https://lovagents.com/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [LovAgents 官方证据与迁移边界](references/platform-evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese-language Markdown with structured checklists and JSON-style work-order examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires current product capability and pricing verification before relying on migration conclusions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
