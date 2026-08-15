## Description:

Proxy AIops helps agents inspect and operate Traefik, Caddy, and HAProxy reverse proxies with route, upstream, certificate, traffic, configuration, RCA, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to troubleshoot and manage self-hosted Traefik, Caddy, and HAProxy edges, including 5xx investigations, upstream health checks, TLS expiry sweeps, route conflict analysis, and reversible proxy changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact write actions can change live routing or load-balancer behavior without an in-tool read-only mode, policy gate, or approval gate.

Mitigation: Install first with read-only or narrowly scoped proxy credentials, require agent-level approval before write tools, and review dry-run output before applying Caddy or HAProxy changes.

Risk: Secrets and local proxy state can expose operational access if shared or committed.

Mitigation: Keep PROXY_AIOPS_MASTER_PASSWORD out of committed or shared configuration and protect ~/.proxy-aiops with owner-only permissions.

## Reference(s):

- [Proxy AIops Homepage](https://github.com/AIops-tools/Proxy-AIops)
- [proxy-aiops ClawHub Skill Page](https://clawhub.ai/zw008/skills/proxy-aiops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call MCP and CLI tools that inspect proxy APIs and, when authorized, perform audited reversible writes.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
