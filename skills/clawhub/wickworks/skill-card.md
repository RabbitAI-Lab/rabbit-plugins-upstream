## Description: <br>
wickworks helps agents compute technical indicators and Smart-Money-Concepts primitives from caller-provided OHLC candlestick bars through a stateless REST or MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-data agents use wickworks when they already have OHLC bars and need technical indicators or SMC structures computed without forecasting, scoring, or stateful data storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The wickworks service is auth-less if exposed beyond localhost. <br>
Mitigation: Bind it to localhost by default and expose it off-host only behind an authenticated reverse proxy or VPN. <br>
Risk: Using an unpinned container image can reduce deployment reproducibility. <br>
Mitigation: Pin a specific Docker image version for deployments that need repeatable behavior. <br>
Risk: Requests can fail when they exceed configured bar limits or do not include enough warm-up bars for selected indicators. <br>
Mitigation: Respect MAX_BARS and MIN_BARS settings, and handle insufficient_bars and 413 responses in the calling workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/wickworks) <br>
- [wickworks setup](references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, API calls, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell, JSON, REST, and MCP examples; service responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Computes stateless, NaN-safe outputs from caller-provided OHLC bars and returns insufficient-input or oversize-request errors when limits are not met.] <br>

## Skill Version(s): <br>
0.6.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
