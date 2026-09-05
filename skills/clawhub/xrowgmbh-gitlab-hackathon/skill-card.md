## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

External contributors and developer agents use this skill to plan legitimate GitLab hackathon participation, select qualifying issues and merge requests, track scoring rules, and avoid unfair or disallowed contribution patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide GitLab actions that affect public projects, including comments, labels, issue closures, and merge requests.

Mitigation: Keep actions user-directed, follow project rules, and review planned GitLab operations before execution.

Risk: A broad GitLab token could allow more access than the hackathon workflow requires.

Mitigation: Use a minimally scoped GitLab token and confirm the separate gitlab-agent skill before installing or using related GitLab operations.

Risk: Optimizing for hackathon points can create unfair contribution patterns such as spam comments, incorrect labels, invalid closures, or padded commits.

Mitigation: Apply the skill's fair-use guidance: prioritize real contributions, link only relevant issues, avoid spam, and document ambiguous edge cases for maintainer clarification.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)
- [xrowgmbh ClawHub Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide GitLab API and CLI actions that should remain user-directed and consistent with project rules.]

## Skill Version(s):

1.84.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
