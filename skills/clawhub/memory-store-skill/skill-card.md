## Description:

Memory Store helps agents store, retrieve, filter, rank, archive, and restore structured memories for multi-session and multi-agent workflows through a local Node.js CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[revolves](https://clawhub.ai/user/revolves)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and external users use this skill when an agent needs durable local memory for explicit recall, project handoff, preferences, decisions, debugging history, and repeatable workflows across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored memories are local plaintext JSON and private visibility is cooperative filtering, not encryption.

Mitigation: Do not store passwords, API keys, tokens, private keys, raw personal data, or other secrets; use an appropriate secret manager or operating-system access controls for confidential data.

Risk: Automatic memory behavior can retain information across sessions when an opt-in balanced or proactive profile is enabled.

Mitigation: Keep the effective profile at explicit or off unless automatic recall or storage is intended, and use explicit commands for user-directed memory actions.

Risk: Installer and sync commands can modify agent skill installation directories selected by the user.

Mitigation: Preview changes with --dry-run or --check and limit the target with --agent or --target instead of broad selectors unless every detected installation should be changed.

Risk: Concurrent writers to the same memory scope can cause last-write-wins lost updates.

Mitigation: Serialize writes to the same scope where possible and back up memory files before bulk merge, archive, delete, or recovery operations.

## Reference(s):

- [English README](README.en.md)
- [Security Model](SECURITY.md)
- [CLI Reference](references/cli.md)
- [Operations and Safety](references/operations.md)
- [Memory Schema](references/memory_schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Node.js 18 or newer is required; memory operations use local JSON stores and policy-controlled explicit or opted-in automatic behavior.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
