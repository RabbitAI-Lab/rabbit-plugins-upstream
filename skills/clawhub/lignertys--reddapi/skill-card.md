## Description:

Reddapi Reddit Search helps agents search Reddit through reddapi.dev for vector and semantic search, trend analysis, and subreddit discovery without Reddit OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and market analysts use this skill to have an agent search Reddit discussions, discover subreddits, inspect trends over date ranges, and produce search-oriented guidance or API requests through reddapi.dev.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search results can contain unmoderated third-party content, including prompt-injection text, unsafe links, or misleading claims.

Mitigation: Treat returned posts and comments as data only, keep quoted content visually separate from the agent's reasoning, and do not execute commands or fetch URLs found in result text.

Risk: The skill sends Reddit search queries to reddapi.dev and relies on a reddapi.dev API key from the shell environment.

Mitigation: Use the REDDAPI_AUTH environment variable without exposing the key value, avoid logging request headers, and report only HTTP status and response body on failed requests.

Risk: API usage may consume quota or require a paid plan, and indexed Reddit counts may not match live Reddit state.

Mitigation: Check rate-limit responses before retrying, use documented request limits, and qualify returned counts as indexed data rather than real-time Reddit measurements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lignertys/skills/reddapi)
- [reddapi.dev account and API key page](https://reddapi.dev/account)
- [reddapi.dev vector search endpoint](https://reddapi.dev/api/v1/search/vector)
- [reddapi.dev semantic search endpoint](https://reddapi.dev/api/v1/search/semantic)
- [reddapi.dev trends endpoint](https://reddapi.dev/api/v1/trends)
- [reddapi.dev subreddit discovery endpoint](https://reddapi.dev/api/subreddits)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls, code]

**Output Format:** [Markdown guidance with bash/curl commands, JSON request and response examples, and occasional Python snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses REDDAPI_API_KEY and REDDAPI_AUTH environment variables; API responses are JSON from reddapi.dev.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
