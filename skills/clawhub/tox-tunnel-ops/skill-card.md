## Description:

Helps agents design, generate, verify, and troubleshoot encrypted ToxTunnel TCP tunnels for SSH, remote desktop, databases, web services, homelab access, and temporary maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentx-icu](https://clawhub.ai/user/agentx-icu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and administrators use this skill to configure and diagnose self-hosted ToxTunnel access for remote services without exposing server ports directly. It supports SSH/RDP, database, web, NAS, SOCKS5, monitoring, and temporary contractor access workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated tunnel configurations can expose sensitive services if local forwards bind beyond loopback or rules allow broad host and port access.

Mitigation: Review generated rules before use, keep forwards loopback-bound or firewalled, and prefer narrow friend, host, and port allowlists.

Risk: Setup guidance may include package installation, service registration, or other privileged local changes.

Mitigation: Run privileged commands only after explicit operator approval and review the intended system change before execution.

Risk: A remote tunnel can preserve access longer than intended if existing sessions are not terminated during revocation.

Mitigation: Use reloads to block new sessions, and restart the tunnel service or revoke access at the target service when live access must end immediately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentx-icu/skills/tox-tunnel-ops)
- [Publisher profile](https://clawhub.ai/user/agentx-icu)
- [ToxTunnel project homepage](https://github.com/agentx-icu/tox-tcp-tunnel)
- [Diagnose reference](references/diagnose.md)
- [Execute reference](references/execute.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with YAML and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational recommendations and configuration examples for a user-approved ToxTunnel deployment.]

## Skill Version(s):

0.4.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
