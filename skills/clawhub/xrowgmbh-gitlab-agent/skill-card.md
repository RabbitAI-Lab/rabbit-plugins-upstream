## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab automation operators use this skill to work assigned GitLab issues and merge requests while enforcing project-access, assignment, workflow-label, CI, and reviewer-selection rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant broad unattended write authority over GitLab issues, merge requests, branches, comments, labels, reviewers, and pipelines.

Mitigation: Install it only for a dedicated, least-privileged GitLab automation account and review the exact projects, token scope, and recurring execution settings before use.

Risk: The workflow uses ci.skip on pushes and then manually triggers merge-request pipelines.

Mitigation: Confirm the organization accepts this CI behavior and monitor that required pipelines are started and completed before review or merge.

Risk: The security gate depends on helper scripts being runnable before the agent works on project objects.

Mitigation: Verify helper script execute permissions and require the access check to pass before reading, cloning, commenting, pushing, or mutating labels for non-owner work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON helper outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN.]

## Skill Version(s):

1.84.6 (source: evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
