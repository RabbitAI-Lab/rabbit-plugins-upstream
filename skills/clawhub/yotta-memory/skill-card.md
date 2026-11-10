## Description:

Yuanyi gives AI agents persistent, file-based memory with shared facts and private per-agent preferences, boundaries, and commitments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use the skill to restore context between sessions, capture durable facts and preferences, and maintain an agent memory store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private memories may be exposed or access restrictions bypassed.

Mitigation: Wait for fixes before storing sensitive information. For evaluation, use a disposable local store over stdio with --tools core, and do not rely on token --scope for access control.

Risk: An exposed remote console or connection may reveal memory data.

Mitigation: Keep the web console on loopback and stop it after use; protect remote connections with an authenticated encrypted tunnel.

Risk: A compromised, damaged, or incorrectly operated store may undermine data recovery.

Mitigation: Keep independent backups and pin the reviewed package version.

Risk: Untrusted exports or unsafe memory operations may introduce harmful content or expose private entries.

Mitigation: Do not import untrusted exports. Follow the documented owner and authorization boundaries when using private-memory and distillation features.

## Reference(s):

- [Memory protocol](references/protocol.md)
- [Provider protocol](references/provider-protocol.md)
- [Frequently asked questions](references/faq.md)
- [Project documentation](https://github.com/YottaMeta/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and structured reports for operating an agent memory store]

## Skill Version(s):

0.23.3 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
