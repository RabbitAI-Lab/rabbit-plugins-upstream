## Description:

Queries Google Trends via Scavio for keyword interest over time, regional interest, related queries, and real-time country trends as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, SEO practitioners, and agents use this skill to retrieve structured Google Trends data for market research, keyword research, regional interest analysis, and current trending searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trend queries are sent to Scavio's external API using the user's SCAVIO_API_KEY.

Mitigation: Confirm the user is comfortable sending the query to Scavio before making API calls, and keep the API key in environment or secret storage.

Risk: Each request consumes one Scavio credit.

Mitigation: Tell the user before making repeated or broad requests and avoid unnecessary retries.

Risk: Google Trends values are relative indices and trending results depend on the selected geography and time window.

Mitigation: Report returned values as relative interest and include the requested geo, date, hours, and data_type context in summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-trends)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)
- [Scavio Google Trends documentation](https://scavio.dev/docs/google-trends)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [Scavio API](https://api.scavio.dev)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON response structures and inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; external API calls consume one Scavio credit per request.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
