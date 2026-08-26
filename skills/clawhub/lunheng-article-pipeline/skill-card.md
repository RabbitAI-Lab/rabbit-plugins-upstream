## Description:

A Chinese long-form writing pipeline for academic papers, business commentary, industry analysis, and deep articles that orchestrates multiple agents for literature, data, case research, analysis, writing, critique, audit, and final review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to coordinate evidence-backed Chinese long-form writing projects that require human checkpoints, source collection, drafting, critique, audit, and final delivery artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates and modifies workspace files and coordinates long-running sub-agent activity.

Mitigation: Use the Phase 0 confirmation step to review the planned file list and proceed only after the workspace effects are acceptable.

Risk: Research, model, and optional image-generation steps may send prompts, URLs, topics, drafts, or source material to external providers.

Mitigation: Use the documented Phase 0 service choices to refuse external services, select local or SVG alternatives, and redact confidential data before use.

Risk: The skill is specialized for Chinese long-form analytical writing and may be a poor fit for short answers, time-sensitive news, literary work, or projects needing first-party data collection.

Mitigation: Use the documented scope and quickstart guidance to choose lighter workflows or a different tool when the task falls outside the pipeline's intended use.

## Reference(s):

- [Quickstart Guide](QUICKSTART.md)
- [Pipeline Manual](references/pipeline-readme.md)
- [Core Glossary](references/glossary.md)
- [Deliverables and Failure Modes](references/deliverables.md)
- [M-Gate Algorithm](references/_shared/M-Gate-Algorithm.md)
- [Audit Checklist](references/_shared/audit-checklist-quickref.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown files, status records, evidence cards, drafts, audit reports, final delivery notes, and optional SVG chart assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a coordinated workspace artifact set for long-form writing projects; normal operation may create or modify about 15-25 files.]

## Skill Version(s):

2.5.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
