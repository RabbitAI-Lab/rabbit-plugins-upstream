## Description:

MxToolbox lets agents perform MxToolbox DNS, mail, blacklist, HTTP, SMTP, ping, monitor, and usage lookups through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT operators, and security teams use this skill to run MxToolbox diagnostics for domains, mail records, blacklist status, monitor status, and API usage through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes one-line remote installer commands executed directly in a shell.

Mitigation: Review the installer source before use and prefer a signed or checksum-verified installer when available.

Risk: Diagnostic lookups are sent through an authenticated MxToolbox connection.

Mitigation: Inspect the live action schema before each call and send only the domains, IPs, or account requests needed for the user's task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mx-toolbox)
- [MxToolbox Homepage](https://mxtoolbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON response payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the OOMOL oo CLI; live action schemas determine payload fields.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
