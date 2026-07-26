## Description: <br>
Search Reddit, read posts and threaded comments, and pull subreddit, user, popular, and trending data as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to query Reddit through Scavio for discussion research, brand monitoring, sentiment analysis, and RAG workflows. It supports searches, post and comment retrieval, subreddit and user lookups, popular feeds, and trending searches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reddit search terms, post URLs or IDs, usernames, subreddit names, and comment cursors are sent to Scavio using the configured API key. <br>
Mitigation: Use the skill only when third-party data sharing with Scavio is approved, and avoid confidential investigations or sensitive identifiers unless that sharing is acceptable. <br>
Risk: The skill depends on a Scavio API key. <br>
Mitigation: Store SCAVIO_API_KEY in approved secret management and avoid exposing it in prompts, logs, examples, or committed files. <br>
Risk: Reddit requests can be slow or temporarily fail due to rate limits, usage limits, or upstream availability. <br>
Mitigation: Set client timeouts of at least 30 seconds and handle 429, 502, and 503 responses with wait-and-retry behavior. <br>


## Reference(s): <br>
- [Scavio Reddit API Documentation](https://scavio.dev/docs/reddit-api) <br>
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-reddit-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with bash and Python examples; API responses are structured JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Reddit requests may take 5-15 seconds; all listed Reddit endpoints cost 1 credit per call.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
