## Description:

Yuanyi (yotta-memory) provides boundary-aware, file-based memory for AI agents, using local Markdown storage, recall and remember workflows, and public FACT versus private PREF/BOUND/COMMIT isolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give AI agents persistent local memory across sessions, recover context at the start of work, save important facts or preferences during work, and archive handoff notes at wrap-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to persist personal or sensitive memory across agent sessions.

Mitigation: Store only information the user wants retained, prefer encrypted private memory, and use the provided review, export, forget, and archive flows to inspect or remove memory.

Risk: LAN serving, bearer tokens, and no-auth modes can expose memory if configured broadly.

Mitigation: Prefer localhost or stdio, avoid 0.0.0.0 and --no-auth unless explicitly required, and manage per-agent tokens carefully.

Risk: Agent configuration edits and external distillation commands can change how agents access memory or execute trusted tooling.

Mitigation: Review MCP configuration edits manually and use distill --model only with commands the user explicitly trusts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [README](README.md)
- [User guide](USER_GUIDE.md)
- [Protocol specification](references/protocol.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide agents to call yotta-memory CLI or MCP operations for memory recall, persistence, context generation, profile generation, maintenance, and archival.]

## Skill Version(s):

0.8.3 (source: SKILL.md frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
