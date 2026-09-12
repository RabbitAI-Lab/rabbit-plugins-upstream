## Description:

Tavily Search helps agents use Tavily through Maton to run web search, extract URL content, crawl or map sites, and perform research tasks with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they need current web search, page extraction, website crawl or map results, or Tavily research outputs through a managed Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking Maton from an unverified source could expose account access or credentials.

Mitigation: Verify the Maton package source before installation and prefer OAuth authentication over long-lived API keys.

Risk: Long-lived API keys can leak through environment variables, logs, command history, or pasted output.

Mitigation: Use the CLI credential store when possible; never print, persist, or pass keys on command lines, and rotate any key that was exposed.

Risk: The Maton API passthrough can reach endpoints beyond the documented Tavily examples when the connection allows it.

Mitigation: Use least-privilege connections, specify the intended connection or profile when needed, and require explicit user confirmation before any state-changing API call.

Risk: Connection creation, deletion, or authorization changes can affect the user's Tavily access.

Mitigation: Confirm the exact account, connection, resource identifier, payload, and intended effect before creating, deleting, or modifying a connection.

Risk: Web content returned by Tavily may contain untrusted or adversarial text.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and extract only the fields needed for the task.

## Reference(s):

- [Tavily Search on ClawHub](https://clawhub.ai/byungkyu/skills/tavily-api)
- [Maton Homepage](https://maton.ai)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Tavily search results, extracted page content, crawled page content, discovered URLs, synthesized research text, and source citations.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
