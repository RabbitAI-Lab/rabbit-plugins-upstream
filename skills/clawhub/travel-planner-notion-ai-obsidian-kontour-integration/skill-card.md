## Description: <br>
Transform any AI agent into a world-class travel planner using Kontour AI's 9-dimension progressive planning model with structured conversation flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skylinehk](https://clawhub.ai/user/skylinehk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel agents, operators, and AI agents use this skill to capture traveler constraints, compare destinations, generate structured itineraries and budget guidance, and prepare map or sharing outputs from bundled offline travel reference data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Offline reference data may not reflect current prices, opening hours, availability, visa rules, or travel restrictions. <br>
Mitigation: Validate live prices, hours, availability, visa requirements, and travel rules before relying on or booking an itinerary. <br>
Risk: Generated Google Maps or Kontour links may open external websites when clicked. <br>
Mitigation: Review generated links before sharing and use only operator-approved public planning links in final traveler-facing output. <br>
Risk: Booking provider entries are roadmap/reference data rather than active integrations. <br>
Mitigation: Treat booking-ready outputs as drafts and confirm searches, reservations, and payments through live provider systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/skylinehk/skills/travel-planner-notion-ai-obsidian-kontour-integration) <br>
- [Destination reference data](references/destinations.json) <br>
- [Airport reference data](references/airports.json) <br>
- [Activity reference data](references/activities.json) <br>
- [Budget benchmarks](references/budget-benchmarks.json) <br>
- [Booking integration roadmap](references/booking-integrations.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, structured JSON, Google Maps URLs, optional KML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs offline with bundled reference data; generated plans should be validated against current travel facts before final use.] <br>

## Skill Version(s): <br>
2.0.34 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
