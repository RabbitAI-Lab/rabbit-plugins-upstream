## Description:

TabAPI enables agents to search Google and retrieve webpage, screenshot, DNS, backlink, traffic, RDAP, WHOIS, and AdSense publisher-site data through an authenticated OOMOL CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to make authenticated TabAPI requests for search and website intelligence tasks while avoiding direct raw credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run unverified remote installer scripts directly in a shell.

Mitigation: Review the installation path before use and prefer a versioned, signed, or checksum-verified OOMOL CLI installer; after installation, authenticate normally and inspect live TabAPI action schemas before sending payloads.

## Reference(s):

- [ClawHub TabAPI Skill](https://clawhub.ai/oomol/skills/oo-tabapi)
- [TabAPI Homepage](https://tabapi.com)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include JSON data, execution identifiers, clean Markdown extracts, or temporary hosted PNG screenshot URLs; live action schemas should be inspected before payload construction.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
