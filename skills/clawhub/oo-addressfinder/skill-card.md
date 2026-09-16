## Description:

Addressfinder (addressfinder.com) lets an agent search, retrieve metadata for, verify, and enrich Australian and New Zealand addresses through an OOMOL-connected Addressfinder account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Addressfinder from an agent workflow without handling raw Addressfinder API credentials directly. It supports autocomplete search, address metadata lookup, and address verification for Australia and New Zealand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Install the oo CLI only through a trusted, user-approved process, verify the source before execution, and do not let an agent run the installer commands automatically.

Risk: Address lookup and verification may involve user-provided address data.

Mitigation: Confirm that the user intends to submit the address data to Addressfinder through the connected OOMOL account before running connector actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-addressfinder)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Addressfinder Homepage](https://addressfinder.com/au)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and execution metadata when actions run successfully.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
