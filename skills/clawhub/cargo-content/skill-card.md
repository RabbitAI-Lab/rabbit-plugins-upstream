## Description:

Guides users through uploading and organizing Cargo workspace knowledge files and managing connector-backed libraries for agent retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace users use this skill to upload, find, rename, and organize knowledge files and manage connector-backed libraries that supply agents with retrievable content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files may be uploaded to the wrong workspace or contain sensitive information.

Mitigation: Confirm the active workspace before writes and obtain approval before uploading sensitive or regulated documents.

Risk: Removing a file or library may delete workspace knowledge unexpectedly.

Mitigation: Check the resource list and confirm UUIDs before remove commands.

Risk: Installing the CLI with @latest may introduce unreviewed changes.

Mitigation: Pin and review the CLI version when reproducibility matters.

## Reference(s):

- [Cargo Content on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-content)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [File and library examples](artifact/references/examples/files.md)
- [Content response shapes](artifact/references/response-shapes.md)
- [Content troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI command results are JSON; the skill itself provides instructions rather than uploading files automatically.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
