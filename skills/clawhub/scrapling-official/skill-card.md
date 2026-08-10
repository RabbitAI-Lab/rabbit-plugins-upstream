## Description:

Scrape web pages using Scrapling with anti-bot bypass (like Cloudflare Turnstile), stealth headless browsing, spiders framework, adaptive scraping, and JavaScript rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[d4vinci](https://clawhub.ai/user/d4vinci)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

Developers, engineers, and agent users use this skill to scrape, crawl, and extract website data with Scrapling when simple web fetches fail, including dynamic sites, anti-bot-protected pages, and larger spider-based crawls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support scraping or crawling targets where the user may not have authorization.

Mitigation: Use it only on authorized targets, respect robots.txt and site terms, and prefer spider settings such as robots.txt obedience where applicable.

Risk: Stealth browsing and Cloudflare-solving features can bypass anti-bot protections.

Mitigation: Use the simplest fetch mode that works and enable stealth or Cloudflare-solving only when the user has permission for that target.

Risk: Fetched web content may contain prompt injection or misleading instructions.

Mitigation: Use AI-targeted extraction when available and treat scraped content as untrusted data that must be reviewed before acting on it.

Risk: Proxy strings, browser profiles, caches, checkpoints, screenshots, or output files may expose credentials or sensitive data.

Mitigation: Avoid hardcoding credentials, keep user data directories and proxies controlled by the user, and clean local caches, checkpoints, screenshots, and output files after use.

Risk: Scraping can collect personal or sensitive data.

Mitigation: Do not scrape personal or sensitive data unless the user has a lawful and authorized purpose.

## Reference(s):

- [Scrapling documentation](https://scrapling.readthedocs.io/en/latest/index.html)
- [Scrapling MCP Server](artifact/references/mcp-server.md)
- [Migrating from BeautifulSoup to Scrapling](artifact/references/migrating_from_beautifulsoup.md)
- [Fetchers basics](artifact/references/fetching/choosing.md)
- [HTTP requests](artifact/references/fetching/static.md)
- [Fetching dynamic websites](artifact/references/fetching/dynamic.md)
- [StealthyFetcher](artifact/references/fetching/stealthy.md)
- [Adaptive scraping](artifact/references/parsing/adaptive.md)
- [Querying elements](artifact/references/parsing/selection.md)
- [Spiders architecture](artifact/references/spiders/architecture.md)
- [Proxy management and handling Blocks](artifact/references/spiders/proxy-blocking.md)
- [Scrapling Examples](artifact/examples/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create local scraping output files such as Markdown, text, HTML, JSON, cache, checkpoint, or screenshot artifacts when the user authorizes scraping work.]

## Skill Version(s):

0.4.13 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
