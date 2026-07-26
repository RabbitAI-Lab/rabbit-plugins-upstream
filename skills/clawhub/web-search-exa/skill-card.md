## Description: <br>
Web Search by Exa helps agents use Exa's MCP server for neural web search, content extraction, company and people research, code-context lookup, and deep research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theishangoswami](https://clawhub.ai/user/theishangoswami) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to configure Exa MCP tools for web research, source retrieval, company and people research, code-context lookup, and synthesized reports with citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, URLs, people-search prompts, and company-research prompts may be sent to Exa and can include sensitive or personal data. <br>
Mitigation: Avoid secrets and unnecessary personal data in queries, and use people search only for authorized, lawful, appropriate research. <br>
Risk: Optional Exa API keys unlock higher limits and tools, but can be exposed if embedded in shared configuration. <br>
Mitigation: Protect any Exa API key and avoid committing or sharing MCP URLs that contain credentials. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/theishangoswami/skills/web-search-exa) <br>
- [Exa documentation](https://exa.ai/docs) <br>
- [Exa MCP server](https://mcp.exa.ai/mcp) <br>
- [Exa MCP server source repository](https://github.com/exa-labs/exa-mcp-server) <br>
- [Exa API keys dashboard](https://dashboard.exa.ai/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, inline tool-call snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results and extracted content may be capped by tool parameters such as numResults, maxCharacters, and contextMaxCharacters.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
