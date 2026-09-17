## Description:

Use this skill to operate Dub through OOMOL-connected credentials for reading, creating, updating, deleting, and analyzing Dub workspace resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to manage Dub short links, folders, tags, and analytics through OOMOL-connected credentials while checking live action schemas before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer a verified package or download-and-inspect workflow before installing the CLI.

Risk: The skill can create, update, and delete Dub workspace resources through connected credentials.

Mitigation: Confirm exact payloads and targets before write or destructive actions, and inspect the live connector schema before execution.

## Reference(s):

- [Dub homepage](https://dub.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected Dub credentials; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
