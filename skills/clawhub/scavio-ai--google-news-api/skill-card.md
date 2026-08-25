## Description:

Searches Google News for headlines by keyword, topic, or publication and returns structured JSON with headline, source, date, and link for current events, monitoring, and news research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, journalists, and agents use this skill to retrieve current Google News headlines for topics, entities, sections, or publishers through Scavio, then summarize or monitor results with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to Scavio as a third-party news API and depends on a SCAVIO_API_KEY.

Mitigation: Confirm third-party API use is acceptable, store SCAVIO_API_KEY in the environment or a secret store, and avoid placing the key directly in source files.

Risk: Each API call spends one Scavio credit, so broad pagination or repeated monitoring can consume credits quickly.

Mitigation: Inform the user before wide pagination, scope queries narrowly, and watch for rate or usage limit responses.

Risk: Current-events answers can be misleading if headlines, sources, dates, or links are fabricated or summarized without citation.

Mitigation: Return only API-provided data, cite source links when summarizing news, and avoid answering time-sensitive news questions from model memory.

Risk: Invalid parameters, missing credentials, rate limits, or upstream outages can cause failed requests.

Mitigation: Validate that one query or token parameter is present, check SCAVIO_API_KEY on authentication errors, wait on rate or upstream errors, and broaden the query when no results are returned.

## Reference(s):

- [Scavio Google News API documentation](https://scavio.dev/docs/google-news)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-news-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured JSON returned from the Scavio API, with Markdown guidance and code examples for setup and use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each request costs one credit; configured timeout is 90 seconds and throttle is 1.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
