## Description:

Install and configure the security-related plugins required by OpenClaw, including the `agent-sentry` plugins. Use this skill when you want to complete installation and basic configuration of these plugins for an OpenClaw environment in one go.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volcengine-skills](https://clawhub.ai/user/volcengine-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to install and prepare the agent-sentry security plugin, complete login activation, and finalize OpenClaw plugin configuration on the current machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound authentication calls and activation flows contact Volcengine/ClawSentry endpoints.

Mitigation: Review the endpoints and run the skill only in environments where those outbound HTTPS calls are permitted.

Risk: The skill transmits and stores a stable device fingerprint for device-linked login.

Mitigation: Confirm device-binding is acceptable for the deployment and avoid shared machines where that identifier should not be exposed.

Risk: Local `.state` files may contain login tokens, activation state, logs, and device-linked data.

Mitigation: Restrict filesystem permissions, avoid exposing `.state` logs, and clean local state after installation if retention is not needed.

Risk: Finalization updates OpenClaw plugin configuration with API credentials and grants conversation-access permission to the security plugin.

Mitigation: Review the generated OpenClaw configuration before production use and confirm the permission is required for the intended security controls.

Risk: The skill restarts the OpenClaw gateway after configuration.

Mitigation: Run finalization during an approved maintenance window or in a controlled environment where a gateway restart is acceptable.

## Reference(s):

- [ClawHub AgentSentry skill page](https://clawhub.ai/volcengine-skills/skills/agentsentry)
- [Volcengine website](https://www.volcengine.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown/plain text with inline shell commands and activation link text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local state files and update OpenClaw plugin configuration during execution.]

## Skill Version(s):

1.0.0 (source: release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
