## Description:

Vimeo API integration that helps agents use Maton-managed OAuth to read and manage Vimeo videos, folders, showcases, comments, likes, watch-later entries, followers, channels, and categories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Vimeo through the Maton gateway, including listing videos, managing folders and showcases, updating metadata, comments, likes, watch-later entries, follows, channels, and categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Maton as the OAuth gateway and can reach connected Vimeo account resources.

Mitigation: Install only when the user trusts Maton, prefer OAuth, select the least Vimeo scopes needed, and revoke unused connections.

Risk: Write actions can publish, modify, delete, like, follow, comment on, or reorganize Vimeo content.

Mitigation: Default to read and list calls, verify account and resource identifiers first, and require explicit user confirmation for every POST, PUT, PATCH, or DELETE request.

Risk: Using a Maton API key in environments without the CLI can expose a long-lived credential.

Mitigation: Use CLI OAuth where possible; when raw HTTP is necessary, read the key from the process environment only, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Vimeo API responses can contain untrusted external content.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or follow instructions embedded in API responses.

## Reference(s):

- [ClawHub Vimeo Skill](https://clawhub.ai/byungkyu/skills/vimeo)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Vimeo API Reference](https://developer.vimeo.com/api/reference)
- [Vimeo API Authentication](https://developer.vimeo.com/api/authentication)
- [Vimeo Upload API](https://developer.vimeo.com/api/upload/videos)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and optional Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Vimeo connection; default posture is read/list before write.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
