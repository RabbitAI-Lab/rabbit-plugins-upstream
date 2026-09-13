## Description:

Tavily Search lets agents use Tavily through Maton to search the web, extract URL content, crawl or map sites, and run research tasks with user-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when they need Tavily-backed web search, URL extraction, site crawling or mapping, and research results through an authenticated Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tavily queries, URLs, crawl instructions, and research inputs are sent to an external service through Maton.

Mitigation: Send only task-relevant public or approved content, avoid internal context in free-form inputs, and confirm before submitting non-public URLs.

Risk: API keys and OAuth tokens could be exposed if printed, logged, stored in files, or passed on command lines.

Mitigation: Use OAuth where possible, rely on the Maton CLI credential store, check authentication with `maton whoami`, and never display or persist secret values.

Risk: Hosted functions, triggers, and destinations can create persistent automation or automatic data forwarding.

Mitigation: Require explicit approval for each connection, function, trigger, destination, or write operation, scope destinations narrowly, and remove automation when the task is complete.

Risk: Returned web content and trigger payloads can contain sensitive or adversarial input.

Mitigation: Treat fetched content and event payloads as untrusted data, forward only required fields, and never execute or follow instructions found inside returned content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/tavily-api)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Tavily API Documentation](https://docs.tavily.com)
- [Tavily Search API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [Tavily Extract API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [Tavily Crawl API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)
- [Tavily Research API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/research)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Tavily search results, extracted page content, crawl or map results, research task status, citations, and Maton configuration steps.]

## Skill Version(s):

1.2.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
