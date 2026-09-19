## Description:

Helps an agent inspect schemas and run read-oriented Venafi TLS Protect Cloud connector actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve certificates, retrieve certificate requests, and list certificates visible to a connected Venafi TLS Protect Cloud account. It is intended for read access through an OOMOL-connected account rather than direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Use a verified installer or package-manager installation path before running the skill.

Risk: Connector routing can be broader than the three listed read-only operations.

Mitigation: Keep use limited to get_certificate, get_certificate_request, and list_certificates unless a broader connector action is explicitly reviewed and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-venafitlsprotectcloud)
- [Venafi TLS Protect Cloud homepage](https://www.paloaltonetworks.com/network-security/next-gen-trust-security/certificate-manager)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides schema inspection before connector execution and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
