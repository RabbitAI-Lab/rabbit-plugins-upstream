## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and contributors use this skill to plan fair GitLab hackathon participation, select reviewable issues and merge requests, track scoring requirements, and avoid exploit-like behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested GitLab actions could apply inaccurate labels, closures, comments, or submissions.

Mitigation: Review each action against the current event rules and project workflow before running it.

Risk: GitLab API operations may use a token with broader access than needed.

Mitigation: Use a least-privilege GitLab token and avoid storing or exposing it in skill outputs.

Risk: Hackathon dates, scoring, and prize requirements may change between releases.

Mitigation: Verify the live GitLab hackathon pages and current hackathon API before optimizing work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, curl, and a GITLAB_TOKEN for GitLab API operations.]

## Skill Version(s):

1.81.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
