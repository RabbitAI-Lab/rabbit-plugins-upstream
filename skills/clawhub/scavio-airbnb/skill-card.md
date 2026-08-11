## Description:

Search Airbnb stays with the full discount ledger, pull one listing with its complete amenity list and rating breakdown, and page through real review bodies. 3 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and compare Airbnb stays, fetch detailed listing amenities and rating breakdowns, and page through guest review bodies for travel research, listing comparison, short-term-rental market research, comp sets, and host analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and each Airbnb API request spends one credit.

Mitigation: Confirm SCAVIO_API_KEY is set and that the user accepts the one-credit-per-request cost before making calls.

Risk: Host profiles and review bodies may contain personal data about real people.

Mitigation: Use the data for listing comparison or travel research, summarize review text, and avoid profiling individuals.

Risk: Airbnb prices can be misleading when dates or currency are omitted because defaulted windows and proxy-dependent currency behavior can change returned prices.

Mitigation: Send explicit check-in and check-out dates plus currency, and check dates_are_defaulted before quoting prices for a dated request.

## Reference(s):

- [Scavio Airbnb Search Documentation](https://scavio.dev/docs/airbnb-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [Scavio Airbnb Skill on ClawHub](https://clawhub.ai/scavio-ai/skills/scavio-airbnb)
- [scavio-ai Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code examples for JSON API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use structured JSON envelopes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
