## Description: <br>
Semantic quote search with source transparency. Find quotes by meaning, not keywords. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quotewisio](https://clawhub.ai/user/quotewisio) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to search for quotes by concept, person, source, exact text, attribution, similarity, or random selection through the Quotewise MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the remote Quotewise MCP service and npm tools invoked with npx. <br>
Mitigation: Install only if you trust Quotewise and the npm tools invoked by npx. <br>
Risk: Configured Authorization headers may be saved by the MCP client. <br>
Mitigation: Use a dedicated Quotewise API key where possible and handle client configuration as credential-bearing material. <br>
Risk: Quote-search queries are sent to an external service. <br>
Mitigation: Avoid sending sensitive private text as quote-search queries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/quotewisio/skills/quotewise) <br>
- [Quotewise Homepage](https://quotewise.io) <br>
- [Quotewise MCP Documentation](https://quotewise.io/developers/mcp/) <br>
- [Quotewise MCP Setup Repo](https://github.com/quotewise/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON MCP responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the remote Quotewise MCP service; optional QUOTEWISE_API_KEY enables collections and higher rate limits.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
