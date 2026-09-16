## Description:

Roboflow helps agents inspect Roboflow schemas and metadata, run hosted object detection, and execute saved or ad hoc Roboflow workflows through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Roboflow-connected OOMOL accounts: inspect action schemas, list projects and versions, read server and workflow metadata, and run Roboflow inference or workflows when approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow execution is broader than read-only Roboflow metadata access.

Mitigation: Use the skill for Roboflow reads by default, and require explicit user approval before running saved or ad hoc workflows.

Risk: First-time setup includes remote pipe-to-shell installer commands for the OOMOL CLI.

Mitigation: Avoid running installer commands unless the OOMOL CLI installer source, version, and integrity have been independently verified.

## Reference(s):

- [Roboflow homepage](https://roboflow.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Roboflow skill page](https://clawhub.ai/oomol/skills/oo-roboflow)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Roboflow connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
