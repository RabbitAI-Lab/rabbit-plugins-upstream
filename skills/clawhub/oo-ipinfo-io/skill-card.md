## Description:

IPinfo lets agents query IPinfo data through the OOMOL oo CLI for current-IP, arbitrary-IP, enrichment, batch, token, and map-report lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve IP geolocation, network, privacy, abuse, carrier, company, token, and batch lookup data from IPinfo through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented oo CLI installation path uses remote shell execution.

Mitigation: Install the oo CLI through a verified method and review installer contents before execution.

Risk: The map_ips action can upload large IP lists and create a hosted report URL.

Mitigation: Use bulk mapping only for IP lists approved for external processing through OOMOL/IPinfo.

Risk: Lookup actions can disclose internal or sensitive infrastructure identifiers to an external service.

Mitigation: Avoid submitting confidential internal infrastructure data unless organizational policy permits that processing.

## Reference(s):

- [IPinfo homepage](https://ipinfo.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ipinfo-io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return IPinfo data fields, enrichment records, token metadata, batch lookup results, or hosted map report URLs depending on the selected connector action.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
