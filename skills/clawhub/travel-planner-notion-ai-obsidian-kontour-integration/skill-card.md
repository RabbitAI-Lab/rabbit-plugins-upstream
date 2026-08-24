## Description:

Transform any AI agent into a world-class travel planner using Kontour AI's 9-dimension progressive planning model with structured conversation flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skylinehk](https://clawhub.ai/user/skylinehk)

### License/Terms of Use:

MIT-0

## Use Case:

External users, travel operators, and AI-agent builders use this skill to structure travel planning conversations, extract trip constraints, compare destinations, and produce provisional itineraries, summaries, and map exports from bundled offline references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated travel plans, public links, and KML exports may be mistaken for final, live-validated travel guidance.

Mitigation: Review generated routes, links, KML files, hours, transit, pricing, and availability before sharing or booking.

Risk: Booking-provider references describe planned integrations and may be interpreted as active booking capability.

Mitigation: Treat booking integration data as roadmap context only and use live provider systems for reservations.

Risk: The skill may redirect off-topic requests back toward travel planning instead of answering them directly.

Mitigation: Use the skill for travel-planning assistance and route medical, technical, legal, or other non-travel questions to appropriate tools or reviewers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/skylinehk/skills/travel-planner-notion-ai-obsidian-kontour-integration)
- [README](README.md)
- [destinations.json](references/destinations.json)
- [airports.json](references/airports.json)
- [airlines.json](references/airlines.json)
- [activities.json](references/activities.json)
- [budget-benchmarks.json](references/budget-benchmarks.json)
- [booking-integrations.json](references/booking-integrations.json)
- [embed-snippets.json](references/embed-snippets.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured JSON, Google Maps URLs, optional KML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated from offline reference data and should be validated before booking, sharing public links, or treating travel availability as final.]

## Skill Version(s):

2.0.36 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
