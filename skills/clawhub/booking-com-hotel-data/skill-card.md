## Description:

Search Booking.com for a destination and stay with live nightly prices, pull one property in full with rooms and rate plans, and read guest reviews with the category breakdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, travel operations teams, and agents use this skill to search Booking.com stays, compare live property prices and ratings, inspect hotel details, and retrieve guest review breakdowns through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each API call spends a Scavio credit, including calls that return empty or failed results.

Mitigation: Validate required parameters such as destination, dates, currency, and hotel URL before making requests.

Risk: Travel query details are sent to Scavio and live prices or availability can change before booking.

Mitigation: Share only appropriate query details with the API and verify current prices, dates, currency, and property URLs before acting on results.

Risk: SCAVIO_API_KEY is required for access.

Mitigation: Store the key in an environment variable or secret store and keep it out of source code.

## Reference(s):

- [Scavio Booking Search Documentation](https://scavio.dev/docs/booking-search)
- [Scavio](https://scavio.dev/?utm_source=clawhub&utm_medium=skill&utm_campaign=scavio-booking)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown with JSON request and response examples, Python and JavaScript code examples, and shell setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and returns structured JSON from Scavio API endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
