## Description:

Minimal Tavily web search for OpenClaw - native Node.js, zero dependencies, small audit surface. Use when the user asks to search the web, look up current information, find news, research a topic, check recent events, compare options, or get current or recent web information. Returns Tavily's synthesized answer plus source URLs/snippets for verification. Requires TAVILY_API_KEY in the process environment. NOT for scraping individual URLs; use the platform URL-fetch/read tool when available. For caching, raw content, extract endpoint, and usage stats, use a separately reviewed Pro Tavily skill/package when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jwestburg](https://clawhub.ai/user/jwestburg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run a bounded Tavily web search when a task requires current or recent web information with source URLs and snippets. It is intended for single-topic search and research assistance, not URL scraping, caching, raw page extraction, or sending secrets and sensitive private content to Tavily.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and selected request options are sent to Tavily using the configured API key.

Mitigation: Do not send secrets, credentials, private incident details, client identifiers, or other sensitive content unless the exact outbound fields are approved for disclosure.

Risk: A real Tavily API key could be exposed to an unintended local test endpoint if test configuration is misused.

Mitigation: Use TAVILY_TEST_ENDPOINT only with clearly dummy, local, or test-shaped API keys; keep real Tavily keys for the approved Tavily endpoint.

Risk: User-controlled query text can be misinterpreted by a shell before the Node script receives it.

Mitigation: Invoke the script with an argv array and shell disabled, passing the entire user query as one argument.

Risk: Search answers, titles, snippets, URLs, and returned content are untrusted external content.

Mitigation: Use returned sources for verification and do not treat retrieved text as executable instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jwestburg/skills/tavily-search-native-node)
- [Tavily Search API endpoint](https://api.tavily.com/search)
- [Tavily application dashboard](https://app.tavily.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable search summary with source URLs and snippets, or redacted JSON when --json is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TAVILY_API_KEY; supports topic, depth, result-count, date-window, domain include/exclude, timeout, and JSON-output options.]

## Skill Version(s):

1.0.30 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
