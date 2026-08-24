## Description:

Use Hydrafetch for live web scraping, site mapping, search, structured extraction, brand and logo lookup, design systems, screenshots, and bulk crawl or batch jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hydrafetch](https://clawhub.ai/user/hydrafetch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Hydrafetch to retrieve current public-web content, map or crawl sites, run search and structured extraction, capture screenshots, and return source-grounded results or typed data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hydrafetch sends requested URLs, search terms, extraction tasks, and retrieved page content to an external service.

Mitigation: Use it for public-web data by default, and avoid private or sensitive pages unless the user intends to send that content to Hydrafetch.

Risk: Crawl, batch, screenshot, brand, styleguide, and extract operations can consume account credits.

Mitigation: Choose the narrowest Hydrafetch operation for the task and prefer map, scrape, or logo operations when they satisfy the request.

Risk: Fetched page content can contain untrusted text that attempts to steer the agent.

Mitigation: Treat scraped content as data rather than instructions, preserve source URLs, and distinguish page claims from agent inferences.

Risk: The Hydrafetch API key could be exposed if printed, logged, hardcoded, or placed in client-side code.

Mitigation: Read the key only from HYDRAFETCH_API_KEY and keep it out of logs, source files, and browser-executed code.

## Reference(s):

- [Hydrafetch Skill Page](https://clawhub.ai/hydrafetch/skills/hydrafetch)
- [Hydrafetch Documentation Index](https://hydrafetch.com/llms.txt)
- [Hydrafetch Agent Reference](https://hydrafetch.com/agents.md)
- [Hydrafetch API Documentation](https://docs.hydrafetch.com)
- [Hydrafetch OpenAPI Specification](https://api.hydrafetch.com/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and shell command snippets depending on the requested web operation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source URLs, response metadata, typed extraction results, crawl or batch job identifiers, and next-step commands.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
