## Description:

Neutrino API helps an agent run OOMOL-managed Neutrino connector actions for IP, domain, email, and phone intelligence lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Neutrino connector schemas and run read-oriented Neutrino lookups for IP blocklists, IP geolocation, domains, email validation, and phone validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded code locally.

Mitigation: Review and verify OOMOL installer sources through a safer install path before running curl-to-shell or PowerShell download-and-execute commands.

Risk: IP addresses, domains, email addresses, and phone numbers submitted through the connector are sent to OOMOL and Neutrino.

Mitigation: Do not submit sensitive or regulated identifiers unless the user accepts the data-sharing implications and the connected account is appropriate for that data.

## Reference(s):

- [ClawHub Neutrino API skill page](https://clawhub.ai/oomol/skills/oo-neutrino)
- [Neutrino API homepage](https://www.neutrinoapi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON data with execution metadata when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
