## Description:

Context.dev helps agents use live public-web search, scraping, crawling, structured extraction, document parsing, screenshots, brand intelligence, monitors, and asynchronous batches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contextdev](https://clawhub.ai/user/contextdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve current public-web data, convert pages and documents into Markdown, HTML, screenshots, or typed JSON, and manage website monitors or high-volume batches through Context.dev.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may call Context.dev for live public-web tasks and consume API quota.

Mitigation: Configure an API key only when intended and review broad crawl, monitor, or batch requests before approval.

Risk: Monitor or batch changes can create, update, run, cancel, or delete tracked work.

Mitigation: Ask for confirmation before mutating monitors or batches unless the user explicitly requested the change.

Risk: Scraped or extracted web content can be incomplete, stale, or untrusted.

Mitigation: Preserve source URLs, separate facts from inference, validate structured outputs against the requested schema, and prefer authoritative sources for research.

## Reference(s):

- [Context.dev documentation index](https://docs.context.dev/llms.txt)
- [Context.dev full agent reference](https://docs.context.dev/skill.md)
- [Context.dev API documentation](https://docs.context.dev)
- [Context.dev MCP server](https://mcp.context.dev/mcp)
- [ClawHub skill page](https://clawhub.ai/contextdev/skills/context-dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, code snippets, shell commands, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source URLs, response metadata, created monitor or batch identifiers, and next inspection commands when relevant.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
