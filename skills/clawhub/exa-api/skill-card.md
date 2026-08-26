## Description:

Exa API integration with managed API key authentication for neural web search, content retrieval, similar-page discovery, cited answers, and asynchronous research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Exa through Maton for web search, content extraction, similar-page discovery, cited answers, and research task workflows without directly handling Exa credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Maton and Exa accounts and API calls may incur provider costs.

Mitigation: Use OAuth where possible, start with read or list calls, and review cost-bearing research or content extraction requests before execution.

Risk: Creating a new Exa connection grants account access through Maton.

Mitigation: Require explicit user approval before running connection creation, choose the least privilege scopes available, and specify the intended connection when multiple accounts exist.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or process listings when the CLI is unavailable.

Mitigation: Prefer Maton OAuth and the CLI credential store; when raw HTTP is unavoidable, feed credentials through stdin, never print or persist them, and send them only to api.maton.ai.

Risk: External content returned by Exa may contain untrusted or adversarial instructions.

Mitigation: Treat fetched content as data, validate it before reuse, and do not execute or let it choose follow-up endpoints, recipients, or local commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/exa-api)
- [Maton](https://maton.ai)
- [Exa API Documentation](https://exa.ai/docs)
- [Exa API Reference](https://exa.ai/docs/reference/search)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Exa API responses with search results, citations, research task status, and cost fields.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
