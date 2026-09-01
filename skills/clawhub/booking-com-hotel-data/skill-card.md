## Description:

Search Booking.com for a destination and stay with live nightly prices, pull one property in full with rooms and rate plans, and read guest reviews with the category breakdown. 3 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-data teams use this skill to search Booking.com stays, compare live prices and review scores, inspect one property in detail, and retrieve guest review summaries for rate-shopping or travel-research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for live Booking.com data.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store, and avoid placing the key in source files, prompts, logs, or shared outputs.

Risk: Each endpoint call spends API credits, including calls that return empty or error responses.

Mitigation: Confirm destination, date range, currency, and filters before calling the API; use search-returned property URLs for hotel and review calls instead of guessing property slugs.

Risk: Live prices and availability can change, and defaulted dates or currencies can make quoted prices misleading.

Mitigation: Read echoed checkin, checkout, nights, currency, price fields, and property URLs from the response before presenting results, and timestamp live quotes.

## Reference(s):

- [Scavio Booking Search Documentation](https://scavio.dev/docs/booking-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/booking-com-hotel-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands, code examples, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Booking.com endpoints cost 1 credit per request and return live data that should be checked against echoed dates, currency, and property URLs.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
