## Description: <br>
wickworks helps an agent send OHLC candlestick bars to a stateless REST or MCP service and receive technical indicators plus Smart-Money-Concepts primitives as JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when they already have OHLC candlestick bars and need technical indicators, Smart-Money-Concepts structure, or pre-baked market-data summaries computed without forecasting or trading opinions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured wickworks endpoint receives the OHLC bar data supplied by the user. <br>
Mitigation: Use only a trusted endpoint, preferably a local instance on 127.0.0.1. <br>
Risk: The wickworks service is auth-less by default when exposed on a reachable network interface. <br>
Mitigation: Bind to loopback by default and put any off-host deployment behind an authenticated reverse proxy or VPN. <br>
Risk: Using the floating Docker image tag can change runtime behavior over time. <br>
Mitigation: Pin the Docker image version for repeatable deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/wickworks) <br>
- [wickworks setup](references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>
- [OpenClaw wickworks plugin](https://github.com/psyb0t/docker-wickworks/tree/main/.agents/plugins/wickworks) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request examples; service responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are camelCase, NaN-safe, stateless market-data primitives computed from caller-supplied OHLC bars.] <br>

## Skill Version(s): <br>
0.6.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
