## Description:

Box API integration with managed OAuth for managing files, folders, collaborations, shared links, and cloud storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access a connected Box account through Maton OAuth, inspect account and folder state, and manage files, folders, collaborations, shared links, uploads, downloads, trash, events, and webhooks with user confirmation for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected Box account can expose or modify files, folders, collaborations, shared links, webhooks, and trash contents.

Mitigation: Review requested OAuth scopes, prefer read-only access where possible, specify the intended connection when multiple accounts exist, and require clear confirmation before uploads, deletions, shared links, collaborations, webhooks, or other write operations.

Risk: Long-lived Maton API keys can be leaked through logs, command lines, shell history, or persisted configuration.

Mitigation: Prefer Maton OAuth through the CLI, avoid printing or persisting credentials, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: Box content and webhook payloads may contain untrusted external data.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and validate identifiers and payloads before follow-up actions.

## Reference(s):

- [Box skill page](https://clawhub.ai/byungkyu/skills/box)
- [Box API Reference](https://developer.box.com/reference)
- [Box Developer Documentation](https://developer.box.com/guides)
- [Box Authentication Guide](https://developer.box.com/guides/authentication)
- [Box SDKs](https://developer.box.com/sdks-and-tools)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list guidance and require explicit user confirmation before connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
