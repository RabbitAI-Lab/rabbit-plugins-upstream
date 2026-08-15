## Description:

Lunheng Article Pipeline orchestrates a Chinese-first multi-agent workflow for producing evidence-grounded long-form articles, research reports, papers, and commentary with retrieval, analysis, writing, audit, revision, illustration, and final delivery stages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to coordinate a Chinese-language research and writing pipeline for substantial articles or reports that need sourced literature, data, opposing arguments, audit review, human approval points, and packaged deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow declares memory_get and memory_search, which server security evidence identifies as unexplained memory-read access.

Mitigation: Review or remove memory-read tool declarations before deployment unless the installation context explicitly requires them.

Risk: The workflow may send search and image prompts to external providers, including fallback image providers.

Mitigation: Require explicit user approval before image generation or provider fallback, and avoid sending sensitive source material to external services.

Risk: The workflow writes a full run/<project> file tree in the current workspace.

Mitigation: Confirm the project name and complete file list before Phase 1, keep writes inside the current workspace, and review generated files before using or publishing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [README](README.md)
- [Pipeline Readme](references/pipeline-readme.md)
- [Design Document](references/设计文档.md)
- [Coordinator Agent](references/agents/00-主控-coordinator.md)
- [Literature Scout Agent](references/agents/01-文献检索-literature-scout.md)
- [Data Scout Agent](references/agents/02-数据检索-data-scout.md)
- [Analyst Agent](references/agents/03-分析-analyst.md)
- [Writer Agent](references/agents/04-写作-writer.md)
- [Auditor Agent](references/agents/05-审计-auditor.md)
- [Case Scout Agent](references/agents/06-案例检索-case-scout.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown files, structured templates, agent prompts, and occasional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a run/<project> workspace tree with task briefs, status, literature cards, data cards, outlines, drafts, audit reports, final article assets, evidence package, and delivery notes.]

## Skill Version(s):

2.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
