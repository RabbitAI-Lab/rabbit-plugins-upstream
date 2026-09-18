## Description:

Provides agent guidance for reading Nylas grants, calendars, and calendar events through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live Nylas connector schemas and run read-oriented Nylas actions for grants, calendars, and calendar events through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes unverified internet installer commands for the oo CLI.

Mitigation: Use an official package or pinned release, verify checksums or signatures when available, and require explicit approval before running setup commands.

Risk: Nylas actions depend on live connector schemas and account connection state.

Mitigation: Inspect the live action schema before constructing payloads and only run authentication, connection, or billing recovery steps after a matching command failure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nylas)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Nylas Homepage](https://www.nylas.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
