## Description:

Quo API integration with managed OAuth for managing calls, messages, contacts, conversations, and call recordings or transcripts through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent access a connected Quo business phone account through Maton for SMS, calls, contacts, conversations, recordings, and transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to Quo business phone-system data through Maton.

Mitigation: Install only when Quo access is intended, use least-privilege Quo scopes, and connect only the accounts needed for the current task.

Risk: Agent actions can send messages, change contacts, delete records, or create new connections.

Mitigation: Require explicit user confirmation before sending messages, changing contacts, deleting records, creating connections, or performing other write operations.

Risk: Maton credentials or API keys can be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Prefer the Maton CLI OAuth flow, avoid exposing credential values, and handle any API-key fallback as a sensitive secret.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/quo)
- [Maton Homepage](https://maton.ai)
- [Quo API Introduction](https://www.quo.com/docs/mdx/api-reference/introduction)
- [Quo API Authentication](https://www.quo.com/docs/mdx/api-reference/authentication)
- [Quo Support Center](https://support.quo.com/core-concepts/integrations/api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user confirmation before writes or new connections.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
