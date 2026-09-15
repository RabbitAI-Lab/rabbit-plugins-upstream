## Description:

Ordinal connector skill for reading, creating, and updating Ordinal data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators who use Ordinal can use this skill to inspect live connector schemas and run OOMOL-mediated Ordinal actions for workspace reads and supported updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote shell installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, verifiable release or package manager; do not let an agent run curl-to-bash or PowerShell iex installers automatically.

Risk: Ordinal actions tagged as write can change workspace state.

Mitigation: Confirm the exact action payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [Ordinal homepage](https://www.tryordinal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before running Ordinal connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
