## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this agent to process work assigned to them in GitLab, including issues, merge requests, and project tasks. It checks configured ownership and assignment boundaries before work and supports guarded merge request delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports broad, partly undeclared GitLab actions and gaps in owner and work-scope checks.

Mitigation: Use the skill only when its GitLab automation is needed, and review its action scope before enabling it.

Risk: The security assessment says analysis is incomplete because some referenced local paths were missing.

Mitigation: Treat the assessment as incomplete and inspect the release contents before relying on its security conclusions.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [OpenClaw: Creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and guidance, with code and shell command examples where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab work item updates or merge request changes when authorized by the skill's scope and checks.]

## Skill Version(s):

1.138.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
