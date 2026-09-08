## Description:

Pull GitHub profiles, repos, READMEs, releases, issues and comments, run GitHub search, and get composite intelligence - a repo dossier, a user's activity velocity, reaction-ranked top issues, and public commit emails. 13 endpoints, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query GitHub profiles, repositories, READMEs, releases, issues, comments, search results, activity velocity, repo dossiers, and public commit email signals through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends GitHub handles, repository names, search queries, issue URLs, and related request data to Scavio.

Mitigation: Install and use it only when third-party API processing by Scavio is acceptable for the intended workflow.

Risk: The public commit email endpoint can return personal data.

Mitigation: Use returned email addresses only for legitimate, responsible purposes and avoid building unnecessary profiles of individuals.

Risk: Several endpoints consume more than one credit per successful request.

Mitigation: Check endpoint credit costs before loops or broad searches and monitor credits_used and credits_remaining in responses.

## Reference(s):

- [Scavio GitHub API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)
- [Scavio API rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=github-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Some endpoints are metered at higher credit costs and public feed activity is capped at 300 events over 90 days.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
