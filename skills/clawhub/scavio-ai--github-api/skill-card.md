## Description:

Pull GitHub profiles, repos, READMEs, releases, issues and comments, run GitHub search, and get composite intelligence - a repo dossier, a user's activity velocity, reaction-ranked top issues, and public commit emails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured GitHub profile, repository, issue, release, search, activity, and public commit email data through Scavio API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub targets, search queries, and handles are sent to Scavio under the user's Scavio account.

Mitigation: Use the skill only when the requested GitHub lookup data is appropriate to share with Scavio.

Risk: The public commit email and profile-velocity endpoints can expose or aggregate personal data.

Mitigation: Use those endpoints only for legitimate public GitHub analysis, avoid profiling individuals, and handle returned personal data responsibly.

Risk: Repeated calls and composite endpoints can consume Scavio credits.

Mitigation: Check endpoint costs before loops and monitor the credits_used and credits_remaining fields returned by the API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/github-api)
- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell, Python, and JSON examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Served API responses include credits_used and credits_remaining fields.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
