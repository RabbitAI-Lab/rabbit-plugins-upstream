## Description:

论衡 is a long-form article and paper production pipeline for academic writing, business commentary, industry analysis, and in-depth public-account articles, with staged research, drafting, critique, audit, and final inspection workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, analysts, and teams use this skill to coordinate evidence-backed long-form Chinese-first writing projects with human checkpoints, multi-agent research, drafting, review, and delivery reports. It is best suited for substantial factual or analytical work rather than short-form copy or time-critical news briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research terms, target URLs, and possibly draft content may leave the local machine depending on the Phase 0 consent choice.

Mitigation: Use the all-local or partial-consent option for sensitive topics, record consent before Phase 1, and rely on host-level network/tool restrictions when mechanical enforcement is required.

Risk: The pipeline creates and modifies multiple project files during normal operation.

Mitigation: Confirm the project name and file list in Phase 0, keep writes scoped to run/<project-name>/ inside the workspace, and retain failed-run files for human review rather than deleting them automatically.

Risk: Long-form research and analysis can still contain weak evidence, stale data, or misleading citations.

Mitigation: Use the skill's staged research, triangle verification, M gates, G audit checks, peer review, and final human-facing delivery notes to surface unresolved limitations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [QUICKSTART.md](QUICKSTART.md)
- [pipeline-readme.md](references/pipeline-readme.md)
- [deliverables.md](references/deliverables.md)
- [permissions.md](references/permissions.md)
- [external-services.md](references/_shared/external-services.md)
- [host-hardening-recipe.md](references/_shared/host-hardening-recipe.md)
- [M-Gate-Algorithm.md](references/_shared/M-Gate-Algorithm.md)
- [failure-modes.md](references/_shared/failure-modes.md)
- [audit-checklist-quickref.md](references/_shared/audit-checklist-quickref.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown files, status records, evidence cards, audit reports, review reports, final article drafts, and delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates approximately 15-25 workspace files under run/<project-name>/ after Phase 0 confirmation; default output language is Chinese, with target language selectable during Phase 0.]

## Skill Version(s):

2.12.27 (source: server release evidence, SKILL.md metadata.openclaw.version, and QUICKSTART.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
