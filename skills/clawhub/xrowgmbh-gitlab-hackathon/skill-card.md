## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan fair, rule-compliant contributions during GitLab hackathons. It helps them identify mergeable issues, track eligibility and scoring requirements, and avoid tactics that could harm maintainers or violate event rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Following contribution guidance can create or change issues, merge requests, labels, or comments in GitLab projects.

Mitigation: Check the current event rules, project, and target content before each write action; use a GITLAB_TOKEN scoped to the needed permissions.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points Guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, API calls]

**Output Format:** [Markdown with checklists and inline shell or API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command examples require glab, jq, curl, and a configured GITLAB_TOKEN.]

## Skill Version(s):

1.137.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
