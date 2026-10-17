## Description:

Initializes and resumes Chinese-first short-drama projects, routes work across creative stages, and offers a local dashboard and project export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Creators and production teams use this skill to organize short-drama projects, route requested work to companion skills, review progress in a local dashboard, and export current project materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project setup and editing can create or change local files.

Mitigation: Use the skill only for projects whose local files you intend to manage, and review outputs before sharing.

Risk: The localhost dashboard can remain running and scan the selected workspace.

Mitigation: Point --workspace only at intended project directories; check --status and use --stop when finished.

## Reference(s):

- [ClawHub short-drama release](https://clawhub.ai/worldwonderer/skills/short-drama)
- [Creator-first workflow](references/creator-workflow.md)
- [Five creator documents](references/creator-documents.md)
- [Runtime preflight](references/runtime-preflight.md)
- [Production forms](references/production-form-profiles.md)
- [Look Development](references/look-development.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Chinese-first text and Markdown, with local project metadata and export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update local project files; exports capture current state, not approval.]

## Skill Version(s):

1.0.12 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
