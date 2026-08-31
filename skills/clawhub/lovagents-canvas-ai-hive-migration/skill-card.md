## Description:

Provides a Chinese-language workflow for evaluating a partial content-layer migration from LovAgents to AI-HIVE MCP, including official capability checks, sample deliverables, agent handoffs, cost and quality metrics, approval, and rollback boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operations teams use this skill to plan and review a controlled LovAgents-to-AI-HIVE MCP partial migration for e-commerce images, ad videos, social covers, and related media-production handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may upload media, brand assets, people, music, or product references without sufficient rights.

Mitigation: Use only owned or authorized assets, preserve source IDs and file hashes, and stop review when rights are missing.

Risk: Paid media generation may exceed budget or proceed without approval.

Mitigation: Capture same-day model and price snapshots, require budget approval before paid generation, and stop migration when budget limits are exceeded.

Risk: The skill could overstate platform replacement quality, price, or completeness without current testing.

Mitigation: Re-check official LovAgents and AI-HIVE capabilities before publication and make comparison claims only after same-day, same-input tests.

Risk: A partial content workflow may be mistaken for a full replacement of LovAgents workspaces or governance features.

Mitigation: Keep LovAgents responsible for proprietary canvas, node editing, collaboration, asset library, and brand workspace functions unless separately validated.

## Reference(s):

- [LovAgents official site](https://lovagents.com/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [LovAgents official evidence and migration boundaries](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/lovagents-canvas-ai-hive-migration)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with checklists, tables, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language migration guidance with human approval, cost tracking, quality checks, and rollback checkpoints.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
