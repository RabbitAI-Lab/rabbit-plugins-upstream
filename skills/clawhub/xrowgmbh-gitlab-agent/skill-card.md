## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to process GitLab work items and merge requests, including reviewing assigned work, making code changes, and managing delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious, citing behavior that may extend GitLab actions beyond assigned work, including adopting unassigned items and changing labels when project access checks fail.

Mitigation: Before granting GitLab access, review the flagged behavior and confirm the skill's project access and assignment boundaries match your expectations.

Risk: The security scan is incomplete, leaving some behavior without scan coverage.

Mitigation: Review the unresolved scan coverage and inspect the skill before installation.

## Reference(s):

- [GitLab Agent skill files](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [GitLab permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Markdown, Guidance]

**Output Format:** [Shell commands, code changes, and Markdown updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab work items and merge requests as part of its configured workflow.]

## Skill Version(s):

1.149.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
