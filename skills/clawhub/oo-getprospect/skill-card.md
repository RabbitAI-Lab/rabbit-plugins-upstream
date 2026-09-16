## Description:

GetProspect (getprospect.com). Use this skill for GetProspect searching and reading tasks through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search GetProspect lead and company data, find or verify business email addresses, and look up saved contact profiles through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may run remote installer scripts directly in a shell.

Mitigation: Review the installer first, prefer signed or versioned packages with checksum or signature verification, and avoid elevated shells unless required.

Risk: Connector actions can query business contact and lead data through an authenticated account.

Mitigation: Use the live action schema before sending payloads and confirm any action marked write or destructive before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getprospect)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [GetProspect homepage](https://getprospect.com)

## Skill Output:

**Output Type(s):** [shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON when --json is used.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
