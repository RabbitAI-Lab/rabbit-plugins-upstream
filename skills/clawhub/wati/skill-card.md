## Description:

WATI provides a Maton-managed integration for sending WhatsApp messages, managing contacts, and working with message templates through CLI, SDK, or raw HTTP guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate WATI accounts through Maton-managed authentication: list contacts, templates, and messages; send session or template messages; update contacts; and troubleshoot API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real WhatsApp messages, including bulk template messages, and modify WATI contacts.

Mitigation: Default to read/list operations and confirm recipients, target resources, payloads, and intended effects before any write.

Risk: Long-lived Maton API keys can be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Use OAuth where possible; when an API key is unavoidable, keep it out of logs and command arguments and send it only to api.maton.ai.

Risk: Stale or ambiguous Maton connections can route actions to the wrong WATI account or keep unused authorization active.

Mitigation: Specify the intended connection when multiple connections exist and revoke unused Maton connections when finished.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/wati)
- [Maton homepage](https://maton.ai)
- [WATI API Documentation](https://docs.wati.io/reference/introduction)
- [WATI Help Center](https://docs.wati.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, and small code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized WATI connection; defaults to read/list guidance and requires user approval for writes.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
