## Description: <br>
ibkr-httpapi lets an agent use a user-operated Interactive Brokers HTTP and MCP bridge for market data, account inspection, technical analysis, and explicitly confirmed order actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-tool users use this skill after deploying ibkr-httpapi and setting IBKR_HTTPAPI_URL. It helps agents retrieve IBKR market data, inspect accounts and positions, run server-side technical analysis, and place, cancel, or exercise orders only after explicit per-action confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent place, cancel, or exercise real IBKR orders with real-money consequences. <br>
Mitigation: Require explicit user confirmation for each mutating action, including resolved account, base URL, symbol, side, quantity, order type, and price details. <br>
Risk: An ibkr-httpapi service without API_TOKEN configured is unauthenticated for any process that can reach it. <br>
Mitigation: Keep the service bound to localhost or behind strong authentication, and set a strong bearer token before exposing it beyond a trusted local environment. <br>
Risk: Requests send market data, account state, and order instructions to the endpoint named by IBKR_HTTPAPI_URL. <br>
Mitigation: Use only an ibkr-httpapi endpoint the user runs or explicitly trusts, and prefer a protected HTTPS or tunnel path when not using loopback. <br>
Risk: Live and paper IBKR accounts can be confused during order workflows. <br>
Mitigation: Check and surface the resolved account before order actions, and prefer paper trading until the setup and confirmation flow are tested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/ibkr-httpapi) <br>
- [ibkr-httpapi project homepage](https://github.com/psyb0t/ibkr-httpapi) <br>
- [Setup reference](references/setup.md) <br>
- [ib_async](https://github.com/ib-api-reloaded/ib_async) <br>
- [wickworks sidecar](https://github.com/psyb0t/docker-wickworks) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, JSON] <br>
**Output Format:** [Markdown guidance with curl examples, JSON request and response shapes, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires IBKR_HTTPAPI_URL and may use API_TOKEN for bearer authentication; mutating brokerage actions require explicit per-action confirmation.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
