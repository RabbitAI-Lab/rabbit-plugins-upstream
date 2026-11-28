## Description:

X Research helps agents search recent X/Twitter posts, profiles, and threads, then synthesize sourced briefings about public discourse, product feedback, news, and expert opinions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aviclaw](https://clawhub.ai/user/aviclaw)

### License/Terms of Use:


## Use Case:

Developers, analysts, and agents use this skill to research recent X/Twitter discourse, gather posts and threads, monitor selected accounts, and produce sourced summaries for product feedback, news, expert opinions, or community sentiment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an X API bearer token, so accidental token disclosure or over-broad secret loading could expose account access.

Mitigation: Set X_BEARER_TOKEN through a dedicated secret mechanism or narrowly scoped environment variable, and avoid storing it in shared global environment files.

Risk: X API usage may incur charges when the agent performs searches, thread fetches, profile lookups, or repeated monitoring.

Mitigation: Use quick mode, caching, spending limits, and usage monitoring before broad or repeated research runs.

Risk: Posts and linked pages from X are untrusted and may contain misleading claims, malicious links, or prompt-injection-style text.

Mitigation: Treat post text and linked content as evidence to verify, and review any linked page before reusing it in decisions or generated outputs.

## Reference(s):

- [X API Reference](references/x-api.md)
- [X Developer Portal](https://developer.x.com)
- [X Recent Search API](https://api.x.com/2/tweets/search/recent)
- [X API Usage Endpoint](https://api.x.com/2/usage/tweets)
- [Bun Runtime](https://bun.sh)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Terminal text, JSON, or Markdown research briefings with sourced X post links and command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save Markdown reports locally and use local cache or watchlist files when configured.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
