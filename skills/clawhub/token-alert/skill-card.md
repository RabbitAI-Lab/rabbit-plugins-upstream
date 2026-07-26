## Description: <br>
Monitors Clawdbot session token usage and alerts users at configured thresholds with CLI output, dashboard views, and optional notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[r00tid](https://clawhub.ai/user/r00tid) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to monitor active session token usage, decide when to summarize or start a new session, and optionally receive local or browser alerts as thresholds are reached. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard can access and export chat history and send commands into a local session. <br>
Mitigation: Use the CLI checker when a read-only posture is needed, and review dashboard actions before enabling export, summary, or session-control workflows. <br>
Risk: Automatic summary or export behavior near high token usage can act on sensitive session content. <br>
Mitigation: Disable or avoid auto-summary and auto-export unless the session content is appropriate for local export and memory-saving workflows. <br>
Risk: Optional notification and provider setup can create a recurring background job and store configuration locally in plaintext. <br>
Mitigation: Run optional setup only after accepting the background schedule and local config behavior; prefer environment variables for provider API keys when possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/r00tid/skills/token-alert) <br>
- [README](artifact/README.md) <br>
- [Quick Start](artifact/QUICKSTART.md) <br>
- [Implementation Report](artifact/IMPLEMENTATION_REPORT.md) <br>
- [Clawdbot Docs](https://docs.clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May launch a local dashboard and optional notifications; some outputs depend on active Clawdbot session state.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
