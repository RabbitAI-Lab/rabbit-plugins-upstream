## Description:

Evermind gives AI agents local cross-session memory recovery by loading core identity, rules, todos, journals, and handover state while using a hash index to avoid re-reading unchanged secondary files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and power users use this skill to restore working context at the start of a new agent session, preserve task handoffs, and reduce repeated context reads. It is intended for local file-based memory layouts across tools such as Hermes, OpenClaw, Claude Code, Cursor, Codex, and other SKILL.md-capable agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can index project or home-directory memory files, which may expose private paths or summaries in generated local outputs.

Mitigation: Run preview mode first, review selected files, and keep .evermind outputs out of shared repositories when they contain private paths or summaries.

Risk: Persisted rules can affect later agent actions, especially when a broad PreToolUse hook is enabled.

Mitigation: Review and approve .evermind/rules.json before enabling hooks, and avoid wildcard hooks for untrusted repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ccy123abcd/skills/evermind-ai-agent-memory)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Configuration example](artifact/config.example.yaml)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus local JSON, Markdown, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local outputs can include .evermind/discovery.json, memory_index.md, memory_index_state.json, optional .evermind/rules.json, and optional .evermind/handover.md.]

## Skill Version(s):

0.4.2 (source: frontmatter, CHANGELOG, version file, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
