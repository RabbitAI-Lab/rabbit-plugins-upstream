## Description:

Search Booking.com for a destination and stay with live nightly prices, pull one property in full with rooms and rate plans, and read guest reviews with the category breakdown. 3 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel operations teams use this skill to search Booking.com properties for specific stays, compare live prices and ratings, inspect one property in detail, and retrieve guest review summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel search details are sent to Scavio when the skill calls the Booking.com endpoints.

Mitigation: Use the skill only when sending those travel details to Scavio is acceptable for the user or organization.

Risk: Each Booking.com endpoint call spends Scavio credits, including empty or failed lookups.

Mitigation: Confirm required parameters before calling endpoints, chain hotel URLs from search results, and avoid brute-force retries.

Risk: Live rates and availability can change after a response is returned.

Mitigation: Include the stay dates, currency, timestamp context, and property URL so users can verify current pricing before booking.

Risk: The SCAVIO_API_KEY grants access to paid API calls.

Mitigation: Keep the API key private, load it from the environment, and do not echo or persist it in outputs.

## Reference(s):

- [Scavio Booking Search Documentation](https://scavio.dev/docs/booking-search)
- [Scavio Rate Limits Documentation](https://scavio.dev/docs/rate-limits)
- [Scavio Booking Skill on ClawHub](https://clawhub.ai/scavio-ai/skills/scavio-booking)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON request and response examples plus inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to return structured JSON from Scavio Booking.com endpoints and to include dates, currency, property URLs, and live-price caveats when quoting results.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
