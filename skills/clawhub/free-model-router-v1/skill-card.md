## Description: <br>
Provides OpenClaw with a local free-model router that configures providers, routes requests, rotates and fails over models, and helps diagnose model availability issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laodao-agent](https://clawhub.ai/user/laodao-agent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to set up and operate a local model-routing proxy that selects free providers, switches primary or fallback models, and diagnoses provider availability problems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a persistent local router with access to OpenClaw configuration, provider API keys, local admin APIs, and device identifiers. <br>
Mitigation: Keep the router bound to localhost, do not expose its port, and review the admin-console behavior before installation. <br>
Risk: Model prompts and responses are forwarded to external model providers selected through the router. <br>
Mitigation: Use only providers acceptable for the data being sent, and avoid routing sensitive prompts through untrusted external providers. <br>
Risk: Optional reporting and telemetry can share health metadata and device identifiers with model-server infrastructure. <br>
Mitigation: Leave reporting disabled unless the user accepts the metadata sharing, and disable it with the documented reporting controls when not needed. <br>
Risk: Update and account-control paths may affect local router behavior after installation. <br>
Mitigation: Review update behavior and account-control functions before use, and restart the router after skill updates so the active process matches the installed files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/laodao-agent/skills/free-model-router-v1) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Event system](references/event-system.md) <br>
- [Idempotency guide](references/idempotency.md) <br>
- [Qwen3 Coder free model reference](https://openrouter.ai/models/qwen/qwen3-coder:free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May instruct the agent to run local Node.js CLI commands and update OpenClaw model-routing configuration.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
