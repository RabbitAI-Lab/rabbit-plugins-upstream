## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using a GitLab agent use this skill to identify worthwhile improvements in the helm-openclaw project, prepare a focused merge request, and manage their own older merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish a new merge request and close older merge requests without clearly limiting those actions to user-approved work.

Mitigation: Scope GitLab credentials to the named project, review proposed content before publishing, and require review before closing existing merge requests.

## Reference(s):

- [Target GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown merge request content and GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses each merge request on one issue; may close the agent's own merge requests that remain unaccepted for 10 days after the latest activity or review state.]

## Skill Version(s):

1.123.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
