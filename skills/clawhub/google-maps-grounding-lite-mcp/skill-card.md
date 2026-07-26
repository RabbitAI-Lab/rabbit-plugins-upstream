## Description: <br>
Google Maps Grounding Lite MCP for location search, weather, and routes via mcporter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryanbaumann](https://clawhub.ai/user/ryanbaumann) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to connect an MCP client through mcporter to Google Maps Grounding Lite for place search, current weather, and route estimates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Maps API key use can expose quota or billing if the key is over-permissive. <br>
Mitigation: Use a restricted Google Maps API key where possible and monitor rate limits, quota, and billing. <br>
Risk: Location, address, weather, or route queries may disclose sensitive places to Google's Maps MCP service. <br>
Mitigation: Avoid sending sensitive addresses or routes unless that sharing is acceptable for the use case. <br>
Risk: The setup depends on installing and running mcporter. <br>
Mitigation: Verify that mcporter is trusted before installation and review commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ryanbaumann/skills/google-maps-grounding-lite-mcp) <br>
- [Google Maps Grounding Lite documentation](https://developers.google.com/maps/ai/grounding-lite) <br>
- [Google Cloud API credentials](https://console.cloud.google.com/apis/credentials) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash command examples and MCP tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mcporter and GOOGLE_MAPS_API_KEY; tool responses may include Google Maps links, weather details, route estimates, and rate-limited API results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
