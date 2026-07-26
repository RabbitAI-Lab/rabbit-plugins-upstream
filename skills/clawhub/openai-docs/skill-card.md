## Description: <br>
Query OpenAI developer documentation via the OpenAI Docs MCP server using a curl/jq CLI wrapper for current API, SDK, ChatGPT Apps SDK, Codex, MCP, endpoint schema, parameter, limit, and migration guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[am-will](https://clawhub.ai/user/am-will) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search and fetch official OpenAI documentation before answering OpenAI API, SDK, Apps SDK, Codex, MCP, schema, limit, or migration questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation searches and requested documentation URLs are sent over the network to the configured MCP endpoint. <br>
Mitigation: Keep MCP_URL at the default OpenAI endpoint unless the replacement endpoint is trusted, and avoid including secrets or private project details in documentation queries. <br>


## Reference(s): <br>
- [OpenAI Docs MCP endpoint](https://developers.openai.com/mcp) <br>
- [OpenAI Responses API migration guide](https://platform.openai.com/docs/guides/migrate-to-responses) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON command output with referenced documentation URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include fetched official documentation text, documentation URLs, OpenAPI endpoint data, and shell commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
