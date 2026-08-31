## Description:

元忆 yotta-memory provides boundary-aware, file-based long-term memory for AI agents, with local Markdown storage, public FACT memory, private PREF/BOUND/COMMIT memory, recall/context workflows, semantic retrieval, feedback, maintenance, and distillation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give agents a local, auditable memory workflow across sessions and projects. Agents can record important facts, restore context, manage private preferences, boundaries, and commitments, and connect to a shared memory service over MCP/LAN when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create durable local memories that may include sensitive personal or operational context.

Mitigation: Review memory entries regularly with the provided view, recall, forget, export, and archive workflows; avoid storing bearer tokens or other live secrets as memory content.

Risk: LAN service, MCP configuration, tokens, recovery keys, and autostart features expand the access surface beyond a single local command.

Mitigation: Keep services bound to localhost unless LAN access is required, review token and MCP settings before enabling remote use, store recovery keys offline, and revoke or disable access when it is no longer needed.

Risk: Direct shell edits to the memory store can bypass the documented owner and scope boundaries.

Mitigation: Use the yotta-memory CLI or MCP tools for memory reads and writes so boundary checks, indexing, encryption, and audit behavior remain in effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [npm package: @yottameta/yotta-memory](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [User Guide](USER_GUIDE.md)
- [Protocol Reference](references/protocol.md)
- [Security Review v0.8.5](docs/SECURITY-REVIEW-v0.8.5.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown/text guidance with inline shell commands and configuration snippets; CLI and MCP operations may create Markdown memory files, JSON exports, and local configuration changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local-first and may include persistent memory entries, recall/context summaries, profile summaries, audit/export files, and MCP setup guidance.]

## Skill Version(s):

0.8.5 (source: SKILL.md frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
