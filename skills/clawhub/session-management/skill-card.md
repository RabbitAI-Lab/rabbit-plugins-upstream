## Description: <br>
Structured session lifecycle for Claude Code - start, checkpoint, end, and daily heartbeat commands that maintain project state across conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers using Claude Code use this skill to start, checkpoint, close, and run daily heartbeat sessions while preserving project state, decisions, blockers, and next actions across conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update local project state and session notes. <br>
Mitigation: Review proposed file changes before relying on them, especially when state files influence future sessions. <br>
Risk: The skill may propose memory, commit, or push actions during session closeout. <br>
Mitigation: Approve only proposals that accurately reflect the work and match the repository's intended workflow. <br>


## Reference(s): <br>
- [Canonical agent-workspace repository](https://github.com/conorbronsdon/agent-workspace) <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/session-management) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project-local state and session files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
