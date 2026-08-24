## Description:

Lunheng Article Pipeline coordinates multiple agent roles to produce Chinese academic papers, business commentary, industry analysis, and other long-form articles with literature, data, case evidence, review gates, and a required Phase 0 consent step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to run a consent-gated, evidence-based workflow for Chinese long-form writing projects such as academic papers, business commentary, industry analysis, and public-account essays. It is intended for projects that need structured research, human checkpoints, audit reports, and final Markdown deliverables rather than quick short-form drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, prompts, URLs, draft content, or image prompts may be sent to external providers when external search, model, or image services are enabled.

Mitigation: Use the Phase 0 consent choices deliberately, select the no-external or local path for confidential work, and avoid enabling optional image generation unless the prompt can be shared externally.

Risk: The workflow creates a multi-file project tree and may produce many research cards, drafts, audits, figures, evidence packages, and delivery notes.

Mitigation: Review the Phase 0 file plan before allowing the workflow to write files, use a dedicated workspace, and keep generated artifacts separate from unrelated project files.

Risk: The skill is specialized for Chinese long-form and Chinese-journal-oriented writing workflows.

Mitigation: Use a different skill for non-Chinese work unless the task is explicitly re-scoped and the target language, citation style, and source expectations are confirmed during Phase 0.

Risk: Generated claims, citations, data interpretations, and audit outcomes may still be incomplete or misleading.

Mitigation: Keep the human review checkpoints, inspect evidence cards and audit reports, and verify high-impact citations or data before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [README](README.md)
- [Quickstart](QUICKSTART.md)
- [Core concepts glossary](references/glossary.md)
- [Pipeline operations guide](references/pipeline-readme.md)
- [Deliverables and review gates](references/deliverables.md)
- [Illustration and writing operations](references/operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown project files, audit notes, research cards, drafts, final articles, and concise agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a workspace project tree after Phase 0 consent; optional image generation is consent-gated.]

## Skill Version(s):

2.4.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
