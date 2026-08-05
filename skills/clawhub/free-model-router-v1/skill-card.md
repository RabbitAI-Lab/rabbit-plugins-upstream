## Description: <br>
Provides an OpenClaw local model router for automatic free-model provider setup, polling, failover, model switching, and availability diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laodao-agent](https://clawhub.ai/user/laodao-agent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure a persistent local router that selects, switches, and fails over across free model providers. It also helps diagnose provider availability and manage OpenClaw model routing without repeatedly editing the main OpenClaw configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a persistent localhost router that can expose or change sensitive routing data. <br>
Mitigation: Install only on a trusted machine and review the local admin/API surface before relying on it. <br>
Risk: Provider API keys are stored locally and may be requested during setup. <br>
Mitigation: Use a secure secret-entry path when available and avoid pasting API keys into ordinary chat. <br>
Risk: The router contacts external freemodel/model provider services and may register scheduled checks. <br>
Mitigation: Confirm the external communication and scheduled checks are acceptable before deployment, and keep reporting disabled unless telemetry is intended. <br>


## Reference(s): <br>
- [Setup Flow Guide](references/setup-guide.md) <br>
- [Event Notification System](references/event-system.md) <br>
- [Installation Idempotency Guide](references/idempotency.md) <br>
- [Qwen3 Coder Free Model Listing](https://openrouter.ai/models/qwen/qwen3-coder:free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run local Node.js CLI commands and register scheduled status or event checks.] <br>

## Skill Version(s): <br>
2.1.2 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
