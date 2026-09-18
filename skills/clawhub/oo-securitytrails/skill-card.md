## Description:

SecurityTrails enables an agent to search and read SecurityTrails domain, DNS, SSL certificate, and subdomain data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to run read-only SecurityTrails lookups for domain intelligence and DNS investigation without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running mutable remote installer commands directly in the local shell.

Mitigation: Review the setup path before installing; prefer a pinned, verifiable oo CLI release or official package-manager flow, and run remote installer commands only after trusting the OOMOL installer source.

## Reference(s):

- [SecurityTrails ClawHub skill page](https://clawhub.ai/oomol/skills/oo-securitytrails)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON action payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running read-only SecurityTrails actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
