## Description: <br>
Monitors local llama.cpp servers on macOS, auto-restarts on failure, sends notifications, and supports customizable hooks for self-healing supervision. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gutchapa](https://clawhub.ai/user/gutchapa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and local LLM operators use this skill to supervise llama.cpp and OpenClaw services on macOS, recover from failed health checks, and receive local or Telegram notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The watchdog can automatically kill and restart local llama.cpp or OpenClaw services. <br>
Mitigation: Use it only where those restarts are acceptable, verify process match targets before unattended use, and use DRY_RUN during setup. <br>
Risk: The watchdog can rewrite Pi/OpenClaw configuration to align local service ports. <br>
Mitigation: Back up Pi/OpenClaw configuration before enabling unattended operation and review the configured host, port, and file paths. <br>
Risk: Telegram alerting can send status externally when credentials are configured. <br>
Mitigation: Disable Telegram notifications unless external alerts are intended, and provide bot tokens and chat IDs only deliberately. <br>


## Reference(s): <br>
- [Server-resolved GitHub source repository](https://github.com/gutchapa/rock-solid-watchdog) <br>
- [ClawHub skill page](https://clawhub.ai/gutchapa/skills/rock-solid-watchdog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
