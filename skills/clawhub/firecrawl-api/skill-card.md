## Description:

Firecrawl API integration with managed authentication for scraping webpages, crawling sites, mapping URLs, and searching web content through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect a Firecrawl account and perform user-approved scrape, crawl, map, search, and extraction requests. It is suited for collecting web content as text, markdown, JSON, screenshots, links, and structured data while preserving explicit approval around target URLs, scope, and cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firecrawl scraping, crawling, browser actions, custom headers, and agent jobs can consume credits or interact with external websites beyond passive reading.

Mitigation: Approve only requests with clear target URLs, crawl limits, intended actions, and cost expectations before execution.

Risk: The skill requires Maton authentication and a connected Firecrawl account.

Mitigation: Install and authenticate the Maton CLI, connect only the needed Firecrawl account, and verify the active connection before use.

Risk: Large crawl or batch operations can expand beyond the intended scope.

Mitigation: Set explicit limits such as crawl limit, maximum depth, included paths, and excluded paths before starting a crawl or batch job.

## Reference(s):

- [ClawHub Firecrawl Skill](https://clawhub.ai/byungkyu/skills/firecrawl-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Firecrawl API Documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)
- [Firecrawl Dashboard](https://firecrawl.dev)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton CLI authentication, and a connected Firecrawl account.]

## Skill Version(s):

1.1.0 (source: server release evidence; artifact frontmatter lists 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
