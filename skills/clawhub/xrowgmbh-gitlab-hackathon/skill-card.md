## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon participation, select qualifying issues and merge requests, track scoring requirements, and avoid rule-abuse patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token with broad permissions could allow unintended labeling, closing, commenting, or merge request activity.

Mitigation: Use the minimum required GitLab token scope and confirm each GitLab action against the current hackathon rules and project norms before execution.

Risk: Outdated hackathon dates, scoring values, prize requirements, or eligibility rules could lead to invalid submissions or misleading priorities.

Mitigation: Verify the live GitLab hackathon pages, current hackathon API, and contribution points documentation before planning or submitting work.

Risk: Optimizing for points can create spam comments, padded commits, incorrect labels, or invalid issue closures.

Mitigation: Prioritize reviewable contributions, link only relevant issues, avoid artificial activity, and document exploit-like edge cases for maintainer clarification.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI, jq, curl, and a minimally scoped GITLAB_TOKEN for GitLab operations.]

## Skill Version(s):

1.81.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
