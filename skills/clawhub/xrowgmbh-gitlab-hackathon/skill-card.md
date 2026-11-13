## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers participating in GitLab hackathons use this skill to plan fair contributions, find reviewable issues, track eligibility and scoring, and avoid rule-abusing tactics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab CLI and API actions can create or update issues and merge requests on the user's account.

Mitigation: Confirm the target project, current hackathon rules, and intended changes before running write operations; use a minimally scoped token.

Risk: Hackathon dates, eligibility rules, and scoring criteria can change between events.

Mitigation: Recheck the current official hackathon pages and API before planning or acting.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points Guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands, API calls]

**Output Format:** [Markdown plans, checklists, and recommendations with inline shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may operate on a GitLab account using GITLAB_TOKEN.]

## Skill Version(s):

1.141.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
