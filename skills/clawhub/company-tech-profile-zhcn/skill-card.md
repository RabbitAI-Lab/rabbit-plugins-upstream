## Description:

Generates an evidence-driven technology profile and R&D assessment for a single company on a specified technical topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Technology leaders, analysts, investment screeners, and diligence teams use this skill to assess a single company's technical strength, R&D direction, and evidence-backed positioning within a defined technology topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous prompts that mention only a company may lead the agent to infer the wrong technology topic.

Mitigation: Ask the user to provide or confirm the technology topic before external research when the intended topic is unclear.

Risk: The workflow runs external research queries and writes local report and evidence files.

Mitigation: Run it in an appropriate writable workspace and review the generated evidence files before relying on the report.

Risk: Weak or degraded evidence paths can make company technology claims less certain.

Mitigation: Record tool coverage in method_decisions.md, maintain query and source ledgers, and lower confidence when structured patent or paper search is unavailable.

## Reference(s):

- [Workflow](references/workflow.md)
- [Source Routing](references/source-routing.md)
- [Deliverables](references/deliverables.md)
- [Evidence Schema](references/evidence-schema.md)
- [Quality Gates](references/quality-gates.md)
- [Method Benchmark](references/method-benchmark.md)
- [Domain Playbooks](references/domain-playbooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured Markdown report with Markdown and CSV evidence files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local evidence files such as request.md, workplan.md, method_decisions.md, query_log.csv, source_index.csv, claim_ledger.csv, and report.md; DOCX/PDF export is optional when host tools support it.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
