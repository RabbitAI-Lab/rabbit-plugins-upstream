## Description:

Coda API integration with managed OAuth for reading, creating, updating, and deleting Coda docs, pages, tables, rows, formulas, controls, analytics, and permissions through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Coda workspaces through authenticated API calls, including discovery, retrieval, creation, updates, deletion, sharing, and analytics tasks. It is intended for workflows where the agent should use read/list calls first and request confirmation before any write, deletion, connection, sharing, or permission change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Coda account may allow both reads and modifications, including endpoints beyond the documented examples when the connection permits them.

Mitigation: Prefer OAuth, select the narrowest available scopes, pin the intended connection when multiple accounts exist, and treat the documented endpoints as the intended surface rather than a hard technical limit.

Risk: Create, update, delete, sharing, and permission operations can alter or remove Coda workspace data.

Mitigation: Use read and list calls first, verify resource identifiers and current state, and require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, DELETE, sharing, or permission change.

Risk: Raw HTTP fallback with a Maton API key can expose a long-lived credential if the key is printed, logged, persisted, or passed on a command line.

Mitigation: Use CLI OAuth where possible; when raw HTTP is required, read the key only from the process environment, never print or persist it, and send it only to api.maton.ai.

Risk: Coda API responses may contain personal, workspace, document, or permission data.

Mitigation: Extract only the fields needed for the task, avoid dumping full response bodies, and do not write raw responses to logs or files unless the user explicitly asks.

## Reference(s):

- [ClawHub Coda Skill](https://clawhub.ai/byungkyu/skills/coda-api)
- [Maton Homepage](https://maton.ai)
- [Coda API Documentation](https://coda.io/developers/apis/v1)
- [Coda API Postman Collection](https://www.postman.com/codaio/coda-workspace/collection/0vy7uxn/coda-api)
- [Coda API Python Library](https://codaio.readthedocs.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API-call guidance and command examples; Coda API responses may contain personal or workspace data and should be minimized to fields needed for the task.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
