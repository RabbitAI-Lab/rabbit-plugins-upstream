## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and contributors use this skill to plan fair GitLab hackathon participation, verify current event rules, select reviewable issues and merge requests, and track scoring without abusing contribution mechanics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to use GitLab tooling with a GitLab token.

Mitigation: Use a least-privilege token and review proposed issue labels, closures, comments, and merge requests before submission.

Risk: Hackathon scoring incentives can encourage low-quality or abusive contribution behavior.

Mitigation: Follow the skill's fair-use guidance: avoid spam comments, commit padding, incorrect labels, invalid closures, and placeholder submissions.

Risk: Hackathon rules, dates, scoring, and prize requirements can change.

Mitigation: Verify current GitLab hackathon pages and APIs before planning or executing work.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [GitLab Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on GitLab CLI access, jq, curl, and a GitLab token for live GitLab operations.]

## Skill Version(s):

1.79.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
