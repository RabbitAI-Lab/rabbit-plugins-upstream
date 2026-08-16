## Description:

Lunheng Article Pipeline coordinates a multi-agent Chinese long-form article and paper workflow from topic definition through research, analysis, outline review, drafting, audit, revision, illustration, and final delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to produce Chinese research essays, reports, papers, and long-form commentary with evidence cards, outline checkpoints, independent audit, revision loops, and a final evidence package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics, prompts, drafts, evidence cards, and image prompts may be sent to configured external search, model, or image providers.

Mitigation: Use the documented Phase 0 consent gate, redact confidential topics, switch cover generation to the local SVG option, and use local model routing where appropriate.

Risk: The workflow writes a run/<project>/ tree and creates multiple task, status, evidence, draft, audit, and final-delivery files.

Mitigation: Review the Phase 0 file list before proceeding and use the documented project-name constraints to keep writes within the current workspace.

Risk: Generated long-form research drafts can contain incorrect, stale, weakly supported, or duplicated claims if evidence is not reviewed.

Mitigation: Use the built-in human checkpoints, evidence-card mapping, source recency checks, independent audit stage, and final human review before publication.

## Reference(s):

- [Pipeline readme](references/pipeline-readme.md)
- [Design document](references/设计文档.md)
- [Coordinator agent card](references/agents/00-主控-coordinator.md)
- [Literature scout agent card](references/agents/01-文献检索-literature-scout.md)
- [Data scout agent card](references/agents/02-数据检索-data-scout.md)
- [Analyst agent card](references/agents/03-分析-analyst.md)
- [Writer agent card](references/agents/04-写作-writer.md)
- [Auditor agent card](references/agents/05-审计-auditor.md)
- [Case scout agent card](references/agents/06-案例检索-case-scout.md)
- [Status template](references/templates/status-template.md)
- [Task brief template](references/templates/任务简报-template.md)
- [Case card template](references/templates/案例卡-template.md)
- [Hand-off report template](references/templates/交接报告-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown files and structured project folders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a run/<project>/ tree with a task brief, status file, evidence cards, analysis outline, drafts, audit reports, final article, figures, evidence package, and delivery notes.]

## Skill Version(s):

2.1.7 (source: server release metadata; artifact frontmatter reports 2.1.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
