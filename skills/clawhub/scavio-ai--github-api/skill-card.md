## Description:

Pull GitHub profiles, repos, READMEs, releases, issues and comments, run GitHub search, and get composite intelligence - a repo dossier, a user's activity velocity, reaction-ranked top issues, and public commit emails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured GitHub data through Scavio, including profiles, repositories, README content, releases, issues, search results, repository dossiers, activity velocity, and public commit emails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub queries, usernames, and repository targets are sent to Scavio.

Mitigation: Avoid sending confidential targets or sensitive investigative context unless disclosure to Scavio is acceptable.

Risk: Some endpoints consume multiple account credits, and automated loops can spend credits quickly.

Mitigation: Check endpoint costs before repeated calls, monitor credits_used and credits_remaining, and avoid broad loops unless intended.

Risk: The public email endpoint can return personal data from public commits.

Mitigation: Use public commit email results only for appropriate purposes and avoid building profiles of individuals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/github-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses include data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
