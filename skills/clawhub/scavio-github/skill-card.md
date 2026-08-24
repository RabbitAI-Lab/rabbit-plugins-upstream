## Description:

Pull GitHub profiles, repositories, READMEs, releases, issues and comments, GitHub search results, and composite intelligence from Scavio's GitHub API as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public GitHub profiles, repository metadata, READMEs, releases, issues, comments, searches, and composite repository or user intelligence through Scavio. It is suited for public open-source research, repository triage, contributor analysis, and structured GitHub data lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends GitHub usernames, repository names, issue URLs, and search queries to Scavio.

Mitigation: Use it only when users are comfortable sending those public GitHub lookup inputs to Scavio, and avoid submitting private or sensitive data as query text.

Risk: The public commit email endpoint can return personal data.

Mitigation: Use public commit email results responsibly, avoid profiling individuals, and return only data provided by the API.

Risk: Composite and intelligence endpoints consume more credits than basic lookups.

Mitigation: Check endpoint credit costs before loops or batch workflows, and monitor credits_used and credits_remaining in each response.

## Reference(s):

- [Scavio GitHub API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-github)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; responses include data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
