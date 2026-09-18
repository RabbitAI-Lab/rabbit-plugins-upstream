## Description:

IPinfo (ipinfo.io). Use this skill for IPinfo requests that search or read IP intelligence through the OOMOL-connected IPinfo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run authenticated IPinfo lookups for public IP addresses, geolocation, organization, privacy, abuse, carrier, hostname, token metadata, and batch or map-report workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can run an unverified remote installer.

Mitigation: Use verified official installation steps and do not let an agent run the remote installer automatically.

Risk: Current-IP actions can reveal the user's public IP address and approximate location.

Mitigation: Confirm before running actions that disclose current public IP or location data.

Risk: Batch and map-report actions can upload large IP address datasets, including sensitive customer, internal, incident-response, or research data.

Mitigation: Confirm the dataset, purpose, and destination before uploading IP lists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ipinfo-io)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [IPinfo](https://ipinfo.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return IPinfo response data as JSON or plain text depending on the selected connector action.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
