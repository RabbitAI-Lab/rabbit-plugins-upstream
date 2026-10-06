## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab hackathon participants use this skill to plan eligible contributions, select reviewable issues and merge requests, and check scoring and prize requirements while avoiding rule abuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token could grant the agent access beyond the intended hackathon projects.

Mitigation: Use a token limited to the minimum scopes and projects needed.

Risk: Incorrect labels, issue closures, comments, or merge requests can affect public project state.

Mitigation: Review proposed changes before posting and confirm they are justified by project rules.

Risk: Outdated event dates, scoring rules, or prize requirements may cause ineligible work.

Mitigation: Check current official hackathon pages and contribution rules before acting.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points Guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)
- [GitLab Hackathon Skill on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Campaign briefs, contribution plans, and exploit watchlists should be checked against current event rules.]

## Skill Version(s):

1.102.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
