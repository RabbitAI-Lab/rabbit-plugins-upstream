## Description:

Search Booking.com for a destination and stay with live nightly prices, pull one property in full with rooms and rate plans, and read guest reviews with the category breakdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, travel researchers, and hospitality operators use this skill to search Booking.com properties, compare live nightly prices and review scores, retrieve property details, and inspect guest review breakdowns through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel search parameters and property URLs are sent to Scavio, and guest-review responses may include personal information.

Mitigation: Use a dedicated, revocable SCAVIO_API_KEY and avoid logging or re-sharing raw review records unless needed.

Risk: Live hotel prices and availability can change, and responses may reflect defaulted dates if dates are omitted.

Mitigation: Send explicit checkin, checkout, and currency values, read echoed stay dates before quoting prices, timestamp quotes, and include the property URL.

Risk: Each endpoint call consumes credits, including empty results and some error paths.

Mitigation: Validate destination or dest_id, paired dates, currency, and filters before calling, and chain the property URL returned by search instead of guessing slugs or country codes.

Risk: Optional SDK packages add dependency surface beyond the direct HTTPS examples.

Mitigation: Prefer direct HTTPS examples or install SDKs in an isolated environment when dependency risk matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/booking-com-hotel-data)
- [Scavio Booking Search API Documentation](https://scavio.dev/docs/booking-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=booking-com-hotel-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=booking-com-hotel-data)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown guidance with JSON API responses and Python, JavaScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and produces structured Booking.com hotel search, property, pricing, and review data through Scavio API calls.]

## Skill Version(s):

1.0.4 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
