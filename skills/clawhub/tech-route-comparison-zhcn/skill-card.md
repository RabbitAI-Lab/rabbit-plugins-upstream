## Description:

This skill guides an agent through evidence-based comparison of two or more technical routes, architectures, or solution paths, including maturity, readiness, risk, opportunity, and management-facing report outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, product strategists, and technical leaders use this skill to structure technical route comparisons before making research, architecture, investment, or roadmap decisions. It is intended for evidence-backed reports that freeze scope, compare routes on a consistent basis, record sources, and surface conditions that could change the recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes standard research files in the active output location, which can overwrite similarly named files if run in an existing folder.

Mitigation: Run the skill in a dedicated output directory and review planned file paths before allowing writes.

Risk: Technical route rankings can be misleading when the evidence base is thin, search tools are downgraded, or routes are compared at inconsistent levels.

Mitigation: Use the documented quality gates: freeze the comparison basis, keep route evidence separate before normalization, maintain source and claim ledgers, and lower confidence when coverage is limited.

Risk: Optional docx or pdf exports may require extra local tooling beyond the core Markdown and CSV outputs.

Mitigation: Review any export step and its tooling before execution; treat Markdown and traceability files as the default deliverables.

## Reference(s):

- [Workflow](references/workflow.md)
- [Deliverables](references/deliverables.md)
- [Quality Gates](references/quality-gates.md)
- [Evidence Schema](references/evidence-schema.md)
- [Source Routing](references/source-routing.md)
- [Method Benchmark](references/method-benchmark.md)
- [Domain Playbooks](references/domain-playbooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured Markdown reports with CSV traceability files and optional docx/pdf exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local research artifacts such as request.md, workplan.md, method_decisions.md, comparison_basis.md, query_log.csv, source_index.csv, claim_ledger.csv, and report.md.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
