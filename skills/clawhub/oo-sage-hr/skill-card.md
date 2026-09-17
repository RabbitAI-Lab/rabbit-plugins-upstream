## Description:

Sage HR lets an agent read Sage HR employee, team, position, termination, and time-off data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized business users use this skill to perform explicit read-only Sage HR lookups through an agent, including employee records, positions, teams, termination reasons, and time off requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes pipe-to-shell installer commands for remote scripts.

Mitigation: Verify the installer through an official, integrity-checked method before running setup commands.

Risk: The skill handles sensitive HR data through OOMOL as an intermediary.

Mitigation: Use the skill only where OOMOL-mediated Sage HR reads are approved and credentials are scoped for the intended account.

Risk: Broad routing language could encourage speculative browsing of employee information.

Mitigation: Limit use to explicit read-only Sage HR lookups and request only the minimum employee or HR records needed.

## Reference(s):

- [ClawHub Sage HR Skill](https://clawhub.ai/oomol/skills/oo-sage-hr)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Sage HR Homepage](https://www.sage.com/en-us/sage-business-cloud/people/)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Sage HR connector actions are run through the oo CLI and return JSON responses.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
