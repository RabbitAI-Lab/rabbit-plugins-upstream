## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon participation, select qualifying issues and merge requests, track scoring requirements, and avoid rule-abusive behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to use GitLab CLI or API workflows with a GitLab token.

Mitigation: Install only when that access is acceptable, scope the token appropriately, and review GitLab commands before execution.

Risk: User-directed activity can create, label, comment on, close issues, or open merge requests.

Mitigation: Review proposed GitLab mutations before they run and confirm they match project workflow and hackathon rules.

Risk: Hackathon rules, dates, scoring, and prize requirements can change.

Mitigation: Verify the live GitLab hackathon pages and current API before optimizing work or submitting entries.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab CLI and API commands that require user review before execution.]

## Skill Version(s):

1.84.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
