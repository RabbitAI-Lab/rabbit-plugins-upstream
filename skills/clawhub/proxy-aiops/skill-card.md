## Description:

Proxy AIops helps agents inspect and operate Traefik, Caddy, and HAProxy reverse proxies for routes, upstream health, TLS certificate checks, 5xx analysis, config lookup, and governed Caddy or HAProxy writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to diagnose and operate self-hosted Traefik, Caddy, and HAProxy edges, including route matching, upstream health, TLS expiry, 5xx RCA, and controlled proxy changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release combines live reverse-proxy write authority, persistent credentials, and an unpinned runtime package, and the security verdict is suspicious.

Mitigation: Install only after pinning the executable package to a reviewed version or digest and reviewing the release before use.

Risk: Caddy config replacement or deletion and HAProxy drain, readiness, maintenance, or weight changes can affect production traffic.

Mitigation: Run with least-privilege proxy accounts, prefer read-only credentials for routine diagnostics, use dry runs where available, and require external approval controls for production-impacting writes.

Risk: Proxy credentials and the master password unlock operational access to live infrastructure.

Mitigation: Avoid placing production master passwords directly in MCP JSON configuration and protect the local proxy-aiops state directory with strict permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxy-aiops)
- [Project homepage](https://github.com/AIops-tools/Proxy-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proxy observations, RCA findings, dry-run guidance, and audit or undo follow-up steps.]

## Skill Version(s):

0.9.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
