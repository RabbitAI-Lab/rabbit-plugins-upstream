## Description:

SmartSuite helps an agent read, create, update, and delete SmartSuite records through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate SmartSuite workspaces through OOMOL, including listing Solutions and Tables and managing records after inspecting the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include one-line remote installer commands for the oo CLI.

Mitigation: Review OOMOL's installer source before use, or install the oo CLI through a verified, pinned, or package-manager method.

Risk: Write and destructive SmartSuite actions can change or delete workspace records.

Mitigation: Inspect the live action schema, confirm the exact payload and target with the user, and require explicit approval before write or delete actions.

## Reference(s):

- [SmartSuite homepage](https://www.smartsuite.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use live SmartSuite connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
