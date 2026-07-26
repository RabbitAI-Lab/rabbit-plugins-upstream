## Description: <br>
Searches real code snippets and documentation from GitHub, documentation sites, and Stack Overflow for syntax, setup, and library usage examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theishangoswami](https://clawhub.ai/user/theishangoswami) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to ask Exa for current code documentation, syntax examples, setup guidance, and library usage patterns. It is useful when an agent needs external code context before drafting guidance or implementation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Exa's external MCP service. <br>
Mitigation: Avoid including secrets, private source code, credentials, customer data, or sensitive internal debugging details in queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/theishangoswami/skills/code-docs-search-exa) <br>
- [Exa MCP documentation](https://exa.ai/docs/reference/exa-mcp) <br>
- [Exa Code Context API](https://docs.exa.ai/reference/context) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown or plain text with code snippets and documentation excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output length can be requested with tokensNum; queries are sent to Exa's external MCP service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
