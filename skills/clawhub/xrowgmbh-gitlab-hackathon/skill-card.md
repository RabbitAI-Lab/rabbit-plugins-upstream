## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and contributors use this skill to plan GitLab hackathon work, verify event rules, choose mergeable issues or merge requests, and avoid unfair scoring behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab API actions may use permissions beyond what the user needs.

Mitigation: Use a GitLab token with the minimum permissions required for the planned hackathon work.

Risk: Outdated event rules or scoring assumptions could lead to ineligible work.

Mitigation: Confirm the live hackathon rules, dates, prize requirements, and contribution-point documentation before acting.

Risk: Suggested labels, issue closures, comments, or merge requests could be incorrect or unfair if posted without review.

Mitigation: Review proposed GitLab actions before posting them and avoid spam, commit padding, incorrect labels, and invalid issue closures.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands, checklists, and planning notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitLab tooling such as glab, jq, and curl; GitLab API actions should be reviewed before execution.]

## Skill Version(s):

1.94.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
