## Description:

AccuLynx helps agents read, create, and update AccuLynx contacts, jobs, company settings, calendars, appointments, and configured business types through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators with an OOMOL-connected AccuLynx account use this skill to retrieve settings and scheduling data, create contacts and Lead-milestone jobs, and add or update a job's initial appointment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup points users to mutable remote installer scripts for the OOMOL CLI.

Mitigation: Review the CLI installation path before running it, prefer official versioned installation instructions with checksum or signature verification, and do not let an agent run curl-to-bash or PowerShell iex installers automatically.

Risk: Write actions can create contacts and jobs or add and update a job's initial appointment in AccuLynx.

Mitigation: Confirm the exact payload, target record, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [AccuLynx ClawHub skill page](https://clawhub.ai/oomol/skills/oo-acculynx)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [AccuLynx homepage](https://acculynx.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [AccuLynx OOMOL connection page](https://console.oomol.com/app-connections?provider=acculynx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when run with the documented --json flag.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
