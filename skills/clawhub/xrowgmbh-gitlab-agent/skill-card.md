## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to process assigned GitLab work, enforce project access and assignment checks, and deliver code changes through guarded merge request workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automation can change excluded projects and may accept work from unintended collaborators.

Mitigation: Use a dedicated GitLab account limited to approved projects, and keep recurring runs disabled until denied-project writes and ambiguous collaborator matching are fixed.

Risk: Fork maintenance and consequential publishing or merging can affect project state.

Mitigation: Explicitly limit fork maintenance and consequential publishing or merging to approved scope.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill creation](https://docs.openclaw.ai/tools/creating-skills)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [Documentation style guide](artifact/references/documentation-style.md)

## Skill Output:

**Output Type(s):** [GitLab work-item updates, Code, Merge requests, Markdown, Shell commands, Configuration instructions]

**Output Format:** [GitLab changes, code, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.122.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
