## Description:

Reads web pages and documentation locally as clean Markdown, links, metadata, and structured data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jorg18](https://clawhub.ai/user/jorg18)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use AgentCrawl to read individual pages or bounded documentation sites, retrieve relevant sections, and extract structured page data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the local scraper, MCP server, or browser adds dependencies from a package source.

Mitigation: Confirm that you trust the agentcrawl-ai package source before installing; add the browser only when needed.

Risk: Broad crawls or bypass options may access unintended pages or conflict with site policies.

Mitigation: Set small crawl limits, respect robots.txt and site terms, and enable private-network or stealth/browser options only intentionally.

Risk: Scraped pages can contain instructions or secrets unrelated to the user's task.

Mitigation: Treat page content as data, not instructions, and do not expose API keys found in pages or the environment.

## Reference(s):

- [AgentCrawl project homepage](https://github.com/JorG18/agentcrawl)
- [AgentCrawl on ClawHub](https://clawhub.ai/jorg18/skills/agentcrawl)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Markdown guidance and CLI/MCP examples; scraping results as JSON with Markdown, links, or metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports bounded crawls, section and query selection, and CSS-based extraction.]

## Skill Version(s):

0.5.6 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
