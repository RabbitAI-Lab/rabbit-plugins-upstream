## Description:

TheHive 5 lets an agent read, create, and update TheHive 5 data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Security operations analysts and incident response teams use this skill to list and retrieve TheHive 5 alerts and cases, and to create alerts or cases through an OOMOL-connected TheHive 5 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute unverified remote installer scripts.

Mitigation: Install the oo CLI through a trusted package manager, or download, pin, and verify the installer before running it.

Risk: The skill routes TheHive data through OOMOL's connector service.

Mitigation: Confirm the organization allows TheHive data to pass through OOMOL before installation and use.

Risk: Write actions can create alerts or cases in TheHive 5.

Mitigation: Inspect the live action schema and confirm the exact write payload and effect with the user before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-thehive5)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [TheHive 5 homepage](https://strangebee.com/thehive)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: evidence metadata and release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
