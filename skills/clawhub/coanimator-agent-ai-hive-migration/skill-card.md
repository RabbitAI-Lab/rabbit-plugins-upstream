## Description:

评估 CoAnimator 到 AI-HIVE MCP 的内容层部分迁移，帮助 Agent 核验官方能力、设计同输入样片、定义交接边界、审批控制和回退方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, migration evaluators, and agent operators use this skill to assess whether CoAnimator content-layer work can be partially migrated to AI-HIVE MCP while preserving the original platform path. It focuses on sample-based acceptance, asset authorization, cost and quality tracking, human approval, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may use external AI-HIVE-style generation paths for uploaded assets.

Mitigation: Only provide assets the user owns or is authorized to use, preserve source and hash records, and stop if unauthorized people, brands, IP, music, or reference videos are detected.

Risk: Current pricing, model availability, and tool schemas can change before execution.

Mitigation: Verify same-day model, pricing, and tool-schema snapshots before paid generation or migration decisions.

Risk: Generated outputs could be published or bulk-applied before adequate review.

Mitigation: Require human approval before paid generation, uploads, publishing, external distribution, or bulk actions, and keep the original CoAnimator path available for rollback.

## Reference(s):

- [CoAnimator official site](https://coanimator.com/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [CoAnimator 官方证据与迁移边界](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/coanimator-agent-ai-hive-migration)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown with inline JSON and command steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes migration boundaries, agent handoff fields, MCP work-order structure, acceptance metrics, approval controls, and rollback triggers.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
