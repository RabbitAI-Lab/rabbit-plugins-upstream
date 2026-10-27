## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect assigned GitLab work and carry out issue and merge request workflows across authorized projects. It applies project access and assignment checks before acting on work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may modify projects that fail its access check or accept work from unintended collaborators.

Mitigation: Keep recurring automation disabled until denied-project label writes and ambiguous collaborator selectors are fixed.

Risk: The skill directs the agent to perform GitLab changes without confirmation, including external or irreversible actions.

Mitigation: Restrict credentials and fork maintenance to approved repositories, define which merges, releases, and configuration changes are allowed, and do not treat the skill's blanket approval statement as authorization.

## Reference(s):

- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands, Code]

**Output Format:** [Markdown or text responses, with JSON reports, shell commands, or code when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab work items and merge requests as part of assigned tasks.]

## Skill Version(s):

1.122.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
