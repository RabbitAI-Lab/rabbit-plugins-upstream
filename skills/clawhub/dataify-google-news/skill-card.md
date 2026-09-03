## Description:

Search Google News for current news results. Do not use for general Google web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run targeted Google News searches through Dataify and receive compact news results with source links and relevant fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google News queries and selected filters are sent to Dataify.

Mitigation: Avoid sensitive private research terms and use the skill only when sharing selected search parameters with Dataify is acceptable.

Risk: Dataify API usage may consume account credits.

Mitigation: Review query scope and filters before high-volume use and confirm the account has enough credits for the intended request.

Risk: Persistent credential configuration can leave API tokens in shell profiles.

Mitigation: Prefer a session-scoped DATAIFY_API_TOKEN unless persistent storage is intentional, and never expose token values in chat or logs.

## Reference(s):

- [Dataify Google News API Reference](references/google_news_api.md)
- [Dataify Google News Skill Page](https://clawhub.ai/dataify-server/skills/dataify-google-news)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, configuration guidance]

**Output Format:** [Markdown summaries by default, with raw JSON or HTML only when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Google News titles, source links, counts, truncation notes, and account setup guidance when credentials are missing.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
