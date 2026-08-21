## Description:

memocap is a local memory-capsule skill that stores, retrieves, archives, imports, exports, and visualizes conversation-derived memories for agent sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use memocap to maintain a persistent local memory layer that can recall prior decisions, preferences, tasks, and project context across sessions. The skill also supports quick memory commands, time capsules, import/export, backups, and HTML memory visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically capture and reuse conversation-derived personal, project, preference, task, and decision data.

Mitigation: Install it only for users who explicitly want persistent local memory, review stored memory content regularly, and use the documented forget, export, backup, and recovery commands to manage retention.

Risk: The plugin modifies persistent local state by copying and overwriting plugin-managed docs and scripts under ~/.local/share/忆时.

Mitigation: Review the local data directory before installation or upgrade, keep backups of important memory data, and isolate testing with the documented data-directory environment variable where appropriate.

Risk: The plugin injects memory instructions into agent sessions and may automatically reuse stored workflow memories.

Mitigation: Use it only in agent profiles where this behavior is expected, review the injected instructions and memory recall behavior, and disable the plugin with DSH_YISHI_DISABLE=1 if persistent memory should not affect a session.

Risk: The plugin can start a background download of an approximately 400MB embedding model.

Mitigation: Confirm network and storage expectations before first use, or run the documented model installation command manually in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [ChromaDB API reference](artifact/references/chroma-api.md)
- [bge-base-zh-v1.5 model files](https://hf-mirror.com/Xenova/bge-base-zh-v1.5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration snippets, JSON-compatible memory records, and generated HTML visualization files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write persistent local memory data, backups, copied documentation and scripts, and generated HTML reports under the configured local data directory.]

## Skill Version(s):

2.4.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
