## Description:

Use this skill for Venafi TLS Protect Datacenter search and read workflows through an OOMOL-connected account, including listing certificates, retrieving certificate details by GUID, and checking effective certificate policy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and certificate operations teams use this skill to inspect Venafi TLS Protect Datacenter certificate data from an OOMOL-connected account. It supports read-oriented workflows such as listing visible certificates, retrieving certificate details, and checking effective certificate policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Install the oo CLI from a trusted, versioned source with checksum or signature verification, and do not allow an agent to run pipe-to-shell installer commands automatically.

Risk: Inline connector payloads can be fragile when values come from users or external systems.

Mitigation: Use file-based JSON payloads for connector data when values are user-provided or externally sourced.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-venafitlsprotectdatacenter)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [CyberArk Certificate Manager Self-Hosted](https://www.cyberark.com/resources/product-datasheets/cyberark-certificate-manager-self-hosted)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence, skill metadata, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
