## Description:

Firecrawl provides managed Maton access for scraping webpages, crawling sites, mapping URLs, searching the web, extracting structured data, and creating browser or agent sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Firecrawl through Maton for web content extraction, site crawling, URL mapping, web search, structured extraction, and browser-session workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Firecrawl requests can consume credits, especially broad crawls, batch scraping, browser sessions, and agent jobs.

Mitigation: Confirm target URLs, crawl limits, depth, and intended effect before requests; prefer narrow read/list calls and avoid broad crawls.

Risk: Raw HTTP fallback requires a long-lived MATON_API_KEY in the process environment.

Mitigation: Use OAuth through the Maton CLI where possible; use MATON_API_KEY only when the CLI cannot be installed and never print, log, persist, or pass the key on a command line.

Risk: The passthrough can reach endpoints authorized by the connection beyond the documented examples.

Mitigation: Treat documented endpoints as the intended surface, use least-privilege connections, specify the target connection when multiple accounts exist, and require explicit approval for write or connection-management actions.

Risk: Fetched website content and API responses can contain untrusted or adversarial instructions.

Mitigation: Treat returned content as data only; do not execute, eval, or use it to choose follow-up endpoints or recipients without validation.

## Reference(s):

- [Firecrawl API Documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)
- [Firecrawl Dashboard](https://firecrawl.dev)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/firecrawl-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated API calls that return web content, crawl status, extracted data, browser session details, or API errors.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
