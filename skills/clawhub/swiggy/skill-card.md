## Description: <br>
Order food, groceries, and book restaurants in India via Swiggy's MCP servers with a safety-first confirmation workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[regalstreak](https://clawhub.ai/user/regalstreak) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent operators use this skill to search Swiggy restaurants, grocery items, and Dineout availability, then prepare orders or bookings for explicit user confirmation. <br>

### Deployment Geography for Use: <br>
India <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send delivery, location, cart, and booking details to Swiggy MCP servers. <br>
Mitigation: Install only when users are comfortable connecting a Swiggy account and sharing those workflow details with Swiggy. <br>
Risk: Food, grocery, and restaurant booking workflows can create real-world commerce commitments. <br>
Mitigation: Require a cart or booking preview and explicit user confirmation before any purchase or booking. <br>
Risk: The server security guidance flags the CLI shell invocation pattern for review. <br>
Mitigation: Avoid using the skill until the CLI uses an argument-array subprocess call instead of shell command construction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/regalstreak/skills/swiggy) <br>
- [Swiggy MCP server manifest](https://github.com/Swiggy/swiggy-mcp-server-manifest) <br>
- [Swiggy Food MCP server](https://mcp.swiggy.com/food) <br>
- [Swiggy Instamart MCP server](https://mcp.swiggy.com/im) <br>
- [Swiggy Dineout MCP server](https://mcp.swiggy.com/dineout) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill routes requests through a Node.js CLI and requires explicit confirmation before purchases or bookings.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
