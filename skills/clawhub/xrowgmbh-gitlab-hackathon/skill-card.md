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

Risk: A GitLab token with broad scopes could expose more repository access than the contribution workflow needs.

Mitigation: Use a GitLab token with only the scopes needed for the intended hackathon workflow and rotate or revoke it after use.

Risk: Optimizing for points can lead to spam comments, invalid labels, invalid closures, or other unfair participation patterns.

Mitigation: Follow the skill's fair-use guidance: make real contributions, label or close issues only when valid, and avoid exploit-like behavior unless maintainers explicitly approve it.

Risk: Hackathon dates, eligibility rules, scoring values, and prize requirements can change between releases.

Mitigation: Verify the live GitLab hackathon pages and current hackathon API before acting on scoring or eligibility guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [GitLab Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, curl, and a GitLab token for GitLab operations.]

## Skill Version(s):

1.84.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
