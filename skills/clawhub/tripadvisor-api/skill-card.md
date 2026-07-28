## Description: <br>
Query TripAdvisor location data for search, nearby places, details, photos, and reviews from a shell with curl against the Terra REST API, with a no-API-key fallback for public location details through the fpx browser bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to look up TripAdvisor location data from scripts or shells without running the TripAdvisor MCP server. It supports API-key-based Terra requests and a narrower browser-session fallback for public location details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional fpx fallback uses the user's browser session and writes fetched TripAdvisor HTML to a temporary file. <br>
Mitigation: Use the fallback only for pages the user intends to fetch, avoid shared machines, delete temporary HTML after parsing, and inspect saved page files before sharing them. <br>
Risk: Lookup commands can fail or return incomplete data when the Terra API key is missing, invalid, from the wrong API family, or rate limited. <br>
Mitigation: Check API-key setup before use, handle 401, 403, and 429 responses explicitly, and back off when quota or QPS limits are reached. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/tripadvisor-api) <br>
- [TripAdvisor Developers](https://www.tripadvisor.com/developers) <br>
- [Terra API Base URL](https://terra.tripadvisor.com/api) <br>
- [Terra API Endpoints](references/terra-endpoints.md) <br>
- [Web Fallback](references/web-fallback.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell, jq, and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are read-only lookup recipes and parsing guidance; API responses are expected to be JSON.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
