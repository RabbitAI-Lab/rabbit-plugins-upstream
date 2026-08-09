## Description: <br>
proxy-aiops helps agents inspect and operate Traefik, Caddy, and HAProxy reverse proxies with route, upstream, certificate, traffic, configuration, RCA, governed write, and undo workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, SREs, and operations teams use this skill to troubleshoot and manage self-hosted Traefik, Caddy, and HAProxy edges, including 5xx analysis, route matching, upstream health, certificate expiry checks, and controlled configuration or server-state changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live reverse-proxy configuration or server state without a built-in MCP approval gate. <br>
Mitigation: Use read-only or tightly scoped proxy/API accounts where possible, keep authorization decisions in the agent or account policy, and review proposed writes before execution. <br>
Risk: Full Caddy config load and delete operations can cause outages if the wrong subtree or full config is applied. <br>
Mitigation: Use dry runs first, rely on CLI double confirmation for high-risk writes, capture snapshots before changes, and use recorded undo descriptors when rollback is needed. <br>
Risk: Credentials and the master password grant access to proxy APIs and encrypted secrets. <br>
Mitigation: Protect PROXY_AIOPS_MASTER_PASSWORD through the MCP client's secret mechanism when available, keep Caddy admin access on localhost or a trusted network, and prefer scoped API credentials. <br>


## Reference(s): <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>
- [Project homepage](https://github.com/AIops-tools/Proxy-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxy-aiops) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured tool results with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live proxy observations, RCA findings, dry-run previews, audit or undo identifiers, and risk-tier labels.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
