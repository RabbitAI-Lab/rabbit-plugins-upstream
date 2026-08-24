## Description:

Search Booking.com for a destination and stay with live nightly prices, pull one property in full with rooms and rate plans, and read guest reviews with the category breakdown. 3 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, travel researchers, and developers use this skill to search Booking.com stays, compare live prices and reviews, retrieve property details, and build hotel-rate research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party Booking.com data provider and requires SCAVIO_API_KEY.

Mitigation: Store the API key in an environment variable or secret manager and install only after accepting Scavio as the data provider.

Risk: Search, hotel, and review requests each spend API credits, including empty or failed calls.

Mitigation: Confirm destination, dates, currency, and filters before making calls, and avoid retry loops that can spend credits.

Risk: Live prices and availability can change, and omitted dates or currency can produce misleading quotes.

Mitigation: Send paired check-in and check-out dates plus currency, read echoed dates from responses, and timestamp quoted prices.

Risk: Bare hotel slugs can resolve against the wrong country and produce billed 404 responses.

Mitigation: Prefer chaining the Booking.com property URL returned by search instead of guessing country codes.

## Reference(s):

- [Scavio Booking Search Documentation](https://scavio.dev/docs/booking-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-booking)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-shaped API parameters and Python, JavaScript, and Bash snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live Booking.com property data returned through Scavio API calls; prices and availability should be timestamped.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
