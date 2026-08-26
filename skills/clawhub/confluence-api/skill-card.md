## Description:

Confluence API integration with managed OAuth for managing pages, spaces, blogposts, comments, and attachments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, create, update, and delete Confluence Cloud content through Maton-managed OAuth. It is suited to workflows that need Confluence API access while keeping credentials in the Maton CLI and requiring explicit approval for new connections or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad authenticated Confluence API passthrough may exceed the narrower content-management scope a reader expects.

Mitigation: Install only when Maton-mediated OAuth access to the intended Confluence account is acceptable; prefer read-only scopes and review the requested endpoint before use.

Risk: Write and delete calls can modify or remove Confluence content.

Mitigation: Confirm every write or delete with exact resource IDs, account or connection, payload, and intended effect before execution.

Risk: Using the raw API-key fallback can expose a long-lived Maton credential.

Mitigation: Use the Maton CLI with OAuth where possible and avoid the raw API-key fallback unless the CLI cannot be used.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Confluence REST API V2 Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Confluence REST API V2 Reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, and API path examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Confluence connection; write operations should be confirmed with exact resource IDs and payloads.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
