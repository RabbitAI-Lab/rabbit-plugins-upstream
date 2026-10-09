## Description:

Coordinates a multi-agent research, drafting, audit, and peer-review workflow for evidence-based academic papers, long-form articles, and industry analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers and researchers use this skill to develop evidence-backed long-form work with structured research, drafting, audits, peer review, and publication-channel advice. The project owner approves the workflow and external-service use before work begins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms or URLs may be sent to external services, potentially exposing sensitive research material.

Mitigation: Confirm external-service choices before starting; use the no-external-services path or redact sensitive inputs.

Risk: The workflow coordinates multiple agents and creates or edits many project files.

Mitigation: Approve the project scope and planned files before starting, and review generated drafts and audit records before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Pipeline user guide](references/pipeline-readme.md)
- [External services and consent](references/_shared/真源/external-services.md)
- [Permissions and tool boundaries](references/permissions.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown articles and review reports, a JSON evidence report, and written delivery guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project files include a final draft, evidence package, audit records, and delivery notes.]

## Skill Version(s):

2.17.0 (source: ClawHub release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
