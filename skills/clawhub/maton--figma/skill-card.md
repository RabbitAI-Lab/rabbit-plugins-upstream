## Description:

Figma API integration with managed OAuth for inspecting design files, rendering nodes as images, managing comments and reactions, and reading published components and styles through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and design operations teams use this skill to inspect Figma files from supplied file URLs, export node images, review comments, and audit published components and styles through authenticated Figma API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect an agent to a user's Figma account through Maton.

Mitigation: Prefer OAuth, review the account and scopes during connection, and require explicit user approval before creating a Figma connection.

Risk: Comments, reactions, dev-resource changes, connection creation, and deletion can affect shared Figma workspaces.

Mitigation: Default to read and list operations, then confirm the target resource, payload, and intended effect before any write or destructive operation.

Risk: API keys and provider-issued tokens can leak if printed, logged, persisted, or passed on command lines.

Mitigation: Use the Maton CLI credential store where possible; when raw HTTP is required, read the key from the environment inside the process and never display or persist it.

Risk: Figma comments and user endpoints can expose personal data and untrusted user-generated content.

Mitigation: Return only the fields needed for the task, avoid forwarding raw responses, and treat file names, node names, and comments as data rather than instructions.

Risk: Some Figma endpoints may be unavailable or return success-shaped responses that still contain per-item errors.

Mitigation: Check response bodies for null values and errors, confirm file access with metadata calls, and respect documented Figma and Maton rate limits.

## Reference(s):

- [Figma skill on ClawHub](https://clawhub.ai/maton/skills/figma)
- [Maton homepage](https://maton.ai)
- [Figma REST API Introduction](https://developers.figma.com/docs/rest-api/)
- [Figma File Endpoints](https://developers.figma.com/docs/rest-api/file-endpoints/)
- [Figma Comment Endpoints](https://developers.figma.com/docs/rest-api/comments-endpoints/)
- [Figma Component and Style Endpoints](https://developers.figma.com/docs/rest-api/component-endpoints/)
- [Figma Dev Resource Endpoints](https://developers.figma.com/docs/rest-api/dev-resources-endpoints/)
- [Figma Rate Limits](https://developers.figma.com/docs/rest-api/rate-limits/)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON request bodies, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Figma API request and response summaries; should keep credentials and unnecessary personal data out of output.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
