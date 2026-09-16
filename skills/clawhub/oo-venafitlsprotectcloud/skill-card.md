## Description:

Helps agents retrieve and list Venafi TLS Protect Cloud certificate data through a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Venafi TLS Protect Cloud certificates and certificate requests from an OOMOL-connected account. It is intended for read-oriented certificate inventory and lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts.

Mitigation: Review the setup path before installation; prefer a verified package or installer with checksum or signature verification.

Risk: The skill can read certificate data visible to the connected Venafi TLS Protect Cloud account.

Mitigation: Connect only an OOMOL/Venafi account whose certificate inventory the agent is allowed to inspect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-venafitlsprotectcloud)
- [Venafi TLS Protect Cloud homepage](https://www.paloaltonetworks.com/network-security/next-gen-trust-security/certificate-manager)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the connected OOMOL and Venafi TLS Protect Cloud account permissions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
