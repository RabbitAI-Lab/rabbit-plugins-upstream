## Description:

Firecrawl API integration with managed authentication for scraping webpages, crawling websites, mapping site URLs, searching the web, and extracting structured content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access Firecrawl through Maton-managed authentication for web scraping, crawling, site mapping, search, browser sessions, and structured extraction tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected target URLs, crawl parameters, prompts, and extracted results through Maton and Firecrawl.

Mitigation: Install only after confirming that this data flow is acceptable for the intended use case and avoid sending sensitive or restricted content unless approved.

Risk: Crawls, batch jobs, browser actions, agent jobs, webhooks, custom headers, and modifying requests can consume credits or create side effects.

Mitigation: Require user confirmation before these operations, define crawl limits and scope up front, and prefer read/list calls before changes.

Risk: Long-lived API keys or provider-issued tokens can be exposed if printed, logged, persisted, or sent to the wrong host.

Mitigation: Use OAuth where possible, let the CLI and operating system credential store handle secrets, and never print, persist, or transmit credentials outside the documented Maton flow.

## Reference(s):

- [ClawHub Firecrawl Skill](https://clawhub.ai/byungkyu/skills/firecrawl-api)
- [Maton Homepage](https://maton.ai)
- [Firecrawl API Documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)
- [Firecrawl Dashboard](https://firecrawl.dev)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Firecrawl request plans, Maton CLI commands, JSON request bodies, and summarized API results.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
