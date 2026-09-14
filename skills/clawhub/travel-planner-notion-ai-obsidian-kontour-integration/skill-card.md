## Description:

Transform any AI agent into a world-class travel planner using Kontour AI's 9-dimension progressive planning model with structured conversation flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skylinehk](https://clawhub.ai/user/skylinehk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn traveler requests into structured trip plans, destination comparisons, itinerary scaffolds, budget guidance, and operator-ready follow-up prompts using bundled travel reference data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated map or KML exports may include a hard-coded Kontour URL despite the approved-link policy.

Mitigation: Review exported artifacts before sharing and replace or remove links unless the current publishing context explicitly approves them.

Risk: The optional review helper may be unsuitable for shared machines until its temporary-file handling is hardened.

Mitigation: Run optional review helpers only in isolated workspaces, or skip them on shared machines until the helper is reviewed.

Risk: Offline reference data can be stale for live travel decisions such as hours, prices, weather, transit, and entry requirements.

Mitigation: Validate current operational details before presenting a final itinerary or booking-ready recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skylinehk/skills/travel-planner-notion-ai-obsidian-kontour-integration)
- [README.md](README.md)
- [destinations.json](references/destinations.json)
- [airports.json](references/airports.json)
- [airlines.json](references/airlines.json)
- [activities.json](references/activities.json)
- [budget-benchmarks.json](references/budget-benchmarks.json)
- [booking-integrations.json](references/booking-integrations.json)
- [embed-snippets.json](references/embed-snippets.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON and Markdown with optional shell command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce trip context JSON, destination comparisons, itinerary scaffolds, budget breakdowns, Google Maps links, KML exports, and operator-ready presentation or follow-up text.]

## Skill Version(s):

2.0.39 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
