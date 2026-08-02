## Description: <br>
Provides TripAdvisor travel data from the Terra API through an MCP server for finding and comparing hotels, restaurants, attractions, ratings, reviews, photos, and nearby places. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel-planning agents use this skill to look up TripAdvisor places, compare lodging or dining options, inspect ratings and reviews, and retrieve photos or nearby attractions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The third-party MCP server receives the user's TripAdvisor Terra API key. <br>
Mitigation: Install only when the publisher and package are trusted, scope and rotate the API key where possible, and avoid sharing credentials outside MCP configuration. <br>
Risk: npx-based setup runs the currently published npm package and may change as package versions are updated. <br>
Mitigation: Pin or review the package version before deployment and scan the installed package in managed environments. <br>
Risk: API usage can consume TripAdvisor Terra quota. <br>
Mitigation: Monitor request volume and configure cache TTL settings to reduce repeated calls. <br>
Risk: The optional browser bridge allows same-origin TripAdvisor page fetches through the user's browser session. <br>
Mitigation: Enable the browser bridge only when needed and only in browser sessions appropriate for TripAdvisor data lookup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/tripadvisor) <br>
- [npm package @chrischall/tripadvisor-mcp](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp) <br>
- [tripadvisor-mcp source](https://github.com/chrischall/tripadvisor-mcp) <br>
- [TripAdvisor Developers](https://www.tripadvisor.com/developers) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only travel data connector output; API responses may include place details, ratings, reviews, photos, and diagnostic healthcheck text.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
