## Description:

Search Reddit, read posts and threaded comments, and pull subreddit, user, popular, and trending data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to search public Reddit discussions, retrieve posts and comments, inspect subreddit or user activity, and gather structured discussion data for research, monitoring, sentiment analysis, or RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search terms, post URLs or IDs, subreddit names, usernames, and the API key are sent to Scavio.

Mitigation: Avoid submitting confidential research topics or sensitive account references, and store the Scavio API key in an environment variable or secret store.

Risk: The optional LangChain adapter requires installing an additional package.

Mitigation: Install the adapter only in an isolated environment when that integration is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/reddit-search-api)
- [Scavio Reddit API documentation](https://scavio.dev/docs/reddit-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=reddit-search-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=reddit-search-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON response descriptions and inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to use Scavio Reddit API endpoints that return structured JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
