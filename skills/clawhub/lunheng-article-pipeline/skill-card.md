## Description:

Coordinates an eight-role multi-agent workflow for long-form research and writing, producing evidence cards, analytical outlines, drafts, critique reports, audit reports, final articles, and delivery notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and content teams use this skill to produce evidence-grounded academic papers, business commentary, industry analysis, and other long-form articles with human review gates. It is best suited to substantial topics that need literature, data, case evidence, counterargument, and independent audit rather than short opinion writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics, prompts, drafts, evidence cards, and image prompts may be sent to configured search, extraction, image generation, or model providers.

Mitigation: Use the documented local/no-external option or anonymized prompts for private, client, or unpublished topics, and record the user's external-service choice during Phase 0.

Risk: The workflow creates a multi-file run/<project>/ tree for each article project.

Mitigation: Review the Phase 0 file list and project name before allowing file creation.

Risk: The pipeline is heavy for short or low-evidence writing tasks.

Mitigation: Reserve the full workflow for substantial long-form work; use the documented lightweight path or direct writer flow for shorter pieces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [README](README.md)
- [Pipeline runbook](references/pipeline-readme.md)
- [Deliverables and gates](references/deliverables.md)
- [M-Gate algorithm](references/_shared/M-Gate-Algorithm.md)
- [Failure modes](references/_shared/failure-modes.md)
- [Audit checklist quick reference](references/_shared/audit-checklist-quickref.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown files and structured project folders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a run/<project>/ workspace containing task briefs, status files, evidence cards, outlines, drafts, audit reports, final article files, optional image assets, evidence packages, and delivery notes.]

## Skill Version(s):

2.2.8 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
