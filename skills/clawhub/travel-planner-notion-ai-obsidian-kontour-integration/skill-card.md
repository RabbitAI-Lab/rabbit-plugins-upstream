## Description:

Transform any AI agent into a world-class travel planner using Kontour AI's 9-dimension progressive planning model with structured conversation flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skylinehk](https://clawhub.ai/user/skylinehk)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to turn natural-language travel requests into structured trip planning context, itinerary scaffolds, budget guidance, route exports, and copy-ready traveler-facing planning summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated map exports can contain a fixed Kontour promotional link even though public planning links are expected to be operator-approved.

Mitigation: Review generated Google Maps and KML output before sharing, and remove or replace the fixed Kontour link unless it has been approved for the deployment context.

Risk: Booking integrations are represented as roadmap/reference data and should not be treated as live booking support.

Mitigation: Use the booking integration data only as planning structure unless a current, approved integration status and provider connection are supplied separately.

Risk: Offline reference data cannot prove current hours, prices, route timing, weather, availability, or booking viability.

Mitigation: Validate live travel details before presenting a plan as final or booking-ready.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/skylinehk/skills/travel-planner-notion-ai-obsidian-kontour-integration)
- [Destinations Reference Data](references/destinations.json)
- [Airports Reference Data](references/airports.json)
- [Airlines Reference Data](references/airlines.json)
- [Activities Reference Data](references/activities.json)
- [Budget Benchmarks](references/budget-benchmarks.json)
- [Booking Integrations Roadmap](references/booking-integrations.json)
- [Embed Snippets](references/embed-snippets.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured JSON and Markdown with optional shell command usage for local planning and map export scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce trip context JSON, itinerary scaffolds, budget breakdowns, Google Maps links, KML exports, operator review packets, and traveler-facing draft responses.]

## Skill Version(s):

2.0.41 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
