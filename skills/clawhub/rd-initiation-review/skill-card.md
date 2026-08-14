## Description:

R&D project initiation pre-screen and proposal audit for go/no-go decisions, public novelty boundary review, innovation-point assessment, and evidence-backed project rating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External reviewers, product teams, and R&D decision makers use this skill to assess a concrete project proposal, initiation report, or innovation package before a go/no-go, budget-release, or committee review decision. It helps separate proposal claims from external evidence, test public novelty and feasibility, and surface material gaps before the next gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process confidential proposal materials and produce local evidence files or reports containing sensitive business information.

Mitigation: Use an appropriate workspace and review generated reports and evidence files before sharing them externally.

Risk: Novelty, overlap, and completeness conclusions can be weaker when structured patent or paper retrieval is unavailable.

Mitigation: Record tool downgrade decisions, state coverage limitations in the report, and lower confidence on affected conclusions.

Risk: Proposal-stated claims can be mistaken for verified conclusions if evidence layers are not kept separate.

Mitigation: Maintain separate proposal-stated, externally corroborated, evidence-backed inference, and open-gap labels in the claim ledger and report.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/rd-initiation-review)
- [Workflow](artifact/references/workflow.md)
- [Deliverables](artifact/references/deliverables.md)
- [Evidence Schema](artifact/references/evidence-schema.md)
- [Source Routing](artifact/references/source-routing.md)
- [Quality Gates](artifact/references/quality-gates.md)
- [Method Benchmark](artifact/references/method-benchmark.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown review report, novelty note, CSV evidence logs, and optional docx or pdf exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local run-folder files such as request.md, workplan.md, method_decisions.md, query_log.csv, source_index.csv, claim_ledger.csv, report.md, and novelty-note.md.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
