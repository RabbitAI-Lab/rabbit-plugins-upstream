## Description:

Operate Pingdom through an OOMOL-connected account to search and read uptime checks, credits, and probe server details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Pingdom uptime monitoring data through the OOMOL oo CLI without handling raw Pingdom API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup documentation asks users to run a remote installer command for the oo CLI.

Mitigation: Prefer a pinned and verifiable oo CLI release, or inspect and verify the installer before running it.

Risk: OOMOL mediates Pingdom requests and setup may create persistent local or account-level state.

Mitigation: Use only an intended OOMOL account connection, review account permissions, and remove stale local or account connections when no longer needed.

Risk: The scanner summary notes that the connector scope is broader than a read-only Pingdom helper should be.

Mitigation: Use this release only for the documented read actions unless future documentation clearly declares write actions and confirmation requirements.

## Reference(s):

- [Pingdom ClawHub listing](https://clawhub.ai/oomol/skills/oo-pingdom)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Pingdom homepage](https://www.pingdom.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-oriented Pingdom connector actions and may include execution metadata returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
