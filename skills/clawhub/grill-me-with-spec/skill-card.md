## Description:

Use when the user needs to create or refine a feature SPEC SDD before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run a Portuguese-first requirements interview before implementation and produce a complete SPEC SDD for feature, bugfix, refactor, API, infrastructure, frontend, or documentation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update local SPEC files under .specs as part of its requirements workflow.

Mitigation: Review the generated SPEC contents and approve them explicitly before allowing implementation to begin.

Risk: The workflow is Portuguese-first for user-facing questions and may not fit teams expecting English requirements interviews.

Mitigation: Confirm the expected interview language before using the skill in a shared delivery process.

## Reference(s):

- [SPEC SDD Template](references/spec-sdd-template.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/grill-me-with-spec)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Source repository metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Portuguese Markdown SPEC SDD file with structured requirements, acceptance criteria, and task plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes or updates a local .specs/SPEC-{YYYYMMDD}-{feature}.md draft and requires user approval before implementation.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
