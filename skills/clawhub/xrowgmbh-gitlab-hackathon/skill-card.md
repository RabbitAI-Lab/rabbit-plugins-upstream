## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

External developers use this skill to plan fair participation in GitLab hackathons, choose reviewable contributions, and track eligibility and scoring requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token with broad permissions could expose projects beyond the intended hackathon work.

Mitigation: Use a token limited to the intended projects and necessary permissions.

Risk: The workflow directs users to a separate gitlab-agent skill that was outside the available security evidence.

Mitigation: Assess that skill before using it for GitLab operations.

## Reference(s):

- [Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [Contribution Points Guide](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, API calls]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on current event rules, eligibility, project permissions, and deadlines.]

## Skill Version(s):

1.127.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
