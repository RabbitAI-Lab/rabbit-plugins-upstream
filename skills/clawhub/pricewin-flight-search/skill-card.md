## Description: <br>
Search live flight fares for a route and date across Agoda, Trip.com, and Traveloka, supporting one-way and round-trip comparisons with airline, timing, stop, duration, price, and booking-link details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare live flight fares for specific routes, dates, passenger counts, and cabin classes. It guides agents to call PriceWin's hosted MCP flight tools, poll for results, and present concise fare summaries without booking or payment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer persistently registers PriceWin's hosted MCP server across multiple local AI agents. <br>
Mitigation: Run `bash install.sh --dry-run` first, review the agent config files that would change, and consider manually registering the server only for the intended agent. <br>
Risk: Travel route, date, passenger-count, cabin, and session queries are sent to PriceWin's hosted service. <br>
Mitigation: Use the skill only when that hosted-service data flow is acceptable, and avoid sending passenger names, payment details, credentials, files, or unrelated personal data. <br>
Risk: The skill returns fare comparisons and provider links but cannot complete bookings or payments. <br>
Mitigation: Treat fares as indicative and re-check all price and booking details on the airline or OTA site before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cotghw/skills/pricewin-flight-search) <br>
- [PriceWin skills homepage](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [Flight Search Tool Reference](artifact/reference.md) <br>
- [Security and Data Handling](artifact/SECURITY.md) <br>
- [PriceWin privacy policy](https://price.win/en/privacy-policy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown flight-fare summaries with booking URLs, plus optional shell setup commands and MCP tool-use guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live fare results are time-sensitive, comparison-only, and depend on the hosted PriceWin MCP server.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
