## Description:

Microsoft OneNote API integration with managed OAuth via Microsoft Graph for accessing notebooks, sections, section groups, and pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect a Microsoft OneNote account through Maton, inspect notebooks and sections, and create or update note pages after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad Microsoft Graph passthrough could exceed the intended OneNote task if OAuth scopes are broad.

Mitigation: Confirm least-privilege OneNote scopes before connecting, start with read-only calls, and require explicit approval before POST, PUT, PATCH, or DELETE.

Risk: Long-lived API keys or surfaced credentials could be mishandled when CLI OAuth is unavailable.

Mitigation: Prefer OAuth through the Maton CLI credential store; use raw API-key access only when the CLI cannot be used and never print, persist, or pass tokens on command lines.

Risk: Fetched OneNote content may contain untrusted instructions or malformed content.

Mitigation: Treat API responses as data, validate identifiers and payloads, and do not let fetched content choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/one-note)
- [Maton Homepage](https://maton.ai)
- [OneNote API Overview](https://learn.microsoft.com/en-us/graph/integrate-with-onenote)
- [OneNote REST API Reference](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [Page HTML Reference](https://learn.microsoft.com/en-us/graph/onenote-input-output-html)
- [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [shell commands, code, configuration, guidance]

**Output Format:** [Markdown with bash, JSON, Python, JavaScript, and HTML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [OneNote API responses may include JSON metadata or HTML page content.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
