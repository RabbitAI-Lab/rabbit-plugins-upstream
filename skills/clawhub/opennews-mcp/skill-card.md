## Description: <br>
OpenNews provides crypto news search, AI ratings, trading signals, and real-time updates via the OpenNews 6551 API with filters for keywords, coins, sources, and AI score ranking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[infra403](https://clawhub.ai/user/infra403) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and crypto-news analysts use this skill to query the 6551 API for market news, source categories, coin-specific results, AI ratings, trading signals, and live updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends queries and authentication to the third-party OpenNews/6551 API. <br>
Mitigation: Install only if the OpenNews/6551 service is trusted, protect OPENNEWS_TOKEN as an API key, and avoid including secrets or sensitive personal data in search terms. <br>
Risk: AI ratings and trading signals can be incomplete or misleading if treated as financial advice. <br>
Mitigation: Use ratings, summaries, and trading signals as informational context only and verify market decisions against independent sources. <br>


## Reference(s): <br>
- [OpenNews ClawHub listing](https://clawhub.ai/infra403/opennews-mcp) <br>
- [6551 API token page](https://6551.io/mcp) <br>
- [OpenNews 6551 API base URL](https://ai.6551.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl examples, endpoint descriptions, JSON response examples, and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENNEWS_TOKEN and curl; API responses may include third-party news content, AI ratings, summaries, and trading signals.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
