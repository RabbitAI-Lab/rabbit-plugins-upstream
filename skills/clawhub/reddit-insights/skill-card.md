## Description: <br>
Search and analyze Reddit content using semantic AI search via the reddapi.dev HTTP API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dowands](https://clawhub.ai/user/dowands) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and product teams use this skill to query Reddit discussions for pain points, market feedback, sentiment, trends, product comparisons, and content ideas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reddit research queries are sent to the third-party reddapi.dev API and may reveal sensitive research intent or confidential topics. <br>
Mitigation: Do not submit secrets, personal data, regulated data, or confidential business plans unless third-party use is approved. <br>
Risk: The skill uses a paid API key and searches may consume account quota or hit rate limits. <br>
Mitigation: Confirm the active reddapi.dev plan, set appropriate query limits, and monitor quota before running repeated or batch searches. <br>
Risk: AI summaries and Reddit discussions can be incomplete, outdated, or unrepresentative. <br>
Mitigation: Review underlying results and source URLs before using findings for product, market, or business decisions. <br>


## Reference(s): <br>
- [ClawHub Reddit Insights Skill](https://clawhub.ai/dowands/skills/reddit-insights) <br>
- [reddapi.dev](https://reddapi.dev) <br>
- [reddapi.dev Account](https://reddapi.dev/account) <br>
- [Semantic Search API](https://reddapi.dev/api/v1/search/semantic) <br>
- [Vector Search API](https://reddapi.dev/api/v1/search/vector) <br>
- [reddapi.dev MCP Endpoint](https://reddapi.dev/api/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with HTTP examples, JSON request and response shapes, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live API use requires REDDAPI_API_KEY; semantic search can include AI summaries, while vector search returns faster similarity results.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
