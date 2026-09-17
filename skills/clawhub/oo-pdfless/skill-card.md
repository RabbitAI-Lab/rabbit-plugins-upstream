## Description:

Pdfless helps agents inspect live Pdfless connector schemas and read workspace or document-template data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to retrieve Pdfless workspace details or list document templates through the OOMOL `oo` CLI. The skill guides schema inspection before requests and provides recovery steps for authentication, connection, CLI setup, and billing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute mutable remote installer scripts directly in a shell.

Mitigation: Review the install step before use and prefer a pinned, signed, or checksum-verified `oo` CLI release; connect only the Pdfless account the agent should read from.

## Reference(s):

- [ClawHub Pdfless Skill Page](https://clawhub.ai/oomol/skills/oo-pdfless)
- [Pdfless Homepage](https://pdfless.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live connector action schemas before constructing `oo connector run` requests.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
