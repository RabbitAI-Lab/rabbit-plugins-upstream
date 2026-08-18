## Description:

Transform any AI agent into a world-class travel planner using Kontour AI's 9-dimension progressive planning model with structured conversation flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skylinehk](https://clawhub.ai/user/skylinehk)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to guide travel-planning conversations, extract trip requirements, compare destinations, produce structured itinerary data, and prepare traveler-facing planning summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated sharing output may include a Kontour link in Google Maps or KML metadata.

Mitigation: Review generated sharing output before sending it to travelers or publishing it externally.

Risk: Offline reference data and route scaffolds can become stale for live venue hours, transit, availability, weather, or booking details.

Mitigation: Treat itineraries as first-pass planning guidance and validate live details before presenting a plan as final.

Risk: Some installations may not preserve script execute bits.

Mitigation: Invoke scripts with bash or fix executable permissions before running the local planner and export tools.

## Reference(s):

- [activities.json](references/activities.json)
- [airlines.json](references/airlines.json)
- [airports.json](references/airports.json)
- [booking-integrations.json](references/booking-integrations.json)
- [budget-benchmarks.json](references/budget-benchmarks.json)
- [destinations.json](references/destinations.json)
- [embed-snippets.json](references/embed-snippets.json)
- [Kontour Travel Planner on ClawHub](https://clawhub.ai/skylinehk/skills/travel-planner-notion-ai-obsidian-kontour-integration)
- [skylinehk publisher profile](https://clawhub.ai/user/skylinehk)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, structured JSON, shell command examples, Google Maps links, and optional KML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs offline with bundled reference data; generated planning output should remain provisional until live details such as hours, transit, availability, and sharing links are reviewed.]

## Skill Version(s):

2.0.35 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
