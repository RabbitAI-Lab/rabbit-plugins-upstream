## Description: <br>
wickworks helps agents compute technical indicators and Smart-Money-Concepts primitives from user-supplied OHLC candlestick bars through a stateless REST or MCP service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and market-data analysts use this skill when an agent needs to compute technical indicators, support/resistance structures, order blocks, fair-value gaps, or related OHLC primitives without producing forecasts or trading opinions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The wickworks service is auth-less by default, so a network-exposed instance can be called by anyone who can reach it. <br>
Mitigation: Bind the service to localhost by default and expose it beyond the machine only behind an authenticated reverse proxy or VPN. <br>
Risk: OHLC bars or account-derived market data sent to an untrusted instance could disclose sensitive data. <br>
Mitigation: Send data only to a wickworks instance operated by the user or another trusted operator. <br>


## Reference(s): <br>
- [wickworks setup](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/wickworks) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>
- [wickworks homepage](https://github.com/psyb0t/docker-wickworks) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON, shell command, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to call a stateless service that returns NaN-safe JSON indicator and SMC outputs from supplied bars.] <br>

## Skill Version(s): <br>
0.6.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
