## Description:

Build event shortlists, dated calendars, and venue comparisons through Crawlora's Ticketmaster and TicketWeb endpoints. Use for public event research with verified venue identity, timing, age restrictions, ticket fees, and availability caveats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public events, compare venues, and produce dated shortlists or calendars with venue identity, local timing, status, age/access notes, ticket pricing scope, availability caveats, and fit rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-chosen event search parameters to Crawlora's API using a Crawlora API key.

Mitigation: Use it for public event research, keep the key in the environment, and avoid passing private notes or unrelated sensitive data in query or body values.

Risk: The bundled shell helper executes API calls through curl.

Mitigation: Review the shell script before installation in environments that restrict shell execution.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/event-venue-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown table or calendar with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event and provider IDs, canonical links, venue/address, local start time and zone, status, age/access information, ticket price scope, availability, and fit rationale.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
