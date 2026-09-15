## Description:

SecurityTrails connector skill for searching and reading domain intelligence, DNS records, SSL certificate details, associated domains, and subdomains through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to run read-only SecurityTrails lookups for domain investigation and DNS intelligence without handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer snippets for the oo CLI, and the server security summary flags those snippets as suspicious if run without review.

Mitigation: Do not let an agent run installer snippets automatically; install the oo CLI only from a trusted, reviewable, version-pinned source and verify system changes before use.

Risk: SecurityTrails lookups can reveal domain intelligence and DNS investigation results that may be sensitive in some environments.

Mitigation: Use the skill only for authorized domains and share returned data according to the user's security and data-handling policies.

## Reference(s):

- [SecurityTrails Skill Page](https://clawhub.ai/oomol/skills/oo-securitytrails)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SecurityTrails Connection Setup](https://console.oomol.com/app-connections?provider=securitytrails)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SecurityTrails action responses are returned as JSON data from the oo CLI when commands are executed.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
