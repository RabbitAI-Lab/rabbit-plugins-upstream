## Description:

评估 Niramana AI 到 AI-HIVE MCP 的工作流重建型迁移，并输出样片设计、职责边界、Agent 交接、成本质量指标、审批和回退方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and migration reviewers use this skill to evaluate a controlled Niramana AI to AI-HIVE MCP migration for agentic movie-production workflows. It guides same-input pilots, media-generation task handoffs, quality and cost measurement, human approval, and rollback decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on stale Niramana AI capabilities or AI-HIVE pricing when making migration claims or routing paid generation.

Mitigation: Recheck official Niramana availability and current AI-HIVE model and price snapshots before comparison claims, paid tasks, or publication.

Risk: Media generation may involve unauthorized reference images, video, people, products, brands, music, or other protected assets.

Mitigation: Use only owned or authorized assets, retain source IDs and file hashes, and stop review when asset rights cannot be confirmed.

Risk: Generated media could be uploaded, externally shared, published, or billed without appropriate human approval.

Mitigation: Require explicit budget and human approval before paid generation, uploads, external sharing, publishing, or bulk actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/niramana-movie-agent-ai-hive-migration)
- [Niramana AI official source](https://niramana.ai/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Niramana AI official evidence and migration boundaries](references/platform-evidence.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown guidance with JSON-style work order examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval gates, cost and quality metrics, asset-rights checks, and rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
