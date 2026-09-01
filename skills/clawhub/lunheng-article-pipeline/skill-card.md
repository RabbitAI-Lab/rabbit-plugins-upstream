## Description:

Lunheng Article Pipeline coordinates a multi-agent Chinese long-form writing workflow for academic papers, business commentary, industry analysis, and deep public articles, with evidence triangulation, structured quality gates, failure-mode checks, data-trust levels, and up to two revision loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, analysts, and developers use this skill to run an evidence-backed Chinese long-form article pipeline from topic confirmation through literature, data, case research, drafting, critique, audit, peer review, and final delivery. It is best suited to projects that need human approval gates, citation discipline, and a structured revision process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports under-disclosed cross-workspace feedback-memory behavior that may move feedback outside the active project boundary.

Mitigation: Review this behavior before installation and require feedback reports to remain inside the project folder when workspace isolation matters.

Risk: Projects may include confidential research, client data, unpublished strategy, or other sensitive inputs.

Mitigation: Use the Phase 0 options to limit or refuse external services, and provide local or desensitized inputs when sensitive material is involved.

Risk: Draft archive retention choices can affect whether intermediate work is preserved for audit or review.

Mitigation: Select keep_all for draft archive retention when preservation, teaching, or later auditability matters.

## Reference(s):

- [Quickstart](QUICKSTART.md)
- [Pipeline Runbook](references/pipeline-readme.md)
- [Glossary and Core Concepts](references/glossary.md)
- [Deliverables, Failure Modes, Gates, and Revision Loop](references/deliverables.md)
- [M-Gate Algorithm](references/_shared/M-Gate-Algorithm.md)
- [Failure Modes](references/_shared/failure-modes.md)
- [Chinese Data Source Integration](references/_shared/中文数据源集成.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance, Configuration instructions]

**Output Format:** [Markdown documents, structured status files, research cards, review reports, and delivery checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates multiple sub-agent phases and human approval gates; no shell execution is required by the skill.]

## Skill Version(s):

2.5.22 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
