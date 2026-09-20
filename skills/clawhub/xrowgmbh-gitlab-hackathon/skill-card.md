## Description:

Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external contributors use this skill to plan fair GitLab hackathon participation, choose qualifying issues and merge requests, track scoring requirements, and avoid rule-abusive behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide GitLab CLI/API actions using a configured token, including comments, labels, issue closures, and merge requests.

Mitigation: Scope GITLAB_TOKEN to the intended projects and actions, and review proposed GitLab changes before allowing execution.

Risk: Hackathon scoring incentives can encourage spam comments, commit padding, incorrect labels, or invalid issue closures.

Mitigation: Follow the skill's fair-use guidance: prioritize real contributions, verify rules, avoid spam or padding, and document edge cases for maintainer clarification.

Risk: Hackathon dates, rules, prize requirements, and scoring values may change between events.

Mitigation: Re-check the official GitLab hackathon pages and current hackathon API before planning or executing contributions.

## Reference(s):

- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon)
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current)
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon)
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown]

**Output Format:** [Markdown guidance with inline shell and GitLab API command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI/API access through GITLAB_TOKEN and local glab, jq, and curl tools.]

## Skill Version(s):

1.93.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
