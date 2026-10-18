## Description:

Operates assigned GitLab work with owner-verified project access and guarded merge request delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to discover assigned GitLab work, implement changes, and manage issues, incidents, merge requests, reviews, and pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous GitLab writes may occur without individual confirmation, including pushes, labels, reviewer changes, and pipeline actions.

Mitigation: Use a least-privilege token or service account with limited project membership, and monitor write activity.

Risk: Recurring work can continue to act on issues, incidents, and merge requests without a fresh user prompt.

Mitigation: Monitor recurring runs and their effects on incidents, merge requests, and pipelines; disable the job when unattended changes are not acceptable.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab permissions and roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [Documentation style reference](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, code changes, and GitLab updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update GitLab issues, incidents, merge requests, labels, reviewers, and pipelines.]

## Skill Version(s):

1.111.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
