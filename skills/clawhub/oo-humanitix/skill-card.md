## Description:

Humanitix (humanitix.com). Use this skill for ANY Humanitix request - searching and reading data. Whenever a task involves Humanitix, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Humanitix event data through an OOMOL-connected account. It supports retrieving event metadata, listing accessible events with filters, and listing account tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes installer commands fetched from the internet and executed locally, which could run arbitrary code if the installer channel is compromised.

Mitigation: Prefer an already installed trusted oo CLI, or download and verify the installer through an official, versioned, checksum- or signature-backed channel before execution.

## Reference(s):

- [Humanitix homepage](https://humanitix.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Humanitix connector schemas before running actions; command responses are JSON when the skill invokes the oo CLI with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
