## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to find assigned GitLab issues, merge requests, and todos, then carry out eligible work under assignment and project access checks. It can also produce queue reports and status updates and create or update GitLab records as work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims broad approval for remote changes, and its discovery behavior may modify projects that fail its owner-access check.

Mitigation: Remove blanket approval claims, limit the allowed projects and remote actions, and ensure denied projects receive no writes before enabling the skill.

Risk: Recurring automation could repeat remote actions before its access controls and write behavior are verified.

Mitigation: Keep recurring execution disabled until the controls are verified, and use a dedicated GitLab account with limited access.

Risk: Merge and vulnerability-exception decisions can affect project security and delivery.

Mitigation: Review the applicable merge and vulnerability-exception policies before enabling remote actions.

## Reference(s):

- [GitLab permissions and default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill creation](https://docs.openclaw.ai/tools/creating-skills)
- [Continuation procedure](artifact/references/continuations.md)
- [Discovery performance notes](artifact/references/discovery-performance.md)
- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [Guidance, Markdown reports, Shell commands, GitLab issue, work item, and merge request updates]

**Output Format:** [Markdown guidance and reports with shell commands and GitLab updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform GitLab writes when work passes the documented project-access and assignment gates.]

## Skill Version(s):

1.123.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
