## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon participation, select qualifying issues and merge requests, track scoring opportunities, and avoid exploit-like behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token with broad permissions could allow unintended issue, merge request, label, or comment actions.

Mitigation: Use a GitLab token scoped only to the projects and permissions needed for the intended hackathon work.

Risk: Hackathon dates, eligibility requirements, scoring values, and prize rules can change between runs.

Mitigation: Verify the live GitLab hackathon pages and current hackathon API before using scoring or qualification guidance.

Risk: Point optimization can drift into spam comments, incorrect labels, invalid closures, or other unfair participation.

Mitigation: Use the skill only for genuine, reviewable contributions that follow published rules and maintainer workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [References GitLab CLI, jq, curl, and the GITLAB_TOKEN environment variable.]

## Skill Version(s):

1.80.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
