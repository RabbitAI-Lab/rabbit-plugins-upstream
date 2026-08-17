## Description:

Manage workspace knowledge files and libraries in the Cargo content domain: upload, list, rename, move, and remove files, and create or sync native and connector-backed libraries for retrieval-augmented generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo workspace knowledge resources for agent grounding, including uploaded files, native libraries, and connector-backed libraries. It helps prepare and organize retrieval resources before attaching them to a deployed Cargo agent release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remove commands can delete Cargo knowledge resources when given the wrong file or library UUID.

Mitigation: List and verify target UUIDs before running remove commands, and confirm that the resource is not needed by a deployed agent release.

Risk: Uploaded or synced documents may contain private business, customer, or workspace information.

Mitigation: Review files and connector sources before upload or sync, and apply the workspace's data handling rules before attaching resources to agents.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [cargo-content ClawHub listing](https://clawhub.ai/cargo-ai/skills/cargo-content)
- [File & library examples](references/examples/files.md)
- [Content response shapes](references/response-shapes.md)
- [Content troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an authenticated Cargo workspace session.]

## Skill Version(s):

1.0.1 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
