## Description:

为 VO3 / Vovoo AI Video Agent 做中立的工作流重建型迁移评估：用宿主 Agent + Skill 重建制片角色，AI-HIVE MCP 负责图片与视频生成，并输出职责边界、Agent 交接、MCP 工单、成本与质量指标、审批和回退要求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operations teams use this skill to evaluate a workflow-rebuild migration from VO3 / Vovoo AI Video Agent to an agent-led process that uses AI-HIVE MCP for image and video generation. It helps structure official-capability checks, sample-video validation, handoffs, cost and quality metrics, approvals, and rollback decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may guide an agent toward paid external AI-HIVE image or video generation.

Mitigation: Confirm model availability, pricing, budget limits, and human approval before creating generation tasks.

Risk: Reference images, videos, people, products, brands, or music may be uploaded without adequate rights.

Mitigation: Use only owned or authorized assets, record source and file hashes, and stop the migration review when rights are unclear.

Risk: Migration claims may overstate equivalence to VO3 / Vovoo AI Video Agent without same-day, same-input validation.

Mitigation: Require a controlled sample with identical input, duration, dimensions, quality metrics, and rollback checks before making comparative conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/vo3-vovoo-video-agent-ai-hive-migration)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [VO3 / Vovoo AI Video Agent official source](https://www.vo3ai.com/ai-video-agent)
- [Platform evidence and migration boundaries](references/platform-evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured JSON work-order examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes migration boundaries, agent handoff fields, approval gates, quality metrics, and rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
