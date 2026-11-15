## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers participating in GitLab hackathons use this skill to check current event rules and eligibility, identify manageable contributions, and organize fair, reviewable merge requests while avoiding score manipulation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hackathon dates, scoring, and eligibility requirements may change.

Mitigation: Check the linked official event and contribution-point pages before choosing work or relying on scoring details.

Risk: GitLab CLI commands can access account resources using GITLAB_TOKEN, and the workflow includes creating or updating contributions.

Mitigation: Review each command, target project, and proposed change before running it; use only the access needed for the task.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, API calls, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans depend on current event rules, eligibility, project access, and participant constraints.]

## Skill Version(s):

1.147.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
