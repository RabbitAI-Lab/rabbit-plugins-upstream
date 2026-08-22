## Description:

A multi-agent pipeline for producing evidence-grounded long-form research articles, business commentary, industry analysis, and public-account essays with literature, data, case research, critique, audit, and human review checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, analysts, and teams use this skill to coordinate a structured long-form article workflow that gathers published literature, public data, and cases, then produces outlines, drafts, critique, audits, final Markdown deliverables, and evidence packages. It is best suited to substantial evidence-based writing rather than short posts, instant answers, literary writing, or original data collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow is heavyweight and can create or modify multiple project files.

Mitigation: Confirm the Phase 0 choices, project name, file list, and expected deliverables before starting the pipeline.

Risk: The workflow can send research topics, URLs, prompts, and draft content to external web search, Tavily, image-generation, and model providers.

Mitigation: Use the documented Phase 0 consent gate to choose full consent, partial consent, desensitized wording, local model use, SVG-only visuals, or refusal of external transfer.

Risk: The skill is not intended for original experiments, surveys, interviews, private data collection, or statistical computation.

Mitigation: Provide original data and computed results as user-supplied evidence, and use a dedicated environment for code execution or statistical analysis.

Risk: Maintenance and version-upgrade references could be mistaken for instructions to perform release-maintenance actions.

Mitigation: Treat maintenance references as documentation unless the user explicitly requests a release-maintenance workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [README](README.md)
- [Quickstart](QUICKSTART.md)
- [Pipeline manual](references/pipeline-readme.md)
- [Glossary](references/glossary.md)
- [Deliverables and gates](references/deliverables.md)
- [M-Gate algorithm](references/_shared/M-Gate-Algorithm.md)
- [Failure modes](references/_shared/failure-modes.md)
- [Audit checklist](references/_shared/audit-checklist-quickref.md)
- [Performance profile](PERFORMANCE-PROFILE.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown files and structured written guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a project file tree with briefs, status, literature cards, data cards, case cards, outlines, drafts, critique reports, audit reports, final article files, optional visual assets, evidence packages, and delivery notes.]

## Skill Version(s):

2.2.18 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
