## Description:

Confluence API integration with managed OAuth for managing pages, spaces, blogposts, comments, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Confluence Cloud content through Maton-managed OAuth, including reading, creating, updating, and deleting pages, spaces, blogposts, comments, attachments, and related metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Confluence content through Maton-mediated access.

Mitigation: Prefer read and list operations first, confirm the exact page, space, comment, payload, and intended effect before any write or delete, and revoke unused Confluence connections when finished.

Risk: Confluence or Maton credentials could be exposed if copied into logs, command arguments, files, or broad environment variables.

Mitigation: Prefer OAuth through the Maton CLI, use the operating system credential store, avoid printing or persisting tokens, and choose the narrowest available OAuth scopes.

Risk: API responses may contain untrusted Confluence content that could try to steer later agent behavior.

Mitigation: Treat returned page, comment, attachment, and webhook content as data; do not execute it or let it select follow-up endpoints, recipients, or commands without validation.

## Reference(s):

- [Confluence Skill on ClawHub](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton Homepage](https://maton.ai)
- [Confluence REST API V2 Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Confluence REST API V2 Reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)
- [Confluence Storage Format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Confluence API paths, Maton CLI commands, request payload examples, and safety checks for credential handling and user approval.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
