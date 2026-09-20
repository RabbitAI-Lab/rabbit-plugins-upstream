## Description:

Gumloop (gumloop.com). Use this skill for Gumloop requests such as reading data, starting saved flow runs, inspecting schemas, polling run details, and killing runs through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to operate Gumloop workbooks, saved flows, and flow runs from an agent session through an OOMOL-connected account. It supports schema discovery before execution and confirmation gates for write or destructive Gumloop actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional oo CLI installer is a remote install command.

Mitigation: Review the oo CLI installer source or use OOMOL's official install guidance before running remote install commands.

Risk: Starting or killing Gumloop flow runs can change Gumloop state or stop active work.

Mitigation: Require explicit user confirmation for the exact payload and target before write or destructive actions.

## Reference(s):

- [Gumloop homepage](https://www.gumloop.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gumloop)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results may include JSON data, execution IDs, run state, logs, and output node values.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
