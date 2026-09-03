## Description:

Yotta Memory provides a file-based local memory system for AI agents with public FACT memories, owner-scoped private PREF/BOUND/COMMIT memories, recall/context workflows, maintenance, consolidation, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give AI agents persistent local memory, restore cross-session context, and manage shared facts, private preferences, boundaries, commitments, and memory lifecycle tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates a persistent local memory system that can store personal context.

Mitigation: Use encrypted stores, review retained data through the user-facing view workflow, and avoid storing unnecessary sensitive information.

Risk: LAN-accessible MCP service mode can expose memory operations beyond the local machine.

Mitigation: Keep authentication enabled, prefer local binding unless LAN access is required, use per-agent tokens, and revoke tokens that are no longer needed.

Risk: Remembered self-profiles or context may include access tokens if users or agents save them as memory.

Mitigation: Do not store tokens in remembered profiles or memory entries; keep secrets in dedicated secret stores or environment-specific configuration.

Risk: Maintenance operations can alter private memories across agents according to the security guidance.

Mitigation: Do not allow remote agents to run archive, maintain --apply, or purge operations until owner-scoped maintenance behavior is fixed or independently reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [GitHub repository](https://github.com/YottaMeta/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [Protocol reference](references/protocol.md)
- [FAQ](references/faq.md)
- [Security review v0.8.5](docs/SECURITY-REVIEW-v0.8.5.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON/MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create, update, archive, consolidate, export, or import local memory files when executed.]

## Skill Version(s):

0.10.0 (source: SKILL.md frontmatter, package.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
