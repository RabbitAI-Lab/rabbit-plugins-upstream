## Description:

proxy-aiops helps agents inspect and operate Traefik, Caddy, and HAProxy reverse proxies, including routes, upstream health, certificates, traffic errors, RCA workflows, and governed configuration or server-state writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and operations engineers use this skill to observe, troubleshoot, and change self-hosted Traefik, Caddy, or HAProxy reverse-proxy environments. It supports route and service inspection, TLS expiry sweeps, 5xx and backend-health RCA, configuration lookup, audited Caddy config changes, and audited HAProxy server state or weight changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable tools can change live proxy routing, configuration, or backend server state without an enforced skill-side approval gate.

Mitigation: Start with read-only or tightly scoped proxy API accounts, enable write-capable credentials only when live changes are intended, and require the agent operator to review proposed writes before execution.

Risk: Exposed Traefik, Caddy, or HAProxy admin APIs can broaden the blast radius of agent or credential misuse.

Mitigation: Keep proxy admin APIs on localhost or trusted networks, verify TLS by default, and avoid disabling certificate checks except in controlled labs.

Risk: Shared or broadly readable MCP configuration can expose the master password used to unlock encrypted proxy credentials.

Mitigation: Store MCP environment configuration with restrictive permissions and avoid putting the master password in shared config files.

Risk: Audit and undo records help recovery but do not prevent an unsafe change from being attempted.

Mitigation: Treat audit and undo as recovery mechanisms, use dry-run previews for writes, and keep independent configuration snapshots for high-risk Caddy changes.

## Reference(s):

- [proxy-aiops homepage](https://github.com/AIops-tools/Proxy-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return proxy observations, RCA summaries, dry-run previews, and configuration or state-change guidance.]

## Skill Version(s):

0.9.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
