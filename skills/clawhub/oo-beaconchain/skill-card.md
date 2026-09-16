## Description:

Beaconcha.in helps agents retrieve Beaconcha.in network, staking queue, validator, and consensus rewards data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect Beaconcha.in network performance, staking queues, validator snapshots, and finalized-epoch validator reward breakdowns from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes direct remote script execution for installing the OOMOL CLI.

Mitigation: Review the installer path before installation and prefer a signed or otherwise verifiable release channel, or download and verify the installer before running it.

Risk: The skill depends on an authenticated OOMOL connection to Beaconcha.in.

Mitigation: Run setup only after an authentication or connection error, and use the connector schema command before actions so payloads match the live contract.

## Reference(s):

- [Beaconcha.in homepage](https://beaconcha.in)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-beaconchain)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance is centered on read-only Beaconcha.in data retrieval and one-time setup steps when authentication or connection errors occur.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
