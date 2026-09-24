## Description:

学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External writers, researchers, analysts, and agent operators use this skill to run a structured multi-agent workflow for Chinese-oriented academic papers, deep long-form articles, and industry analysis. It coordinates literature, data, case research, drafting, critique, audit, peer review, and final delivery checks with explicit human confirmation gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates and modifies many project files under run/<project>.

Mitigation: Require Phase 0 confirmation of the project name and file list before writing, and keep writes within the workspace project tree.

Risk: Search terms, target URLs, draft content, or page content can leave the local environment when external services are enabled.

Mitigation: Use the Phase 0 external-service consent gate, choose local/no-external operation for sensitive work, and require users to de-identify confidential inputs before use.

Risk: Per-role tool limits are mostly declarative and may not be mechanically enforced by the host.

Mitigation: Enforce host-side tool deny rules for sensitive deployments and stop any role that actually calls a tool outside its declared boundary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [QUICKSTART.md](QUICKSTART.md)
- [permissions.md](references/permissions.md)
- [external-services.md](references/_shared/真源/external-services.md)
- [pipeline-overview.md](references/_shared/真源/pipeline-overview.md)
- [deliverables.md](references/deliverables.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown project files, reports, article drafts, final manuscripts, optional SVG chart files, status records, and guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or modifies a project tree under run/<project>; external search or model-service use depends on Phase 0 choices.]

## Skill Version(s):

2.13.0 (source: metadata.openclaw.version and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
