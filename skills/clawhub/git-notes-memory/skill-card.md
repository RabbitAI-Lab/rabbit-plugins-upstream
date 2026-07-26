## Description: <br>
Provides a branch-aware Claude Code memory system that stores, retrieves, updates, and organizes project context, decisions, tasks, and learnings in local git notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mourad-ghafiri](https://clawhub.ai/user/mourad-ghafiri) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers using Claude Code can use this skill to maintain project continuity across sessions by recording and retrieving branch-aware memories about decisions, preferences, tasks, and learned context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed for silent memory operations and may persist project or user context without prompting. <br>
Mitigation: Enable it only for projects where always-on local memory is intended, and add local rules that require explicit approval before storing sensitive or personal information. <br>
Risk: The memory script can initialize git state, update local git configuration, create an empty initial commit, and write git notes in the target directory. <br>
Mitigation: Review repository state before enabling the skill, confirm git notes and possible initialization are acceptable, and inspect or delete stored notes periodically. <br>
Risk: Stored memories can include durable decisions, preferences, tasks, and context that may be inappropriate for sensitive repositories. <br>
Mitigation: Exclude secrets, credentials, personal data, and confidential project details from memory, and disable the skill for repositories where persistent local notes are not permitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mourad-ghafiri/skills/git-notes-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides an agent to invoke a local Python memory script and interpret compact JSON responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
