## Description:

Manage your doxx.net private network: tunnels, devices, firewall, domains, DNS blocking, IP addresses, profiles, account settings, bandwidth stats, and security alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doxxnet](https://clawhub.ai/user/doxxnet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers who administer doxx.net private networks use this skill to inspect and manage tunnels, devices, DNS, domains, firewall rules, IP addresses, tokens, account settings, usage stats, and guided setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a doxx.net token to administer tunnels, firewall rules, domains, account settings, and other network resources.

Mitigation: Use a scoped net-admin or read-only token with expiration and IP fencing, and review proposed network changes before applying them.

Risk: Token values, WireGuard configurations, and QR codes are sensitive secrets.

Mitigation: Keep tokens out of chat, avoid printing full token values, and store WireGuard configuration or QR output only where the user expects it.

Risk: Local WireGuard setup can require privileged changes that affect host networking.

Mitigation: Do not run sudo or write to /etc/wireguard until the generated configuration and network impact have been reviewed.

## Reference(s):

- [doxx.net skill page](https://clawhub.ai/doxxnet/skills/doxxnet)
- [Project homepage](https://github.com/doxxcorp/doxx-skills)
- [Manage doxx.net Account](references/manage-account.md)
- [Manage doxx.net Addresses & Profiles](references/manage-addresses.md)
- [Manage doxx.net Devices](references/manage-devices.md)
- [Manage doxx.net DNS Blocking](references/manage-dns-blocking.md)
- [Manage doxx.net Domains](references/manage-domains.md)
- [Manage doxx.net Firewall](references/manage-firewall.md)
- [Manage doxx.net Tokens](references/manage-tokens.md)
- [Manage doxx.net Tunnels](references/manage-tunnels.md)
- [doxx.net Network Stats](references/network-stats.md)
- [doxx.net Network Status](references/network-status.md)
- [doxx.net Network Wizard](references/network-wizard.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request commands, WireGuard configuration guidance, tables of network status or usage data, and setup steps.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
