## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use the agent to work assigned GitLab issues and merge requests, prepare code changes, and manage delivery through project access checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanners report overly broad GitLab actions, changes after project access is denied, and instructions permitting work without user approval.

Mitigation: Review each proposed action, verify project access before any write, stop when access is denied, and require owner approval for GitLab mutations.

Risk: The security scan was partial: 22 of 23 components were fully inspected, and static analysis of one expression was limited.

Mitigation: Complete the remaining component and expression review before relying on the scan assessment or installing the skill.

## Reference(s):

- [GitLab Agent release on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [Discovery performance reference](artifact/references/discovery-performance.md)
- [Documentation style reference](artifact/references/documentation-style.md)

## Skill Output:

**Output Type(s):** [API calls, Code, Shell commands, Markdown, Configuration instructions, Guidance]

**Output Format:** [GitLab work, code changes, and Markdown summaries supported by shell commands and API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab issues, merge requests, branches, comments, labels, and time records when operating on assigned work.]

## Skill Version(s):

1.151.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
