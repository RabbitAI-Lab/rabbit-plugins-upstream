## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues and merge requests, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon work, choose qualifying issues and merge requests, monitor scoring requirements, and avoid rule-abusing behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab operations may use a GITLAB_TOKEN with glab and can affect public projects.

Mitigation: Install only if comfortable using that token, and review comments, labels, issue closures, and merge requests before submitting actions.

Risk: Hackathon rules, dates, scoring, and prize requirements can change between events.

Mitigation: Verify the live hackathon pages and current API before optimizing work or claiming eligibility.

Risk: Score-focused activity can become spammy or unfair if comments, labels, issue closures, or commits are padded.

Mitigation: Use the exploit watchlist and restrict activity to real, reviewable contributions that match published rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require glab, jq, curl, and a GITLAB_TOKEN for GitLab operations.]

## Skill Version(s):

1.86.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
