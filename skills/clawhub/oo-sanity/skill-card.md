## Description:

Sanity (sanity.io) support for reading, creating, updating, and deleting data through OOMOL's Sanity connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Sanity Content Lake documents through an OOMOL-connected account. It supports document reads, GROQ queries, and explicit user-reviewed mutation transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a remotely fetched installer directly in the shell without verification.

Mitigation: Install the oo CLI only from a trusted source, preferably using a verified or package-managed method instead of piping a remote script directly into a shell.

Risk: Sanity mutation transactions can remove, overwrite, or otherwise change production content.

Mitigation: Review the exact JSON payload, dataset, and document targets, then obtain explicit user approval before any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sanity)
- [Sanity homepage](https://www.sanity.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Sanity connector results returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
