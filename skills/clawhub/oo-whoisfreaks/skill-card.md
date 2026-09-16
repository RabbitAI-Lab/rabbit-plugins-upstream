## Description:

This skill lets agents use WhoisFreaks through the OOMOL oo CLI to retrieve WHOIS records, ASN WHOIS records, domain availability, and known subdomains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query WhoisFreaks through an OOMOL-connected account for domain, IP, ASN, domain availability, and subdomain lookup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote install commands that can modify the user's machine.

Mitigation: Review setup commands before installing; prefer installing the oo CLI from a verified, pinned, or signed source, and avoid piping downloaded scripts directly into a shell.

Risk: Domain, IP, ASN, and subdomain lookup inputs are sent through OOMOL's connector to WhoisFreaks during normal use.

Mitigation: Use only lookup inputs appropriate to share with the connected service and account, and avoid sensitive internal targets unless authorized.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-whoisfreaks)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [WhoisFreaks Homepage](https://whoisfreaks.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
