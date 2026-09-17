## Description:

Linkup lets agents search the web, fetch webpages, return sourced answers or structured results, and check credits through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external agent users use this skill to query Linkup for web search answers, raw search results, structured data, webpage content, and account credit balance information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include mutable remote shell installers for the OOMOL CLI.

Mitigation: Review the installer source and prefer official, versioned, signed, or checksum-verified releases before installing; do not let an agent run curl-to-shell or PowerShell install pipelines automatically.

Risk: Connector requests may send user-provided data to Linkup through an OOMOL-connected account.

Mitigation: Avoid sending secrets or unrelated private data in connector payloads, and inspect the live connector schema before constructing requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-linkup)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Linkup homepage](https://www.linkup.so)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Linkup-sourced answers, raw search results, normalized structured data, fetched webpage markdown, optional HTML and images, or credit balance data.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
