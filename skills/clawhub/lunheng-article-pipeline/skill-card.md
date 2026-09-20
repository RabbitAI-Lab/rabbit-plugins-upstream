## Description:

学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, analysts, and teams use this skill to coordinate evidence-backed long-form articles, academic papers, and industry analysis through a multi-agent workflow for research, outlining, drafting, critique, audit, peer review, and final inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes many local project files, status records, audit reports, drafts, and heartbeat artifacts.

Mitigation: Review the Phase 0 file plan before starting and keep execution scoped to the intended workspace run/<project>/ directory.

Risk: Search terms, URLs, or draft content may be sent to external services depending on Phase 0 choices.

Mitigation: For sensitive or unpublished work, choose no-external or local-only options and avoid optional metadata or scraping integrations.

Risk: A multi-agent workflow can produce degraded independence if worker agents are unavailable or taken over by the coordinator.

Mitigation: Review status, audit, and final disclosure artifacts for worker failures, coordinator fallback, and residual limitations before relying on the final article.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [SKILL.md](SKILL.md)
- [QUICKSTART.md](QUICKSTART.md)
- [permissions.md](references/permissions.md)
- [external-services.md](references/_shared/external-services.md)
- [pipeline-overview.md](references/_shared/pipeline-overview.md)
- [phase-order.yaml](references/_shared/phase-order.yaml)
- [M-Gate-Algorithm.md](references/_shared/M-Gate-Algorithm.md)
- [G14 Chinese AI trace gate](references/gates/14-中文AI痕迹-gate.md)
- [Chinese AI trace checker](references/checkers/中文AI痕迹-checker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Code, Guidance]

**Output Format:** [Markdown files and structured project artifacts, with optional SVG code and checklist-style review reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates scoped files under run/<project>/ after Phase 0 consent; the skill declares no shell execution.]

## Skill Version(s):

2.12.66 (source: SKILL.md metadata.openclaw.version and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
