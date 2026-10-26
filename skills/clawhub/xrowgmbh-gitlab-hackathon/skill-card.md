## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan eligible GitLab hackathon contributions, choose reviewable issues and merge requests, track scoring requirements, and avoid abusive or disqualifying activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token may have access beyond the projects needed for the hackathon work.

Mitigation: Limit token permissions to the intended projects and confirm the scope before using GitLab commands.

Risk: Hackathon dates, eligibility rules, and scoring requirements may change, making an old plan inaccurate.

Mitigation: Verify the current hackathon rules, dates, and scoring guidance before relying on them.

Risk: Public contribution activity can be misused through spam, invalid labels, or unjustified issue closures.

Mitigation: Keep contributions useful and transparent; only comment, label, or close issues for valid project reasons.

## Reference(s):

- [GitLab Hackathon skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [Contribution points guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown plans and checklists, with example shell commands and GitLab API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses current event rules and project context; GitLab command examples require glab, jq, curl, and a suitably scoped GITLAB_TOKEN.]

## Skill Version(s):

1.122.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
