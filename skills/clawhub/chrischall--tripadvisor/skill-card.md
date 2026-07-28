## Description: <br>
TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, ratings, reviews, photos, and nearby places. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to query TripAdvisor Terra data through an MCP server when comparing places to stay, eat, visit, or inspect near a location. It supports read-only location search, details, photos, and reviews, with an optional browser bridge for public page details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires installing and running the third-party npm package @chrischall/tripadvisor-mcp. <br>
Mitigation: Install only after reviewing and trusting the package source and release, as recommended by the server security guidance. <br>
Risk: The main MCP tools require a TripAdvisor Terra API key in MCP configuration. <br>
Mitigation: Store the API key only in the MCP environment configuration and avoid exposing it in prompts, logs, or shared files. <br>
Risk: Optional browser-bridge behavior can fetch public TripAdvisor pages without an API key. <br>
Mitigation: Review whether browser-bridge use is acceptable before enabling tools that fetch public TripAdvisor page details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor) <br>
- [npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp) <br>
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, API calls, Text] <br>
**Output Format:** [Markdown with inline JSON, shell commands, and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a TripAdvisor Terra API key for the main MCP tools; optional browser-bridge behavior can fetch public TripAdvisor page details without an API key.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
