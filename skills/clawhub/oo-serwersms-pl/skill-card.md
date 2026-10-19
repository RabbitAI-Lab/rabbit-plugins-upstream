## Description:

Operates SerwerSMS.pl through an OOMOL-connected account to send or schedule SMS, manage sender names, check limits and delivery reports, and cancel scheduled messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using SerwerSMS.pl can ask an agent to send or schedule SMS, check delivery and account limits, manage sender names, or cancel scheduled messages through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup suggests running a remote installer directly on the user's machine.

Mitigation: Do not let the agent run the installer automatically; use verified OOMOL installation documentation or inspect and verify the installer first.

Risk: SMS and account data pass through OOMOL as an intermediary.

Mitigation: Use this skill only if sharing that data with the OOMOL connector is acceptable.

Risk: Sending SMS, creating sender names, or canceling scheduled messages changes account state.

Mitigation: Confirm the exact payload and intended effect before each such action.

## Reference(s):

- [SerwerSMS.pl](https://serwersms.pl/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-serwersms-pl)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queued SMS is not proof of delivery.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
