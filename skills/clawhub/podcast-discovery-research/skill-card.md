## Description:

Discovers and compares public podcast shows, episodes, charts, rankings, and related programs using Apple Podcasts and Spotify Podcasts through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use this skill to discover public podcast shows and episodes, compare platform-specific charts, inspect show metadata, and build bounded guest or partnership shortlists from public episode evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast search terms, platform IDs, and related query parameters are sent to the Crawlora API with the user's Crawlora API key.

Mitigation: Use this skill only when sharing those queries with Crawlora is acceptable, and avoid private or sensitive research queries unless they meet the user's data-sharing requirements.

Risk: Podcast descriptions, show notes, related-show suggestions, and chart rankings may be incomplete, promotional, locale-specific, or time-sensitive.

Mitigation: Preserve platform IDs, URLs, locales, chart definitions, and retrieval time, and distinguish source claims from independently corroborated facts.

Risk: Chart rank can be mistaken for audience size, downloads, revenue, or cross-platform popularity.

Mitigation: Compare rankings only within aligned platform, country, category, chart, and date windows, and do not infer audience or revenue metrics from rank.

Risk: The helper uses an API key to access a third-party service.

Mitigation: Keep CRAWLORA_API_KEY out of logs and shared command lines; the bundled helper stores the header in a private temporary curl config and restricts calls to documented GET routes.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/podcast-discovery-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses from the Crawlora helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided CRAWLORA_API_KEY and emits public podcast metadata retrieved from documented GET endpoints.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
