## Description:

AI Observability is a hands-on playbook and local checklist toolkit for designing runtime monitoring, tracing, quality metrics, cost tracking, guardrail monitoring, alerting, and rollout practices for production AI applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI platform teams, SREs, operations teams, and quality owners use this skill to plan production observability for AI applications, including logs, metrics, traces, quality dashboards, cost monitoring, guardrail monitoring, and alerting. It helps agents produce structured monitoring guidance and local command outputs rather than operating a live monitoring platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the playbook and helper scripts for a deployed monitoring product.

Mitigation: Use the outputs as design guidance, then implement and test instrumentation, dashboards, and alerts in the organization's chosen observability platform.

Risk: Redistribution or commercial reuse may be affected by additional knowledge-copyright language alongside the MIT license.

Mitigation: Review the license and attestation text before redistribution, resale, model-training use, or broad commercial reuse.

Risk: Suggested metrics and thresholds may not fit every business risk level or production workload.

Mitigation: Calibrate thresholds against live traffic, incident history, cost targets, and domain-specific safety requirements before relying on alerts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-observability)
- [01 可观测性全景](references/01-可观测性全景.md)
- [02 调用追踪与日志](references/02-调用追踪与日志.md)
- [03 质量监控指标](references/03-质量监控指标.md)
- [04 性能与成本监控](references/04-性能与成本监控.md)
- [05 护栏与安全监控](references/05-护栏与安全监控.md)
- [06 告警体系](references/06-告警体系.md)
- [07 平台与落地](references/07-平台与落地.md)
- [08 常见问题 FAQ](references/08-FAQ.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional local shell command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zero-dependency local helper commands print observability checklists, metric tables, alert design, tracing standards, and rollout plans.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
