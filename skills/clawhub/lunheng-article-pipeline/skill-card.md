## Description:

A multi-agent workflow for producing evidence-based long-form articles or research papers through topic framing, parallel literature and data retrieval, analysis, human outline review, writing, audit, revision, optional graphics, and final delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to coordinate a structured writing pipeline for deep articles, research reports, papers, and long-form commentary that need sourced literature, sourced data, adversarial argument planning, independent audit, and human checkpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow includes a persistent role-file self-update step without clear approval boundaries.

Mitigation: Clarify or disable persistent role-file updates before use, and require explicit user approval before lessons from a project are written back into skill instructions.

Risk: The workflow performs web research, writes project files, and may run for hours, so unchecked claims or stale artifacts can enter the final article.

Mitigation: Keep the documented human checkpoints and review the evidence package, audit report, and final delivery notes before publishing or relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Pipeline runbook](references/pipeline-readme.md)
- [Coordinator role card](references/agents/00-主控-coordinator.md)
- [Literature scout role card](references/agents/01-文献检索-literature-scout.md)
- [Data scout role card](references/agents/02-数据检索-data-scout.md)
- [Analyst role card](references/agents/03-分析-analyst.md)
- [Writer role card](references/agents/04-写作-writer.md)
- [Auditor role card](references/agents/05-审计-auditor.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown files, structured project folders, role handoff reports, audit reports, delivery notes, and optional chart-generation commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are organized as a project workspace with task briefs, status tracking, literature cards, data cards, analysis outlines, drafts, revision notes, final article files, graphics, and evidence packages.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
