## Description:

Query Google Trends for interest-over-time, by-region, and related queries for a keyword, and pull real-time trending searches for a country as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, SEO researchers, and market-research agents use this skill to retrieve Google Trends interest, regional, related-query, and real-time trending-search data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends queries to Scavio as a third-party trends-data provider.

Mitigation: Use it only when Scavio's data-handling practices fit the task, and avoid submitting sensitive private terms unless that is acceptable.

Risk: The skill requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret manager and keep it out of source control.

Risk: Each API request consumes Scavio credits and may hit rate or usage limits.

Mitigation: Check expected usage before running repeated requests, monitor credit balance, and back off on rate-limit responses.

Risk: Google Trends values are relative indices, not absolute search counts.

Mitigation: Describe returned values as relative interest and do not fabricate or overstate trend data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-trends-api)
- [Scavio Google Trends documentation](https://scavio.dev/docs/google-trends?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-trends-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-trends-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio Google Trends endpoints and return only API-provided trend values, regions, and trending terms.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
