## Description:

Search Google Finance for stocks, indices, funds, currencies, or futures through the Dataify Scraper API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Google Finance data for stocks, indices, funds, currencies, or futures by submitting a finance query and optional output, language, time-window, and cache settings to Dataify. It is not intended for general web search or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Finance lookup queries and the Dataify API token are sent to Dataify's scraper API.

Mitigation: Use DATAIFY_API_TOKEN from the environment, never paste tokens into chat, and install only if this data flow is acceptable.

Risk: Broad requests or cache-bypassing requests can increase Dataify credit usage.

Mitigation: Review query scope and cache settings before high-volume or no-cache searches.

Risk: Finance data can be misread as personalized investment advice.

Mitigation: Present results as retrieved market data, preserve source links, and avoid giving personalized financial advice.

## Reference(s):

- [Dataify Google Finance API](references/google_finance_api.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-finance)
- [Dataify Scraper API Endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, shell commands, and raw JSON or HTML when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact user-facing finance results by default; preserves source links and distinguishes missing fields from empty values.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
