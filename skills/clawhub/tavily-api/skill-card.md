## Description:

Tavily Search helps agents use the Tavily API through Maton to search the web, extract URL content, crawl sites, map site structure, and run research tasks with citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform web search, URL extraction, site crawling, site mapping, and research workflows through a managed Tavily connection. It is suited for tasks that need current web content, source discovery, extracted page text, or cited research output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton credentials or raw MATON_API_KEY values could be exposed if printed, logged, persisted, or passed on a command line.

Mitigation: Prefer Maton CLI OAuth with the operating system credential store; never print, log, persist, or inspect credential values, and use the raw API key fallback only when the CLI cannot be used.

Risk: Creating or deleting connections, or sending POST, PUT, PATCH, or DELETE requests, can change account state or trigger side effects.

Mitigation: Default to read and list calls, confirm connection creation and deletion explicitly, and verify the target connection ID, payload, and intended effect before any modifying request.

Risk: External web content returned by Tavily may contain adversarial or misleading instructions.

Mitigation: Treat fetched content as untrusted data; do not execute it, eval it, or let it choose endpoints, recipients, shell commands, or follow-up actions.

Risk: Ambiguous Maton profiles or multiple Tavily connections could send requests through the wrong account.

Mitigation: Specify the intended profile and connection when more than one exists, and verify account context before making API calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/tavily-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Tavily API Documentation](https://docs.tavily.com)
- [Tavily Search API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [Tavily Extract API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [Tavily Crawl API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)
- [Tavily Research API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/research)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and optional Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Tavily connection; API responses may include external web content and citations.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
