## Description:

Memory Store helps agents store, retrieve, filter, archive, and restore structured cross-session memory through a local Node.js CLI under explicit or configured memory policies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[revolves](https://clawhub.ai/user/revolves)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give supported agents durable local memory for project decisions, preferences, workflows, debugging history, and handoffs while keeping recall and storage policy-controlled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory records are persistent plaintext files, and private visibility is a cooperative CLI filter rather than encryption.

Mitigation: Do not store secrets, credentials, tokens, raw personal data, or other confidential material; use operating-system controls or a secret manager for real confidentiality.

Risk: Automatic recall or storage can add unintended memory activity when stronger profiles are enabled.

Mitigation: Keep the memory profile at explicit or off unless automatic behavior is desired, and use balanced or proactive only with stable agent identity and policy awareness.

Risk: Concurrent writes to the same memory scope can lose updates because writes are atomic but not fully transaction locked.

Mitigation: Serialize writes to the same scope when possible and back up memory files before bulk maintenance, merge, archive, or delete operations.

## Reference(s):

- [Memory Store Skill Page](https://clawhub.ai/revolves/skills/memory-store-skill)
- [CLI Reference](references/cli.md)
- [Operations and Safety](references/operations.md)
- [Memory Schema](references/memory_schema.json)
- [Security Model](SECURITY.md)
- [npm Package](https://www.npmjs.com/package/memory-store-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer; memory records are stored as local plaintext JSON.]

## Skill Version(s):

1.1.1 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
