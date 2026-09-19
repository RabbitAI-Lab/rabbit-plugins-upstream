## Description:

WhoisFreaks (whoisfreaks.com) helps agents retrieve WHOIS, ASN, domain availability, and subdomain information through an OOMOL-connected WhoisFreaks account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to look up domain, IP, ASN, domain availability, and subdomain data from WhoisFreaks through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute local code.

Mitigation: Review the installer path before use, prefer a signed or package-manager installation method, and run setup from a non-elevated account.

Risk: Account sign-in and provider connection can persist beyond a single lookup request.

Mitigation: Only perform first-time setup after an authentication or connection failure, and confirm the intended account and provider connection before proceeding.

## Reference(s):

- [WhoisFreaks homepage](https://whoisfreaks.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-whoisfreaks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to return WhoisFreaks connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
