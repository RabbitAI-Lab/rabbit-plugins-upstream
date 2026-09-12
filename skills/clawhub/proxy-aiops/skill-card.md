## Description:

Proxy AIops helps agents inspect and operate Traefik, Caddy, and HAProxy reverse proxies with route, upstream, certificate, traffic, configuration, RCA, governed write, and undo workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate reverse-proxy routing, backend health, TLS expiry, traffic errors, and configuration state across Traefik, Caddy, and HAProxy. It can also guide audited, reversible Caddy configuration changes and HAProxy server state or weight changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent live write access to Caddy configuration and HAProxy server state, which could disrupt traffic if misused.

Mitigation: Start with read-only or least-privileged proxy accounts, use dry-run flows, and require human approval outside the tool before Caddy config or HAProxy state changes.

Risk: Authenticated proxy APIs and the master password can expose sensitive operational control if configured broadly.

Mitigation: Use HTTPS or a protected tunnel for non-loopback APIs, avoid storing the master password in broadly readable MCP config, and lock down ~/.proxy-aiops.

Risk: Full Caddy config replacement and destructive config edits can affect every service behind the proxy.

Mitigation: Capture a config snapshot before changes, prefer targeted edits, use the recorded undo flow when rollback is needed, and validate route and error behavior after each change.

## Reference(s):

- [Proxy AIops source repository](https://github.com/AIops-tools/Proxy-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxy-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proxy health summaries, RCA findings, dry-run write plans, audit or undo references, and platform-specific teaching errors.]

## Skill Version(s):

0.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
