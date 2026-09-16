## Description:

ChangShen helps agents recover cross-session memory by loading core identity, rules, todos, and work logs while using a local hash index to avoid rereading unchanged files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and frequent agent users use ChangShen to resume work across AI-agent sessions, keep user rules and current work state loaded, and reduce repeated context reads with a local change index.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist workspace instructions into .changshen/rules.json for later rule alignment or optional action blocking.

Mitigation: Use it only in trusted workspaces, keep rule sources to files you control, and review .changshen/rules.json before enabling hooks.

Risk: Automatic session-start recovery in an untrusted repository could load misleading local instructions into the agent's working context.

Mitigation: Preview discovery with python scripts/memory_index.py --list, prefer manual configuration when trust is unclear, and avoid automatic recovery until the workspace is reviewed.

Risk: Optional action-time blocking depends on user-maintained rule extraction and may not reflect every positive instruction or nuanced preference.

Mitigation: Treat the gate as a narrow prohibition checker, keep agent rule alignment in the recovery report, and verify important actions manually.

## Reference(s):

- [ChangShen ClawHub skill page](https://clawhub.ai/ccy123abcd/skills/changshen-agent-memory)
- [ccy123abcd publisher profile](https://clawhub.ai/user/ccy123abcd)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Configuration example](artifact/config.example.yaml)
- [Automatic recovery snippet](artifact/assets/agents-snippet.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local Markdown/JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local recovery artifacts such as memory_index.md, memory_index_state.json, .changshen/discovery.json, and optional .changshen/rules.json or .changshen/handover.md.]

## Skill Version(s):

0.5.0 (source: frontmatter, changelog released 2026-09-15, version file, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
