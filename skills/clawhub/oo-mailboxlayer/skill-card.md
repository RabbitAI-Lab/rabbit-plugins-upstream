## Description:

Mailboxlayer guides an agent to validate email addresses through an OOMOL-connected Mailboxlayer account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Mailboxlayer email validation through an already connected OOMOL account and receive quality signals for a single email address.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute internet-fetched installer scripts on the user's machine.

Mitigation: Review the setup path before installing, use a verified oo CLI package or documented release process, and do not let an agent run curl-to-bash or PowerShell iex installers automatically.

Risk: The action payload must match the live Mailboxlayer connector schema.

Mitigation: Inspect the connector schema immediately before constructing and running a JSON payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailboxlayer)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Mailboxlayer Connection Setup](https://console.oomol.com/app-connections?provider=mailboxlayer)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action-schema inspection before constructing JSON payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
