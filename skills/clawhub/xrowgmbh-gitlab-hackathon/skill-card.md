## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon participation, verify current rules, select qualifying issues and merge requests, and track scoring opportunities without spam or rule abuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to use a GitLab token for issues, merge requests, labels, comments, and closures.

Mitigation: Use a scoped GitLab token and review each proposed GitLab action before it is taken.

Risk: Hackathon scoring actions can become spammy or invalid if they do not follow current GitLab hackathon rules.

Mitigation: Verify current rules, dates, scoring, and prize requirements from the live GitLab contributors pages before acting.

## Reference(s):

- [GitLab Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab tooling context and may reference glab, jq, curl, and GITLAB_TOKEN for user-approved GitLab operations.]

## Skill Version(s):

1.91.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
