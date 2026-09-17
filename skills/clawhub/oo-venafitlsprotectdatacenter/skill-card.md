## Description:

Venafi TLS Protect Datacenter (cyberark.com). Use this skill for ANY Venafi TLS Protect Datacenter request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform operators, and certificate administrators use this skill to inspect Venafi TLS Protect Datacenter certificates and effective certificate policy through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute changing network code on a user's machine.

Mitigation: Review the oo CLI installation process before installing, prefer official signed or checksum-verified packages where available, and do not let an agent run the remote installer automatically.

Risk: The connector can access certificate and policy data from a connected Venafi TLS Protect Datacenter account.

Mitigation: Connect only the Venafi permissions needed for read-only certificate and policy lookup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-venafitlsprotectdatacenter)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Venafi TLS Protect Datacenter product information](https://www.cyberark.com/resources/product-datasheets/cyberark-certificate-manager-self-hosted)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; responses include connector data and an execution identifier.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
