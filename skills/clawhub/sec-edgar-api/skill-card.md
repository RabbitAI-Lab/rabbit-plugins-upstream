## Description:

Resolve a ticker to a CIK, then pull SEC EDGAR filer profiles, filings, XBRL financial concepts and full-text search across 2001-today. 6 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to resolve public-company identifiers and retrieve SEC EDGAR profiles, filings, XBRL facts, XBRL concept history, and full-text filing search results through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC lookup requests and the Scavio API key are sent to Scavio.

Mitigation: Use this skill only when that data sharing is acceptable, load SCAVIO_API_KEY from a secret store or environment variable, and keep it out of source control.

Risk: API calls consume account credits.

Mitigation: Check credit balance and endpoint cost expectations before high-volume lookups or filing searches.

Risk: Returned filing data may be incomplete if queries are too narrow, pagination is ignored, or EDGAR search coverage limits apply.

Mitigation: Use the documented pagination controls, include historical filings when needed, and report source filing context for extracted figures.

## Reference(s):

- [Scavio SEC EDGAR Lookup Documentation](https://scavio.dev/docs/sec-edgar-lookup?utm_source=agent-skills&utm_medium=skill&utm_campaign=sec-edgar-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=sec-edgar-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/sec-edgar-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API request and SDK code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured SEC EDGAR data through Scavio endpoints; requests consume account credits.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
