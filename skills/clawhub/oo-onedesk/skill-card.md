## Description:

OneDesk (onedesk.com). Use this skill for OneDesk requests that search and read OneDesk data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live OneDesk connector schemas, filter projects and work items, and retrieve OneDesk records through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path documents remote installer scripts that are piped directly into a shell.

Mitigation: Use an already installed oo CLI when available; before running the setup installer, verify that the OOMOL installer endpoint is trusted and that local installation and login changes are acceptable.

## Reference(s):

- [OneDesk homepage](https://www.onedesk.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before running read-oriented OneDesk actions with JSON payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
