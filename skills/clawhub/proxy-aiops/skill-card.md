## Description:

Helps operators inspect and troubleshoot Traefik, Caddy, and HAProxy routes, upstreams, certificates, and errors, and perform supported proxy changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Proxy operators and developers use this skill to investigate routing, backend health, TLS certificates, and 5xx errors on Traefik, Caddy, or HAProxy, and to make supported Caddy or HAProxy changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable sessions can change live Caddy configuration or HAProxy server behavior without an enforced approval gate or read-only mode.

Mitigation: Require external approval before writes, use read-only or tightly scoped proxy credentials when possible, and review changes before production use.

Risk: Persistent credentials and local proxy state may be exposed if stored insecurely.

Mitigation: Avoid placing PROXY_AIOPS_MASTER_PASSWORD in persistent MCP configuration when possible and restrict access to ~/.proxy-aiops.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/proxy-aiops)
- [Project homepage (listed in skill metadata)](https://github.com/AIops-tools/Proxy-AIops)
- [Capabilities and platform support](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proxy status, diagnostic findings, and suggested changes.]

## Skill Version(s):

0.11.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
