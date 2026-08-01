## Description: <br>
Guides agents to query TripAdvisor location search, nearby results, details, photos, and reviews through Terra REST API curl commands, with a read-only fpx browser fallback for public page details when no API key is available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve TripAdvisor location data from shell workflows without running the tripadvisor-mcp server. It is suited for read-only search, nearby discovery, location detail, photos, reviews, and limited public-page detail lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional fpx fallback uses the user's signed-in TripAdvisor browser session. <br>
Mitigation: Prefer the Terra API path when possible, use a dedicated low-privilege browser profile for fpx, and do not fetch non-TripAdvisor or arbitrary URLs through that profile. <br>
Risk: Terra API workflows depend on an API key that can fail, be mismatched with the legacy API, or hit quota limits. <br>
Mitigation: Keep the key in TRIPADVISOR_API_KEY, avoid exposing it in logs or shared commands, and handle 401, 403, and 429 responses before retrying. <br>


## Reference(s): <br>
- [Terra API endpoints](references/terra-endpoints.md) <br>
- [Web fallback](references/web-fallback.md) <br>
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers) <br>
- [TripAdvisor Terra API](https://terra.tripadvisor.com/api) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tripadvisor-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl, jq, shell, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only TripAdvisor data guidance; Terra API calls require TRIPADVISOR_API_KEY, and the fpx fallback requires a paired browser profile.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
