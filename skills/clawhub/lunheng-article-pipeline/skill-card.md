## Description:

论衡 is a Chinese long-form writing pipeline for academic papers, business commentary, industry analysis, and deep essays, coordinating multiple agent roles for research, evidence checks, drafting, critique, audit, and final delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, analysts, and writers use this skill to run a structured multi-agent workflow for evidence-backed Chinese long-form articles and papers. It is most useful when the task needs literature, data, case evidence, revision controls, audit reports, and human approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may create or modify many project files.

Mitigation: Confirm the project name, workspace path, and Phase 0 file list before starting, and keep outputs confined to run/<project-name>/.

Risk: Search terms, URLs, prompts, drafts, or optional image prompts may be sent to external providers after user consent.

Mitigation: For sensitive work, choose the no-external or redacted mode during Phase 0, keep optional image generation off, and avoid sending proprietary drafts to external services.

Risk: Memory assistance can expose prior workspace context if enabled.

Mitigation: Leave memory assistance disabled unless needed, and explicitly name the allowed memory files and purpose when enabling it.

Risk: Long-form evidence synthesis can still include weak sources, stale data, or unresolved audit items.

Mitigation: Review the generated evidence package, audit report, delivery notes, and any listed human verification items before publishing or submitting the final text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart guide](QUICKSTART.md)
- [Pipeline manual](references/pipeline-readme.md)
- [Deliverables and gates](references/deliverables.md)
- [M-Gate algorithm](references/_shared/M-Gate-Algorithm.md)
- [Failure modes](references/_shared/failure-modes.md)
- [Audit checklist](references/_shared/audit-checklist-quickref.md)
- [Tool capability boundaries](references/_shared/工具能力边界.md)
- [G14 Chinese AI trace gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance, configuration]

**Output Format:** [Markdown project files, research cards, audit reports, final draft files, delivery notes, and optional SVG or export guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow writes project artifacts under a user-confirmed run/<project-name>/ tree and may produce optional image or export artifacts only after consent.]

## Skill Version(s):

2.7.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
