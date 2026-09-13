## Description:

All-Industry Officers helps an agent route and execute organization operations work across HR, finance, administration, IT, compliance, customer operations, analytics, knowledge management, and related business functions using a 125-unit capability framework with reference templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams use this skill to plan, draft, and coordinate business operations deliverables such as policies, reports, checklists, routing plans, and domain-specific templates. It is intended for broad organizational support workflows and should be calibrated with the user's industry, organization, and approved source materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review classifies the release as suspicious because it requests powerful tools and can affect broad business-operations workflows.

Mitigation: Review the skill before installing, run it in a sandboxed workspace, and avoid granting Bash unless the host can require per-command approval.

Risk: The skill may be used with HR, finance, customer, meeting, or audit-log data.

Mitigation: Use it with real organizational data only after confirming privacy, authorization, retention, and internal policy requirements.

Risk: The skill presents multi-agent labels that may not correspond to independently launched agents in the host environment.

Mitigation: Treat role labels as presentation unless the host actually launches separate agents and exposes auditable agent delegation.

Risk: Business, legal, tax, finance, labor, and compliance outputs can become inaccurate if generated from stale or unsupported assumptions.

Mitigation: Require user-provided authoritative materials or current verified sources for regulated workflows, and route sensitive decisions through qualified human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/all-industry-officers)
- [AIO catalog](references/AIO-catalog.md)
- [AIO requirements](references/AIO-requirements.md)
- [AIO exemplars](references/AIO-exemplars.md)
- [AIO-X0 routing and orchestration templates](references/AIO-X0-路由编排域范本.md)
- [AIO-N1 human resources templates](references/AIO-N1-人力资源域范本.md)
- [AIO-N2 finance and accounting templates](references/AIO-N2-财务会计域范本.md)
- [AIO-N3 administration templates](references/AIO-N3-行政办公域范本.md)
- [AIO-N4 information technology templates](references/AIO-N4-信息技术域范本.md)
- [AIO-B1 intelligence collection and monitoring templates](references/AIO-B1-情报采集与监测域范本.md)
- [AIO-B2 certification and regulatory templates](references/AIO-B2-资质认证与监管域范本.md)
- [AIO-B3 content production and distribution templates](references/AIO-B3-内容生产与传播域范本.md)
- [AIO-B4 event operations templates](references/AIO-B4-活动运营与执行域范本.md)
- [AIO-B5 customer and partner operations templates](references/AIO-B5-客户与伙伴运营域范本.md)
- [AIO-B6 supply chain and operations assurance templates](references/AIO-B6-供应链与运营保障域范本.md)
- [AIO-B7 data analysis and decision templates](references/AIO-B7-数据分析与决策域范本.md)
- [AIO-B8 process collaboration and project management templates](references/AIO-B8-流程协同与项目管理域范本.md)
- [AIO-B9 compliance review and risk control templates](references/AIO-B9-合规审核与风控域范本.md)
- [AIO-B10 knowledge management and training templates](references/AIO-B10-知识管理与培训域范本.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text, with optional generated files or inline shell commands when the host permits them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be calibrated to user-provided organization context and checked against authoritative source materials for HR, finance, legal, compliance, customer, and audit-sensitive workflows.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
