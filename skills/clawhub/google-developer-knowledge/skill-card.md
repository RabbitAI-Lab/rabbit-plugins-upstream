## Description: <br>
Retrieve current, source-backed official Google developer documentation for Google Cloud, Firebase, Android, Google AI, Gemini CLI, Flutter, Go, Maps, Web, TensorFlow, and related products for setup, migrations, troubleshooting, architecture, and code examples when current Google documentation matters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wei840222](https://clawhub.ai/user/wei840222) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to retrieve and synthesize current official Google developer documentation for setup, migrations, troubleshooting, architecture decisions, and code examples. It is most useful when answers need source-backed Google documentation and a clear retrieval record. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation queries may disclose sensitive project details to a configured MCP server or Google REST API. <br>
Mitigation: Use product names, public error text, and minimal non-sensitive context; do not include secrets, proprietary code, or private incident details in queries. <br>
Risk: Search snippets or quick grounded answers can be insufficient for pricing, quota, security, migration, or version-sensitive claims. <br>
Mitigation: Retrieve the relevant full document, cite official URLs or document URIs, and mark missing details as unverified instead of inferring them. <br>
Risk: Unavailable MCP capability, authentication failures, or rate limits can lead to unsupported fallback behavior. <br>
Mitigation: Run capability discovery first, use REST only with the required API key or OAuth credentials and quota project, bound retries, and report the selected method and fallback reason. <br>


## Reference(s): <br>
- [Developer Knowledge API](https://developers.google.com/knowledge/api) <br>
- [Developer Knowledge Quickstart](https://developers.google.com/knowledge/quickstart) <br>
- [Search and retrieve documents](https://developers.google.com/knowledge/howto) <br>
- [AnswerQuery guide](https://developers.google.com/knowledge/answer-query) <br>
- [Developer Knowledge MCP setup](https://developers.google.com/knowledge/mcp) <br>
- [Developer Knowledge MCP reference](https://developers.google.com/knowledge/reference/mcp) <br>
- [search_documents tool reference](https://developers.google.com/knowledge/reference/mcp/tools_list/search_documents) <br>
- [answer_query tool reference](https://developers.google.com/knowledge/reference/mcp/tools_list/answer_query) <br>
- [get_documents tool reference](https://developers.google.com/knowledge/reference/mcp/tools_list/get_documents) <br>
- [Corpus reference](https://developers.google.com/knowledge/reference/corpus-reference) <br>
- [Google Developer Knowledge via mcporter](references/mcporter-workflow.md) <br>
- [Developer Knowledge REST API Fallback](references/api-fallback.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with source URLs, document URIs, retrieval records, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mcporter, jq, and curl when using the documented MCP or REST workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
