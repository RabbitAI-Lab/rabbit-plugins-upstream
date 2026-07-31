## Description: <br>
Scrape, crawl, and extract web data with Scrapling using static requests, JavaScript rendering, stealth browsing, adaptive parsing, and spider workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[d4vinci](https://clawhub.ai/user/d4vinci) <br>

### License/Terms of Use: <br>
BSD 3-Clause <br>


## Use Case: <br>
Developers and agents use this skill to fetch, render, parse, and crawl authorized websites with Scrapling when simple web fetching is insufficient or when dynamic content, adaptive selectors, spiders, or optional anti-bot handling are needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable broad web scraping, including anti-bot bypass, proxy rotation, and persistent sessions. <br>
Mitigation: Use it only for websites the operator is permitted to access, and avoid paywalled, authenticated, personal, or sensitive data unless explicit authorization exists. <br>
Risk: Browser sessions, crawl directories, and Scrapling cache files can retain scraped content or session state on disk. <br>
Mitigation: Close browser sessions when finished and clean up .scrapling_cache, crawl directories, temporary scrape outputs, and browser session data. <br>
Risk: An HTTP MCP server exposed publicly could allow unauthorized scraping actions. <br>
Mitigation: Do not expose the MCP HTTP server publicly without authentication and TLS. <br>
Risk: Scraped web content can contain prompt injection or hidden instructions. <br>
Mitigation: Use AI-targeted or main-content extraction options where available and review scraped content before relying on it. <br>


## Reference(s): <br>
- [Scrapling Documentation](https://scrapling.readthedocs.io/en/latest/index.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/d4vinci/skills/scrapling-official) <br>
- [Scrapling MCP Server](references/mcp-server.md) <br>
- [HTTP requests](references/fetching/static.md) <br>
- [Fetching dynamic websites](references/fetching/dynamic.md) <br>
- [StealthyFetcher](references/fetching/stealthy.md) <br>
- [Fetchers basics](references/fetching/choosing.md) <br>
- [Querying elements](references/parsing/selection.md) <br>
- [Adaptive scraping](references/parsing/adaptive.md) <br>
- [Spiders architecture](references/spiders/architecture.md) <br>
- [Getting started](references/spiders/getting-started.md) <br>
- [Proxy management and handling Blocks](references/spiders/proxy-blocking.md) <br>
- [Scrapling Examples](examples/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline Python, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to produce scraper code, CLI commands, MCP tool calls, or local scrape output files depending on the task.] <br>

## Skill Version(s): <br>
0.4.12 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
