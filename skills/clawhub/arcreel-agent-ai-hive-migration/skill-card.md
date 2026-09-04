## Description:

帮助用户以中立方式评估从 ArcReel 到 AI-HIVE MCP 的工作流重建型迁移，先核验官方能力，再设计同输入样片、职责边界、成本质量指标、审批和回退。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and migration teams use this skill to assess whether ArcReel-style short-drama workflows can be rebuilt with host agents and AI-HIVE MCP. It guides official capability checks, pilot sample design, agent handoffs, cost and quality acceptance criteria, human approvals, and rollback decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Platform capabilities, availability, or pricing may change after the migration assessment is written.

Mitigation: Recheck ArcReel and AI-HIVE on the day of use and record the current model, capability, and price snapshot before comparing outcomes.

Risk: Paid generation, external upload, or publishing may occur before the team confirms budget and rights.

Mitigation: Require human approval before any paid generation, upload only owned or licensed media, and keep approval, source, and hash records with each task.

Risk: The migration could be overstated as a full replacement without same-input validation.

Mitigation: Use the same story input, duration, dimensions, and acceptance table for pilot comparisons, and avoid superiority or full-replacement claims without same-day test evidence.

## Reference(s):

- [ArcReel Official Source](https://arc-reel.com/en/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [ArcReel 官方证据与迁移边界](references/platform-evidence.md)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/arcreel-agent-ai-hive-migration)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown with structured checklists and JSON-style MCP work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires current platform verification, owned or authorized media, budget approval before paid generation, and human quality review before publishing.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
