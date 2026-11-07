## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to plan fair participation in GitLab hackathons, identify reviewable contributions, understand scoring and eligibility rules, and track rule edge cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab actions use an access token and can create public contributions or close issues.

Mitigation: Limit the token to intended projects and permissions, and review public contributions and issue closures.

Risk: GitLab operations depend on the separately required gitlab-agent skill, which is outside this artifact's security review.

Mitigation: Inspect the gitlab-agent skill before use.

## Reference(s):

- [Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [Contribution Points Guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, API calls]

**Output Format:** [Markdown with prose, checklists, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event rules, dates, eligibility, and scoring values should be checked against current GitLab sources.]

## Skill Version(s):

1.130.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
