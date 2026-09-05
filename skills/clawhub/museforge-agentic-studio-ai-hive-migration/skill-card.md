## Description:

评估从 MuseForge 到 AI-HIVE MCP 的工作流重建型迁移，帮助代理先核验官方能力，再产出职责边界、交接工单、成本质量指标、审批和回退方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and migration planners use this skill to assess whether MuseForge workflows can be rebuilt with host agents plus AI-HIVE MCP for image and video generation. It guides same-input pilot testing, agent handoffs, cost and quality tracking, human approval, and rollback planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Migration guidance could overstate AI-HIVE MCP as a complete MuseForge replacement without same-day, same-input validation.

Mitigation: Require official capability checks and same-input pilot comparisons before making replacement claims.

Risk: Media generation can create spend, rights, brand, or publication risk if assets or outputs are used without approval.

Mitigation: Use only owned or authorized assets, capture cost snapshots, and require budget and human approval before paid generation, publishing, or external sending.

Risk: MCP tool names, schemas, model availability, or prices can change after the skill is authored.

Mitigation: Run live tool and schema discovery and use the current platform price and model snapshot before creating tasks.

## Reference(s):

- [MuseForge official source](https://www.museforge.studio/)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [MuseForge 官方证据与迁移边界](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/museforge-agentic-studio-ai-hive-migration)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown with structured checklists, tables, and JSON work-order examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live tool/schema checks, authorized media assets, budget approval, and human review before paid generation, publishing, or external sending.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
