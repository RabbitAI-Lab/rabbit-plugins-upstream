## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan fair, eligible contributions during GitLab hackathons. It helps them check current rules, choose reviewable issues, track qualifying work, and avoid score-seeking actions that would burden maintainers or violate event rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab account actions can be inaccurate or unfair if current event rules, issue status, or eligibility are misunderstood.

Mitigation: Verify the current rules and eligibility, then review each proposed issue, label, comment, merge request, or closure for accuracy and relevance before acting.

Risk: The GitLab CLI uses GITLAB_TOKEN for authenticated access, so exposing the token could expose the associated account permissions.

Mitigation: Keep GITLAB_TOKEN in a secure environment variable and do not include it in commands, logs, or shared output.

## Reference(s):

- [Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [Contribution Points Guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.151.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
