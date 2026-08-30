## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and contributors use this skill to plan fair GitLab hackathon participation, select reviewable issues and merge requests, verify scoring requirements, and avoid rule-abuse edge cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token could grant more access than needed for hackathon planning and contribution work.

Mitigation: Use a GitLab token with the minimum permissions needed and avoid sharing production or broadly scoped credentials.

Risk: Proposed issue, merge request, label, comment, or closure actions could be incorrect or unfair under event rules.

Mitigation: Review proposed GitLab actions before allowing them and verify current hackathon rules, dates, scoring, and eligibility requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [GitLab current hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require GitLab CLI/API access through GITLAB_TOKEN.]

## Skill Version(s):

1.84.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
