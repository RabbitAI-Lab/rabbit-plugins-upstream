## Description: <br>
Keep Claude Code sessions productive across resets with output filtering, session logging, and auto-resume. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to keep long Claude Code sessions recoverable by summarizing command output, maintaining a project session log, and resuming in-progress work after context resets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently stores user prompts and command history in a project-root session log without redaction or containment. <br>
Mitigation: Use it only where such logging is acceptable, avoid sensitive prompts and secrets, and add session.log to .gitignore or choose a safer log location. <br>


## Reference(s): <br>
- [Context Mode on ClawHub](https://clawhub.ai/mohitagw15856/skills/context-mode) <br>
- [Context Mode homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/context-mode.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with structured status messages, log templates, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces filtered command summaries, session.log entries, resume announcements, and CLAUDE.md installation text.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
