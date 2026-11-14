## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this agent to process assigned GitLab to-dos, issues, and merge requests, make scoped code changes, and report work status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the release suspicious because it may act beyond assigned GitLab work or make changes without reliable project authorization.

Mitigation: Before enabling it, confirm project access and task authorization, then review proposed repository and GitLab changes before delivery.

Risk: The scan is partial and could not resolve three local references, so its evidence is incomplete.

Mitigation: Resolve and review the missing references and complete a full security review before enabling unattended runs.

## Reference(s):

- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)

## Skill Output:

**Output Type(s):** [Code, Shell commands, GitLab issue and merge request updates, Markdown status reports]

**Output Format:** [GitLab updates and code changes, with shell commands and Markdown status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by assigned GitLab task; may include scoped repository changes and updates to issues or merge requests.]

## Skill Version(s):

1.144.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
