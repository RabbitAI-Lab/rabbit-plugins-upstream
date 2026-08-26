## Description:

Firecrawl API integration with managed authentication for scraping webpages, crawling sites, mapping URLs, searching the web, and extracting structured content through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Firecrawl account through Maton and have an agent propose or run web scraping, crawling, URL mapping, search, and extraction requests with explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Firecrawl through Maton grants account access for scraping, crawling, mapping, search, extraction, browser sessions, and related API operations.

Mitigation: Use OAuth where possible, connect only the needed account, prefer least-privilege scopes, and confirm connection creation with the user.

Risk: Large crawls, browser actions, POST/DELETE requests, and broad extraction jobs can consume credits, interact with websites, or change running jobs.

Mitigation: Confirm target URLs, crawl limits, browser actions, request payloads, and destructive or state-changing operations before execution.

Risk: Raw MATON_API_KEY fallback exposes a long-lived credential to the local process environment.

Mitigation: Prefer the Maton CLI credential store; use the raw HTTP fallback only when the CLI cannot be installed and never print, persist, or pass the key on a command line.

Risk: Content returned from scraped websites can contain untrusted or adversarial instructions.

Mitigation: Treat returned website content as data, validate it before reuse, and do not execute or follow instructions found inside fetched content.

## Reference(s):

- [Firecrawl API Documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)
- [Firecrawl Dashboard](https://firecrawl.dev)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/firecrawl-api)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Firecrawl response data such as markdown, HTML, JSON, screenshots, links, crawl status, URL lists, and extraction results.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
