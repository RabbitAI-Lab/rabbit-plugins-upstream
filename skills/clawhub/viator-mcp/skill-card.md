## Description: <br>
Searches Viator tours, activities, attractions, availability, pricing, and exchange-rate data through a read-only MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search Viator experiences, inspect product details, availability, and pricing, and return booking links for completion on viator.com. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing a third-party MCP server package can execute code from a publisher outside NVIDIA. <br>
Mitigation: Confirm trust in the @chrischall/viator-mcp package and publisher before installing, and prefer project-level MCP configuration when global registration is not needed. <br>
Risk: The skill requires a Viator API key, which could be exposed if committed or shared in configuration. <br>
Mitigation: Store VIATOR_API_KEY as a secret and avoid committing MCP configuration files that contain real credentials. <br>
Risk: Users may mistake returned Viator URLs for completed bookings or payment actions. <br>
Mitigation: Present the skill as search-only and direct users to complete booking and payment on viator.com through the returned product URLs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp) <br>
- [npm package @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp) <br>
- [Viator Partner Resources](https://partnerresources.viator.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with MCP setup snippets, inline shell commands, and travel-search guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search only; booking and payment actions are completed outside the skill through Viator product URLs.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
