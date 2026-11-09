## Description:

Give a trusted self-hosted workload configured WireGuard-backed SOCKS5 and HTTP exits through pr0xteus's bearer-protected private API. Request an operator-approved ISO country or logical pool, inspect leased-cell state, replace a failed assignment with excludeProxy, or integrate the Go client with VPN-only or public-first retry behavior. It uses operator-owned WireGuard bundles, Docker-spawned cells, country routing, fallback pools, and controller-fronted proxies. Use when a service needs controlled country-specific egress without exposing an open proxy or accepting caller-supplied Docker and provider configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a trusted service to country-specific SOCKS5 or HTTP egress managed by their private pr0xteus controller. It also guides them through inspecting active pools and assignments, replacing a failed proxy, and integrating the Go client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Control API tokens and returned proxy URLs act as credentials; exposing them can grant access to the private controller or its proxy gateways.

Mitigation: Use a trusted private controller, keep tokens in a secret store, and keep returned proxy URLs out of logs and public services.

Risk: Installation writes executable commands and starts persistent containers, while system-wide setup grants broader operator access.

Mitigation: Download and inspect installer and wrapper code before running it, choose user or system-wide setup deliberately, and prefer a fixed image digest.

Risk: Exit-IP preflight checks can disclose both the selected proxy exit IP and the caller's normal public IP to the check services.

Mitigation: Run preflight checks only when that disclosure is acceptable, and review which destinations the checks contact.

## Reference(s):

- [Setup guide](references/setup.md)
- [Project repository](https://github.com/psyb0t/pr0xteus)
- [Complete operator example](https://github.com/psyb0t/pr0xteus/blob/main/docs/complete-example.md)
- [Tailscale sidecar deployment](https://github.com/psyb0t/pr0xteus/blob/main/docs/deploy.md#tailscale-sidecar)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Code]

**Output Format:** [Markdown with shell and curl examples, JSON API payloads, YAML configuration, and Go integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.11.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
