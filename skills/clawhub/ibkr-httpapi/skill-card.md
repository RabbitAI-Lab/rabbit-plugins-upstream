## Description: <br>
HTTP+JSON control plane over Interactive Brokers for agents that need to query market data, inspect accounts and positions, run server-side technical analysis, and place, cancel, or exercise orders through a user-run ibkr-httpapi server with explicit confirmation for account-mutating actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill when they already run ibkr-httpapi and want an agent to retrieve Interactive Brokers market data, review account state, run technical analysis, or perform confirmed trading operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate real brokerage actions, including order placement, order cancellation, option combo orders, and option exercise or lapse. <br>
Mitigation: Require explicit per-action confirmation with the resolved account, base URL, symbol, side, quantity, order type, and price before every account-mutating call. <br>
Risk: An ibkr-httpapi server without an API token can expose account data and trading controls to anyone who can reach the socket. <br>
Mitigation: Set a strong API token, keep the service bound to localhost or behind strong authentication, and avoid public exposure until the authentication chain is verified. <br>
Risk: A live IBKR account can be confused with a paper account before trading. <br>
Mitigation: Check the account list before mutating calls, surface whether the account appears paper or live, and prefer paper trading first. <br>
Risk: Requests send market data, account state, and order instructions to the endpoint in IBKR_HTTPAPI_URL. <br>
Mitigation: Point IBKR_HTTPAPI_URL only at a user-run or explicitly trusted ibkr-httpapi instance, and prefer loopback, HTTPS, or a trusted tunnel for non-local access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/ibkr-httpapi) <br>
- [ibkr-httpapi setup](references/setup.md) <br>
- [ibkr-httpapi homepage](https://github.com/psyb0t/ibkr-httpapi) <br>
- [ib_async](https://github.com/ib-api-reloaded/ib_async) <br>
- [wickworks indicators](https://github.com/psyb0t/docker-wickworks#available-indicators) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline curl commands and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only API guidance by default and requires explicit user confirmation before account-mutating order, cancellation, combo, or option exercise calls.] <br>

## Skill Version(s): <br>
0.5.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
