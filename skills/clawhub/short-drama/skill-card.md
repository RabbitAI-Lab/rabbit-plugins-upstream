## Description:

Initializes and continues filesystem-based short-drama and animated-drama projects, routes work across creator documents, and supports a local dashboard, production-form and Look Development decisions, and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

For writers and production teams managing short-drama or animated-drama projects: initialize a project, track its progress, route work to focused creator skills, view or edit project documents in a local dashboard, and export current materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: In a shared workspace, dashboard.log may expose the dashboard editing-access key to other users.

Mitigation: Restrict access to the workspace and dashboard.log or use foreground mode; keep the access-key URL private, avoid logging it, and stop the dashboard when finished.

Risk: Companion skills and external adapters require separate security review.

Mitigation: Review companion skills and external adapters separately before installing or using them.

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/short-drama)
- [Creator workflow](references/creator-workflow.md)
- [Creator documents](references/creator-documents.md)
- [Runtime preflight](references/runtime-preflight.md)
- [Production form profiles](references/production-form-profiles.md)
- [Look Development](references/look-development.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown guidance, JSON project configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update files in the selected project workspace and run the local dashboard when requested.]

## Skill Version(s):

1.0.34 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
