## Description:

Resolve a ticker to a CIK, then pull SEC EDGAR filer profiles, filings, XBRL financial concepts and full-text search across 2001-today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to retrieve structured public SEC EDGAR company, filing, XBRL, and full-text search data through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC lookup terms and the Scavio API key are sent to Scavio when the agent makes API calls.

Mitigation: Keep SCAVIO_API_KEY in environment or secret storage and avoid placing it in source code, logs, prompts, or shared transcripts.

Risk: API usage may consume free credits or paid balance.

Mitigation: Confirm the intended query scope before running broad searches or paginated filing retrieval, and monitor credits remaining in API responses.

Risk: Financial figures or filing search results may be incomplete if the agent uses the wrong CIK, guesses an XBRL concept, or relies on default pagination.

Mitigation: Resolve tickers to CIKs first, discover valid XBRL concepts through the facts endpoint, cite filing sources for reported figures, and use documented pagination or history options when completeness matters.

## Reference(s):

- [Scavio SEC EDGAR API Documentation](https://scavio.dev/docs/sec-edgar-lookup?utm_source=agent-skills&utm_medium=skill&utm_campaign=sec-edgar-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=sec-edgar-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/sec-edgar-api)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with API request examples and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to make authenticated Scavio API calls that return structured JSON.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
