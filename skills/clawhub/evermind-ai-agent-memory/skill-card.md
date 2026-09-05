## Description:

Evermind helps AI agents recover cross-session memory by discovering local memory files, reading required context, and using a generated change index to avoid rereading unchanged files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to resume AI-agent sessions with local identity, rules, todo, journal, and profile context while reducing repeated context reads. It is suited for agents running across Hermes, ClawHub/OpenClaw, Claude Code, Cursor, Codex, and other SKILL.md-compatible environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to discover and read local memory files that may include rules, todos, journals, profiles, and configured extras.

Mitigation: Run the --list preview first, review .evermind/discovery.json and config.yaml, and avoid adding sensitive folders or secrets as tracked files.

Risk: The skill writes persistent local discovery, index, and state files.

Mitigation: Review or delete .evermind/discovery.json, memory_index.md, and memory_index_state.json to reset or remove cached local state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ccy123abcd/skills/evermind-ai-agent-memory)
- [README](README.md)
- [Agent instructions](SKILL.md)
- [Example configuration](config.example.yaml)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, local file paths, and generated local index files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script can generate .evermind/discovery.json, memory_index.md, and memory_index_state.json locally.]

## Skill Version(s):

0.3.0 (source: frontmatter, CHANGELOG, version file, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
