## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and contribution teams use this skill to plan rule-compliant GitLab hackathon work, select mergeable issues and merge requests, track scoring requirements, and avoid exploit-like behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token with broader permissions than needed could expose unnecessary account or project capabilities.

Mitigation: Use a GitLab token scoped only to the contribution and review actions required for the hackathon workflow.

Risk: Labels, issue closures, comments, or merge requests can affect public projects if applied incorrectly.

Mitigation: Review each proposed public GitLab action against the current hackathon rules and project workflow before executing it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [GitLab Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference GitLab CLI, curl, jq, and GITLAB_TOKEN for user-authorized GitLab operations.]

## Skill Version(s):

1.82.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
