## Description: <br>
Search flights via Google Flights. Find nonstop/connecting flights, filter by time and cabin class, get booking links. Supports city names (NYC, London, Tokyo) with automatic multi-airport search. No API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brennerspear](https://clawhub.ai/user/brennerspear) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search flight schedules and prices, compare nonstop or connecting itineraries, filter by departure time and cabin class, and retrieve Google Flights booking links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup notes include an optional command that pipes a remote uv installer script into a shell. <br>
Mitigation: Use a package manager or follow uv's official installation instructions, and review installation commands before running them. <br>
Risk: The skill runs a bundled flight-search CLI and installs the fast-flights dependency through uvx on first use. <br>
Mitigation: Install only in an environment where using uv and executing the bundled CLI are acceptable. <br>


## Reference(s): <br>
- [Flights on ClawHub](https://clawhub.ai/brennerspear/skills/flights-search) <br>
- [fast-flights Python package](https://github.com/AWeirdDev/flights) <br>
- [uv documentation](https://docs.astral.sh/uv/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and tabular text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flight data is returned as text listings with local airport times, USD prices, and optional booking links.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
