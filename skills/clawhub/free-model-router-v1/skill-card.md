## Description: <br>
Free Model Router provides OpenClaw with a local proxy for routing requests across free model providers, with setup guidance, automatic polling, failover, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laodao-agent](https://clawhub.ai/user/laodao-agent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure and operate a persistent localhost model router, manage provider keys and model choices, and recover from provider or model failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a persistent localhost model proxy with broad admin controls. <br>
Mitigation: Keep the router bound to localhost, avoid reverse proxies or shared hosts, and review admin actions before enabling or changing providers. <br>
Risk: Provider keys are stored locally and may be exposed if the host or skill data directory is compromised. <br>
Mitigation: Use the skill only on trusted machines, restrict local account and file access, and rotate provider keys if local exposure is suspected. <br>
Risk: Prompts and model responses are forwarded to third-party model providers. <br>
Mitigation: Review provider terms and avoid sending sensitive or regulated data unless the selected provider is approved for that use. <br>
Risk: The security review flags under-disclosed update and data-flow behavior. <br>
Mitigation: Review update and admin features carefully, and prefer explicit /free-model-router commands for provider disabling, model switching, and other changes. <br>


## Reference(s): <br>
- [Setup Flow Guide](references/setup-guide.md) <br>
- [Event Notification System](references/event-system.md) <br>
- [Installation Idempotency Guide](references/idempotency.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/laodao-agent/skills/free-model-router-v1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with inline shell commands and concise status or configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose OpenClaw configuration changes and local CLI commands that should be reviewed before execution.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release, package.json, artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
