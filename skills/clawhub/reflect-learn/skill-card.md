## Description: <br>
Self-improvement through conversation analysis that extracts learnings from corrections and success patterns, proposes updates to agent files, or creates new skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevengonsalvez](https://clawhub.ai/user/stevengonsalvez) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Reflect to review conversation history for corrections, approved patterns, and reusable discoveries, then propose persistent agent, memory, or skill updates for human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation-derived learnings can encode incorrect or misleading guidance into persistent agent or skill files. <br>
Mitigation: Review every proposed diff before approval and reject or modify low-confidence learnings before they are written. <br>
Risk: The skill can persist learning records globally and write live agent, memory, reflection, or skill files. <br>
Mitigation: Inspect or periodically delete ~/.claude/reflections, ~/.reflect, ~/.claude/session, and generated .claude/skills entries. <br>
Risk: Auto-reflection hooks may create files during context compaction. <br>
Mitigation: Keep auto-reflection disabled unless this behavior is intended, or configure reminder-only mode for manual review. <br>


## Reference(s): <br>
- [Reflect Skill Page](https://clawhub.ai/stevengonsalvez/skills/reflect-learn) <br>
- [Signal Detection Patterns](references/signal_patterns.md) <br>
- [Agent Mappings Reference](references/agent_mappings.md) <br>
- [Skill Template Reference](references/skill_template.md) <br>
- [Reflect Hooks Integration](hooks/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reflection reports with diffs, shell commands, configuration snippets, and optional generated skill files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write reflection records, learning logs, metrics, hook logs, and proposed agent or skill file changes after user approval.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
