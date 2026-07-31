## Description: <br>
Track in-session work progress, register multi-step tasks, update task status, and resume remaining work across Claude Code and Antigravity agent sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to keep multi-step work visible during a session, recover outstanding work after compaction, and coordinate task cleanup or continuation through supported task-tracking media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct agents to delete or rewrite task state. <br>
Mitigation: Review task cleanup behavior before deployment and require explicit confirmation before deleting pending tasks. <br>
Risk: The skill can direct network or GitHub verification checks during task recovery. <br>
Mitigation: Install only where those checks are expected, and restrict credentials or network access according to the workspace policy. <br>
Risk: The skill includes behavior around shared Claude-side files, including Copilot rate-limit cache state. <br>
Mitigation: Review or disable the cache and hook behavior if writes under ~/.claude or shared session effects are not wanted. <br>
Risk: The task-completion hook reacts to user-message keyword matches. <br>
Mitigation: Review the hook patterns before enabling it and disable the hook if prompt-triggered task deletion reminders are not appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip) <br>
- [Antigravity WIP Tracking](antigravity.md) <br>
- [Claude Code WIP TaskCreate/TodoWrite API guide](claude.md) <br>
- [Resume task cleanup and remaining work workflow](resume.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with task records, code snippets, shell commands, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update agent task lists, checklist files, task artifacts, and Claude-side cache or hook files when the host environment supports those actions.] <br>

## Skill Version(s): <br>
0.4.2 (source: server release metadata and changelog, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
