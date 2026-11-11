## Description:

Deploys an HTTP(S) proxy that exposes OpenClaw agent capability as a REST API over a network IP, with API key authentication, optional TLS, deny-list filtering, prompt-injection hardening, and OpenClaw hook-based request isolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to expose an OpenClaw agent as an internal REST API that other trusted systems can call for open-ended agent runs or targeted skill execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes an OpenClaw agent as a remotely callable HTTP service, which can become a remote control surface for file, shell, messaging, or other agent capabilities.

Mitigation: Install only when this exposure is intentional, bind to localhost or a tightly firewalled interface, and allow access only from trusted callers.

Risk: Default HTTP transport can expose API keys, prompts, and results in cleartext for cross-host traffic.

Mitigation: Enable TLS for any cross-host or production traffic and avoid skipping certificate verification.

Risk: The watchdog and initialization flow can modify and restore global OpenClaw hook configuration.

Mitigation: Review the OpenClaw configuration changes before deployment and disable the watchdog unless persistent self-healing is required.

Risk: API keys are bearer credentials, and deny_skills is not a hard security boundary while the open-ended /agent/run endpoint is enabled.

Mitigation: Rotate exposed keys, keep credentials out of logs and shell history, restrict reachable clients, and use allowlists or tighter routing controls where possible.

## Reference(s):

- [README](README.md)
- [Deployment Guide](references/deployment.md)
- [Design Document](references/design.md)
- [TLS and Authentication Standard](references/tls-auth-standard.md)
- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/agent-easy-http)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration paths, and REST API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce service setup instructions, API usage examples, configuration guidance, and operational troubleshooting steps.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
