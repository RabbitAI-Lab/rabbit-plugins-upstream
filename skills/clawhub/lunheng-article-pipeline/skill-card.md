## Description:

学术论文、深度长文和行业分析流水线，提供多 Agent 研究、写作、审计、同行评审以及期刊或发布渠道匹配建议，并声明不调用执行类工具。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, analysts, and agent operators use this skill to run a structured long-form writing workflow for evidence-backed academic papers, industry analysis, and serious essays. It is intended for projects that need human checkpoints, research collection, drafting, critique, audit, final inspection, and optional publication-channel advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create multiple project files in the workspace.

Mitigation: Require Phase 0 confirmation of the project name and file list before writing, and keep writes scoped to the workspace project folder.

Risk: Research lookup can send search terms, URLs, or selected content to external services when enabled.

Mitigation: Use the Phase 0 consent choices to select no external services, partial consent, or only approved lookup categories for sensitive material.

Risk: Long-form research and citation workflows can produce misleading claims if drafts are used without review.

Mitigation: Use the built-in human checkpoints, audit, peer-review, and final-inspection stages before sharing or publishing outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [QUICKSTART.md](artifact/QUICKSTART.md)
- [Pipeline overview](artifact/references/_shared/真源/pipeline-overview.md)
- [Phase order](artifact/references/_shared/真源/phase-order.yaml)
- [Permissions and tool boundaries](artifact/references/permissions.md)
- [External services](artifact/references/_shared/真源/external-services.md)
- [Deliverables and failure modes](artifact/references/deliverables.md)
- [Audit checklist](artifact/references/_shared/真源/audit-checklist-quickref.md)
- [M-Gate algorithm](artifact/references/_shared/真源/M-Gate-Algorithm.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown documents, status files, audit reports, review reports, and final long-form text in a workspace project folder]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged research, drafting, review, and final-inspection artifacts; external lookup and worker-agent activity are governed by Phase 0 user consent.]

## Skill Version(s):

2.12.73 (source: server release metadata and SKILL.md metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
