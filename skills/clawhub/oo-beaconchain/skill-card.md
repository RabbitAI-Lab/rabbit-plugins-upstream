## Description:

Beaconcha.in (beaconcha.in). Use this skill for ANY Beaconcha.in request — searching and reading data. Whenever a task involves Beaconcha.in, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Beaconcha.in through an OOMOL-connected account for Ethereum beacon chain network performance, staking queue metrics, validator snapshots, validator lists, and finalized-epoch consensus reward details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes a pipe-to-shell installer for the oo CLI.

Mitigation: Install the oo CLI from a trusted, reviewable, version-pinned source when possible, and review the installer before execution.

Risk: Connector requests are routed through OOMOL infrastructure.

Mitigation: Use an appropriate OOMOL account and Beaconcha.in connection, and avoid sending data that should not be processed by that service path.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-beaconchain)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Beaconcha.in homepage](https://beaconcha.in)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses from the oo CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
