## Description:

Exa API integration with managed API key authentication for neural web search, page content retrieval, similar-page discovery, AI-generated answers with citations, and async research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the web, retrieve source contents, find similar pages, generate cited answers, and run Exa research tasks through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External packages and Maton CLI installation may introduce supply-chain risk.

Mitigation: Install only from verified Maton sources and avoid sudo or administrator installation unless necessary.

Risk: Long-lived API keys or printed tokens could expose Maton or connected Exa credentials.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, and do not print, log, export, or persist credential values.

Risk: Fetched web content may contain adversarial instructions or prompt injection.

Mitigation: Treat API results as untrusted data and do not let fetched content choose follow-up actions, endpoints, commands, or credential handling.

Risk: Connection creation or modifying API calls can authorize access or create side effects.

Mitigation: Confirm any new Exa connection and every POST, PUT, PATCH, or DELETE request with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/exa-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Exa API Documentation](https://exa.ai/docs)
- [Exa API Reference](https://exa.ai/docs/reference/search)
- [Exa Dashboard](https://dashboard.exa.ai)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, SDK examples, API request payloads, and guidance for handling returned web content and credentials.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
