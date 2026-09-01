## Description:

here.now lets agents publish websites and files to live URLs in seconds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to publish local files, folders, websites, and private Drive content to here.now URLs, configure access, and manage updates or workspace-owned sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected local files or folders to here.now and make them available through live URLs.

Mitigation: Review the publish target and intended access mode before publishing, especially when files may contain private or sensitive data.

Risk: The skill can store a here.now API key locally for future authenticated publishing.

Mitigation: Confirm credential saving before use and avoid passing API keys on command lines in interactive sessions.

Risk: Drive sharing can create broad or writable access tokens for private Drive contents.

Mitigation: Use the narrowest path prefix, short TTLs, and read-only permissions unless write access is required.

Risk: Delete and overwrite operations can remove or replace remote Drive or Site content.

Mitigation: Confirm destructive actions explicitly and reconcile version conflicts before using overwrite behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)
- [here.now docs](https://here.now/docs)
- [here.now OpenAPI schema](https://here.now/openapi.json)
- [here.now workspace docs](https://here.now/docs#workspaces)
- [here.now access control docs](https://here.now/docs#access-control)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and live URL strings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include site URLs, workspace URLs, Drive share blocks, publish status details, and access-control guidance.]

## Skill Version(s):

1.26.0 (source: server release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
