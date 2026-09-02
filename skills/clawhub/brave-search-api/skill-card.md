## Description:

Brave Search API integration with managed authentication for web, image, news, video, local, autosuggest, spellcheck, and summarizer queries through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Brave web, images, news, videos, local results, suggestions, spellcheck, and summaries from an agent workflow through managed Maton authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authentication with Maton and authorization of a Brave Search connection.

Mitigation: Prefer OAuth, require explicit user approval before creating a connection, and select only the scopes needed for the current task.

Risk: Long-lived API keys can be exposed through environment variables, command arguments, logs, or persisted files.

Mitigation: Use OAuth and the credential store when possible; if raw HTTP is unavoidable, do not print, log, persist, or pass the key on the command line.

Risk: Search results and other API responses may contain untrusted external content.

Mitigation: Treat returned content as data, avoid executing or evaluating it, and do not let fetched content choose follow-up endpoints or recipients.

Risk: Passthrough access includes additional Brave Search endpoints such as local POI, autosuggest, spellcheck, and summaries.

Mitigation: Review endpoint paths and payloads before use, default to read/list calls, and confirm any write, deletion, or new connection with the user.

## Reference(s):

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brave-search-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance and commands for authenticated Brave Search API calls; API responses are JSON from Brave Search or Maton passthrough endpoints.]

## Skill Version(s):

1.1.0 (source: server release metadata; skill frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
