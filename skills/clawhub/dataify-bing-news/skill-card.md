## Description:

Search Bing News for current news results. Do not use for general Bing web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Bing News searches through Dataify's scraper API and receive compact news results with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify API token and the security evidence notes broader credential handling than the instructions disclose.

Mitigation: Configure DATAIFY_API_TOKEN through the environment only, never paste tokens into chat or prompts, and review the skill before installing in sensitive environments.

Risk: Search queries are sent to Dataify's scraper API.

Mitigation: Avoid sending confidential or regulated information in news search queries.

## Reference(s):

- [Dataify Bing News API Reference](references/api.md)
- [Dataify Scraper API Endpoint](https://scraperapi.dataify.com/request)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, parameter tables, setup commands, or raw JSON/HTML when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN from the environment and sends search queries to Dataify's scraper API.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
