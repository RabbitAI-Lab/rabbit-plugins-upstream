## Description: <br>
This skill helps an agent work with a user's Kia Access or Kia Owners account to read vehicle status, location, EV charge state, and confirm-gated vehicle commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and vehicle owners use this skill to connect an agent to Kia Access or Kia Owners workflows for vehicle status checks and carefully confirmed vehicle actions. It is suited for environments where the user intentionally trusts the MCP server with Kia account credentials, vehicle location, and enabled controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Kia account credentials, refresh tokens, vehicle location, and enabled vehicle controls. <br>
Mitigation: Install it only when the MCP server is trusted, protect the Kia password and exported refresh token as vehicle-access credentials, and choose the least permissive KIA_WRITE_MODE that fits the intended use. <br>
Risk: Write-mode tools can affect a real vehicle, including climate, charging, and door lock or unlock actions. <br>
Mitigation: Require explicit user confirmation for every command, preview dry runs accurately, and enable door lock or unlock only when the user intentionally selects the all write mode. <br>
Risk: Cached status can be stale, accepted commands may not equal confirmed state changes, and some charging endpoints are documented as unverified. <br>
Mitigation: Refresh and re-read status when freshness matters, report command acceptance separately from state confirmation, and clearly disclose unverified command behavior when presenting results. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with JSON configuration examples and tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should distinguish dry runs, accepted commands, and confirmed vehicle state changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
