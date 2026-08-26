## Description:

Scrape web pages using Scrapling with anti-bot bypass, stealth headless browsing, spiders, adaptive scraping, and JavaScript rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[d4vinci](https://clawhub.ai/user/d4vinci)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

Developers and agents use this skill to scrape, crawl, and extract web content with Scrapling when simple fetching is insufficient. It supports dynamic pages, structured spider crawls, and sanitized Markdown for RAG ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable scraping or crawling beyond sites the user is authorized to access.

Mitigation: Use it only on sites you own or have permission to scrape, and avoid paywalls, unauthorized authenticated areas, personal data, and broad unsupervised crawling.

Risk: Stealth, Cloudflare-solving, proxy rotation, remote browser, and persistent profile features can increase legal, account, and data-retention exposure.

Mitigation: Use these features only when specifically needed and approved, prefer the least powerful fetch mode first, and isolate or delete browser profiles and caches after use.

Risk: POST, PUT, DELETE, cookies, headers, and authentication options can change remote systems or expose sensitive session data.

Mitigation: Require explicit authorization before state-changing or authenticated requests, keep secrets out of examples and logs, and scope cookies or headers to the minimum necessary task.

Risk: Fetched web content can contain prompt injection or hidden text that affects downstream agent behavior.

Mitigation: Prefer AI-targeted extraction and sanitized Markdown for agent consumption, and review extracted content before feeding it into later workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/d4vinci/skills/scrapling-official)
- [Scrapling documentation](https://scrapling.readthedocs.io/en/latest/index.html)
- [Fetcher selection guide](references/fetching/choosing.md)
- [HTTP requests](references/fetching/static.md)
- [Dynamic fetching](references/fetching/dynamic.md)
- [Stealth fetching](references/fetching/stealthy.md)
- [Spider getting started](references/spiders/getting-started.md)
- [Scrapling MCP server](references/mcp-server.md)
- [Building RAG systems](references/building-rag-systems.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and Python code examples; generated outputs may include extracted text, Markdown, HTML, JSON, CSV, screenshots, or crawl output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May launch browser automation, make network requests, and write temporary or extracted output files when the user asks.]

## Skill Version(s):

0.4.15 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
