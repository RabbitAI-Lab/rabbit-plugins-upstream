## Description: <br>
Gurkerl.at grocery shopping via MCP - search products, manage cart, orders, recipes, favorites. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[florianbeer](https://clawhub.ai/user/florianbeer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to interact with Gurkerl.at grocery shopping through MCP, including product search, cart management, orders, recipes, favorites, and customer care workflows. <br>

### Deployment Geography for Use: <br>
Austria <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires grocery-account credentials and may expose them through environment or service configuration. <br>
Mitigation: Install only when the Gurkerl MCP endpoint is trusted, protect password-bearing environment and systemd files, and limit access to the runtime environment. <br>
Risk: The skill exposes actions that can place or change orders, payment settings, cancellations, claims, credits, deposits, ratings, feedback, URL fetches, and support emails. <br>
Mitigation: Require explicit user approval before executing any purchasing, payment, cancellation, customer-care, URL-fetching, rating, feedback, or support-email action. <br>


## Reference(s): <br>
- [Gurkerl MCP server](https://www.gurkerl.at/seite/mcp-server) <br>
- [ClawHub skill listing](https://clawhub.ai/florianbeer/skills/gurkerl) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON tool arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, GURKERL_EMAIL, and GURKERL_PASS; tool calls can affect carts, orders, payment methods, support requests, and URL fetching.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
