## Description:

A Chinese-language multi-agent pipeline for producing long-form research articles and papers through topic confirmation, parallel evidence retrieval, analysis, human outline review, drafting, audit, revision, illustration, and final delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and editorial teams use this skill to coordinate evidence-backed Chinese long-form articles, research reports, papers, and commentary with human review gates and independent audit steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send research topics, prompts, drafts, search queries, and image prompts to configured web, Tavily, model, and image providers.

Mitigation: Use the Phase 0 consent gate, anonymized wording, local model inference, and SVG or local image generation for sensitive or private topics.

Risk: The skill spawns multiple sub-agents and writes a project tree under run/<project>.

Mitigation: Review the Phase 0 file plan before execution and keep generated files scoped to the confirmed project directory.

Risk: Research and writing outputs may include incorrect, stale, or misleading evidence if used without review.

Mitigation: Use the built-in human review gates, evidence cards, source URLs, time-sensitivity labels, and independent audit phase before publication.

Risk: Shell snippets in documentation could be copied into an environment where they have unintended effects.

Mitigation: Treat shell snippets as manual review aids and inspect them before running any command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Pipeline README](references/pipeline-readme.md)
- [Design document](references/设计文档.md)
- [Coordinator role card](references/agents/00-主控-coordinator.md)
- [Literature scout role card](references/agents/01-文献检索-literature-scout.md)
- [Data scout role card](references/agents/02-数据检索-data-scout.md)
- [Analyst role card](references/agents/03-分析-analyst.md)
- [Writer role card](references/agents/04-写作-writer.md)
- [Auditor role card](references/agents/05-审计-auditor.md)
- [Case scout role card](references/agents/06-案例检索-case-scout.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown project files, evidence cards, outlines, drafts, audit reports, final article files, and delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a run/<project> workspace tree and may produce data visualizations or image-generation prompts when the user approves those phases.]

## Skill Version(s):

2.1.8 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
