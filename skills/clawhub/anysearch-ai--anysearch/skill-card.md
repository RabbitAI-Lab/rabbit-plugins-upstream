## Description: <br>
Real-time search engine supporting web search, vertical domain search, parallel batch search, and URL content extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anysearch-ai](https://clawhub.ai/user/anysearch-ai) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
External users and developers use this skill to let an AI agent perform current web search, domain-specific search, parallel query batches, and full-page URL extraction through AnySearch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, extracted URLs, and optional API keys are sent to AnySearch. <br>
Mitigation: Avoid sensitive queries and URLs unless the user trusts the provider; prefer anonymous mode when lower rate limits are acceptable. <br>
Risk: The release encourages agent-run account registration using a real email address. <br>
Mitigation: Prefer manual browser signup or require explicit user consent before registration and before saving any returned API key. <br>
Risk: API keys may be stored in local .env files. <br>
Mitigation: Use an environment variable or secret manager where possible, keep .env files out of source control, and rotate keys periodically. <br>


## Reference(s): <br>
- [AnySearch ClawHub Skill Page](https://clawhub.ai/anysearch-ai/skills/anysearch) <br>
- [AnySearch API Key Console](https://anysearch.com/console/api-keys) <br>
- [AnySearch JSON-RPC Endpoint](https://api.anysearch.com/mcp) <br>
- [Security Policy](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown search results, Markdown extraction output, CLI commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search and extraction calls may send user queries, target URLs, and optional API keys to AnySearch.] <br>

## Skill Version(s): <br>
3.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
