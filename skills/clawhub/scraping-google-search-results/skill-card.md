## Description:

Scrapes Google search results for search terms or Google search URLs using apidojo's Google Search scraper on Apify and returns SERP result fields such as URL, title, snippet, position, and feature type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

SEO analysts, researchers, journalists, and competitive intelligence teams use this skill to collect Google SERP data for keywords or Google search URLs and export result datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to Apify and may contain confidential, personal, regulated, or client-sensitive terms.

Mitigation: Review query terms before execution and avoid using the skill for sensitive searches unless the user is allowed to disclose them to Apify.

Risk: REST examples place the API token in request URLs, which can expose credentials through shell history, logs, or copied commands.

Mitigation: Prefer the MCP or SDK path where available, keep API tokens in environment variables, and avoid sharing commands or logs that include tokenized URLs.

Risk: Exported SERP datasets may contain search-derived data that the user is not permitted to store or redistribute.

Mitigation: Export datasets only when the user is authorized to store and handle the resulting search data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-google-search-results)
- [Apify actor: apidojo/google-search-scraper](https://apify.com/apidojo/google-search-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and optional JSON or CSV dataset exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns SERP records with query, position, URL, title, description, type, and optional SERP feature fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
