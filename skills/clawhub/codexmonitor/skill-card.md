## Description: <br>
List, inspect, and watch local OpenAI Codex sessions from the CLI or VS Code using the CodexMonitor Homebrew formula. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install and operate CodexMonitor so they can browse, inspect, export, and watch local OpenAI Codex session logs. It is most useful when reviewing local session history or identifying a session to resume intentionally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CodexMonitor reads local Codex session history, which may contain sensitive prompts, outputs, or project context. <br>
Mitigation: Treat session contents as sensitive and scope CODEX_SESSIONS_DIR or CODEX_HOME to the intended sessions directory when practical. <br>
Risk: Installation depends on the third-party cocoanetics Homebrew tap. <br>
Mitigation: Install only when the publisher and Homebrew tap are trusted for the environment. <br>
Risk: The resume command can append to an existing Codex session. <br>
Mitigation: Use resume only after confirming the target session id and intentionally choosing to continue that session. <br>


## Reference(s): <br>
- [CodexMonitor setup instructions](SETUP.md) <br>
- [CodexMonitor homepage](https://github.com/Cocoanetics/CodexMonitor) <br>
- [ClawHub Codexmonitor skill page](https://clawhub.ai/odrobnik/skills/codexmonitor) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include CLI commands that list, show, watch, or resume Codex sessions; JSON output is available from supported codexmonitor commands.] <br>

## Skill Version(s): <br>
0.2.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
