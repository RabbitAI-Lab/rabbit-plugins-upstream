## Description:

CallerAPI lets agents use the OOMOL oo CLI connector to look up phone reputation, business details, complaints, HLR carrier data, and authenticated account information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to query CallerAPI through an OOMOL-connected account for phone-number intelligence and account status. The skill guides agents to inspect the live connector schema before constructing each action payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote installer scripts for the oo CLI.

Mitigation: Install the CLI only when it is missing, review the installation path first, and prefer a signed or checksum-verified installer when available.

Risk: CallerAPI lookup inputs pass through the OOMOL connector, and account actions can retrieve the authenticated email and credit balance.

Mitigation: Use the skill only with data authorized for CallerAPI lookup, and request account information only when it is needed for the user task.

Risk: Billing, connection, or authentication failures can require account setup or recharge actions outside the lookup itself.

Mitigation: Pause on those errors and follow the documented setup or billing steps only for the matching failure condition.

## Reference(s):

- [CallerAPI homepage](https://callerapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-callerapi)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
