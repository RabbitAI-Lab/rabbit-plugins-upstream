## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon participation, verify current rules and dates, select mergeable issues or merge requests, and track scoring opportunities without spam or rule abuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this skill may use a GitLab token to inspect or act on GitLab issues and merge requests.

Mitigation: Use a least-privilege token and confirm target projects and hackathon rules before allowing GitLab operations.

Risk: Mutating GitLab actions such as labeling, commenting, closing issues, or opening merge requests can affect live projects.

Mitigation: Require explicit approval for mutating actions and verify that each action is valid for the selected project and event.

Risk: Hackathon scoring optimization can become spam or rule abuse if comments, labels, commits, or closures are padded for points.

Mitigation: Follow published event rules, prioritize real contributions, and avoid comments, labels, commits, or closures that do not move work forward.

## Reference(s):

- [ClawHub GitLab Hackathon Skill](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab tooling and a configured GITLAB_TOKEN for GitLab operations.]

## Skill Version(s):

1.84.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
