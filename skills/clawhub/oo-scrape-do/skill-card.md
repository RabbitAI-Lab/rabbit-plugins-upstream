## Description:

Scrape.do enables agents to fetch public URLs as HTML or JSON, retrieve account usage, and render screenshots through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to retrieve data from public web pages through Scrape.do, inspect account usage, or capture page screenshots via the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer scripts that could be risky if run without verification.

Mitigation: Review setup commands before installation, prefer official version-pinned and checksum- or signature-verified oo CLI instructions, and avoid running remote installers from an elevated shell.

Risk: Scrape.do connector actions can retrieve public URLs or account information through connected credentials.

Mitigation: Run actions only for user-requested public URLs or account information, and inspect the live action schema before constructing each payload.

## Reference(s):

- [Scrape.do homepage](https://scrape.do)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrape-do)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include HTML, parsed JSON, account usage metadata, or base64 screenshots.]

## Skill Version(s):

1.0.4 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
