## Description:

元忆 yotta-memory provides boundary-aware, file-based persistent memory for AI agents, using local Markdown files, shared FACT records, and private PREF, BOUND, and COMMIT records for recall, context restoration, profile aggregation, feedback, maintenance, and consolidation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to give AI agents local, auditable, cross-session memory with shared facts and per-agent private records. It supports recalling context at session start, saving important information during work, generating profile and context summaries, and maintaining or consolidating old memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores persistent memory that may contain personal details, preferences, commitments, and agent identity data.

Mitigation: Install only when a persistent local memory store is acceptable, keep the store under user control, use encrypted private storage when appropriate, and avoid storing bearer tokens in memory records.

Risk: LAN or HTTP MCP serving can expose memory data beyond the local machine if configured broadly or run without authentication.

Mitigation: Prefer local stdio or localhost use, bind services to 127.0.0.1 when possible, avoid LAN mode unless the exposure is understood, and do not use --no-auth except in a trusted environment.

Risk: MCP configuration edits, autostart setup, and token registration can create durable access paths to the memory store.

Mitigation: Review MCP config changes, autostart setup, bearer-token handling, and each agent identity before approving them; revoke or rotate tokens that are no longer needed.

Risk: Maintenance commands such as archive, maintain --apply, consolidate --apply, and purge can move, merge, summarize, or delete memory records.

Mitigation: Use dry-run previews where available, keep backups before applying maintenance, verify batch audit output, and avoid purge unless irreversible deletion is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [npm package: @yottameta/yotta-memory](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [Agent Skills standard](https://agentskills.io/)
- [User Guide](USER_GUIDE.md)
- [Protocol Reference](references/protocol.md)
- [FAQ](references/faq.md)
- [Security Review v0.8.5](docs/SECURITY-REVIEW-v0.8.5.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI and MCP command examples, plus generated context, recall, profile, feedback, maintenance, and consolidation text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to create, retrieve, summarize, archive, export, and import local memory records; private memory may contain sensitive personal data.]

## Skill Version(s):

0.11.0 (source: SKILL.md frontmatter, package.json, CHANGELOG.md, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
