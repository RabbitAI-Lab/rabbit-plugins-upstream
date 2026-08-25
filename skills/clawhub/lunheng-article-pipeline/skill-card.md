## Description:

A Chinese-oriented multi-agent pipeline for serious long-form writing, including academic papers, business commentary, industry analysis, and deep public-account articles, with literature/data/case triangulation, quality gates, failure-mode checks, trust grading, and revision loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to coordinate evidence-backed Chinese long-form writing workflows with human confirmation gates, subagent research roles, drafting, audit, review, and final delivery files. It is intended for Chinese academic, analytical, and business writing where citations, data provenance, and revision discipline matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates and modifies workspace files as part of normal article production.

Mitigation: Use the Phase 0 consent gate, review the planned file list and project name before work begins, and run it only in the intended workspace.

Risk: Research, model prompts, optional image generation, and web extraction may share task content with external providers after consent.

Mitigation: For confidential work, redact prompts, choose local models where available, use SVG-only image generation, and decline external services that are not needed.

Risk: Subagent coordination and session-history access can expose work-in-progress context across the run.

Mitigation: Limit session-history review to the subagents spawned for the current project and avoid loading unrelated or sensitive sessions.

Risk: The workflow is specialized for Chinese long-form writing and may be unsuitable for non-Chinese, short-form, real-time news, experimental, or code-execution-heavy tasks.

Mitigation: Use it only for its documented Chinese long-form research and writing scope, and select a simpler workflow for short or unsupported tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline manual](references/pipeline-readme.md)
- [Core concepts glossary](references/glossary.md)
- [Deliverables, failure modes, gates, and revision loop](references/deliverables.md)
- [M-Gate algorithm](references/_shared/M-Gate-Algorithm.md)
- [Audit checklist quick reference](references/_shared/audit-checklist-quickref.md)
- [Chinese AI-trace gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown files, status files, audit reports, evidence cards, final article drafts, and optional SVG chart code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and modifies workspace files during normal operation after Phase 0 consent.]

## Skill Version(s):

2.5.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
