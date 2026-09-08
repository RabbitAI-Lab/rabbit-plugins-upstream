## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan legitimate GitLab hackathon participation, select mergeable issues and merge requests, track scoring criteria, and avoid rule abuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using this skill with GITLAB_TOKEN may let an agent interact with the user's GitLab account.

Mitigation: Use a least-privilege token, keep it scoped appropriately, and review proposed issue, merge request, comment, label, and close actions before execution.

Risk: Hackathon rules, dates, eligibility criteria, and point values can change between events.

Mitigation: Verify the current GitLab hackathon pages and API before planning work or optimizing scoring.

Risk: Score optimization could encourage spam comments, padded commits, incorrect labels, or invalid issue closures if misused.

Mitigation: Limit activity to genuine contributions, correct labels, relevant comments, and maintainer-appropriate issue or merge request actions.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, curl, and a GitLab token for GitLab API operations.]

## Skill Version(s):

1.90.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
