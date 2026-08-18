## Description:

Single-company technology profile and R&D assessment for a defined technology topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Technical leaders, analysts, and investment screeners use this skill to assess one company's technical strength, R&D direction, and core technology layout for a defined topic using patent, paper, product, and public evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company-only prompts can cause the skill to infer a likely technology topic.

Mitigation: Specify the company, topic, decision purpose, and time window explicitly, and ask the agent to pause when scope is ambiguous.

Risk: Public research and local report-file creation may proceed when a company and technology area are supplied.

Mitigation: Run the skill in the intended workspace and review the generated request, workplan, source, claim, and report files before sharing.

Risk: Downgraded retrieval paths can reduce coverage for patent, paper, and public-signal evidence.

Mitigation: Require the report to state the retrieval tier, coverage limits, and confidence level whenever structured patent or paper retrieval is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/company-tech-profile)
- [Workflow](references/workflow.md)
- [Source Routing](references/source-routing.md)
- [Evidence Schema](references/evidence-schema.md)
- [Quality Gates](references/quality-gates.md)
- [Method Benchmark](references/method-benchmark.md)
- [Domain Playbooks](references/domain-playbooks.md)
- [Deliverables](references/deliverables.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured Markdown report with CSV evidence files; optional docx or pdf export when the host supports rendering.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a run folder containing request, workplan, method decisions, query log, source index, claim ledger, and report files.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
