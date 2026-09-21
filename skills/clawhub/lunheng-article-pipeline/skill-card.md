## Description:

A multi-agent long-form writing pipeline for academic papers, in-depth articles, and industry analysis, with advisory peer review and journal or publishing-channel matching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, analysts, and writers use this skill to coordinate evidence-backed long-form article production with human confirmation, staged research, drafting, critique, audit, final inspection, and optional publishing-channel advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may write a project folder, status files, audit reports, and heartbeat files during long-running article work.

Mitigation: Review and approve the Phase 0 file plan before starting, and keep generated work inside the project-local workspace.

Risk: Research lookups and external model or metadata services may disclose task context if approved for confidential work.

Mitigation: Use local or no-external options for sensitive topics, redact confidential details, and avoid placing secrets in prompts, task briefs, status files, or reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Publisher profile](https://clawhub.ai/user/zuoyunlai)
- [Pipeline README](references/pipeline-readme.md)
- [Permissions](references/permissions.md)
- [External services](references/_shared/external-services.md)
- [Asset index](references/_shared/asset-index.md)
- [Pipeline overview](references/_shared/pipeline-overview.md)
- [Phase order](references/_shared/phase-order.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown project files, status reports, research cards, review reports, audit notes, and final long-form drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a project-local run folder with status files, audit reports, templates, and optional telemetry heartbeat files after user confirmation.]

## Skill Version(s):

2.12.68 (source: server release metadata and SKILL.md metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
