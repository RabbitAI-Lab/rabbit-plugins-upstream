## Description: <br>
Search Viator tours, activities, attractions, availability, pricing, and exchange-rate information through an MCP server using the Viator Partner API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Viator travel products, compare activities or attractions, check details, pricing, availability, and exchange rates, and obtain Viator booking links without making bookings through the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel search queries may be sent to a third-party commercial travel API. <br>
Mitigation: Use the skill only when Viator-backed travel search is desired, and avoid sending sensitive personal information in queries. <br>
Risk: Returned booking links preserve affiliate attribution and may not represent provider-neutral travel planning. <br>
Mitigation: Confirm the user wants Viator results and review returned product links before relying on them for recommendations or booking decisions. <br>
Risk: The skill requires a Viator Partner API key. <br>
Mitigation: Store the API key in the MCP server environment and do not expose it in prompts, shared files, or generated output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp) <br>
- [npm package @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp) <br>
- [Viator Partner Resources](https://partnerresources.viator.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Viator Partner API queries; returned booking and attraction links may preserve affiliate attribution.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
