## Description:

Airtable (airtable.com). Use this skill for ANY Airtable request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Airtable through an OOMOL-connected account, including reading bases and records, inspecting schemas, and creating, updating, or deleting Airtable resources with explicit confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI only from a trusted, verified source.

Risk: Airtable write and destructive actions can create, modify, or delete data.

Mitigation: Confirm the exact Airtable payload, target resource, and expected effect before execution, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-airtable)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Airtable Homepage](https://airtable.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL Airtable connector through the oo CLI and may return JSON responses.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
