## Description: <br>
Recover from context compaction by scanning memory files and surfacing where you left off. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[boscoeuk](https://clawhub.ai/user/boscoeuk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill after context compaction, session start, or handoff to summarize current task notes, active context files, recent decisions, and open loops from local workspace memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workspace memory and active context files may contain sensitive or stale notes. <br>
Mitigation: Use the skill deliberately after compaction or for handoff, and review the briefing before sharing or acting on it. <br>
Risk: The briefing may surface incomplete task status, decisions, or open loops from local notes. <br>
Mitigation: Confirm important items against the current workspace state before resuming work. <br>


## Reference(s): <br>
- [Context Anchor on ClawHub](https://clawhub.ai/boscoeuk/skills/context-anchor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Structured terminal briefing with markdown-oriented sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Pure Bash skill with no external dependencies; reads local workspace memory and active context markdown files.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
