## Description:

Yuanyi yotta-memory gives AI agents a boundary-aware, file-based long-term memory workflow for cross-session context recovery, semantic recall, verified memory writes, archiving, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to add local-first persistent memory to AI agent workflows, including start-of-session context recovery, saving durable facts or preferences, and maintaining auditable memory stores. It is intended for agents that can run the yotta-memory CLI or MCP tools while respecting public and private memory boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private-memory isolation and secret-handling controls have verified weaknesses in the scanned release.

Mitigation: Review before installation, use encrypted private memory, keep bearer tokens out of memory entries, and require explicit agent keys for private access.

Risk: Shared or multi-agent deployments can expose more capability than needed for routine memory use.

Mitigation: Run MCP in core mode for daily use and reserve full maintenance tools for reviewed, owner-approved maintenance sessions.

Risk: Unpinned installs can pull a different package version than the reviewed artifact.

Mitigation: Pin package version 0.16.5 when installing and verify the installed CLI, skill manifest, and changelog versions match before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project Homepage](https://github.com/YottaMeta/yotta-memory)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [User Guide](USER_GUIDE.md)
- [Protocol Reference](references/protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline CLI commands and MCP configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run yotta-memory CLI or MCP tools that read, write, recall, archive, back up, or diagnose local memory files.]

## Skill Version(s):

0.16.5 (source: SKILL.md frontmatter, package.json, skill-manifest.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
