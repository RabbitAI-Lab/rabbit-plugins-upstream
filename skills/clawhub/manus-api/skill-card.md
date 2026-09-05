## Description:

Manus AI Agent API integration with managed API key authentication for creating and managing AI agent tasks, projects, files, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access Manus through Maton, list or create tasks and projects, manage files, and configure webhooks while keeping credentials behind the gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a connected Manus account through Maton, including write-capable API operations.

Mitigation: Install only when Manus access through Maton is intended, use least-privilege connections, and confirm every create, update, upload, webhook, or delete action before execution.

Risk: The Maton passthrough can reach endpoints beyond the examples if the connection permits.

Mitigation: Default to documented read and list calls, verify the endpoint and payload with the user, and limit connection scopes where Manus offers scope selection.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI; use raw HTTP only where the CLI cannot be installed, avoid printing or logging the key, and rotate it if exposed.

Risk: API responses and webhook payloads may contain personal data or adversarial content.

Mitigation: Treat returned content as untrusted data, extract only fields needed for the task, and do not execute or persist raw responses unless explicitly requested.

## Reference(s):

- [Manus API Overview](https://open.manus.im/docs)
- [Manus API Reference](https://open.manus.im/docs/api-reference)
- [Manus Website](https://manus.im)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/manus-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline shell commands, HTTP examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON from Manus and Maton APIs.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
