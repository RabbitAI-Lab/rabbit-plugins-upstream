## Description:

Evermind helps an agent recover cross-session memory by always reading core context, checking a local change index before rereading secondary files, and deferring detail files until they are needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to let SKILL.md-compatible agents resume personal or project context at the start of a new session while reducing unnecessary rereads. It is most relevant for multi-session workflows that maintain local identity, rules, todo, work-log, role, project, or configuration files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent and the companion indexer to read local memory files selected in config.yaml.

Mitigation: Keep memory_root, must_read, and tracked_files narrow; include only files the agent is allowed to inspect.

Risk: Scheduling the local indexer hashes and summarizes configured tracked files on a recurring basis.

Mitigation: Schedule the indexer only when recurring local hashing and memory_index.md generation are acceptable for the configured files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ccy123abcd/skills/evermind-ai-agent-memory)
- [Publisher profile](https://clawhub.ai/user/ccy123abcd)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Configuration example](artifact/config.example.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and YAML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The companion script can produce local memory_index.md and memory_index_state.json files from user-selected configured paths.]

## Skill Version(s):

0.2.0 (source: frontmatter and CHANGELOG, released 2026-09-04; artifact/version says 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
