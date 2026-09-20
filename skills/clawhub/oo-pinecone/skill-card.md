## Description:

Pinecone lets agents operate Pinecone through an OOMOL-connected account to read, create, update, and delete indexes and vector data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Pinecone indexes and vector records from an agent session through the OOMOL connector, including read, search, write, and destructive maintenance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup commands pipe remote installer scripts into a local shell.

Mitigation: Use the official install guide, inspect the installer, and verify source integrity before running any installer command.

Risk: Write and destructive Pinecone actions can modify or delete indexes and vector records.

Mitigation: Confirm the exact action, target index or namespace, and payload with the user before running write or destructive operations.

Risk: The connector relies on OOMOL-mediated Pinecone account access.

Mitigation: Confirm that the user trusts OOMOL and the connected Pinecone account before installing or using the connector.

## Reference(s):

- [Pinecone homepage](https://www.pinecone.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute read, write, or destructive Pinecone actions after schema inspection and required user confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
