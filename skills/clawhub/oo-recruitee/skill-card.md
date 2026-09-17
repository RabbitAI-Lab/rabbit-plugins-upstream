## Description:

Recruitee skill for reading, creating, and updating Recruitee data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and agents use this skill to operate Recruitee through a connected OOMOL account. It supports candidate creation, offer lookup, offer listing, and candidate search after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback recommends running remote installer scripts directly in a shell.

Mitigation: Review the installer path before installation and prefer a trusted, versioned, checksum-verified oo CLI source.

Risk: The create_candidate action changes Recruitee state.

Mitigation: Inspect the live action schema and confirm the exact JSON payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub Recruitee skill](https://clawhub.ai/oomol/skills/oo-recruitee)
- [Recruitee homepage](https://recruitee.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
