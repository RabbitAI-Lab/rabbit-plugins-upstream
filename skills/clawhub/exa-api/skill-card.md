## Description:

Exa API integration with managed API key authentication for neural web search, page content retrieval, similar page discovery, AI-generated answers, and async research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the web with Exa, retrieve URL contents, find similar pages, request answer-style research results with citations, and run async research tasks through an authenticated Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, URLs, and research instructions are sent to Exa and may contain private context.

Mitigation: Review each query or URL before sending sensitive data and use only the fields needed for the task.

Risk: Raw API keys can expose long-lived credentials when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Functions, triggers, destinations, and other persistent automation can continue acting or forwarding data after setup.

Mitigation: Require explicit confirmation before creating or updating persistent automation, disclose the destination and data flow, and remove automation when it is no longer needed.

## Reference(s):

- [Exa API Documentation](https://exa.ai/docs)
- [Exa API Reference](https://exa.ai/docs/reference/search)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Exa Skill on ClawHub](https://clawhub.ai/byungkyu/skills/exa-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, API calls]

**Output Format:** [Markdown with inline shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Exa connection.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
