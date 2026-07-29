## Description: <br>
ibkr-httpapi helps agents use a deployed Interactive Brokers HTTP+JSON bridge for market data, account and position review, technical analysis, and explicitly confirmed order actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, trading-system operators, and agent users use this skill when they have already deployed ibkr-httpapi and want an agent to query IBKR market data, inspect account state, run server-side technical analysis, or prepare order actions. Account-mutating requests are appropriate only when the user gives explicit confirmation for the exact order, cancellation, combo order, or option exercise. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate, cancel, or exercise real Interactive Brokers orders through a user-controlled bridge. <br>
Mitigation: Require explicit confirmation for each exact mutating action, including symbol, side, quantity, order type, price, account, and IBKR_HTTPAPI_URL before making the request. <br>
Risk: An unset or weak API token can expose brokerage account access to any process that can reach the server. <br>
Mitigation: Use a strong API_TOKEN before any non-loopback exposure and keep the bridge behind loopback, a tunnel, or another trusted authentication layer. <br>
Risk: Requests send market data, account state, and order instructions to the endpoint named by IBKR_HTTPAPI_URL. <br>
Mitigation: Point IBKR_HTTPAPI_URL only at an instance the user controls or explicitly trusts, and prefer paper trading until endpoint routing and authentication are verified. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/psyb0t/skills/ibkr-httpapi) <br>
- [Setup Guide](artifact/references/setup.md) <br>
- [ib_async](https://github.com/ib-api-reloaded/ib_async) <br>
- [docker-wickworks Indicator Catalog](https://github.com/psyb0t/docker-wickworks#available-indicators) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses IBKR_HTTPAPI_URL and optional API_TOKEN; account-mutating actions require explicit per-action user confirmation.] <br>

## Skill Version(s): <br>
0.5.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
