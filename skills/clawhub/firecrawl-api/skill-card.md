## Description:

Firecrawl API integration with managed authentication for scraping, crawling, mapping, and searching web content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to access Firecrawl through Maton-managed authentication, extract web content, crawl sites, map URLs, and search the web while keeping approvals explicit for writes, new connections, and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scraping non-public, authenticated, or tokenized URLs can disclose sensitive targets and fetched content to Firecrawl as an external processor.

Mitigation: Confirm the exact URLs and content scope with the user before sending them to Firecrawl, and do not scrape authenticated or non-public targets unless the user explicitly approves that disclosure.

Risk: Broad crawls, browser sessions, hosted functions, triggers, and event destinations can spend credits or create ongoing automation.

Mitigation: Use narrow crawl limits and depths, review hosted functions and triggers before use, and require separate user approval for any automation or persistent destination.

Risk: Maton API keys and provider credentials can be exposed if placed in command lines, trigger destination headers, body templates, logs, or scripts.

Mitigation: Prefer OAuth and the CLI credential store, keep Maton credentials out of destination templates and logs, and use raw HTTP with environment-provided keys only where the CLI cannot be installed.

## Reference(s):

- [Firecrawl API Documentation](https://docs.firecrawl.dev/api-reference/v2-introduction)
- [Firecrawl Dashboard](https://firecrawl.dev)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/firecrawl-api)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Firecrawl request guidance, Maton CLI commands, hosted function examples, trigger setup notes, and risk-aware approval prompts.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
