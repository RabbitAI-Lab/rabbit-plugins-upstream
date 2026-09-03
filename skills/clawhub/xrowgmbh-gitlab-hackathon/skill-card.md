## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and contributors use this skill to plan fair GitLab hackathon participation, choose qualifying issues and merge requests, track scoring requirements, and avoid rule-abusive behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab token permissions could grant broader account access than needed for hackathon planning.

Mitigation: Review token scopes before use, keep GitLab actions user-directed, and revoke or rotate the token when it is no longer needed.

Risk: Optimizing for hackathon scoring can lead to spam comments, invalid labels, invalid issue closures, or point-padding behavior.

Mitigation: Follow the skill's fair-use guidance: make real contributions, link only relevant issues, use labels and closures only when correct, and avoid padding commits or comments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [GitLab current hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference GitLab CLI, jq, curl, and a user-provided GitLab token for user-directed GitLab operations.]

## Skill Version(s):

1.84.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
