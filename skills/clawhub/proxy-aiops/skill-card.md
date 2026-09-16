## Description:

Proxy AIops helps agents operate Traefik, Caddy, and HAProxy reverse proxies by inspecting routes, services, upstream health, TLS certificates, traffic and error counters, and performing governed Caddy and HAProxy writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect and troubleshoot Traefik, Caddy, and HAProxy edges, including route matching, upstream health, certificate expiry, 5xx errors, and reversible operational changes on supported platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live changes to reverse-proxy configuration or HAProxy server state.

Mitigation: Start with read-only or tightly scoped API accounts, use dry-run paths before writes, and review each write against the current operational change window.

Risk: Authenticated admin endpoints and examples may be exposed over plaintext HTTP if deployed without a protected channel.

Mitigation: Use HTTPS, localhost binding, an internal network, or a protected tunnel for authenticated endpoints before connecting the skill.

Risk: Persistent credentials and the master password can expand blast radius if stored in shared or ordinary config locations.

Mitigation: Keep secrets in the encrypted store, provide the master password through a controlled environment, and avoid committing or sharing credential-bearing configuration.

Risk: Executable installs may resolve newer package contents unless the operator pins the package version.

Mitigation: Review and pin the exact executable package version before enabling write tools in an agent runtime.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxy-aiops)
- [Project homepage](https://github.com/AIops-tools/Proxy-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational analyses, dry-run guidance, and undo-oriented remediation steps for supported proxy platforms.]

## Skill Version(s):

0.9.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
