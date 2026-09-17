## Description:

Qichacha helps agents inspect schemas and run Qichacha connector read actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Qichacha company data, such as shareholders and historical investments, through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run mutable remote installer scripts directly in a shell.

Mitigation: Review the official install guide, inspect downloaded installers, verify available signatures or checksums, and avoid elevated shells for setup.

Risk: Connector use depends on a signed-in OOMOL account, an active Qichacha connection, and available billing credit.

Mitigation: Run setup, connection, or billing recovery steps only after the matching command failure occurs.

Risk: Future Qichacha actions tagged write or destructive could change or remove data.

Mitigation: Confirm the exact payload, target, and effect with the user before running any tagged write or destructive action.

## Reference(s):

- [Qichacha API homepage](https://openapi.qcc.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qichacha)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON with data and meta.executionId when invoked with --json.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
