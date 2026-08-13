## Description:

Generates Chinese-language, evidence-driven competitive landscape analysis for a technology domain, covering player tiers, technical-route differentiation, leading player profiles, and white-space opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and strategy teams use this skill to analyze multi-player technology competitive landscapes for strategic planning, market entry, investment screening, or R&D direction setting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated research artifacts may contain business-sensitive topics, source lists, or competitive assessments.

Mitigation: Run the skill in an appropriate project folder and review report.md, source_index.csv, and claim_ledger.csv before sharing outputs.

Risk: The skill creates local research files during normal operation.

Mitigation: Use a dedicated writable run directory and inspect generated files before publishing or exporting them.

Risk: Evidence completeness depends on available patent, paper, database, and web search tools.

Mitigation: Record tool availability and fallback choices in method_decisions.md, and weaken completeness claims when using lower-confidence routes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/competitive-landscape-zhcn)
- [Workflow](references/workflow.md)
- [Source Routing](references/source-routing.md)
- [Quality Gates](references/quality-gates.md)
- [Evidence Schema](references/evidence-schema.md)
- [Deliverables](references/deliverables.md)
- [Domain Playbooks](references/domain-playbooks.md)
- [Method Benchmark](references/method-benchmark.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Structured Markdown reports with CSV evidence logs and optional DOCX/PDF exports when the host supports rendering]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local research files such as request.md, workplan.md, method_decisions.md, query_log.csv, source_index.csv, claim_ledger.csv, and report.md.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
