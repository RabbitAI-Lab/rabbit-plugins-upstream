## Description:

Use this skill to inspect schemas and read BlazeMeter Performance user, account, workspace, project, and test data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve BlazeMeter Performance profile, account, workspace, project, and test information through the OOMOL connector while relying on live schemas for command payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Install the oo CLI only through a reviewed, signed, or checksum-verified process before using the skill.

Risk: Connecting BlazeMeter through OOMOL gives the connector access to account and test metadata available to the configured API key.

Mitigation: Use a scoped BlazeMeter API key with only the access needed for the intended read operations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-blaze-meter-performance)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [BlazeMeter Performance homepage](https://www.blazemeter.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing BlazeMeter action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
