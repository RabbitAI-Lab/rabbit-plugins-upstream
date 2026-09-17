## Description:

StatusCake (statuscake.com). Use this skill for reading, creating, updating, and deleting StatusCake data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage StatusCake uptime tests and read monitoring data through the OOMOL oo CLI without handling raw StatusCake tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote shell installer commands that could change the local system if the installer source is not independently trusted.

Mitigation: Review the install path and verify the OOMOL installer source and expected system changes before running curl-to-bash or irm-to-iex setup commands.

Risk: Write and destructive StatusCake actions can alter uptime test configuration or delete monitoring tests.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write or destructive command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-statuscake)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [StatusCake](https://www.statuscake.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
