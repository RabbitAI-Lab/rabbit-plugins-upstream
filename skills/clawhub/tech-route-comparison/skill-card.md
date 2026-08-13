## Description:

Provides evidence-backed comparison of two or more technical routes, architectures, or solution paths for route selection, maturity assessment, feasibility analysis, opportunity mapping, and management-grade technical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, R&D teams, and technical decision makers use this skill to compare technical routes on a normalized evidence basis and produce a scenario-specific recommendation. It is intended for route comparison, maturity or TRL assessment, feasibility review, opportunity mapping, and management-ready technical pre-research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research runs can become overly broad or low-confidence when the route set, application scenario, or available retrieval tools are unclear.

Mitigation: Freeze the scope and comparison basis before wide retrieval, record tool-tier downgrades in method_decisions.md, and weaken confidence language when evidence coverage is degraded.

Risk: Route recommendations can mislead readers if claims are not traceable or counterevidence is skipped.

Mitigation: Use source_index.csv and claim_ledger.csv for major judgments, require counterevidence and update triggers, and complete the quality gates before treating report.md as final.

## Reference(s):

- [Workflow](references/workflow.md)
- [Deliverables](references/deliverables.md)
- [Source Routing](references/source-routing.md)
- [Quality Gates](references/quality-gates.md)
- [Evidence Schema](references/evidence-schema.md)
- [Method Benchmark](references/method-benchmark.md)
- [Domain Playbooks](references/domain-playbooks.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Structured Markdown reports with CSV evidence ledgers and optional docx or PDF exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local run-folder files such as request.md, workplan.md, method_decisions.md, comparison_basis.md, query_log.csv, source_index.csv, claim_ledger.csv, and report.md.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
