## Description:

Uses an OOMOL-connected Reverse Contact account to enrich company and professional profiles through connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enrich company profiles from domains and professional profiles from email, name, or company context through Reverse Contact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run unverified remote installer scripts for the OOMOL CLI.

Mitigation: Prefer a signed or package-manager installation, or download and verify the installer before execution.

Risk: Reverse Contact connector schemas may change over time, which can make stale payload assumptions unreliable.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-reversecontact)
- [Reverse Contact homepage](https://www.reversecontact.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects live connector schema inspection before payload construction and uses an OOMOL-connected account for Reverse Contact access.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
