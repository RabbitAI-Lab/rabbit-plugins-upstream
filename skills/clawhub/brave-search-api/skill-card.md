## Description:

Brave Search API integration with managed authentication for web, image, news, video, local, autosuggest, spellcheck, and summary search through Maton OAuth and CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Brave Search through Maton for web, image, news, video, local, suggestion, spellcheck, and summary results while relying on managed authentication. It is suited for search and retrieval tasks where the agent should start with read-oriented API calls and ask for approval before new connections or modifying requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton or provider credentials may be exposed if printed, stored in files, passed on command lines, or copied from credential stores.

Mitigation: Prefer OAuth login, let the CLI and operating system credential store handle secrets, and never print, persist, export, or inspect credentials.

Risk: A new Brave Search connection or ambiguous default connection could access the wrong account.

Mitigation: Require explicit user approval before creating a connection, use least privilege, and specify the intended profile or connection when multiple accounts exist.

Risk: External search results can contain adversarial or misleading content.

Mitigation: Treat returned content as untrusted data, do not execute or follow instructions found in results, and validate data before using it in commands or prompts.

Risk: The generic API path can call documented Brave Search endpoints beyond the headline search examples.

Mitigation: Confirm intent before POST, PUT, PATCH, or DELETE calls and describe the endpoint, payload, and expected effect before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Maton](https://maton.ai)
- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Brave Search connection for authenticated API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
