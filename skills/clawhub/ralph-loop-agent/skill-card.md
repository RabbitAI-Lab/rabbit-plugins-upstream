## Description: <br>
Ralph Loop (Agent Mode) guides OpenClaw agents to orchestrate PLANNING and BUILDING coding-agent loops with TTY-backed exec/process sessions, prompt and plan files, sandboxing guidance, and completion checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[addozhang](https://clawhub.ai/user/addozhang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill through an OpenClaw agent to plan, run, monitor, and complete coding-agent loops for software implementation work. It is intended for workflows that need prompt files, implementation plans, test backpressure, TTY support for interactive coding CLIs, and explicit completion sentinels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to run other coding agents with broad command, file, and background-process access. <br>
Mitigation: Install and use it only inside trusted projects, keep the working directory narrow, and prefer disposable branches or sandboxes. <br>
Risk: Auto-approval and permission-skipping flags can allow changes without normal review. <br>
Mitigation: Avoid --yolo and permission-skipping flags; require explicit approval before commits, hard resets, rollback commands, or use of project credentials. <br>
Risk: Long-running or background coding-agent sessions may continue after the desired work is complete or after a timeout. <br>
Mitigation: Monitor sessions with process polling and logs, use bounded timeouts and iteration limits, and kill sessions when completion or failure conditions are reached. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/addozhang/skills/ralph-loop-agent) <br>
- [OpenClaw Documentation](https://openclaw.com/docs) <br>
- [Original Ralph Loop](https://github.com/openclaw/skills/blob/main/skills/jordyvandomselaar/ralph-loop/SKILL.md) <br>
- [Coding Agent](https://github.com/openclaw/skills/blob/main/skills/steipete/coding-agent/SKILL.md) <br>
- [Ralph Wiggum Playbook](https://ralphwiggum.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, prompt templates, file names, and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses PROMPT.md, AGENTS.md, IMPLEMENTATION_PLAN.md, specs/*.md, process sessions, timeouts, and completion sentinel text.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
