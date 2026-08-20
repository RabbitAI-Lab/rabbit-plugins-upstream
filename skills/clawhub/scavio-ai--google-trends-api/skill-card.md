## Description:

Google Trends search-interest data as structured JSON: interest over time, interest by region (country, region, DMA or city), and related or rising queries and topics for a keyword, scoped by geo, date range and Google property, plus real-time trending searches per country.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to query Scavio for Google Trends interest over time, regional interest, related queries or topics, and real-time trending searches as structured JSON for research, SEO, market analysis, and demand-signal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trend queries, locations, dates, and filters are sent to Scavio with the configured SCAVIO_API_KEY.

Mitigation: Avoid putting secrets, personal data, or highly sensitive investigation terms into query parameters, and install only when this external API use is acceptable.

Risk: The skill consumes API credits and may hit rate or usage limits.

Mitigation: Check credits_remaining in responses, handle 429 responses by waiting before retrying, and account for the documented 1-credit cost per endpoint call.

Risk: Google Trends values are relative indices, so they can be misread as absolute search counts.

Mitigation: Describe trends value fields as relative 0-100 interest indices and do not fabricate interest values, regions, or trending terms.

## Reference(s):

- [Scavio Google Trends API Documentation](https://scavio.dev/docs/google-trends?utm_source=clawhub&utm_medium=skill&utm_campaign=google-trends-api)
- [Scavio API Homepage](https://scavio.dev/?utm_source=clawhub&utm_medium=skill&utm_campaign=google-trends-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=clawhub&utm_medium=skill&utm_campaign=google-trends-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-trends-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with API request examples and structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented endpoint costs 1 credit and returns cached/status metadata such as response_time, credits_used, credits_remaining, and cached.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
