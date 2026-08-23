## Description:

A multi-agent workflow for producing evidence-grounded long-form articles, academic essays, business commentary, and industry analysis with literature, data, and case retrieval, staged human review, critique, audit, and final delivery controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run an OpenClaw long-form writing pipeline that coordinates research, analysis, drafting, critique, audit, and final delivery for fact-heavy articles. It is best suited to projects that need published literature, public data, case evidence, citation discipline, and human approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell/process access confusion could expand the workflow beyond its intended writing and review boundary.

Mitigation: Install only into an agent with exec and process access disabled, and do not grant shell access to satisfy command examples in the role cards.

Risk: The workflow can create or modify multiple project files during a long-form writing run.

Mitigation: Review the Phase 0 file list before approval and keep outputs inside the user-confirmed project directory.

Risk: Research topics, prompts, or user-provided materials may be sent to external search, extraction, model, or image-generation services.

Mitigation: Use desensitized topics and materials, approve only the external services needed for the run, and choose local or SVG-only alternatives when sensitive content is involved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [README](README.md)
- [Quickstart](QUICKSTART.md)
- [Pipeline manual](references/pipeline-readme.md)
- [Core glossary](references/glossary.md)
- [Delivery boundaries and safeguards](references/deliverables.md)
- [Operations guide](references/operations.md)
- [Error guide](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown files and structured writing workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project files under a user-confirmed run directory, including briefs, status reports, evidence cards, outlines, drafts, audit reports, final manuscripts, evidence packages, and delivery notes.]

## Skill Version(s):

2.3.17 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
