## Description:

Provides OpenClaw with a local free-model routing service that can configure providers, route requests through a localhost proxy, poll model health, switch models, and fail over across available providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laodao-agent](https://clawhub.ai/user/laodao-agent)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to set up a localhost model router, configure provider API keys, route requests to free model providers, diagnose availability, and switch or fail over models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a persistent localhost router and modifies OpenClaw model configuration.

Mitigation: Review setup, model-role, stop, and uninstall actions before execution, and rely on the documented backup and rollback behavior for configuration changes.

Risk: Prompts and model responses are routed to external model providers selected by the user.

Mitigation: Avoid routing sensitive content unless the selected provider is approved for that data and its terms are acceptable.

Risk: Provider keys are stored locally and the router communicates with freemodel control servers for provider and health metadata.

Mitigation: Protect the local router configuration directory and keep optional health reporting disabled unless the user deliberately enables it.

Risk: The local admin surface and router endpoint could be risky if exposed outside the host.

Mitigation: Keep the router bound to 127.0.0.1, avoid proxying or tunneling port 5678, and do not set ADMIN_TOKEN for ordinary end-user installs.

Risk: Provider-disable, uninstall, stop, and model-role changes can disrupt OpenClaw routing.

Mitigation: Require explicit user confirmation before commands that disable providers, change model roles, stop the router, or uninstall the skill.

## Reference(s):

- [Setup guide](references/setup-guide.md)
- [Event system](references/event-system.md)
- [Idempotency guide](references/idempotency.md)
- [ClawHub skill page](https://clawhub.ai/laodao-agent/skills/free-model-router-v1)
- [Publisher profile](https://clawhub.ai/user/laodao-agent)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline CLI commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to start or stop a persistent local router and update OpenClaw model configuration.]

## Skill Version(s):

2.2.0 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
