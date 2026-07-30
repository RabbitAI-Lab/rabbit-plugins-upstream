## Description: <br>
Discover restaurants on Tock via MCP, including cities, venue search, venue details, bookable experiences, prices, party sizes, open dates and times, and signed-in reservation or profile reads when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to discover Tock restaurants and availability through an MCP server. It can also read the signed-in user's Tock reservations and profile when the required browser extension is paired with a signed-in Tock tab. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP server and browser extension can use a signed-in Tock browser session to read Tock pages, including reservation and profile information for account tools. <br>
Mitigation: Install only if comfortable with that session access, review the external npm package and browser extension before use, and keep account tools limited to intended signed-in contexts. <br>
Risk: Tock booking, cancellation, and payment flows are prepaid or checkout-gated and are not performed by this read-only skill. <br>
Mitigation: Use the skill for discovery and availability lookup, then complete booking, cancellation, or payment directly on Tock. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tock-mcp) <br>
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>
- [Tock](https://exploretock.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only Tock discovery and account lookup guidance; booking, cancellation, and payment actions are completed directly on Tock.] <br>

## Skill Version(s): <br>
0.2.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
