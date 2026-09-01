## Description:

Exa API integration with managed API key authentication for neural web search, page content retrieval, similar-page discovery, AI-generated answers, and asynchronous research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to access Exa through Maton for web search, URL content extraction, similarity search, cited answers, and research workflows. It is suited to tasks that need current web context with user-approved authentication and cautious handling of API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exa API calls through Maton can incur provider costs for searches, content extraction, answers, or research tasks.

Mitigation: Review planned calls before execution, use limits where available, and confirm cost-bearing research or extraction requests with the user.

Risk: Authentication or connection setup can expose long-lived credentials or authorize the wrong Exa account if handled carelessly.

Mitigation: Use OAuth when possible, let the Maton CLI manage credentials, approve new Exa connections explicitly, and specify the intended connection when multiple accounts are available.

Risk: POST, PUT, PATCH, or DELETE requests can create or modify resources through the proxied API.

Mitigation: Default to read and list calls, then require user approval with the target, payload, and intended effect before any modifying request.

Risk: Web content returned by Exa may contain untrusted or adversarial instructions.

Mitigation: Treat returned content as data, validate it before reuse, and do not let fetched content choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/exa-api)
- [Maton Homepage](https://maton.ai)
- [Exa API Documentation](https://exa.ai/docs)
- [Exa API Reference](https://exa.ai/docs/reference/search)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Exa search results, extracted page content, cited answers, research task status, and cost metadata through Maton API calls.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
