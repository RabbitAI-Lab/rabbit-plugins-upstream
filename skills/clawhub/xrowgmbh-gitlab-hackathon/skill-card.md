## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

External contributors and developers use this skill to plan fair GitLab hackathon participation, select qualifying issues and merge requests, verify scoring requirements, and avoid rule abuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide GitLab CLI/API activity through GITLAB_TOKEN, which may affect comments, labels, issue closures, or merge requests.

Mitigation: Use the least-privileged practical GitLab token and review any proposed comments, labels, closures, or merge requests before posting.

Risk: Hackathon optimization can drift into spammy or unfair activity if scoring levers are pursued without review.

Mitigation: Verify current rules before each event and avoid padded commits, spam comments, incorrect labels, invalid closures, or placeholder submissions.

Risk: The skill references a separate gitlab-agent skill for GitLab operations.

Mitigation: Inspect the referenced gitlab-agent skill separately before relying on it for repository or API actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon)
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab contribution points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on GitLab CLI/API access through GITLAB_TOKEN when executing GitLab operations.]

## Skill Version(s):

1.91.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
