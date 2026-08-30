## Description:

Pull GitHub profiles, repos, READMEs, releases, issues and comments, run GitHub search, and get composite intelligence - a repo dossier, a user's activity velocity, reaction-ranked top issues, and public commit emails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public GitHub profiles, repositories, READMEs, releases, issues, comments, search results, and composite repository or user activity intelligence through Scavio's structured JSON API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and consumes Scavio credits for successful API calls.

Mitigation: Configure SCAVIO_API_KEY through a secret store or environment variable, review endpoint credit costs before loops or batch use, and monitor credits_used and credits_remaining in responses.

Risk: Queries and public GitHub identifiers are sent to Scavio.

Mitigation: Use the skill only for intended public GitHub lookups and avoid sending sensitive, private, or unnecessary identifiers.

Risk: The public commit email endpoint can return personal data.

Mitigation: Use the email endpoint only for legitimate, user-directed purposes and avoid profiling individuals or retaining personal data beyond the task need.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/github-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with code examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses include data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
