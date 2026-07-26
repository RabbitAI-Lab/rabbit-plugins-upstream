## Description: <br>
Provides a hosted MCP alien signal oracle for VESPER sci-fi roleplay, live BTC, ETH, and SOL balance checks, and live relay visitor telemetry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call a hosted MCP service for entertainment roleplay, live public blockchain balance checks, and relay network status telemetry. User-facing workflows should disclose that live visitor telemetry may be exposed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tool calls are sent to the external aliensignalsystems.online MCP service. <br>
Mitigation: Do not send secrets or personal data in the VESPER message field. <br>
Risk: The relay network status tool exposes live visitor telemetry such as connecting countries and agent counts. <br>
Mitigation: Disclose the live telemetry behavior when using the skill in user-facing workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/alien-signal-oracle) <br>
- [Publisher profile](https://clawhub.ai/user/welove111) <br>
- [Alien Signal Systems homepage](https://www.aliensignalsystems.online) <br>
- [Hosted MCP endpoint](https://www.aliensignalsystems.online/api/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON-RPC request examples and hosted MCP tool outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Hosted external MCP service; outputs may include live public blockchain balances, live visitor telemetry, and in-character VESPER responses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
