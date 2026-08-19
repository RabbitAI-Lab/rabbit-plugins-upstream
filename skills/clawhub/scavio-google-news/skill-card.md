## Description:

Search Google News for headlines by keyword, topic, or publication as structured JSON, including headline, source, date, and link for current events, monitoring, and news research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, journalists, and agent builders use this skill to retrieve fresh Google News results for keywords, topics, companies, people, or publications. It supports current-events answers, monitoring, and news research when the agent has a Scavio API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends news search queries to Scavio and requires a Scavio API key.

Mitigation: Use only when sharing those queries with Scavio is acceptable, and provide the API key through the SCAVIO_API_KEY environment variable or an approved secret store.

Risk: Each API request consumes one credit.

Mitigation: Confirm broad pagination or repeated searches before running them, and monitor Scavio credit usage.

Risk: News answers may be misleading if an agent summarizes without grounding in returned results.

Mitigation: Return or cite the source and link from API results, and do not fabricate headlines, sources, dates, or links.

## Reference(s):

- [Scavio Google News documentation](https://scavio.dev/docs/google-news)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-news)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance, Code]

**Output Format:** [Structured JSON responses and concise Markdown guidance with optional code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each request costs 1 credit; supports query and Google News token parameters for localized or feed-based results.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
