## Description: <br>
Searches and compares current travel inventory, prices, availability, and booking links for package tours, hotels, flights, and activities through a read-only travel MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[missial](https://clawhub.ai/user/missial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need an agent to query live travel search data and present concise options for tours, hotels, flights, activities, or destination lookup. It is intended for search and comparison, not booking or general itinerary planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel search criteria are sent to an external BotClaw travel MCP service and may include itinerary, dates, traveler counts, budget, and preferences. <br>
Mitigation: Avoid entering names, contacts, passport or payment details, credentials, or unnecessary sensitive data. <br>
Risk: Returned travel comparisons may be incomplete when a provider is unavailable or flight prices are cached. <br>
Mitigation: Treat results as search guidance, preserve partial results transparently, and refresh selected tour details before booking guidance. <br>
Risk: The skill searches and compares travel options but does not complete bookings or access private accounts. <br>
Mitigation: Keep booking actions outside the skill and use only links or details returned by the read-only service. <br>


## Reference(s): <br>
- [Travel Search CLI usage](references/usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/missial/skills/travel-search-ru) <br>
- [Travel MCP endpoint](https://mcp.botclaw.ru/travel) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and JSON command inputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Travel search criteria are sent to the external read-only MCP service; command invocations print one JSON document to stdout.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter, package.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
