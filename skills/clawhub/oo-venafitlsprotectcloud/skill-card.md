## Description:

Venafi TLS Protect Cloud (paloaltonetworks.com). Use this skill for ANY Venafi TLS Protect Cloud request - searching and reading data. Whenever a task involves Venafi TLS Protect Cloud, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Venafi TLS Protect Cloud certificates and certificate requests through an OOMOL-connected account. It is focused on read-only certificate listing and retrieval workflows using the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote CLI installation and connected-account setup can introduce supply-chain or authorization exposure.

Mitigation: Install the oo CLI only when needed, use the documented OOMOL source, and review Venafi TLS Protect Cloud connected-account scopes before use.

Risk: Future connector actions could change or remove Venafi TLS Protect Cloud data if write or destructive actions are added.

Mitigation: Confirm the exact payload and effect with the user before any write action, and require explicit approval before destructive actions.

## Reference(s):

- [Venafi TLS Protect Cloud homepage](https://www.paloaltonetworks.com/network-security/next-gen-trust-security/certificate-manager)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-venafitlsprotectcloud)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads/results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before composing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
