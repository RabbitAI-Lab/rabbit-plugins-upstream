## Description:

Tavily Search lets agents use a Maton-managed Tavily connection to search the web, extract URL content, crawl or map sites, and run research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to perform Tavily-backed web research, URL extraction, site crawling, site mapping, and research tasks through a managed Maton connection. It is suited to tasks where the user has authorized Tavily access and wants concise web-derived results or citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tavily and Maton process submitted searches, URLs, crawl targets, and research prompts.

Mitigation: Send only data the user intends to disclose, keep queries narrow, and avoid private or tokenized URLs unless the user deliberately wants Tavily to fetch them.

Risk: Connection creation or credential handling can authorize access or expose long-lived secrets.

Mitigation: Prefer OAuth, avoid printing or storing credentials, and require explicit user approval before creating or changing connections.

Risk: Hosted functions, triggers, and destinations can create persistent automated data flows.

Mitigation: Approve each function, trigger, or destination only after reviewing the destination, data fields, frequency, account identity, and network policy.

Risk: Fetched web content and event payloads are untrusted input.

Mitigation: Treat returned content as data rather than instructions, and validate it before using it in commands, prompts, or follow-up actions.

## Reference(s):

- [Tavily API Documentation](https://docs.tavily.com)
- [Tavily Search API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [Tavily Extract API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [Tavily Crawl API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)
- [Tavily Research API Reference](https://docs.tavily.com/documentation/api-reference/endpoint/research)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell command snippets, and API response excerpts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Tavily search, extract, crawl, map, or research results; returned content can include third-party web data and citations when requested.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
