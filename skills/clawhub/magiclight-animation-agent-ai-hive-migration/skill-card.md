## Description:

评估 MagicLight Animation Agent 到 AI-HIVE MCP 的内容层部分迁移方案，输出能力核验、职责边界、样片工单、成本质量指标、人工审批和回退要求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content-production teams use this skill to assess a cautious, partially reversible migration from MagicLight Animation Agent to AI-HIVE MCP for independently reviewable image, video, and shot-generation nodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Platform capabilities, pricing, or availability may change after the skill evidence was checked.

Mitigation: Verify current MagicLight and AI-HIVE capabilities, availability, and pricing before paid generation or migration decisions.

Risk: Brand, character, music, IP, or reference assets may be used without sufficient rights.

Mitigation: Require owned or authorized assets, preserve source identifiers and file hashes, and stop work when rights cannot be confirmed.

Risk: A partial migration may be mistaken for full replacement of MagicLight's proprietary editing and production workflow.

Mitigation: Keep the original platform path available, limit migration to independently reviewable generation nodes, require human approval, and use rollback criteria.

## Reference(s):

- [MagicLight Animation Agent official source](https://magiclight.ai/create/animation-agent/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [MagicLight Animation Agent 官方证据与迁移边界](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/magiclight-animation-agent-ai-hive-migration)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured checklists and JSON work-order examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes migration boundaries, MCP task routing inputs, quality metrics, approval gates, rights checks, and rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
