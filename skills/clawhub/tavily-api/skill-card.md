## Description:

Tavily Search helps agents use Tavily through Maton to search the web, extract URL content, crawl and map sites, and run research tasks with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a task needs web search, citation-oriented research, URL content extraction, site crawling, or site mapping through a Tavily account connected with Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or provider tokens could be exposed through logs, files, shell history, or raw environment variables.

Mitigation: Prefer Maton OAuth through the CLI and its credential store; do not print, persist, inspect, or pass credentials on command lines, and use the raw MATON_API_KEY fallback only when the CLI cannot be used.

Risk: A new Tavily connection or modifying API call could affect the wrong account or create unintended side effects.

Mitigation: Require explicit user approval before creating connections or running POST, PUT, PATCH, or DELETE operations, and specify the intended connection or Maton profile when more than one exists.

Risk: Web content returned by Tavily may contain adversarial instructions or untrusted data.

Mitigation: Treat fetched content as data, not instructions; do not execute it or let it choose follow-up endpoints, recipients, commands, or prompts without validation.

## Reference(s):

- [Tavily API Documentation](https://docs.tavily.com)
- [Tavily Search API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [Tavily Extract API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [Tavily Crawl API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)
- [Tavily Research API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/research)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and text or markdown API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a connected Tavily account.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
