## Description:

Provides a Chinese-language, evidence-based workflow for comparing two or more technology routes, architectures, or solution paths and producing decision-ready route analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and technical decision-makers use this skill to structure Chinese-language technology route comparisons, maturity assessments, opportunity scans, and management-facing technical research reports. It helps freeze scope, normalize comparison criteria, gather evidence, track claims, and produce a structured Markdown report with supporting evidence files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may create local research files and use available search or document-reading tools.

Mitigation: Review the task scope, working directory, and tool availability before running the workflow, and inspect generated files before sharing or relying on them.

Risk: Route comparisons can become misleading when routes, evidence levels, or comparison layers are mixed.

Mitigation: Use the provided comparison basis, source index, claim ledger, and quality gates to freeze scope, normalize assumptions, and trace major recommendations to evidence.

Risk: The skill is not intended for legal patent advice, freedom-to-operate analysis, infringement analysis, company profiling, market sizing, or proposal package review.

Mitigation: Redirect those tasks to the appropriate workflow or qualified reviewer before treating the output as decision support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/tech-route-comparison-zhcn)
- [Workflow](artifact/references/workflow.md)
- [Deliverables](artifact/references/deliverables.md)
- [Quality gates](artifact/references/quality-gates.md)
- [Evidence schema](artifact/references/evidence-schema.md)
- [Source routing](artifact/references/source-routing.md)
- [Method benchmark](artifact/references/method-benchmark.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports with CSV and Markdown evidence-tracking files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local working files such as request.md, workplan.md, comparison_basis.md, query_log.csv, source_index.csv, claim_ledger.csv, and report.md.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
