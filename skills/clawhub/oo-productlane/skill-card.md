## Description:

Productlane lets agents read, create, update, and delete Productlane workspace data through the OOMOL-connected productlane connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Productlane workspaces from an agent, including listing, retrieving, creating, updating, and soft-deleting company and contact records after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the install path, use the trusted OOMOL CLI distribution channel, and avoid running pipe-to-shell or iex installers from an elevated shell.

Risk: Productlane write and destructive actions can change or soft-delete workspace records.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [Productlane homepage](https://productlane.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs can return JSON responses containing data and meta.executionId; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
