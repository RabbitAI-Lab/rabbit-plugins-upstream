## Description: <br>
Order food, groceries, and book restaurants in India via Swiggy's MCP servers with a safety-first confirmation workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aditya4206360-prog](https://clawhub.ai/user/aditya4206360-prog) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users in India use this skill to search Swiggy food, Instamart grocery, and Dineout restaurant options, then prepare cart, order, or booking commands for explicit user confirmation. <br>

### Deployment Geography for Use: <br>
India <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill can send searches, location or address details, cart contents, orders, and booking details to Swiggy-operated services. <br>
Mitigation: Install and authenticate only if that data sharing is acceptable for the intended user and account. <br>
Risk: Cash-on-delivery orders may not be cancellable after placement. <br>
Mitigation: Before approving an order, verify the items, quantities, total, delivery address, expected timing, and no-cancellation limitation. <br>
Risk: The CLI implementation must be supplied by the installer or another trusted source. <br>
Mitigation: Confirm the installed command comes from the expected release source before authenticating or placing orders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aditya4206360-prog/skills/sr1) <br>
- [Swiggy Food MCP endpoint](https://mcp.swiggy.com/food) <br>
- [Swiggy Instamart MCP endpoint](https://mcp.swiggy.com/im) <br>
- [Swiggy Dineout MCP endpoint](https://mcp.swiggy.com/dineout) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command-line arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cart previews, totals, addresses, booking options, and confirmation prompts before command execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
