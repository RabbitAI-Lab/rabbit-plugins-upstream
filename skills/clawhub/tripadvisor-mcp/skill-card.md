## Description: <br>
TripAdvisor MCP gives agents read-only access to TripAdvisor Terra API travel data for searching hotels, restaurants, and attractions, and for retrieving place details, photos, and reviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer travel planning questions by looking up TripAdvisor place search results, ratings, reviews, photos, and nearby options through a configured MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel lookup requests are sent to an external TripAdvisor/Terra-backed service through the configured MCP integration. <br>
Mitigation: Install and enable the skill only when external TripAdvisor/Terra travel lookups are intended, and scope activation to relevant travel queries. <br>
Risk: The Terra-backed tools require a TripAdvisor API key and may use the account's quota or plan. <br>
Mitigation: Provide a valid Terra API key through local environment configuration, monitor usage, and avoid using legacy or inactive keys. <br>


## Reference(s): <br>
- [TripAdvisor MCP npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp) <br>
- [TripAdvisor Developers](https://www.tripadvisor.com/developers) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown with travel lookup results, MCP tool guidance, and setup snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the @chrischall/tripadvisor-mcp package and a TripAdvisor Terra API key for Terra-backed tools; the public-page bridge tool can work without an API key.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
