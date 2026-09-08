## Description:

Search Google Flights for fares and itineraries through Dataify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to convert flight-search requests into Dataify Google Flights parameters, execute searches with a Dataify API token, and present concise fare and itinerary results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight-search details are sent to Dataify when the skill executes a search.

Mitigation: Use the skill only when sharing the requested route, dates, passenger counts, and filters with Dataify is acceptable.

Risk: A Dataify API token is required and could be exposed if pasted into chat or logs.

Mitigation: Store the token in a session-scoped DATAIFY_API_TOKEN environment variable and never print or paste the token value.

Risk: Deep search, cache bypass, high-volume, or multi-page searches can consume extra Dataify credits.

Mitigation: Review cost-affecting options before execution and keep default cached, single-search behavior unless broader collection is needed.

## Reference(s):

- [Dataify Google Flights API Reference](references/google_flights_api.md)
- [Dataify Google Flights skill page](https://clawhub.ai/dataify-server/skills/dataify-google-flights)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, configuration guidance]

**Output Format:** [Markdown tables and concise text, with optional raw JSON or HTML when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns compact user-facing results by default and preserves source links when available.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
