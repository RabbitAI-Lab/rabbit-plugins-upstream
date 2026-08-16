## Description:

Runs SERP and keyword research via the Crawlora API for Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends, returning normalized JSON for rankings, SERP snapshots, autocomplete ideas, and trend signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO analysts, and marketers use this skill to collect public SERP snapshots, keyword suggestions, and Google Trends signals through Crawlora instead of scraping result pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, locations, tickers, business lookups, and other request parameters are sent to Crawlora when the helper is used.

Mitigation: Avoid passing secrets, private prompts, or sensitive business data in queries or JSON bodies, and install only where Crawlora API use is acceptable.

Risk: The bundled helper can call broader Crawlora endpoints than the SERP and keyword-research purpose described by the skill.

Mitigation: Review intended endpoint paths before execution and restrict use to the SERP, suggestion, and trend endpoints required for the task.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/serp-keyword-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends request parameters to Crawlora.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
