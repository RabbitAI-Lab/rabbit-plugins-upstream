## Description:

Evermind helps agents recover cross-session memory by discovering local memory files, reading required context, maintaining a change index, and preparing handover notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to resume work across sessions without re-reading every memory file. It is intended for local agent workflows that need rule recall, context recovery, change indexing, and task handover.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist agent rules discovered from project files and influence future agent behavior.

Mitigation: Run preview or list mode first, inspect .evermind/discovery.json, and review .evermind/rules.json before enabling hook-based enforcement.

Risk: Local state files and handover notes can be written, overwritten, or deleted during recovery workflows.

Mitigation: Keep generated outputs inside .evermind, review configuration paths for absolute paths or parent-directory traversal, and remember that handover notes are one-shot state.

Risk: The security verdict requires review before deployment.

Mitigation: Install only in trusted repositories and review the configuration, generated discovery data, and action hook behavior before normal use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ccy123abcd/skills/evermind-ai-agent-memory)
- [Publisher profile](https://clawhub.ai/user/ccy123abcd)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Example configuration](config.example.yaml)
- [Handover template](assets/handover-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local recovery guidance and may direct creation of .evermind state files, memory_index.md, rules.json, and handover notes.]

## Skill Version(s):

0.4.1 (source: SKILL.md frontmatter, CHANGELOG, version file, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
