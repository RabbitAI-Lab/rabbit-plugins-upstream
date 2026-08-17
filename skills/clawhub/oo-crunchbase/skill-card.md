## Description:

Crunchbase (crunchbase.com). Use this skill for ANY Crunchbase request — searching and reading data. Whenever a task involves Crunchbase, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Crunchbase organization, acquisition, and IPO data through an OOMOL-connected Crunchbase account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crunchbase access is mediated through OOMOL-connected accounts.

Mitigation: Install only if the user is comfortable using OOMOL as the intermediary for Crunchbase access.

Risk: Setup or login commands can alter local authentication state or open account-connection flows.

Mitigation: Run setup, login, or connection steps only when the CLI reports that they are needed.

Risk: Incorrect payload assumptions can produce failed or misleading Crunchbase lookups.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-crunchbase)
- [Crunchbase Homepage](https://www.crunchbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution.]

## Skill Version(s):

1.0.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
