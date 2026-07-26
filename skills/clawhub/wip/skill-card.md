## Description: <br>
Tracks in-session work progress by registering multi-step tasks, updating task status, recovering work after context compaction, and guiding cleanup or resume flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and coding agents use this skill to keep multi-step work visible during a session, resume remaining tasks after interruptions or compaction, and maintain task records across Claude Code and Antigravity environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can steer an agent to delete task records or mutate checklist files. <br>
Mitigation: Review task cleanup decisions before installation and require explicit confirmation before deleting pending tasks or changing persistent checklist files. <br>
Risk: The workflow can steer an agent to run GitHub, remote, deploy, ssh, or curl checks. <br>
Mitigation: Require explicit user approval before external checks and restrict execution to repositories and endpoints the user has authorized. <br>
Risk: The workflow may manage home-directory state such as a Claude cache file. <br>
Mitigation: Install only if home-directory writes and removals are acceptable, and review any home-directory operation before allowing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip) <br>
- [WIP skill entry](SKILL.md) <br>
- [Resume workflow](resume.md) <br>
- [Claude Code WIP guide](claude.md) <br>
- [Antigravity WIP tracking](antigravity.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with task-record examples, inline code blocks, and a shell hook script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to create, update, or delete task records and to run external verification checks when the workflow requires primary-source status.] <br>

## Skill Version(s): <br>
0.4.1 (source: server release metadata and changelog, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
