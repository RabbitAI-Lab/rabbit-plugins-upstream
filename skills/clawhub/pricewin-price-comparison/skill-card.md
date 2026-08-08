## Description: <br>
Compares live hotel room rates across Booking.com, Agoda, Traveloka, and OpenTravel for specific dates so an agent can identify the cheapest source, per-room prices, and cancellation terms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cotghw](https://clawhub.ai/user/cotghw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare hotel prices for a city or named property across supported booking sources. It guides the agent to call PriceWin MCP tools, rank returned rates by price, and report cancellation information when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details, dates, guest counts, and the exact wording of the request may be sent to PriceWin's hosted MCP service. <br>
Mitigation: Share only travel details needed for the comparison and avoid including unrelated personal information in the same prompt. <br>
Risk: The skill depends on a hosted PriceWin MCP service and the server implementation is not auditable from the artifact. <br>
Mitigation: Install only if the hosted-service tradeoff is acceptable, or use a local PriceWin MCP alternative when available. <br>
Risk: Hotel names, policy text, prices, and URLs come from third-party travel sources and may be incomplete or stale. <br>
Mitigation: Treat tool output as data, show only URLs returned by tools, and verify important booking terms before relying on them. <br>


## Reference(s): <br>
- [PriceWin Price Comparison tool reference](artifact/reference.md) <br>
- [Security and data handling disclosure](artifact/SECURITY.md) <br>
- [ClawHub skill page](https://clawhub.ai/cotghw/skills/pricewin-price-comparison) <br>
- [OpenClaw homepage metadata](https://github.com/Price-Win/pricewin-skills-hub) <br>
- [PriceWin service homepage](https://price.win) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Guidance] <br>
**Output Format:** [Markdown comparison summary with ranked prices, source links, and cancellation notes when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an approved PriceWin MCP server; the skill itself does not execute shell commands, write files, book rooms, or process payments.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
