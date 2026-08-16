## Description:

Scrape web pages using Scrapling with anti-bot bypass, stealth headless browsing, spiders, adaptive scraping, and JavaScript rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[d4vinci](https://clawhub.ai/user/d4vinci)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

Developers and agents use this skill to extract data from websites, generate Scrapling Python code, run Scrapling CLI commands, and choose between static HTTP fetching, browser rendering, stealth fetching, and spider-based crawling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable scraping on sites where the user is not authorized to collect data.

Mitigation: Use it only on sites you own or are authorized to scrape, and check site terms, robots.txt expectations, and applicable legal limits before running commands or spiders.

Risk: Anti-bot bypass, Cloudflare solving, proxy rotation, authenticated cookies, CDP, and persistent browser profiles can increase misuse and data-handling risk.

Mitigation: Enable these options only when necessary, document the authorization basis, avoid storing credentials in commands or files, and verify where browser profiles, cached pages, and scraped data are saved.

Risk: Fetched page content can contain prompt injection or hidden content intended to influence an agent.

Mitigation: Prefer the skill's AI-targeted extraction mode for CLI scraping, scope extraction with selectors where practical, and review scraped content before using it to drive further actions.

## Reference(s):

- [Scrapling documentation](https://scrapling.readthedocs.io/en/latest/index.html)
- [Fetcher selection guide](references/fetching/choosing.md)
- [HTTP requests](references/fetching/static.md)
- [Fetching dynamic websites](references/fetching/dynamic.md)
- [StealthyFetcher](references/fetching/stealthy.md)
- [Adaptive scraping](references/parsing/adaptive.md)
- [Querying elements](references/parsing/selection.md)
- [Spiders architecture](references/spiders/architecture.md)
- [Proxy management and handling blocks](references/spiders/proxy-blocking.md)
- [Scrapling MCP Server](references/mcp-server.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline Python and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands or code that fetch web pages, use browser automation, manage proxies, or create scraping spiders.]

## Skill Version(s):

0.4.14 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
