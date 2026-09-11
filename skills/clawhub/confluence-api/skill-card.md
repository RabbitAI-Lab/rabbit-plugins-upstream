## Description:

Confluence API integration with managed OAuth for managing pages, spaces, blogposts, comments, and attachments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Confluence Cloud content through managed OAuth, including listing, reading, creating, updating, and deleting pages, spaces, blogposts, comments, attachments, and related properties.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking the Maton CLI or SDK from an unverified source could run unexpected third-party code.

Mitigation: Verify the Maton package source before installation and use the documented package channels.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, shell history, files, or child processes.

Mitigation: Prefer OAuth, keep credentials in the CLI-managed credential store, never print or persist token values, and rotate any key that was exposed.

Risk: Write or delete operations can modify or remove Confluence content in the connected account.

Mitigation: Default to read and list calls, confirm every write or delete with the user, and include the target resource ID, payload, and intended effect before execution.

Risk: Requests may affect the wrong Confluence site or account when multiple Maton profiles or connections exist.

Mitigation: Use explicit profile and connection identifiers when ambiguity exists and verify the target account before changes.

Risk: Confluence content returned by the API can contain untrusted instructions or data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and validate values before using them in follow-up API calls.

## Reference(s):

- [Confluence REST API V2 Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Confluence REST API V2 Reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)
- [Confluence Storage Format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/confluence-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON request and response examples, and SDK snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Confluence API calls that read, create, update, or delete remote content after user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
