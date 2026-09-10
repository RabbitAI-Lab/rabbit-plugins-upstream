## Description:

Exa API integration with managed API key authentication for neural web search, page content retrieval, similar-page discovery, cited answers, and async research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Exa through Maton for web search, content extraction, similarity search, cited question answering, and longer-running research tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton or provider credentials could be exposed if tokens or MATON_API_KEY are printed, logged, persisted, or passed on a command line.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the OS credential store, check authentication with maton whoami, and never print or persist credential values.

Risk: API requests could target the wrong Maton profile or Exa connection when multiple accounts or connections exist.

Mitigation: Specify the intended profile and connection before making calls, and verify active connections before acting.

Risk: Connection creation or write-like API requests may authorize access or cause side effects without clear user intent.

Mitigation: Require explicit user approval for connection creation and for POST, PUT, PATCH, or DELETE requests after checking the target account and payload.

Risk: Content returned by Exa may contain untrusted or adversarial instructions.

Mitigation: Treat fetched content as data, do not execute or follow instructions from API results, and validate data before using it in commands or follow-up requests.

## Reference(s):

- [Exa API Documentation](https://exa.ai/docs)
- [Exa API Reference](https://exa.ai/docs/reference/search)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/exa-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API request examples, authentication guidance, connection management steps, endpoint notes, error handling, and risk controls.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
